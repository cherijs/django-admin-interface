from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_interface', '0036_alter_theme_css_module_menu_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='form_submit_sidebar',
            field=models.BooleanField(default=False, verbose_name='sidebar submit'),
        ),
    ]
