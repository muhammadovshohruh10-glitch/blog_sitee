from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name




class Genre(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ForeignKey(Author,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Fakultet(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Fanlar(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ForeignKey(Author,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Universitet(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL)
    fanlar = models.ForeignKey(Fanlar, null=True, on_delete=models.CASCADE)
    fakultet = models.ForeignKey(Fakultet, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    universitet = models.ForeignKey(Universitet, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
