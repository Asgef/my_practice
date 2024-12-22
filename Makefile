lint:
	poetry run flake8 .

test:
	poetry run pytest .

test_js:
	npm run test

test_psql:
	psql -U asgef -d asgef_db -f python_sql/dao/init.sql
	poetry run pytest ./python_sql/dao/tests -vv