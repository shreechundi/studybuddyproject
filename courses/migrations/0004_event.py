# Generated by Django 4.1.1 on 2022-11-07 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_student_class_list_alter_department_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
