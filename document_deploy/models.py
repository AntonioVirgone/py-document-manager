from django.db import models
from django.utils import timezone


class Document(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    projectCode = models.CharField(max_length=200)
    directoryCode = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Project(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    serviceName = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Directory(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
