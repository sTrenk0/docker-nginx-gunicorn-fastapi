.PHONY: up down full_down reload_nginx

up:
	docker compose up -d --build

down:
	docker compose down

full_down:
	docker compose down -v

reload_nginx:
	docker compose restart nginx
