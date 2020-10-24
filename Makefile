reqs:
	pip freeze > requirements.txt

deploy:
	git push origin master

migrate:
	heroku run python manage.py migrate

createsuperuser:
	heroku run python manage.py createsuperuser
	
rqstats:
	heroku run python manage.py rqstats
	
shell:
	heroku run python manage.py shell
	
test:
	python manage.py test
	
coverage:
	coverage run manage.py test
	coverage report
	coverage html