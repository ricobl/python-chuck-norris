test: clean
	@nosetests --verbose --with-coverage --cover-package=chuck -sd
	@pep8 *.py
clean:
	@find . -name "*.pyc" -delete
	@rm -rf build/ dist/ *.egg-info/ .coverage
upload:
	@sudo python setup.py sdist upload --show-response
