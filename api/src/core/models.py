import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.core import validators

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.urls import reverse

# Create your models here.

MESSAGES = {
    'invalid_email': 'ERROR: invalid email address is not allowed!',
}


class UserManager(BaseUserManager):
    def _create_user(self, firstName, lastName, email, password=None, **extra_fields):
        if not firstName:
            raise ValueError('Указанное Имя должно быть установлено')

        if not lastName:
            raise ValueError('Указанная Фамилия должна быть установлена')

        if not email:
            raise ValueError(
                'Данный адрес электронной почты должен быть установлен')

        email = self.normalize_email(email)
        user = self.model(firstName=firstName,
                          lastName=lastName, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, firstName, lastName, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(firstName, lastName, email, password, **extra_fields)

    def create_superuser(self, firstName, lastName, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(firstName, lastName, email, password, **extra_fields)


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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('email',)

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.firstName

    def get_short_name(self):
        return self.firstName

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


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
