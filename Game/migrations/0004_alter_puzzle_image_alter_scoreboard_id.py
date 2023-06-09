# Generated by Django 4.2 on 2023-04-23 15:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0003_clues_clue1_clues_clue2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='image',
            field=models.ImageField(upload_to='Images'),
        ),
        migrations.AlterField(
            model_name='scoreboard',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
