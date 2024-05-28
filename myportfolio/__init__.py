from django.conf import settings
from django.db import connection

SCHEMA = 'portfolio'

def set_search_path():
    with connection.cursor() as cursor:
        cursor.execute(f'SET search_path TO {SCHEMA}')

set_search_path()
