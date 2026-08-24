"""Shared helpers for migrations."""

from django.db import migrations


class AddFieldIfNotExists(migrations.AddField):
    """AddField that skips the database change when the column already exists.

    Some fields were added on two parallel branches (0023/0024 vs 0033), so
    depending on which branch a database migrated through first, the column
    may already be present. Checking the live schema keeps the operation
    portable across backends (raw ``IF NOT EXISTS`` SQL is PostgreSQL-only
    and breaks SQLite).
    """

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        model = to_state.apps.get_model(app_label, self.model_name)
        table = model._meta.db_table
        with schema_editor.connection.cursor() as cursor:
            columns = [
                column.name
                for column in schema_editor.connection.introspection.get_table_description(
                    cursor, table
                )
            ]
        if self.name in columns:
            return
        super().database_forwards(app_label, schema_editor, from_state, to_state)

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        model = from_state.apps.get_model(app_label, self.model_name)
        table = model._meta.db_table
        with schema_editor.connection.cursor() as cursor:
            columns = [
                column.name
                for column in schema_editor.connection.introspection.get_table_description(
                    cursor, table
                )
            ]
        if self.name not in columns:
            return
        super().database_backwards(app_label, schema_editor, from_state, to_state)
