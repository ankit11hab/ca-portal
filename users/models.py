
import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, firstname, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('username', 'superuser')
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email,  firstname, password, "email", **other_fields)

    def create_user(self, email, firstname, password, provider, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email,
                          firstname=firstname, provider=provider, ** other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    id = models.SlugField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=False, default="user")
    firstname = models.CharField(max_length=150, blank=True)
    phone = PhoneNumberField(unique=False, blank=True)
    college = models.CharField(max_length=200, unique=False)
    department = models.CharField(max_length=200, unique=False)
    degree = models.CharField(max_length=200, unique=False)
    course_duration = models.CharField(max_length=200, unique=False)
    graduation_year = models.CharField(max_length=200, unique=False)
    date_joined = models.DateTimeField(default=timezone.now)
    provider = models.CharField(max_length=200, unique=False, default="email")
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname']

    def __str__(self):
        return str(self.id)

# Username for admin is admin, superuser is superuser
# firstname field stores the user full name not the username


class Profile(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.firstname} Profile'