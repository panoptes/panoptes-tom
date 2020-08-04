from panoptes_tom.remoterequests.models import Profile

from django.contrib.auth.models import User
from django.test import TestCase
from django.template.defaultfilters import slugify


class RemoteRequestTests(TestCase):
    def setup_test_data(self):
        self.user = User.objects.create_user(
            username="testuser", email="foo@foo.com", password="shh"
        )
        self.slug = slugify(self.test_user)
        self.remote_observers = {"remote_observers": self.remote_observers}

        Profile(
            user=self.user, slug=self.slug, remote_observer=self.remote_observers
        )  # TODO: Figure out how to properly test remote_observers (Many to Many field)

    def test_profile(self):
        # test_user = user
        # slug = slugify(self.user)

        self.assertEqual(Profile.user.username, "testuser")
        self.assertEqual(Profile.user.email, "foo@foo.com")
        self.assertEqual(Profile.user.password, "shh")
        self.assertEqual(Profile.slug, Profile.user.username)

