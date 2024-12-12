lint:
	poetry run flake8 .

test:
	poetry run pytest .

test_psql:
	psql -U asgef -d asgef_db -f python_sql/workflow/init.sql
	poetry run pytest python_sql