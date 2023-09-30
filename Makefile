run:
	docker-compose up

build: build_base_image
	docker-compose build

build_base_image:
	docker build --file=docker/Dockerfile .

migrate:
	docker-compose run web python manage.py migrate

createsuperuser:
	docker-compose run web python manage.py createsuperuser

test:
	docker-compose run web pytest -vv

clean:
	docker-compose down

clean_volumes:
	docker-compose down --volumes

lock:
	docker-compose run web pip-compile -v --generate-hashes --allow-unsafe --resolver=backtracking --strip-extras --output-file=requirements.txt requirements.in
	docker-compose run web pip-compile -v --generate-hashes --allow-unsafe --resolver=backtracking --strip-extras --output-file=requirements-dev.txt requirements-dev.in