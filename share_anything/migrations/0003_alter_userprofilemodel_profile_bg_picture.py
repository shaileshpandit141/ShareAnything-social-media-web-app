# Generated by Django 4.2.3 on 2023-10-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_anything', '0002_alter_postmodel_code_text_alter_postmodel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='profile_bg_picture',
            field=models.ImageField(default='/share_anything/media/default-user-bg.jpg', upload_to='profile_pics/bg'),
        ),
    ]