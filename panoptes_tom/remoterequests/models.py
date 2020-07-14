from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.template.defaultfilters import slugify


class Profile(models.Model):
    """User Profile Class

    This class creates a user profile in a one to many relationship.
    That is, one user profile can be associated with multiple observation requests.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    remote_observers = models.ManyToManyField("Profile", blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse(
            "remoterequests:profile_view", args=[str(self.slug)]
        )  # TODO: Reevaluate this later

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.user)

        super(Profile, self).save(*args, **kwargs)

    # This sender/receiver model is created when a user is created
    def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
        if created:
            try:
                Profile.objects.create(user=instance)
            except:
                pass

    post_save.connect(post_save_user_model_receiver, sender=User)


class ObservationRequest(models.Model):
    """An observation requests model.

    This model has to_user and from_user foreign keys which allow for certain elements in one
    database table to be tied into elements in another database table.
    """

    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)  # timestamp is set when request is made

    def __str__(self):
        return "Observation request from {}, to {}".format(
            self.from_user.username, self.to_user.username
        )

