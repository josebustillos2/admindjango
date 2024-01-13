from django.db import models


class InvoiceChoices(models.BooleanField):
    YES_NO_CHOICES = ((False, "NO"), (True, "SI"))
