from django.db import models
from django.utils.timezone import now
class Student(models.Model):
    COURSES = [
        ('Web Development', 'Web Development'),
        ('Data Science', 'Data Science' ),
        ('Cyber Security', 'Cyber Security'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Software Engineering', 'Software Engineering'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Machine Learning', 'Machine Learning'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Blockchain', 'Blockchain'),
        
    ]

    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    photo = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Profile Photo")  
    address = models.CharField(max_length=100, verbose_name="Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    interested_course = models.CharField(max_length=50, choices=COURSES, verbose_name="Interested Course")
    remarks = models.TextField(verbose_name="Remarks")
    date_of_register = models.DateTimeField(default=now, verbose_name="Date of Registration")

    def __str__(self):
        return self.full_name
