# Generated by Django 2.2.4 on 2019-09-02 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0002_auto_20190901_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='created_at',
            new_name='realisacao',
        ),
    ]
