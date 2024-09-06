# Generated by Django 4.2.16 on 2024-09-06 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0002_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="crud.category",
            ),
            preserve_default=False,
        ),
    ]
