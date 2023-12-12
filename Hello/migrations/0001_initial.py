# Generated by Django 4.2.5 on 2023-10-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.IntegerField(max_length=4)),
                ('student_name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=30)),
                ('jdate', models.DateField()),
            ],
        ),
    ]
