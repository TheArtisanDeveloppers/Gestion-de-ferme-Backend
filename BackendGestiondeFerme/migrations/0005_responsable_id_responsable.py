# Generated by Django 4.1.7 on 2023-03-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendGestiondeFerme', '0004_delete_drink_remove_responsable_id_responsable'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsable',
            name='id_responsable',
            field=models.IntegerField(null=True),
        ),
    ]