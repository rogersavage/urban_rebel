# Generated by Django 4.2.15 on 2024-08-14 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.collection'),
        ),
    ]
