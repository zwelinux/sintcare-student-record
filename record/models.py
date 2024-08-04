from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    experience = models.TextField()
    address = models.TextField()
    guardian = models.CharField(max_length=255)
    guardian_phone_number = models.CharField(max_length=255)
    person_ID = models.TextField()

    def __str__(self):
        return self.name
    
class Instructor(models.Model):

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    experience = models.TextField()
    address = models.TextField()
    person_ID = models.CharField(max_length=255)
    skill_set = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_duration = models.IntegerField()
    course_start_time = models.CharField(max_length=255)
    course_end_time = models.CharField(max_length=255)
    course_level = models.CharField(max_length=255)
    course_instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course_requirement = models.TextField()
    course_participant_count = models.TextField()

    def __str__(self):
        return self.course_name

class Registration(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_name = models.ForeignKey(User, on_delete=models.CASCADE)
    fees_amount = models.IntegerField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.student_name)

