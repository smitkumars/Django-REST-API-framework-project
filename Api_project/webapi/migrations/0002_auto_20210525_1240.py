# Generated by Django 3.2 on 2021-05-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('emp_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]