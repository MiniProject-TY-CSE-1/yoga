# Generated by Django 4.2.5 on 2023-10-02 17:08

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='', validators=[app.validators.file_size]),
        ),
    ]
