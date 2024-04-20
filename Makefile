
.PHONY: build
build: ## Build development docker container.
	docker build -t fastapi .

.PHONY: start
start: ## Start development docker container.
	docker stop fastapi || echo "Container not found"
	docker rm fastapi || echo "Container not found"
	docker run --name fastapi -p 5000:5000 -v ${PWD}:/app -d fastapi

.PHONY: logs
logs: ## Stop development docker container.
	docker logs fastapi -f

.PHONY: stop
stop: ## Stop development docker container.
	docker stop fastapi

.PHONY: run-test
run-test: ## Run SQLAlchemy migration
	pylint -ry app/ -sy
	pytest -s app/

.PHONY: shell
shell: ## Enter inside surgery container
	docker exec -it fastapi bash
