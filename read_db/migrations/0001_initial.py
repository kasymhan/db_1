# Generated by Django 2.1.5 on 2019-01-29 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAbiturient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enlisted', models.BooleanField()),
                ('abiturient', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='read_db.BlogAbiturient')),
            ],
        ),
        migrations.CreateModel(
            name='BlogArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCountr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogFacully',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogSpecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('out_id', models.IntegerField()),
                ('fac', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='read_db.BlogFacully')),
            ],
        ),
        migrations.AddField(
            model_name='blogapplication',
            name='special',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='read_db.BlogSpecial'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='area',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='read_db.BlogArea'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='read_db.BlogCity'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='country',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='read_db.BlogCountr'),
        ),
        migrations.AddField(
            model_name='blogabiturient',
            name='region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='read_db.BlogRegion'),
        ),
    ]
