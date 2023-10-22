# Generated by Django 4.2.3 on 2023-10-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_anything', '0005_alter_userprofilemodel_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='code_text',
            field=models.TextField(default='null', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default='null', null=True, upload_to='user_post_image/'),
        ),
    ]