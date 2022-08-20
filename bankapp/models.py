from django.db import models
from django.urls import reverse


# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    wiki = models.TextField(blank=True)

    class meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def get_url(self):
        return reverse('bankapp:d_by_details', args=[self.slug])

    def __str(self):
        return '{}'.format(self.name)


class Branch(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'



    def __str__(self):
        return '{}'.format(self.name)


class Register(models.Model):
    name = models.CharField(max_length=250, unique=True)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phone = models.IntegerField()
    mail = models.EmailField()
    address = models.TextField()


    class meta:
        ordering = ('name',)
        verbose_name = 'register'
        verbose_name_plural = 'registers'

    def __str__(self):
        return '{}'.format(self.name)


class Account(models.Model):
    name = models.CharField(max_length=250, unique=True)

    slug = models.SlugField(max_length=250, unique=True)

    class meta:
        ordering = ('name',)
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def get_url(self):
        return reverse('bankapp:a_by_details', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Materials(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class meta:
        ordering = ('name',)
        verbose_name = 'material'
        verbose_name_plural = 'materials'

    def get_url(self):
        return reverse('bankapp:m_by_details', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)
