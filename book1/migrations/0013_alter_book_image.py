# Generated by Django 5.0.4 on 2024-04-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book1', '0012_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='meme.jpeg', null=True, upload_to='media/'),
        ),
    ]