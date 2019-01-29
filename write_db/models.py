from django.db import models

# Create your models here.



class BlogAbiturient(models.Model):
    name = models.TextField()
    area = models.OneToOneField('BlogArea', on_delete=models.DO_NOTHING, unique=True)
    city = models.OneToOneField('BlogCity', on_delete=models.DO_NOTHING, unique=True)
    country = models.OneToOneField('BlogCountr', on_delete=models.DO_NOTHING, unique=True)
    region = models.OneToOneField('BlogRegion', on_delete=models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'blog_abiturient'


class BlogApplication(models.Model):
    enlisted = models.BooleanField()
    abiturient = models.OneToOneField(BlogAbiturient, on_delete=models.DO_NOTHING, unique=True)
    special = models.OneToOneField('BlogSpecial', on_delete=models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'blog_application'


class BlogArea(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_area'


class BlogCity(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_city'


class BlogCountr(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_countr'


class BlogFacully(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_facully'


class BlogRegion(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_region'


class BlogSpecial(models.Model):
    name = models.TextField()
    fac = models.OneToOneField(BlogFacully, on_delete=models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'blog_special'

