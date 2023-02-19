# Generated by Django 4.1.4 on 2023-02-14 13:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("title", models.CharField(max_length=200)),
                ("desc", models.TextField(blank=True, null=True)),
                ("demo_link", models.CharField(max_length=1000)),
                ("source_link", models.CharField(max_length=1000)),
                ("vote_total", models.ImageField(default=0, upload_to="")),
                ("vote_ratio", models.ImageField(default=0, upload_to="")),
                ("created", models.DateTimeField(auto_now_add=True)),
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
            ],
        ),
    ]
