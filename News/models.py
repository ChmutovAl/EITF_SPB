from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    about = models.CharField(max_length=500, verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Текст')
    banner = models.ImageField(upload_to='post_image', verbose_name='Баннер записи')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='Дата редактирования')

    def __str__(self):
        return self.title


class Club(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название')
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
