from django.db import models
from django.contrib.auth.models import User


class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    fathers_name=models.CharField(null=True, blank=True, max_length=80)
    contact_number=models.IntegerField(null=True)
    address=models.CharField(null=True, blank=True, max_length=100)
    gender = models.CharField(max_length=3, null=True)
    designation = models.CharField(max_length=5, null=True)
    blood_group=models.CharField(null=True, max_length=10)
    about = models.TextField(blank=True,null=True)
    profile_pic = models.FileField(upload_to = "profiles/",null=True, blank=True)
    # Qualification = models.CharField(max_length=14, blank=True, default=None)
    # identity_info = models.CharField(max_length=14, blank=True, default=None)
    # resume = models.CharField(max_length=14, blank=True, default=None)
    

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Register"

