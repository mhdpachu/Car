# Generated by Django 5.1 on 2024-12-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carname', models.CharField(max_length=50)),
                ('Carimage', models.ImageField(upload_to='image')),
                ('Carmodels', models.IntegerField()),
                ('Owner', models.IntegerField()),
                ('History', models.TextField()),
                ('Contactnumber', models.IntegerField()),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
    ]