from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(UserManager):

    def create_user(self, email: str, password: str, **other_fields):
        '''Function for custom user creation.'''

        if not email:
            raise ValueError(_('Valid email was not provided'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email: str, password: str, **other_fields):
        '''Function fo custom admin account creation.'''

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if not other_fields.get('is_staff'):
            raise ValueError(_('Superuser must be assigned is_staff=True'))
        
        if not other_fields.get('is_superuser'):
            raise ValueError(_('Superuser must be assigned is_superuser=True'))

        return self.create_user(email, password, **other_fields)
        

class CustomUser(AbstractUser, PermissionsMixin):
    '''A class to override default user model'''
    
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ### -- Fields to ommit -- ###
    username = None
    first_name = None
    last_name = None
    date_joined = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.email.split('@')[0]}'
    

class CustomUserAddress(models.Model):
    '''A class to model user address.'''

    first_line = models.CharField(max_length=200)
    second_line = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.city}, {self.country}'


class CustomUserDetails(models.Model):
    '''A class to model user details.'''

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.ForeignKey(CustomUserAddress, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'