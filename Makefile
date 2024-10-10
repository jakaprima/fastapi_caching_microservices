# Makefile

# Variables
APP_NAME = fastapi-cache-service
IMAGE_NAME = $(APP_NAME)
CONTAINER_NAME = $(APP_NAME)_container
DOCKER_COMPOSE_FILE = docker-compose.yml

.PHONY: all build run stop remove

build:
	docker compose -f $(DOCKER_COMPOSE_FILE) build

run:
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d

stop:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

remove:
	docker rm -f $(CONTAINER_NAME)

update: build stop run

# Default target
all: update
