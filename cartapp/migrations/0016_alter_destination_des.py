# Generated by Django 4.2 on 2023-04-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0015_remove_destination_payability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='des',
            field=models.CharField(choices=[('OR', 'Original'), ('MI', 'Mirror'), ('EG', 'Egyptian'), ('SH', 'SHIRTS'), ('JA', 'JACKETS')], max_length=2),
        ),
    ]
