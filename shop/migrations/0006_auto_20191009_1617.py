# Generated by Django 2.2.6 on 2019-10-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_reg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]