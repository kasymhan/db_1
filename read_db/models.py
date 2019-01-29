from django.db import models


# Create your models here.


class BlogAbiturient(models.Model):
    name = models.TextField()
    area = models.OneToOneField('BlogArea', on_delete=models.DO_NOTHING, unique=True)
    city = models.OneToOneField('BlogCity', on_delete=models.DO_NOTHING, unique=True)
    country = models.OneToOneField('BlogCountr', on_delete=models.DO_NOTHING, unique=True)
    region = models.OneToOneField('BlogRegion', on_delete=models.DO_NOTHING, unique=True)


    def __str__(self):
        return self.name


class BlogApplication(models.Model):
    enlisted = models.BooleanField()
    abiturient = models.OneToOneField('BlogAbiturient', on_delete=models.DO_NOTHING, unique=True)
    special = models.OneToOneField('BlogSpecial', on_delete=models.DO_NOTHING, unique=True)



    def __str__(self):
        return self.name


class BlogArea(models.Model):
    name = models.TextField()
    out_id = models.IntegerField()


    def __str__(self):
        return self.name


class BlogCity(models.Model):
    name = models.TextField()
    out_id = models.IntegerField()


    def __str__(self):
        return self.name


class BlogCountr(models.Model):
    name = models.TextField()
    out_id = models.IntegerField()


    def __str__(self):
        return self.name


class BlogFacully(models.Model):
    name = models.TextField()
    out_id = models.IntegerField()


    def __str__(self):
        return self.name

class BlogRegion(models.Model):
    name = models.TextField()
    out_id = models.IntegerField()

    def __str__(self):
        return self.name


class BlogSpecial(models.Model):
    name = models.TextField()
    fac = models.OneToOneField('BlogFacully', on_delete=models.DO_NOTHING, unique=True)
    out_id = models.IntegerField()


    def __str__(self):
        return self.name
