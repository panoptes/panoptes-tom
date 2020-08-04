from panoptes_tom.remoterequests.models import Profile

from django.contrib.auth.models import User
from django.test import TestCase
from django.template.defaultfilters import slugify


class RemoteRequestTests(TestCase):
    def setup_test_data(self):
        User.objects.create_user(
            username="testuser", email="foo@foo.com", password="shh"
        )
        slugify(self.user)

        Profile(user=self.user, slug=self.slug)
        # self.remote_observers = {"remote_observers": self.remote_observers}

    def test_profile(self):
        # test_user = user
        # slug = slugify(self.user)

        self.assertEqual(Profile.user.username, "testuser")
        self.assertEqual(Profile.user.email, "foo@foo.com")
        self.assertEqual(Profile.user.password, "shh")
        self.assertEqual(Profile.slug, Profile.user.username)

