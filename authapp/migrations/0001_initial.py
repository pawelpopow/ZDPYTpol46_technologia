# Generated by Django 4.0.3 on 2022-04-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]
