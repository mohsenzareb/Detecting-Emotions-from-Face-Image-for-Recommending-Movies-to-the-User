# Generated by Django 4.1 on 2022-08-30 15:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_comedy_pic_fantasy_pic_horror_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Emotional_state_feature",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("emotional_state", models.CharField(max_length=7)),
                ("romance", models.IntegerField()),
                ("horror", models.IntegerField()),
                ("comedy", models.IntegerField()),
                ("action", models.IntegerField()),
                ("fantasy", models.IntegerField()),
                ("no_of_votes", models.IntegerField()),
            ],
        ),
    ]
