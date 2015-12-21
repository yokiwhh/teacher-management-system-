# -*- coding: utf-8 -*-
from django.db import models

# Create your models here. 
class Major(models.Model):
    number = models.CharField(max_length=20)
    majorname = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['number']    
    
    def __unicode__(self):
        return u'%s %s' % (self.number, self.majorname)

class College(models.Model):
    number = models.CharField(max_length=20)
    collegename = models.CharField(max_length=100)

    class Meta:
        ordering = ['number']

    def __unicode__(self):
        return u'%s %s' % (self.number, self.collegename)

class Teacher(models.Model):
    kind = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    teacherID = models.CharField(max_length=10) 
    reseachdirection = models.ForeignKey(Major)
    college = models.ForeignKey(College)
    
    class Meta:
        ordering = ['name']    
    
    def __unicode__(self):
        return u'%s %s %s' % (self.kind, self.name, self.teacherID)
      
class Student(models.Model):
    kind = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    studentID = models.CharField(max_length=10)
    profession = models.ForeignKey(Major)
    college = models.ForeignKey(College)
    
    class Meta:
        ordering = ['name']    
    
    def __unicode__(self):
        return u'%s %s %s' % (self.kind, self.name, self.studentID)
    
class Message(models.Model):
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher)
    kind = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    class Meta:
        ordering = ['kind']
    
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (self.teacher.name, self.teacher.teacherID, self.student.name, self.student.studentID, self.kind, self.date, self.time)

class Busy(models.Model):
    teacher = models.ForeignKey(Teacher)
    kind = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['kind']

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.teacher.name, self.teacher.teacherID, self.kind, self.date, self.time)




    