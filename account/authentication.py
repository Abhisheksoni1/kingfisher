from django.contrib.auth.models import User
from .models import Profile

class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class PhoneAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            profile = Profile.objects.get(phone=username)
            if profile.user.check_password(password):
                return profile.user
            return None
        except User.DoesNotExist:
            return None


    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None