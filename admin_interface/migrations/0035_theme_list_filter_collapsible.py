from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0034_merge_20260303_2315"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="list_filter_collapsible",
            field=models.BooleanField(
                default=True,
                verbose_name="collapsible",
            ),
        ),
    ]
