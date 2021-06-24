from django.db import models

# Create your models here.9
from .utils import create_slug


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Название населённого пункта",
                            unique=True)
    slug = models.CharField(max_length=50,
                            blank=True,
                            unique=True)


    class Meta:
        verbose_name = "Название населённого пункта"
        verbose_name_plural = "Название населённых пунктов"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name)
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Язык программирования",
                            unique=True)
    slug = models.CharField(max_length=50,
                            blank=True,
                            unique=True)

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name)
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250,
                            verbose_name='Название вакансии')
    company = models.CharField(max_length=250,
                            verbose_name='Название компании')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True,
                                 verbose_name='Вряме сохранения')

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title

