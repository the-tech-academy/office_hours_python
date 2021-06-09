from django.db import models

# Create your models here.
class classManager(models.Manager):
    def create_class(self, Title, Course_Number, Instructor_Name, Duration):
        djangoClass = self.create(Title=Title, Course_Number=Course_Number, Instructor_Name=Instructor_Name, Duration=Duration)
        return djangoClass
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60)
    Duration = models.DecimalField(max_digits=1000, decimal_place=3)

    objects = classManager()

    def __str__(self):
        return self.Title

obj1 = djangoClasses.objects.create_class("Test1", 1, "Steve", 2.2)
obj2 = djangoClasses.objects.create_class("Test2", 2, "Julie", 0.3)
obj1 = djangoClasses.objects.create_class("Test3", 3, "Phillip", 1.8)
