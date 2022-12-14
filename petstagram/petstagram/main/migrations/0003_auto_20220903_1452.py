# Generated by Django 3.2.13 on 2022-09-03 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20220903_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='petphoto',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.petstagramuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='profiles/'),
        ),
    ]
