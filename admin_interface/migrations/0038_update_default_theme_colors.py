import colorfield.fields
from django.db import migrations, models


OLD_TO_NEW = {
    "title_color": ("#F5DD5D", "#FFFFFF"),
    "css_header_background_color": ("#0C4B33", "#252830"),
    "css_header_text_color": ("#44B78B", "#5bb0ed"),
    "css_header_link_hover_color": ("#C9F0DD", "#5bb0ed"),
    "css_header_menu_color": ("#0C4B33", "#383d4b"),
    "css_header_menu_accent_color": ("#0C3C26", "#4298DE"),
    "css_module_background_color": ("#44B78B", "#5d6478"),
    "css_module_background_selected_color": ("#FFFFCC", "#f1f1f1"),
    "css_module_link_hover_color": ("#C9F0DD", "#5bb0ed"),
    "css_generic_link_color": ("#0C3C26", "#0d64a2"),
    "css_generic_link_hover_color": ("#156641", "#4298DE"),
    "css_generic_link_active_color": ("#29B864", "#5bb0ed"),
    "css_save_button_background_color": ("#0C4B33", "#0d64a2"),
    "css_save_button_background_hover_color": ("#0C3C26", "#252830"),
}


def update_theme_colors(apps, schema_editor):
    Theme = apps.get_model("admin_interface", "Theme")
    for theme in Theme.objects.all():
        changed = False
        for field, (old_val, new_val) in OLD_TO_NEW.items():
            current = getattr(theme, field, None)
            if current == old_val or current == old_val.upper() or current == old_val.lower():
                setattr(theme, field, new_val)
                changed = True
        if changed:
            theme.save()


def revert_theme_colors(apps, schema_editor):
    Theme = apps.get_model("admin_interface", "Theme")
    for theme in Theme.objects.all():
        changed = False
        for field, (old_val, new_val) in OLD_TO_NEW.items():
            current = getattr(theme, field, None)
            if current == new_val or current == new_val.upper() or current == new_val.lower():
                setattr(theme, field, old_val)
                changed = True
        if changed:
            theme.save()


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0037_theme_form_submit_sidebar"),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='css_generic_link_active_color',
            field=colorfield.fields.ColorField(blank=True, default='#5bb0ed', help_text='#5bb0ed', image_field=None, max_length=10, samples=None, verbose_name='link active color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_generic_link_color',
            field=colorfield.fields.ColorField(blank=True, default='#0d64a2', help_text='#0d64a2', image_field=None, max_length=10, samples=None, verbose_name='link color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_generic_link_hover_color',
            field=colorfield.fields.ColorField(blank=True, default='#4298DE', help_text='#4298DE', image_field=None, max_length=10, samples=None, verbose_name='link hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_background_color',
            field=colorfield.fields.ColorField(blank=True, default='#252830', help_text='#252830', image_field=None, max_length=10, samples=None, verbose_name='background color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_link_hover_color',
            field=colorfield.fields.ColorField(blank=True, default='#5bb0ed', help_text='#5bb0ed', image_field=None, max_length=10, samples=None, verbose_name='link hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_menu_accent_color',
            field=colorfield.fields.ColorField(blank=True, default='#4298DE', help_text='#4298DE', image_field=None, max_length=10, samples=None, verbose_name='menu accent color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_menu_color',
            field=colorfield.fields.ColorField(blank=True, default='#383d4b', help_text='#383d4b', image_field=None, max_length=10, samples=None, verbose_name='menu color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_header_text_color',
            field=colorfield.fields.ColorField(blank=True, default='#5bb0ed', help_text='#5bb0ed', image_field=None, max_length=10, samples=None, verbose_name='text color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_background_color',
            field=colorfield.fields.ColorField(blank=True, default='#5d6478', help_text='#5d6478', image_field=None, max_length=10, samples=None, verbose_name='background color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_background_selected_color',
            field=colorfield.fields.ColorField(blank=True, default='#f1f1f1', help_text='#f1f1f1', image_field=None, max_length=10, samples=None, verbose_name='background selected color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_link_hover_color',
            field=colorfield.fields.ColorField(blank=True, default='#5bb0ed', help_text='#5bb0ed', image_field=None, max_length=10, samples=None, verbose_name='link hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_module_menu_enabled',
            field=models.BooleanField(default=True, help_text="Enable the navigation menu bar. To customise menu items, set <code>ADMIN_INTERFACE_MENU</code> in your settings to a subclass of <code>MenuManager</code>:<pre style='margin:8px 0;padding:10px 14px;background:#f6f6f6;border:1px solid #ddd;border-radius:4px;font-size:12px;line-height:1.5'>ADMIN_INTERFACE_MENU = 'myapp.admin_menu.MenuConfig'</pre><pre style='margin:0;padding:10px 14px;background:#f6f6f6;border:1px solid #ddd;border-radius:4px;font-size:12px;line-height:1.5'>from admin_interface.menu import ChildItem, MenuManager, ParentItem\n\nclass MenuConfig(MenuManager):\n    def __init__(self, available_apps, context, request):\n        super().__init__(available_apps, context, request)\n        self.menu = [\n            ParentItem('My App', children=[\n                ChildItem('Items', model='myapp.item'),\n                ChildItem('External', url='https://example.com', target_blank=True),\n            ]),\n        ]</pre>", verbose_name='menu enabled'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_save_button_background_color',
            field=colorfield.fields.ColorField(blank=True, default='#0d64a2', help_text='#0d64a2', image_field=None, max_length=10, samples=None, verbose_name='background color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='css_save_button_background_hover_color',
            field=colorfield.fields.ColorField(blank=True, default='#252830', help_text='#252830', image_field=None, max_length=10, samples=None, verbose_name='background hover color'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title_color',
            field=colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='#FFFFFF', image_field=None, max_length=10, samples=None, verbose_name='color'),
        ),
        migrations.RunPython(update_theme_colors, revert_theme_colors),
    ]
