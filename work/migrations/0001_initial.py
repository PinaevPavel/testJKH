# Generated by Django 2.0.5 on 2020-02-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accrual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('month', models.CharField(choices=[('Я', 'Январь'), ('Ф', 'Февраль'), ('Мр', 'Март'), ('А', 'Апрель'), ('М', 'Май'), ('Ин', 'Июнь'), ('Ил', 'Июль'), ('Ав', 'Август'), ('С', 'Сентябрь'), ('О', 'Октабрь'), ('Н', 'Ноябрь'), ('Д', 'Декабрь')], max_length=2)),
                ('pay', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Долг',
                'verbose_name_plural': 'Долги',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('month', models.CharField(choices=[('Я', 'Январь'), ('Ф', 'Февраль'), ('Мр', 'Март'), ('А', 'Апрель'), ('М', 'Май'), ('Ин', 'Июнь'), ('Ил', 'Июль'), ('Ав', 'Август'), ('С', 'Сентябрь'), ('О', 'Октабрь'), ('Н', 'Ноябрь'), ('Д', 'Декабрь')], max_length=2)),
                ('for_debt', models.BooleanField(default=False)),
                ('accrual', models.ManyToManyField(to='work.Accrual')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
