from django.contrib import admin
import read_db.models
from write_db.models import *
admin.site.register(BlogAbiturient)
admin.site.register(read_db.models.BlogAbiturient)