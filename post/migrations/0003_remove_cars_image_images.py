# Generated by Django 5.0.4 on 2024-05-07 10:39

import django.db.models.deletion
import post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_cars_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='image',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=post.models.get_image_filename, verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post.cars')),
            ],
        ),
    ]