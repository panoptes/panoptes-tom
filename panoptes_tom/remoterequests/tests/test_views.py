from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from panoptes_tom.remoterequests.views import (
    user_info,
    send_obs_request,
    cancel_obs_request,
    accept_obs_request,
    delete_obs_request,
    profile_view,
)
from mixer.backend.django import mixer

import pytest


@pytest.mark.django_db
class TestViews:
    def test_user_info_authenticated(self):
        path = reverse("remoterequests:user-profile", kwargs={"id": 1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = user_info(request, id=1)
        assert response.status_code == 200

    def test_sent_request(self):
        path = reverse("remoterequests:send-obs-request", kwargs={"id": 1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = send_obs_request(request, id=1)
        assert "remoterequests/<slug> user.profile.slug" in response.url

    def test_cancelled_request(self):
        path = reverse("remoterequests:cancel-obs-request", kwargs={"id": 1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = cancel_obs_request(request, id=1)
        assert response.status_code == 200

    def test_accepted_request(self):
        path = reverse("remoterequests:accept-obs-request", kwargs={"id": 1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = accept_obs_request(request, id=1)
        assert response.status_code == 200

    def test_deleted_request(self):
        path = reverse("remoterequests:delete-obs-request", kwargs={"id": 1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = delete_obs_request(request, id=1)
        assert response.status_code == 200
