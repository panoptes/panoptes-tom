import logging
from django.core.mail import send_mail

from django.template.loader import render_to_string

from tom_observations.models import ObservationRecord


logger = logging.getLogger(
    "panoptes_tom.settings.logging"
)  # TODO: Fix logging. It isn't working for some reason.


def observation_change_state(observation, previous_status):

    if observation.status == "IN_PROGRESS":
        logger.warning(
            "Sending email, observation %s is %s", observation, observation.status,
        )
        send_mail(
            render_to_string("tom_observations/email/email_obs_in_progress_subject.txt",),
            render_to_string(
                "tom_observations/email/email_obs_in_progress_message.txt",
                context={"observation": observation},
            ),
            from_email=None,
            recipient_list=[observation.email],
            fail_silently=False,
        )

    elif observation.status == "COMPLETED":
        logger.warning(
            "Sending email, observation %s changed state from %s to %s.",
            observation,
            previous_status,
            observation.status,
        )
        send_mail(
            render_to_string("tom_observations/email/email_obs_completed_subject.txt"),
            render_to_string(
                "tom_observations/email/email_obs_completed_message.txt",
                context={"observation": observation},
            ),
            from_email=None,
            recipient_list=[observation.email],
            fail_silently=False,
        )
