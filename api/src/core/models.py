from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.urls import reverse

# Create your models here.

MESSAGES = {
    'invalid_email': 'ERROR: invalid email address is not allowed!',
}
# xyi


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new user"""
        if not email:
            raise ValueError(MESSAGES['invalid_email'])
        user = self.model(email=self.normalize_email(email),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports user email instead of username"""
    email = models.EmailField(
        max_length=255, unique=True,  verbose_name="Email")
    firstName = models.CharField(max_length=255,  verbose_name="First Name")
    lastName = models.CharField(max_length=255,  verbose_name="Last Name")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")

    objects = UserManager()
    USERNAME_FIELD = 'email'


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Event text")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Time created")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Time updated")
    is_published = models.BooleanField(
        default=True, verbose_name="Is published?")
    cat = models.ForeignKey(
        'Category', on_delete=models.PROTECT, verbose_name="Categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_slug': self.slug})

    class Meta:
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
