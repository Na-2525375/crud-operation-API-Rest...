# Generated by Django 5.0 on 2023-12-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Management_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Marks', models.CharField(max_length=100, null=True)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Students_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Marks', models.CharField(max_length=100, null=True)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Stuff_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Marks', models.CharField(max_length=100, null=True)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Marks', models.CharField(max_length=100, null=True)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
    ]
