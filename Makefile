# Include variables
include config.mk

## dist		: Prepare the package for distribution
.PHONY : dist
dist :
	$(RM) dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

## develop 	: Install the package in development mode
.PHONY : develop 
develop :
	python setup.py develop

## install	: Install the package
.PHONY : install
install :
	python setup.py install

## test		: Run tests
.PHONY : test
test :
	pytest --cov=pyleiades --cov-config=$(COVERAGE_CONFIG) --cov-report html

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
