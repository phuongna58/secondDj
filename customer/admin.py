from django.contrib import admin
from .models import Customer, LogMessage, Book, Author

# Register your models here.
admin.site.register(Customer)
admin.site.register(LogMessage)
admin.site.register(Book)
admin.site.register(Author)
