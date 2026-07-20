load:
	python src/etl/loader.py

test:
	pytest

clean:
	python clean.py

dashboard:
	python dashboard/app.py

report:
	python reports/report.py

api:
	python api/main.py

ratios:
	python src/etl/ratios.py