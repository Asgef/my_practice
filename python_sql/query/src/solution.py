import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect('postgresql://asgef:secret@localhost:5432/asgef_db')
