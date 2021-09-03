PYTHON_VERSION := 3.8.2
ALPINE_VERSION := 3.11

DOCKER_REPO := michalsw
NAME := notejam-k8s
APP_PORT := 5000
DOCKER_VOLUME := notejamdb

VERSION ?= $(shell git describe --tags --always)
BUILD_TIME ?= $(shell date -u '+%Y-%m-%d %H:%M:%S')
LAST_COMMIT_USER ?= $(shell git log -1 --format='%cn <%ce>')
LAST_COMMIT_HASH ?= $(shell git log -1 --format=%H)
LAST_COMMIT_TIME ?= $(shell git log -1 --format=%cd --date=format:'%Y-%m-%d %H:%M:%S')

.DEFAULT_GOAL := help
.PHONY: help build run logs stop

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ \
	{ printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

build: ## Build docker image
	docker build \
	--pull \
	--build-arg PYTHON_VERSION="$(PYTHON_VERSION)" \
	--build-arg ALPINE_VERSION="$(ALPINE_VERSION)" \
	--label="build.version=$(VERSION)" \
	--label="build.time=$(BUILD_TIME)" \
	--label="commit.user=$(LAST_COMMIT_USER)" \
	--label="commit.hash=$(LAST_COMMIT_HASH)" \
	--label="commit.time=$(LAST_COMMIT_TIME)" \
	--tag="$(DOCKER_REPO)/$(NAME):$(VERSION)" \
	.

run: ## Create docker volume and run docker container
	docker volume create $(DOCKER_VOLUME) && \
	docker run -d --rm \
	--name $(NAME) \
	-p $(APP_PORT):$(APP_PORT) \
	-v $(DOCKER_VOLUME):/tmp/app/notejam/ \
	"$(DOCKER_REPO)/$(NAME):$(VERSION)"

logs: ## Get logs from docker container
	docker logs -f $(NAME)

stop: ## Stop docker container and remove docker volume
	docker stop $(NAME)
	docker volume remove $(DOCKER_VOLUME)
 