.PHONY: help build serve test deploy

help:
	@echo 'Makefile for pythonineducation.org'
	@echo ''
	@echo 'Usage:'
	@echo '   make build    build the site into the output directory'
	@echo '   make serve    build the site and serve on port 8000, watching for changes'
	@echo '   make test     test that site builds, has no broken links, and spells the conference name correctly'
	@echo '   make deploy   deploy site'
	@echo ''

build:
	python manage.py buildsite

serve:
	python manage.py serve 8000

test:
	./pre-flight-checks.sh

deploy:
	./deploy.sh
