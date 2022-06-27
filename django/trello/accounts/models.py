from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self,  email, name, password=None):
        if not email:
            raise ValueError('user must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.role = UserAccount.SUPER_ADMIN
        user.set_password(password)
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    SUPER_ADMIN = 0
    USER = 1

    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'

    USER_STATUSES = (
        (INACTIVE, 'Inactive'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
    )

    ROLE_TYPES = (
        (SUPER_ADMIN, 'SUPER_ADMIN'),
        (USER, 'USER'),)

    role = models.IntegerField(choices=ROLE_TYPES, default=3)
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=150)
    last_name = models.CharField(
        max_length=150, null=True, blank=True, default="")
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    device_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=USER_STATUSES, default=ACTIVE, null=True, blank=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name


class UserOTP(models.Model):
    email = models.CharField(max_length=500, null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_email_verified = models.BooleanField(default=False)
    is_email_verifieds = models.BooleanField(default=False)
