import datetime
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Pet(models.Model):
    '''CONSTANTS'''
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPES = [(x, x) for x in [CAT, DOG, BUNNY, PARROT, FISH, OTHER]]

    NAME_MAX_LENGTH = 30

    '''COLUMNS/ FIELDS'''
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    '''ONE TO ONE RELATIONS'''

    '''ONE TO MANY RELATIONS'''
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    '''MANY TO MANY RELATIONS'''

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    '''DUNDER METHODS'''

    '''META'''

    class Meta:
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    IMAGE_UPLOAD_DIR = 'profiles/'
    photo = models.ImageField(
        upload_to=IMAGE_UPLOAD_DIR,
    )

    # TODO validate at least one pet
    tagged_pets = models.ManyToManyField(Pet, )

    description = models.TextField(null=True, blank=True)

    publication_date = models.DateTimeField(
        auto_now_add=True,

    )
    likes = models.IntegerField(
        default=0,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
