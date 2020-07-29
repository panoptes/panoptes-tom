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
    end = forms.CharField(required=False, widget=forms.TextInput(attrs={"type": "date"}))

    min_nexp = forms.IntegerField(min_value=1)
    exp_time = forms.FloatField(
        min_value=5, widget=forms.TextInput(attrs={"placeholder": "Seconds"})
    )
    exp_set_size = forms.IntegerField(min_value=1)
    priority = forms.FloatField(min_value=0)

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
            Div(Div("period", css_class="col"), css_class="form-row"),
        )

    def observation_payload(self):
        """
        This method is called to extract the data from the form into a dictionary that
        can be used by the rest of the module. In the base implementation it simply dumps
        the form into a json string.
        """
        target = Target.objects.get(pk=self.cleaned_data["target_id"])

        return {
            "target_id": target.id,
            "parameters": self.serialize_parameters(),
        }


class PanoptesObservationFacility(BaseRoboticObservationFacility):

    name = "PAN012"
    observation_types = [("OBSERVATION", "Custom Observation")]
    # The SITES dictionary is used to calculate visibility intervals in the
    # planning tool. All entries should contain latitude, longitude, elevation
    # and a code.

    SITES = {
        "Mt. Wilson": {
            "sitecode": "wil",
            "latitude": 34.22,
            "longitude": -118.06,
            "elevation": 1700,
        }
    }

    def data_products(self, observation_id, product_id=None):
        return []

    def get_form(self, observation_type):
        return PanoptesObservationFacilityForm

    # def get_facility_status(self):
    #     """Get the telescope_states from the LCO API endpoint and simply
    #     transform the returned JSON into the following dictionary hierarchy
    #     for use by the facility_status.html template partial.
    #     facility_dict = {'code': 'LCO', 'sites': [ site_dict, ... ]}
    #     site_dict = {'code': 'XYZ', 'telescopes': [ telescope_dict, ... ]}
    #     telescope_dict = {'code': 'XYZ', 'status': 'AVAILABILITY'}
    #     Here's an example of the returned dictionary:
    #     literal_facility_status_example = {
    #         'code': 'LCO',
    #         'sites': [
    #             {
    #                 'code': 'BPL',
    #                 'telescopes': [
    #                     {
    #                         'code': 'bpl.doma.1m0a',
    #                         'status': 'AVAILABLE'
    #                     },
    #                 ],
    #             },
    #             {
    #                 'code': 'ELP',
    #                 'telescopes': [
    #                     {
    #                         'code': 'elp.doma.1m0a',
    #                         'status': 'AVAILABLE'
    #                     },
    #                     {
    #                         'code': 'elp.domb.1m0a',
    #                         'status': 'AVAILABLE'
    #                     },
    #                 ]
    #             }
    #         ]
    #     }
    #     :return: facility_dict
    #     """
    #     # make the request to the LCO API for the telescope_states
    #     response = make_request(
    #         "GET",
    #         PORTAL_URL + "/api/telescope_states/",
    #         headers=self._portal_headers(),  # TODO: Determine what we're going to replace portal url with
    #     )
    #     telescope_states = response.json()

    #     # Now, transform the telescopes_state dictionary in a dictionary suitable
    #     # for the facility_status.html template partial.

    #     # set up the return value to be populated by the for loop below
    #     facility_status = {"code": "LCO", "sites": []}

    #     for telescope_key, telescope_value in telescope_states.items():
    #         [site_code, _, _] = telescope_key.split(".")

    #         # extract this telescope and it's status from the response
    #         telescope = {"code": telescope_key, "status": telescope_value[0]["event_type"]}

    #         # get the site dictionary from the facilities list of sites
    #         # filter by site_code and provide a default (None) for new sites
    #         site = next(
    #             (site_ix for site_ix in facility_status["sites"] if site_ix["code"] == site_code),
    #             None,
    #         )
    #         # create the site if it's new and not yet in the facility_status['sites] list
    #         if site is None:
    #             new_site = {"code": site_code, "telescopes": []}
    #             facility_status["sites"].append(new_site)
    #             site = new_site

    #         # Now, add the telescope to the site's telescopes
    #         site["telescopes"].append(telescope)

    #     return facility_status

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
