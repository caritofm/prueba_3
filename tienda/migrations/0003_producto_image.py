# Generated by Django 4.1.2 on 2024-07-03 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_cliente_email_cliente_name_cliente_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
