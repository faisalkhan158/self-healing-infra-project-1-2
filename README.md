# Self-Healing Infra & GitOps with ArgoCD 🚀

This repository contains two DevOps projects that demonstrate modern automation and GitOps principles using Prometheus, Alertmanager, Ansible, ArgoCD, and Kubernetes.

---

## 📁 Projects Included

### 1. **Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible** 🛠️

**Objective:** Automatically detect service failures and recover them using alerts and automation.

**Tools Used:**  
Prometheus, Alertmanager, Python Flask (Webhook), Ansible, Docker, Docker Compose, NGINX, AWS EC2 (Ubuntu)

**Highlights:**  
- Monitors an `nginx-app` using Prometheus.
- Triggers alerts via Alertmanager when the service is down.
- Webhook (Flask app) executes an Ansible playbook to restart the container.
- Fully containerized setup using Docker Compose.
- Self-healing in action with screenshots and logs.

📁 Project Directory: `self-healing-infra/`  
📷 Screenshots: `self-healing-infra/screenshots`  
📄 Project Report: `Self-Healing-Infra-Report.pdf`  
📜 Readme: [`self-healing-infra/README.md`](./self-healing-infra/README.md)

---

### 2. **GitOps Workflow using ArgoCD on Kubernetes** ⚙️

**Objective:** Implement GitOps by syncing Kubernetes deployment states directly from a Git repository using ArgoCD.

**Tools Used:**  
ArgoCD, Minikube, GitHub, Docker, kubectl

**Highlights:**  
- Built and deployed a custom Guestbook frontend container image.
- Used ArgoCD to sync Kubernetes manifests from GitHub.
- Auto-sync tested by updating image version via Git commit.
- Included notes and screenshots explaining GitOps flow.

📁 Project Directory: `gitops-argocd-project/guestbook-app/`  
📷 Screenshots: `gitops-argocd-project/screenshots/`  
📝 GitOps Flow Notes: `GitOps-Flow-Notes.txt`  
📜 Readme: [`gitops-argocd-project/guestbook-app/README.md`](./gitops-argocd-project/guestbook-app/README.md)

---

## 📌 Final Notes

- ✅ Both projects follow best practices and are well documented.
- ✅ Fully working implementations tested on local Minikube and AWS EC2.
- ✅ Ideal for showcasing in interviews and DevOps portfolios.

> **Note:** This repo is structured as per internship guidelines — both projects are placed in a single repository with individual directories, readmes, screenshots, and required deliverables.

---

## 🧠 Author
Mohammed Faisal Khan

---

Thanks for checking out the projects! Feel free to explore and give a ⭐ if you found it helpful!
