# Generated by Django 4.0.5 on 2022-07-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0005_zonaniños'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregables',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='archivos'),
        ),
    ]
