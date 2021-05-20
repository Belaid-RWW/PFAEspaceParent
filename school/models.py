from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('1ère année','1ère année'),
('2ème année Sciences','2ème année Sciences'),
('2ème année Lettres','2ème année Lettres'),
('2ème année Eco & Gestion','2ème année Eco & Gestion'),
('2ème année Informatique','2ème année Informatique'),
('3ème année Sciences','3ème année Sciences'),
('3ème année Lettres','3ème année Lettres'),
('3ème année Eco & Gestion','3ème année Eco & Gestion'),
('3ème année Informatique','3ème année Informatique'),
('4ème année Sciences','4ème année Sciences'),
('4ème année Lettres','4ème année Lettres'),
('4ème année Eco & Gestion','4ème année Eco & Gestion'),
('4ème année Informatique','4ème année Informatique'),]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=30,choices=classes,default='1ère année')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)


class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)

class Marks(models.Model):
    Class=models.CharField(max_length=30,choices=classes,default='1ère année')
    Matière=models.CharField(max_length=10,null=True)
    Note=models.PositiveIntegerField(null=True)
    Coefficient=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.Matière
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name


class Punitions(models.Model):
    Class=models.CharField(max_length=30,choices=classes,default='1ère année')
    Reason=models.CharField(max_length=30,null=True)
    Decision=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.Reason


class Emplois(models.Model):
    Class=models.CharField(max_length=30,choices=classes,default='1ère année')
    Emp=models.FileField(null=True)
    def __str__(self):
        return self.Class

    def get_absolute_url(self):
        return reverse('x:y',kwargs={"pk": self.pk})


class ListEmplois(models.Model):
    Classe=models.CharField(max_length=100)
    pdf = models.FileField()
    
 