# Generated by Django 4.1.7 on 2023-02-23 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='created_by',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='created_by',
            field=models.CharField(max_length=200, null=True),
        ),
    ]