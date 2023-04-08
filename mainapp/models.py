from django.db import models

from datetime import timedelta
from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()

class School(models.Model):
    logo= models.ImageField (upload_to="image/",null=True, blank=True)
    whatsapp=models.URLField(verbose_name='Вотсап',null=True, blank=True)
    twitter= models.URLField(verbose_name='Твиттер',null=True, blank=True)
    facebook= models.URLField(verbose_name='Фейсбук',null=True, blank=True)
    name= models.CharField(max_length=120,verbose_name='Название',null=True, blank=True)
    description= models.TextField(verbose_name='Описание',null=True, blank=True)
    admissiontouniversity= models.CharField(max_length=120,verbose_name='Поступлений в Университет',null=True, blank=True)
    staff = models.CharField(max_length=120, verbose_name='Сотрудников',null=True, blank=True)
    students = models.PositiveIntegerField(verbose_name='Количествое учеников',null=True, blank=True)
    successworkyear= models.CharField(max_length=120,verbose_name='Успешных лет',null=True, blank=True)
    mail= models.URLField(verbose_name='Почта')
    address=models.CharField(max_length=120,verbose_name= 'Адрес')
    number=models.PositiveIntegerField(verbose_name='Номер')
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    number3 = models.IntegerField()
    discriptions2 = models.TextField()
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Школа'
        verbose_name_plural='Школы'

class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    position= models.CharField(max_length=120,verbose_name='Должность')
    name= models.CharField(max_length=120,verbose_name='Имя')
    photo  = models.ImageField(upload_to="image/",verbose_name='Фото')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Учитель'
        verbose_name_plural = 'Учителя'

class Galeria(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='galleries')
    photo = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=127,verbose_name='название',null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Rewiew(models.Model):
    School = models.ForeignKey(to=School, on_delete=models.CASCADE, related_name='rewiews')
    photo = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=127,verbose_name='название',null=True)
    parent = models.CharField(max_length=127,verbose_name='родитель')
    description = models.TextField(verbose_name='описание')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = verbose_name + 'ы'


# class News(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     last_viewed_by = models.ForeignKey(User, related_name="last_viewed_articles", on_delete=models.CASCADE)
#     last_viewed_at = models.DateField(auto_now_add=True)
#     today = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'Новость'
#         verbose_name_plural = 'Новости'

class Newss(models.Model):
    School = models.ForeignKey(to=School, on_delete=models.CASCADE, related_name='newsss')
    author = models.CharField(max_length=120, verbose_name='Автор')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField()#auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'   

    @property
    def create_date(self):
        now = date.today()
        delta = now - self.created_at
        return delta.days 
        