from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(null=True, max_length=200)
    familyMember = models.ManyToManyField("self", null=True)

    def __str__(self):
        return str(self.name)

class Client(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    msp = models.IntegerField(unique=True)
    sin = models.IntegerField(unique=True)
    password = models.CharField(max_length = 200)

    def __str__(self):
        return str(Person.objects.get(pk=self.person.id))

class Doctor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(Person.objects.get(pk=self.person.id))

class Hospital(models.Model):
    name = models.CharField(unique=True, max_length=200)
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return str(self.name)

class CreditCard(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    number = models.IntegerField(primary_key=True)
