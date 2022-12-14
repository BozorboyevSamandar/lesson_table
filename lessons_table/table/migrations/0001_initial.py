# Generated by Django 3.2 on 2022-08-03 08:02

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)])),
            ],
            options={
                'ordering': ('classroom_number',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=150)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)])),
            ],
            options={
                'ordering': ('group_name',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.CharField(max_length=13)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.studentgroup')),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
        migrations.CreateModel(
            name='LessonTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday')], max_length=150)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 3, 13, 2, 25, 876944), null=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.classroom')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.studentgroup')),
                ('lesson_name', models.ManyToManyField(to='table.Lesson')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.teacher')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
