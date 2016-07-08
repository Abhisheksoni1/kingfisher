from django.db import models

# Create your models here.
from django.conf import settings
from django.core.validators import RegexValidator
import phonenumber_field.modelfields as phones
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    phone = phones.PhoneNumberField()

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
