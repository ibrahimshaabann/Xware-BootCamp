from django.contrib import admin

from .models import Notifications

from .models import User
admin.site.register(User)
admin.site.register(Notifications)


# Register your models here.
