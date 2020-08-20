import requests

from astropy import units as u
from crispy_forms.layout import Div, HTML, Layout
from dateutil.parser import parse
from django import forms
from django.conf import settings
from django.core.cache import cache

from tom_common.exceptions import ImproperCredentialsException
from tom_observations.cadence import CadenceForm
from tom_observations.facility import (
    BaseRoboticObservationFacility,
    BaseRoboticObservationForm,
    get_service_class,
)
from tom_observations.observing_strategy import GenericStrategyForm
from tom_targets.models import (
    Target,
    REQUIRED_NON_SIDEREAL_FIELDS,
    REQUIRED_NON_SIDEREAL_FIELDS_PER_SCHEME,
)

from astropy.utils.iers import conf
import json
import copy

conf.auto_max_age = None


def make_request(*args, **kwargs):
    response = requests.request(*args, **kwargs)
    if 400 <= response.status_code < 500:
        raise ImproperCredentialsException("PAN: " + str(response.content))
    response.raise_for_status()
    return response


class PanoptesObservationFacilityForm(BaseRoboticObservationForm):
    name = forms.CharField()
    start = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))
    end = forms.CharField(widget=forms.TextInput(attrs={"type": "date"}))

    min_nexp = forms.IntegerField(initial=60)
    exp_time = forms.FloatField(
        initial=120, widget=forms.TextInput(attrs={"placeholder": "Seconds"})
    )
    exp_set_size = forms.IntegerField(initial=10)
    priority = forms.FloatField(initial=100)

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            self.common_layout, self.layout(), self.cadence_layout, self.button_layout()
        )

    def layout(self):
        return Div(
            Div(
                Div("name", "start", "end", css_class="col",),
                Div("min_nexp", "exp_time", "priority", "exp_set_size", css_class="col",),
                css_class="form-row",
            ),
        )

    # Overrides existing parameters so that RA and DEC get submitted to the db
    def serialize_parameters(self):
        target = Target.objects.get(pk=self.cleaned_data["target_id"])
        parameters = copy.deepcopy(self.cleaned_data)
        parameters.pop("groups", None)
        parameters["field_ra"] = target.ra
        parameters["field_dec"] = target.dec
        return json.dumps(parameters)

    def observation_payload(self):
        """
        This method is called to extract the data from the form into a dictionary that
        can be used by the rest of the module. In the base implementation it simply dumps
        the form into a json string.
        """
        target = Target.objects.get(pk=self.cleaned_data["target_id"])
        observation_payload = {
            "target_id": target.id,
            "parameters": self.serialize_parameters(),
        }

        return observation_payload


class PanoptesObservationFacility(BaseRoboticObservationFacility):

    name = "PAN001"
    # The SITES dictionary is used to calculate visibility intervals in the
    # planning tool. All entries should contain latitude, longitude, elevation
    # and a code.

    SITES = {
        "Mauna Loa": {
            "sitecode": "mau",
            "latitude": 19.54,
            "longitude": -155.58,
            "elevation": 3400,
        }
    }

    observation_forms = {"OBSERVATION": PanoptesObservationFacilityForm}

    def data_products(self, observation_id, product_id=None):
        return []

    def get_form(self, observation_type):
        return PanoptesObservationFacilityForm

    # TODO: Have observation_id return the status from an external service (ie. Google IOT)
    def get_observation_status(self, observation_id):
        return ["IN_PROGRESS"]

    def get_observation_url(self, observation_id):
        return ""

    def get_observing_sites(self):
        return self.SITES

    def get_terminal_observing_states(self):
        return ["IN_PROGRESS", "COMPLETED"]

    def submit_observation(self, observation_payload):

        print(observation_payload)

        return [1]

    def validate_observation(self, observation_payload):
        pass
