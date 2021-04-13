# Generated by Django 3.1.7 on 2021-04-11 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0007_auto_20210411_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='helper.question'),
        ),
    ]