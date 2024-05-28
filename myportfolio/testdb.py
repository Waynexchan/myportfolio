from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Test database connection and schema access'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            self.stdout.write(self.style.SUCCESS('Database connection successful'))

            cursor.execute(f'SET search_path TO portfolio')
            cursor.execute('SELECT table_name FROM information_schema.tables WHERE table_schema = %s', ['portfolio'])
            tables = cursor.fetchall()
            self.stdout.write(self.style.SUCCESS(f'Tables in schema "portfolio": {tables}'))
