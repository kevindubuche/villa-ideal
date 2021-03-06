# Generated by Django 3.2.8 on 2021-10-14 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0006_auto_20211014_1009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Catégorie de produit'},
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quatity', models.PositiveIntegerField(default=0, help_text='Entrez la quantité du produit', verbose_name='Quantité*')),
                ('cost', models.DecimalField(decimal_places=3, default=0.0, help_text='Entrez le prix de vente du produit (sensible au millième)', max_digits=10, verbose_name='Prix de vente du produit*')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.product', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'Vente',
                'ordering': ['-date_added'],
            },
        ),
    ]
