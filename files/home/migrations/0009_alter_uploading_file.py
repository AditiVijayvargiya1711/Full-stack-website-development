# Generated by Django 5.0 on 2024-01-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_uploading_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploading',
            name='file',
            field=models.ImageField(default=None, max_length=1000, null=True, upload_to='media/'),
        ),
    ]
