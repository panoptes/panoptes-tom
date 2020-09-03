from django.urls import reverse, resolve


class TestUrls:
    def test_profile_url(self):
        path = reverse("remoterequests:profile-view", kwargs={"slug": "django"})
        assert resolve(path).view_name == "remoterequests:profile-view"

    def test_user_info_url(self):
        path = reverse("remoterequests:user-profile", kwargs={"id": 1})
        assert resolve(path).view_name == "remoterequests:user-profile"

    def test_send_request_url(self):
        path = reverse("remoterequests:send-obs-request", kwargs={"id": 1})
        assert resolve(path).view_name == "remoterequests:send-obs-request"

    def test_cancel_request_url(self):
        path = reverse("remoterequests:cancel-obs-request", kwargs={"id": 1})
        assert resolve(path).view_name == "remoterequests:cancel-obs-request"

    def test_accept_obs_request_url(self):
        path = reverse("remoterequests:accept-obs-request", kwargs={"id": 1})
        assert resolve(path).view_name == "remoterequests:accept-obs-request"

    def test_delete_request_url(self):
        path = reverse("remoterequests:delete-obs-request", kwargs={"id": 1})
        assert resolve(path).view_name == "remoterequests:delete-obs-request"

