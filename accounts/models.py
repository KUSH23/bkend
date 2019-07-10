from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
  # is_active = models.BooleanField('active status', default=False)
  is_admin = models.BooleanField('admin status', default=False)
  is_manager = models.BooleanField('manager status', default=False)
  is_service_manager = models.BooleanField('service_manager status', default=False)

class Admin(models.Model):
  user = models.OneToOneField(User, default=1 ,on_delete=models.SET_DEFAULT)

class Manager(models.Model):
  user = models.OneToOneField(User, default=1 ,on_delete=models.SET_DEFAULT)
  
class ServiceManager(models.Model):
  user = models.OneToOneField(User, default=1 ,on_delete=models.SET_DEFAULT)