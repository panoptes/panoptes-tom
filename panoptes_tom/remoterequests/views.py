from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, ObservationRequest
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

User = User


def user_info(request, id=None):
    """This returns profile info on a given user.

    Args:
        request : A request to view the profile info.
        id (int): An identifier for a particular user. Defaults to None.

    Returns:
       The profile info page.
    """
    if id:
        user = User.objects.get(id=id)
    else:
        user = request.user
    args = {"user": user}
    return render(request, "user/user_profile.html", args)


def observers_list(request):
    """Observers List

    Returns a list of all the observers excluding ourself.
    """
    observers = Profile.objects.exclude(user=request.user)
    context = {"observers": observers}
    return render(request, "remoterequests/home.html", context)


def send_obs_request(request, id):
    """Send Observation Request

    Args:
        request: An observation request
        id (int): The id of the user that we are sending the request to.

    The .get_or_create() method is used to prevent scenarios where an observation request is sent but already exists.
    Returns:
        An http redirect to the /observations page.
    """
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        ob_req, created = ObservationRequest.objects.get_or_create(
            from_user=request.user, to_user=user
        )
        return redirect("remoterequests:profile-view", request.user.profile.slug)


def cancel_obs_request(request, id):
    """Cancels observation request.

    Filters requests by those that exist and deletes the request item for to_user.
    """
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        ob_req = ObservationRequest.objects.filter(
            from_user=request.user, to_user=user
        ).first()  # .first() gets the only item in the list
        ob_req.delete()
        return redirect("remoterequests:profile-view", user.profile.slug)


def accept_obs_request(request, id):
    from_user = get_object_or_404(User, id=id)
    ob_req = ObservationRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    user1 = ob_req.to_user
    user2 = from_user
    user1.profile.remote_observers.add(user2.profile)
    # TODO: remote_observers.add() is just a placeholder. Eventually, we want a system where a "virtual" telescope request gets sent to the cloud.
    user2.profile.remote_observers.add(user1.profile)
    ob_req.delete()
    return redirect("remoterequests:profile-view", user1.profile.slug)


def delete_obs_request(request, id):
    """Delete an observation request

    This allows the user receiving the request to choose whether or not they want to delete the request.
    """
    from_user = get_object_or_404(User, id=id)
    ob_req = ObservationRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    ob_req.delete()
    return redirect("remoterequests:profile-view")


def profile_view(request, slug):
    """Profile Info

    Displays profile information such as sent and received observation requests.
    """

    p = Profile.objects.filter(slug=slug).first()
    u = p.user
    sent_obs_requests = ObservationRequest.objects.filter(from_user=p.user)
    rec_obs_requests = ObservationRequest.objects.filter(to_user=p.user)

    remote_observers = p.remote_observers.all()

    # is this user a remote observer on our telescope
    button_status = "none"
    if p not in request.user.profile.remote_observers.all():
        button_status = "not_remote_observer"  # TODO: Once remote observers are done observing, they need to be removed from the remote observers list

        # if we sent user an observation request
        if (
            len(ObservationRequest.objects.filter(from_user=request.user).filter(to_user=p.user))
            == 1
        ):
            button_status = "observation_request_sent"

    context = {
        "u": u,
        "button_status": button_status,
        "remote_observer_list": remote_observers,
        "sent_obs_requests": sent_obs_requests,
        "rec_obs_requests": rec_obs_requests,
    }

    return render(request, "remoterequests/profile.html", context)

