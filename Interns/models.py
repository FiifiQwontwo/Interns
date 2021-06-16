from django.db import models
import string
import random
from django.utils.text import slugify


# Create your models here.


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Languages(models.Model):
    language_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.language_name)
        super(Languages, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        return self.language_name


class Frameworks(models.Model):
    framework_name = models.CharField(max_length=100)
    language_of_framework = models.ForeignKey(Languages, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.framework_name)
        super(Frameworks, self).save(*args, **kwargs)

    def __str__(self):
        return self.framework_name


class SchoolName(models.Model):
    name_of_university = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.name_of_university)
        super(SchoolName, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_of_university


class Internship(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(unique=True, max_length=254)
    name_of_school = models.ForeignKey(SchoolName, on_delete=models.CASCADE)
    year = models.CharField(max_length=5)
    course = models.CharField(max_length=100)
    language_name = models.ForeignKey(Languages, on_delete=models.CASCADE)
    framework_name = models.ForeignKey(Frameworks, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.last_name)
        super(Internship, self).save(*args, **kwargs)

    def __str__(self):
        return self.last_name + ' - ' + self.first_name
