from django.db import models

# Create a model for Department
class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# Create a model for Course
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create a model for Purpose
class Purpose(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create a model for the FormData
class FormData(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    materials_provided = models.ManyToManyField('Material')

    def __str__(self):
        return self.name

# Create a model for Materials
class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name