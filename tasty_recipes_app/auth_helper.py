from tasty_recipes_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def no_profile_created():
    profile = get_profile()
    if profile:
        return False
    else:
        return True
