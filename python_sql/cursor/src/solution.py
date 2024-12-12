import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect('postgresql://asgef:secret@localhost:5432/asgef_db')
