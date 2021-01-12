# Generated by Django 3.1.4 on 2021-01-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about_faculty', models.CharField(max_length=400)),
                ('academic', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('faculty_website', models.URLField(blank=True)),
            ],
        ),
    ]
