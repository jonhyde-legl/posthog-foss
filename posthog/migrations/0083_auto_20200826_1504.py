# Generated by Django 3.0.7 on 2020-08-26 15:04

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0082_personalapikey"),
    ]

    operations = [
        migrations.AddField(model_name="team", name="ingested_event", field=models.BooleanField(default=False),),
        migrations.AddField(
            model_name="team", name="uuid", field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]