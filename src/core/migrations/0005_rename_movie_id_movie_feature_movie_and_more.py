# Generated by Django 4.1 on 2022-08-29 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_users_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie_feature", old_name="movie_id", new_name="movie",
        ),
        migrations.RenameField(
            model_name="vote", old_name="movie_id", new_name="movie",
        ),
    ]
