.PHONY: docs
init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock
test:
	pipenv run python setup.py test

flake8:
	pipenv run flake8 --ignore=E501,F401,E128,E402,E731,F821 pyionic

coverage:
	pipenv run coverage run --append setup.py test

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg requests.egg-info

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
