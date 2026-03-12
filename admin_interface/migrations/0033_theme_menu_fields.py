from django.db import migrations, models

import colorfield.fields


# All three fields in this migration are also added by the parallel branch
# (0023_auto_20211018_2058 + 0024_theme_css_header_menu_accent_color).
# Use SeparateDatabaseAndState with IF NOT EXISTS for each to avoid
# DuplicateColumn errors when both branches run on a fresh database.


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0032_alter_theme_defaults"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
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
            ],
            database_operations=[
                migrations.RunSQL(
                    sql="ALTER TABLE admin_interface_theme ADD COLUMN IF NOT EXISTS css_header_menu_color varchar(10) DEFAULT '#0C4B33' NOT NULL",
                    reverse_sql=migrations.RunSQL.noop,
                ),
            ],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
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
            ],
            database_operations=[
                migrations.RunSQL(
                    sql="ALTER TABLE admin_interface_theme ADD COLUMN IF NOT EXISTS css_header_menu_accent_color varchar(10) DEFAULT '#0C3C26' NOT NULL",
                    reverse_sql=migrations.RunSQL.noop,
                ),
            ],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AddField(
                    model_name="theme",
                    name="css_module_menu_enabled",
                    field=models.BooleanField(
                        default=True,
                        verbose_name="menu enabled",
                    ),
                ),
            ],
            database_operations=[
                migrations.RunSQL(
                    sql="ALTER TABLE admin_interface_theme ADD COLUMN IF NOT EXISTS css_module_menu_enabled boolean DEFAULT true NOT NULL",
                    reverse_sql=migrations.RunSQL.noop,
                ),
            ],
        ),
    ]
