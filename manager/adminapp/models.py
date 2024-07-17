from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.name}, {self.country.name}"

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.name}, {self.state.name}"

class Institution(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='institutions')
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return f"{self.name}, {self.city.name}"

class Department(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return f"{self.name}, {self.institution.name}"

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return f"{self.name}, {self.department.name}"

class Stream(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='streams')
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return f"{self.name}, {self.course.name}"

class Semester(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='semesters')
    number = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Semester {self.number}, {self.stream.name}"

class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.name} ({self.code}), Semester {self.semester.number}"
