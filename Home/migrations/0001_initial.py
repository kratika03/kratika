# Generated by Django 4.0.1 on 2022-01-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('contact', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=122)),
            ],
        ),
    ]
