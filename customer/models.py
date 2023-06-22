from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=300, null=True)
    age = models.IntegerField(null=True)
    place = models.TextField(null=True)
    phone = PhoneNumberField(null=True, blank=True)
    status = models.BooleanField(default=False)


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
