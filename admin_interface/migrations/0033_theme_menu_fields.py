from django.db import migrations, models

import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0032_alter_theme_defaults"),
    ]

    operations = [
        migrations.AddField(
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
        migrations.AddField(
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
        migrations.AddField(
            model_name="theme",
            name="css_module_menu_enabled",
            field=models.BooleanField(
                default=True,
                verbose_name="menu enabled",
            ),
        ),
    ]
