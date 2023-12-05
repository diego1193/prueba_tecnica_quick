# Makefile

.PHONY: web web-logs celery celery-logs stop

web:
	python manage.py runserver > /dev/null 2>&1 &

celery:
	celery -A prueba_quick worker --loglevel=info > /dev/null 2>&1 &

web-logs:
	python manage.py runserver

celery-logs:
	celery -A prueba_quick worker --loglevel=info

stop:
	-pkill -f 'python manage.py runserver'
	-pkill -f 'celery -A prueba_quick worker'