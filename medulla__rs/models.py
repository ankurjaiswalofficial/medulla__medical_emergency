from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            name=name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone_number, password):
        user = self.create_user(
            name,
            phone_number,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


# def DriverImageStorage(instance, filename):
#     base_url = "/drivers/images/"

#     return f"{base_url}{str(instance.name).replace(' ', '')}.{filename.split('.')[-1]}"

class DriverImageStorage(FileSystemStorage):
    base_url = '/drivers/images/'

    def get_path(self, instance, filename):
        return f'drivers/{instance.id}/{filename}'

class AmbulanceType(models.Model):
    TYPE_CHOICES = (
        ('VAN', 'Ambulance Van'),
        ('SPRINTER', 'Ambulance Sprinter'),
        ('SUV', 'Ambulance SUV'),
        ('MOTORCYCLE', 'Ambulance Motorcycle'),
        ('OTHER', 'Other'),
    )
    name = models.CharField(
        max_length=255, choices=TYPE_CHOICES, default='VAN')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PublicQueryModel(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255, )
    phone_number = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f"{self.name} ({self.phone_number})"




class AmbulanceDriver(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    ambulance_number = models.CharField(max_length=15, unique=True)
    ambulance_type = models.ForeignKey(AmbulanceType, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=255, blank=True)
    driving_experience = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    driver_image = models.ImageField(upload_to=DriverImageStorage().get_path, blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.ambulance_number})"
