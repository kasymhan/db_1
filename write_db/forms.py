from django import forms
import django.db
from django.core.exceptions import ValidationError
import read_db.models
import write_db.models

class Write(forms.ModelForm):
    class Meta:
        model = read_db.models.BlogAbiturient
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        new_name = str(self.cleaned_data['name'])
        db_1 = read_db.models.BlogAbiturient.objects.filter(name=new_name).values()
        db_2 = write_db.models.BlogAbiturient.objects.using('user').filter(name=new_name).values()
        if not db_1:
            raise ValidationError('нет такого пользователь ')
        if db_2:
            raise ValidationError('есть такой пользователь')
        else:
            return str(new_name)

    def write(self):
        global context
        try:
            new_name = self.cleaned_data['name']
            name_post = read_db.models.BlogAbiturient.objects.filter(name=new_name)
            abatement = name_post.values()
            lis = [abatement[0]['id'],
               abatement[0]['name'],
               abatement[0]['country_id'],
               abatement[0]['region_id'],
               abatement[0]['area_id'],
               abatement[0]['city_id']]
            countr = read_db.models.BlogCountr.objects.filter(id=lis[2]).values()
            region = read_db.models.BlogRegion.objects.filter(id=lis[3]).values()
            area = read_db.models.BlogArea.objects.filter(id=lis[4]).values()
            city = read_db.models.BlogCity.objects.filter(id=lis[5]).values()
            lis_countr = [
                countr[0]['name'],
                countr[0]['out'],
            ]
            lis_region = [
                region[0]['name'],
                region[0]['out'],
            ]
            lis_area = [
                area[0]['name'],
                area[0]['out'],
            ]
            lis_city = [
                city[0]['name'],
                city[0]['out'],
            ]
            special = read_db.models.BlogSpecial.objects.filter(out=lis_city[1]).values()[0]
            lis_special = [
                special['id'],
                special['name'],
                special['fac_id'],

            ]
            fac = read_db.models.BlogFacully.objects.filter(id=lis_special[2]).values()[0]
            lis_fac = [
                fac['name']

            ]
            app = read_db.models.BlogApplication.objects.filter(special=lis[0]).values()[0]
            lis_app = [
                app['enlisted']
            ]
            creat_area = write_db.models.BlogArea.objects.using('user').create(id=lis_area[1],name=lis_area[0])
            create_region = write_db.models.BlogRegion.objects.using('user').create(id=lis_region[1], name=lis_region[0]).save()
            creat_city = write_db.models.BlogCity.objects.using('user').create(id=lis_city[1], name=lis_city[0]).save()
            creat_countr = write_db.models.BlogCountr.objects.using('user').create(id=lis_countr[1], name=lis_countr[0]).save()
            creat_fac = write_db.models.BlogFacully.objects.using('user').create(id=lis_fac[1], name=lis_fac[0]).save()
            creat_special = write_db.models.BlogSpecial.objects.using('user').create(id=lis_special[1],name=lis_special[1],fac=creat_fac)
            creat_ab = write_db.models.BlogAbiturient.objects.using('user').create(name=lis[1],
                                                                                   area=creat_area,
                                                                                   city=creat_city,
                                                                                   country=creat_countr,
                                                                                   region=create_region)
            creat_app = write_db.models.BlogApplication.objects.using('user').create(abiturient=creat_ab,
                                                                                     enlisted=lis_app[0],
                                                                                     special=creat_special)
            return 'write_ok'
        except django.db.utils.IntegrityError:
            return  'update_id'

class Read(forms.ModelForm):
    class Meta:
        model = write_db.models.BlogAbiturient
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        new_name_1 = self.cleaned_data['name']
        db_1 = read_db.models.BlogAbiturient.objects.filter(name=new_name_1).values()
        if not db_1:
            raise ValidationError('нет такого пользователь ')
        else:
            raise ValidationError('есть такой пользователь')
        return new_name_1

    def read(self):
        new_name = self.cleaned_data['name']
        name_post =  read_db.models.BlogAbiturient.objects.filter(name=new_name)
        abiturient = name_post.values()
        lis = [abiturient[0]['id'],
               abiturient[0]['name'],
               abiturient[0]['country_id'],
               abiturient[0]['region_id'],
               abiturient[0]['area_id'],
               abiturient[0]['city_id']]
        countr =  read_db.models.BlogCountr.objects.filter(id=lis[2]).values()
        region = read_db.models.BlogRegion.objects.filter(id=lis[3]).values()
        area =  read_db.models.BlogArea.objects.filter(id=lis[4]).values()
        city =  read_db.models.BlogCity.objects.filter(id=lis[5]).values()
        lis_countr = [
            countr[0]['id'],
            countr[0]['name'],
            countr[0]['out_id'],
        ]
        lis_region = [
            region[0]['id'],
            region[0]['name'],
            region[0]['out_id'],
        ]
        lis_area = [
            area[0]['id'],
            area[0]['name'],
            area[0]['out_id'],
        ]
        lis_city = [
            city[0]['id'],
            city[0]['name'],
            city[0]['out_id'], ]
        context = {'name': lis[1], 'countr': lis_countr[1], 'region': lis_region[1], 'area': lis_area[1],
                   'city': lis_city[1]}
        return context


