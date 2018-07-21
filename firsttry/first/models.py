from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .UserManager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('آدرس ایمیل'), unique=True, help_text="1@gmail.com")
    first_name = models.CharField(_('نام'), max_length=30, blank=True)
    last_name = models.CharField(_('نام خانودگی'), max_length=30, blank=True)
    date_Birth = models.DateTimeField(_('تاریخ تولد'), blank=True,null=True, help_text="روز-ماه-سال")
    contact = models.CharField(_('شماره تماس'),null=True, max_length=30, blank=True)
    # user_gender = models.CharField(_('جنسیت'), choices=((0, 'woman'), (1, 'men')), max_length=30)
    user_name = models.CharField(_('نلم کاربری'), unique=True, max_length=30)
    avatar = models.ImageField(upload_to='image/', null=True, blank=True)
    national_number = models.CharField(_('شماره ملی'), unique=True, max_length=30)
    # date_joined = models.DateTimeField(_('date joined'), default=timezone)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    AbstractBaseUser.password = (_('رمز عبور'))
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'national_number']

    class Meta:
        db_table = 'first_profile'
        ordering = ['-last_name', 'first_name']
        verbose_name = _('userProfile')
        verbose_name_plural = _('usersProfile')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)

        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Request(models.Model):
    writer = models.ForeignKey('User', on_delete=models.CASCADE)
    subject = models.CharField(_('موضوع'), max_length=500)
    text = models.TextField(_('درخواست'))
    SRATUS = ((0, 'درانتظار پاسخ رهی'), (1, 'در حال پاسخ دهی'),  (2, 'اتمام کار'))
    state = models.IntegerField(_('وضعیت'), choices=SRATUS, default=0)
    response = models.TextField(_('پاسخ'))

    class Meta:
        db_table = 'Requests'
        verbose_name = _('request')
        verbose_name_plural = _('requests')

    def __str__(self):
        return self.text
