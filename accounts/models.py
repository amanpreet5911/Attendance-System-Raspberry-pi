from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

# Create your models here.


class Company_info(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=12, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='created_by_user')
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='updated_by_user')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'


class Designation(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    company = models.ForeignKey(
        Company_info, on_delete=models.CASCADE, blank=False, null=False)


class Shift(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    shift_start_time = models.TimeField(null=False, blank=False)
    shift_end_time = models.TimeField(null=False, blank=False)
    break_start_time = models.TimeField(null=False, blank=False)
    break_end_time = models.TimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must provide an Email.")
        if not username:
            raise ValueError("User must provide an Username.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        user.is_staff = True
        user.save(using=self._db)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    company = models.ForeignKey(
        Company_info, blank=True, null=True, on_delete=models.DO_NOTHING)
    ip_address = models.CharField(max_length=15, null=True, blank=True)
    # status = models.CharField()
    Designation = models.ForeignKey(
        Designation, blank=True, null=True, on_delete=models.DO_NOTHING)
    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='added_by_user')
    # updated_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='modified_by_user')
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    time = models.CharField(max_length=15, null=True, blank=True, default=None)
    employee_id = models.SmallIntegerField(
        blank=True, null=True)
    shift = models.ForeignKey(
        Shift, null=True, blank=True, on_delete=models.DO_NOTHING)
    available_leaves = models.FloatField(null=True, blank=True)
    available_short_leave = models.FloatField(null=True, blank=True)
    # Required Fields

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True

    @property
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'


class User_details(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    logout_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shift_start = models.TimeField(null=True, blank=True)
    shift_end = models.TimeField(null=True, blank=True)
    work_hours = models.TimeField(null=True, blank=True)
    early_arrival = models.TimeField(null=True, blank=True)
    late_arrival = models.TimeField(null=True, blank=True)
    overtime_hours = models.TimeField(null=True, blank=True)
    early_departure = models.TimeField(null=True, blank=True)
    late_departure = models.TimeField(null=True, blank=True)
    employee_code = models.SmallIntegerField(null=True, blank=True)
    card_no = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'


class Pi_users(models.Model):
    rfid_uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    employee = models.SmallIntegerField(
        blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)


class Pi_attendance(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    clock_in = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE, blank=True, null=True, related_name='attendanceuser')



