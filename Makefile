test: clean
	@nosetests --verbose --with-coverage --cover-package=chuck -sd
clean:
	@find . -name "*.pyc" -delete
	@rm -rf build/ dist/ *.egg-info/
