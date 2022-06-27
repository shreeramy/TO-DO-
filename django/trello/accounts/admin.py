from django.contrib import admin
from . models import UserAccount, UserOTP
# Register your models here.


admin.site.register(UserAccount)

admin.site.register(UserOTP)
