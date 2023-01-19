# Generated by Django 4.1.5 on 2023-01-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_singleimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='RightImage name')),
                ('name1', models.CharField(max_length=30, verbose_name='RightImage name1')),
                ('about', models.TextField(verbose_name='RightImage about')),
                ('about1', models.TextField(verbose_name='RightImage about1')),
                ('img', models.ImageField(upload_to='media', verbose_name='RightImage image')),
            ],
            options={
                'verbose_name': 'RightImage',
                'verbose_name_plural': 'RightImages',
            },
        ),
    ]
