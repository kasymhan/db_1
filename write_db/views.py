from django.shortcuts import render , redirect
from django.views.generic import View
from write_db.forms import *


class Write_Abiturient(View):
    def get(self, request):
        abatement = Write()
        return render(request, 'write_db/write.html', context={'form': abatement})

    def post(self, request):
        abatement = Write(request.POST)
        if abatement.is_valid():
            absorbent_write = abatement.write()
            return redirect(absorbent_write)
        return render(request, 'write_db/write.html', context={'form': abatement})


class Read_Abiturient(View):

    def get(self, request):
        abatement = Read()
        return render(request, 'write_db/read.html', context={'form': abatement})

    def post(self, request):
        abatement = Read(request.POST)

        if abatement.is_valid():
            absorbent_read = abatement.read()
            return redirect(absorbent_read)
        return render(request, 'write_db/read.html', context={'form': abatement})

class Update(View):
    def get (self,request):
        abatement = 'обновити id'
        return render(request, 'write_db/update.html', context={'form': abatement})

class Ok(View):
    def get (self,request):
        abatement = 'пользователь перенаправлен'
        return render(request, 'write_db/update.html', context={'form': abatement})

def Site(request):
    return render(request, 'base.html')
