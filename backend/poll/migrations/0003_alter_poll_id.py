# Generated by Django 4.2.8 on 2023-12-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("poll", "0002_remove_voter_ip_address_alter_poll_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="poll",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
