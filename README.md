# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## 🚀 Overview
A self-healing infrastructure project that detects service failures using Prometheus and Alertmanager and automatically resolves them using Ansible.

## 🔧 Tech Stack
- Prometheus
- Alertmanager
- Docker & Docker Compose
- Ansible
- Flask (Python webhook)
- NGINX

## 📦 Features
- Monitors NGINX availability via NGINX Exporter.
- Sends alerts using Alertmanager.
- Executes an Ansible playbook to restart NGINX when it goes down.
- Clean and modular Docker-based setup.

## 🚀 How It Works
1. **NGINX container** is deployed and monitored using **NGINX Prometheus Exporter**.
2. **Prometheus** scrapes metrics and triggers an alert when NGINX exporter is down.
3. **Alertmanager** sends this alert to a **custom Flask webhook**.
4. The **webhook** runs an **Ansible playbook** that restarts the NGINX container — achieving self-healing.

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

## 🧪 How to Run This Project
```bash
# Clone the repository
git clone https://github.com/faisalkhan158/self-healing-infra-project-1-2
cd self-healing-infra-project-1-2

# Start all services
```bash
docker-compose up -d --build

# To test the auto-heal:
```bash
docker stop nginx-app

see the magic of Auto-healing
