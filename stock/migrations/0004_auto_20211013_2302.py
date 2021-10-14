# Generated by Django 3.2.8 on 2021-10-14 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0003_auto_20211013_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='added_by',
        ),
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
