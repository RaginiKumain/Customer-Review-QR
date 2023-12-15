
from django.contrib import admin
from .models import CustomUser  # Import the CustomUser model

admin.site.register(CustomUser)  # Register the CustomUser model with the admin site
