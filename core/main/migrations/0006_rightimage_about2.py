# Generated by Django 4.1.5 on 2023-01-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rightimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='rightimage',
            name='about2',
            field=models.TextField(null=True, verbose_name='RightImage about2'),
        ),
    ]