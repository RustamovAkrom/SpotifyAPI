from django.contrib import admin
from .models import User, UserProfile, PlayList

admin.site.register([User, UserProfile, PlayList])
