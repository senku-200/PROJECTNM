# Generated by Django 4.2 on 2023-04-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_user_firstname_alter_user_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]