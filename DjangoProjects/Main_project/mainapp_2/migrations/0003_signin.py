# Generated by Django 3.2.5 on 2021-07-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_2', '0002_fifth_standard_seventh_standard_sixth_standard'),
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=30)),
                ('Register_number', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=20)),
                ('Mobile_number', models.IntegerField()),
                ('Email_Id', models.CharField(max_length=20)),
            ],
        ),
    ]
