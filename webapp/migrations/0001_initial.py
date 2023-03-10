# Generated by Django 4.1.6 on 2023-02-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Задача')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('date_todo', models.CharField(max_length=10, verbose_name='Исполнить до')),
                ('state', models.CharField(max_length=10, verbose_name='Состояние')),
            ],
        ),
    ]
