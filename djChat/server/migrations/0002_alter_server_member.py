# Generated by Django 5.1.3 on 2024-12-01 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="server",
            name="member",
            field=models.ManyToManyField(
                default=models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="sever_owner",
                    to=settings.AUTH_USER_MODEL,
                ),
                related_name="server_member",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
