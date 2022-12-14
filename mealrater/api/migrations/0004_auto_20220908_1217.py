# Generated by Django 3.2 on 2022-09-08 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_rating_drink'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='drink',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='api.drink'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='meal',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='api.meal'),
        ),
    ]
