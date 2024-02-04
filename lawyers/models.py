from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.conf import settings

from django.db import models
from django.utils import timezone
from phone_field import PhoneField

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name,mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')
        client = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )
        client.set_password(password)
        client.save(using=self._db)
        return client
    def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)
    def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

class Client(AbstractBaseUser,PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240,default ="")
    last_name = models.CharField(max_length=255,default ="")
    mobile = models.CharField(max_length=50,default ="")

    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','mobile']
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='client_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='client_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        # This is important for preventing clashes
        swappable = 'AUTH_USER_MODEL'
        db_table = 'client'
    def __str__(self):
        return self.email
# Add related_name attributes to the groups and user_permissions fields
Client._meta.get_field('groups').related_name = 'client_groups'
Client._meta.get_field('user_permissions').related_name = 'client_user_permissions'

class Category(models.Model):
    name = models.CharField("Name", max_length=250)
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200,unique = True,primary_key = True )

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    body = models.TextField()

class Avocat(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    numero_tlfn = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category, blank=True)
    email = models.EmailField()
    languages =models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return f"{self.nom}"

class ProfilAvocat(models.Model):
    avocat = models.OneToOneField(Avocat,related_name = "profile", on_delete=models.CASCADE)
    experience = models.TextField()
    photo = models.ImageField(upload_to='photos/' ,default="avocat001-230x230_eqCZhNQ.jpg")
    rating = models.FloatField(null=True)
    site_web = models.URLField(blank=True, null=True)
    blogs = models.ManyToManyField(Blog, related_name='profils_avocats', blank=True)
    working_hours=  models.TextField(default='N/A')

    def __str__(self):
        return f"{self.avocat.nom}"

class Appointment(models.Model):
    AppointmentID =models.AutoField("rdvID" , primary_key=True)
    lawyer= models.ForeignKey(Avocat, related_name='appointments', on_delete=models.CASCADE)
    user= models.ForeignKey(settings.AUTH_USER_MODEL,related_name='customer_appointments' , on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    SCHEDULED = 'Scheduled'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'
    STATUS_CHOICES = [
        (SCHEDULED, 'Scheduled'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]
    status=models.CharField(max_length=50,choices= STATUS_CHOICES ,null=True)
    context = models.TextField(default= 'N/A')

class Review(models.Model):
    lawyer= models.ForeignKey(Avocat, related_name='rating', on_delete=models.CASCADE)
    sender= models.ForeignKey(settings.AUTH_USER_MODEL,related_name='sent_ratings' , on_delete=models.CASCADE)
    comment=models.TextField("Comment", default='N/A' )
    rating = models.IntegerField("Stars" , default=0,choices={(str(i), i) for i in range(1,6)})
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return f"{self.sender.username}: {self.comment},{self.rating} stars"
