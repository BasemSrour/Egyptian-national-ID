from django.db import models
from django.core.exceptions import ValidationError


class NationalID(models.Model):
    # The ID number that is entered from the user
    number = models.BigIntegerField(blank=False, null=False)
    # The validity of the ID number
    validity = models.BooleanField(default=False)
    # The data extracted from the ID number due to its validation
    birth_year = models.IntegerField(default=0000)
    birth_month = models.IntegerField(default=00)
    birth_day = models.IntegerField(default=00)

    def clean(self):
        """
        Validating the ID number length
        """
        if len(str(self.number)) != 14:
            raise ValidationError('The ID number Must be 14 digits')

    def __str__(self):
        return f"Egyptian national ID number: {self.number}" 
