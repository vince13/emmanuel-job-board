from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(models.Model):
    company = models.CharField(max_length=100, blank=True, null=True)
    is_employer = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Custom User"

    def __str__(self):
        return self.company


class Job(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return str(self.applicant.company)
