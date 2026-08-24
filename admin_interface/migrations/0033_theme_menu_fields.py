from django.db import migrations, models

import colorfield.fields

from admin_interface.migration_operations import AddFieldIfNotExists

# All three fields in this migration are also added by the parallel branch
# (0023_auto_20211018_2058 + 0024_theme_css_header_menu_accent_color).
# AddFieldIfNotExists skips the database change when the column is already
# present, whichever branch ran first, and works on every backend.


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0032_alter_theme_defaults"),
    ]

    operations = [
        AddFieldIfNotExists(
            model_name="theme",
            name="css_header_menu_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#0C4B33",
                help_text="#0C4B33",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="menu color",
            ),
        ),
        AddFieldIfNotExists(
            model_name="theme",
            name="css_header_menu_accent_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#0C3C26",
                help_text="#0C3C26",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="menu accent color",
            ),
        ),
        AddFieldIfNotExists(
            model_name="theme",
            name="css_module_menu_enabled",
            field=models.BooleanField(
                default=True,
                verbose_name="menu enabled",
            ),
        ),
    ]
