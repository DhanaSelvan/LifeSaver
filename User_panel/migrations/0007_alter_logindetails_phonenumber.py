# Generated by Django 4.2.5 on 2023-11-05 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_panel', '0006_alter_logindetails_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindetails',
            name='Phonenumber',
            field=models.CharField(default='', max_length=20),
        ),
    ]
