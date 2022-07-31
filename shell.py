from main_app.models import Course, Student

c1 = Course.objects.get(name='Python')
# c1 = Course.objects.filter(name='Python')

# s = Student.objects.filter(course = c1, email='simura@internet.ru')

s = Student.objects.all()[:2]
print(s)