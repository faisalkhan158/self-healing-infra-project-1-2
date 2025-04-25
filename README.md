# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## 🚀 Overview
A self-healing infrastructure project that detects service failures using Prometheus and Alertmanager and automatically resolves them using Ansible.

## 🔧 Tech Stack
- Prometheus
- Alertmanager
- Docker & Docker Compose
- Ansible
- Flask (Python webhook)

## 📦 Features
- Monitors NGINX availability via NGINX Exporter.
- Sends alerts using Alertmanager.
- Executes an Ansible playbook to restart NGINX when it goes down.
- Clean and modular Docker-based setup.

## 📂 Project Structure
- `prometheus/` — Configs for Prometheus and alert rules
- `alertmanager/` — Alertmanager config with webhook
- `webhook/` — Python Flask app, Ansible playbook and Dockerfile
- `nginx/` — NGINX config
- `docker-compose.yml` — Everything bundled here

## ✅ Output
- Alert fired on Prometheus
- Webhook triggered and Ansible playbook executed
- NGINX container automatically restarted

## 📸 Screenshots
*(Screenshots available in the `screenshots/` directory)*

## 🧠 Author
Mohammed Faisal Khan
