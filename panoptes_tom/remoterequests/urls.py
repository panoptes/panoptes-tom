from django.urls import path, include
from .views import (
    user_info,
    profile_view,
    send_obs_request,
    cancel_obs_request,
    accept_obs_request,
    delete_obs_request,
)

app_name = "remoterequests"
urlpatterns = [
    path(
        "remoterequests/<slug>/", profile_view, name="profile-view"
    ),  # TODO: Consider renaming slug
    path("remoterequests/user-profile/<int:id>/", user_info, name="user-profile"),
    path("observation-request/send/<int:id>/", send_obs_request, name="send-obs-request"),
    path("observation-request/cancel/<int:id>/", cancel_obs_request, name="cancel-obs-request"),
    path("observation-request/accept/<int:id>/", accept_obs_request, name="accept-obs-request"),
    path("observation-request/delete/<int:id>/", delete_obs_request, name="delete-obs-request"),
]
