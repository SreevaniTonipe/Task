# Generated by Django 2.0 on 2020-02-09 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField()),
                ('task_desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_type', models.DateField()),
                ('task_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.Task')),
            ],
        ),
    ]