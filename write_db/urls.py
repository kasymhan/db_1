from django.urls import path
from write_db.views import *


urlpatterns = [
    path('', Site, name='home'),
    path('read/', Read_Abiturient.as_view(), name='read'),
    path('write/', Write_Abiturient.as_view(), name='write'),
    path('update/',Update.as_view(),name='update_id'),
    path('ok/',Ok.as_view(),name='write_ok')
]
