# Generated by Django 4.1 on 2022-08-29 21:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_action_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comedy_pic",
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
                (
                    "image",
                    models.ImageField(
                        blank=True, default="default_movie.png", null=True, upload_to=""
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fantasy_pic",
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
                (
                    "image",
                    models.ImageField(
                        blank=True, default="default_movie.png", null=True, upload_to=""
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Horror_pic",
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
                (
                    "image",
                    models.ImageField(
                        blank=True, default="default_movie.png", null=True, upload_to=""
                    ),
                ),
            ],
        ),
    ]
