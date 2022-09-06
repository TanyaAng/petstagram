from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from petstagram.accounts.managers import PetstagramUserManager
from petstagram.common.validators import only_letters_validator


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGHT = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGHT,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    # Authenticate by
    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDER = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,

        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,

        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True)

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDER),
        choices=GENDER,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )

    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
