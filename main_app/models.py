from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование курса',
                            help_text='Введите наименование курса')
    description = models.TextField(verbose_name='Краткое описание курса', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Student(models.Model):
    age = models.IntegerField(verbose_name='Возраст', blank=True, null=True)
    email = models.EmailField(verbose_name='Электронка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        db_table = 'students'

    def __str__(self):
        return self.email
