# Generated by Django 3.1.4 on 2021-01-11 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nitkapp', '0007_auto_20210110_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coursesinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
    ]
