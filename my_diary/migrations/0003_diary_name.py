# Generated by Django 4.2.4 on 2023-08-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_diary', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='name',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]