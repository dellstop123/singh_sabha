from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class Donation(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        template = '{0.name} {0.price} {0.date}'
        return template.format(self)

class News(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    link = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Programme(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='programme_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class About(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title                 