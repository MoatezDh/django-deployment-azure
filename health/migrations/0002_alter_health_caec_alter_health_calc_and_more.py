# Generated by Django 5.0.2 on 2024-03-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='CAEC',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='CALC',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='Transportation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
