# Generated by Django 3.2.8 on 2021-10-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200, verbose_name='Nom du produit')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix du produit')),
                ('description', models.TextField(null=True, verbose_name='Description du produit')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
            ],
            options={
                'verbose_name': 'Produit',
                'ordering': ['-date_added'],
            },
        ),
    ]
