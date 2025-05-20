import re
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

cyrillic_slug_validator = RegexValidator(
    regex=r'^[-\w\u0400-\u04FF]+$',  # \u0400-\u04FF — диапазон кириллицы в Unicode
    message='Slug может содержать только буквы, цифры, дефисы и подчёркивания.'
)

def cyrillic_slugify(value):
    value = value.lower()  # в нижний регистр
    value = re.sub(r'\s+', '-', value)  # пробелы → дефисы
    # удалить всё, кроме букв (кириллица и латиница), цифр, дефисов и подчёркиваний
    value = re.sub(r'[^\w\-а-яё0-9]', '', value, flags=re.UNICODE)
    return value


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    about = models.CharField(max_length=500, verbose_name='Краткое описание')
    slug = models.CharField(max_length=255,
        unique=True,
        validators=[cyrillic_slug_validator],
        blank=True,
        null=True)
    content = models.TextField(verbose_name='Текст')
    banner = models.ImageField(upload_to='post_image', verbose_name='Баннер записи')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='Дата редактирования')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = cyrillic_slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Получаем прямую ссылку на статью
        """
        return reverse('post_detail', kwargs={'slug': self.slug})


class Club(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='Slug')
    manager = models.CharField(max_length=200, verbose_name='Руководитель клуба')
    about = models.TextField(verbose_name='Описание')
    students = models.IntegerField(verbose_name='Количество занимающихся')
    district = models.CharField(max_length=100, verbose_name='Район')
    main_address = models.CharField(max_length=300, verbose_name='Адрес главного зала')
    image = models.ImageField(upload_to='club', verbose_name='Лого клуба')
    url = models.URLField(verbose_name='Сайт', blank=True, null=True)

    def __str__(self):
        return self.name


class Filial(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    address = models.CharField(max_length=300, verbose_name='Адрес')
    trainer = models.CharField(max_length=200, verbose_name='Главный тренер')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name='Клуб')

    def __str__(self):
        return f'{self.name} {self.address}'


class Staff(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    mid_name = models.CharField(max_length=100, verbose_name='Отчество')
    position = models.CharField(max_length=150, verbose_name='Должность')
    about = models.CharField(max_length=300, verbose_name='Описание')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    ava = models.ImageField(upload_to='staff', verbose_name='Изображение')

    def __str__(self):
        return f'{self.last_name} {self.name}'
