# 🚀 GitOps Workflow using ArgoCD on Kubernetes

## 📖 Overview

This project implements a **GitOps workflow** using **ArgoCD** to continuously sync and deploy a Kubernetes application directly from a Git repository.

🎯 **Objective**: Automatically deploy and update a sample guestbook app using GitOps principles.

---

## 🛠️ Tools & Technologies

- 🧰 **Kubernetes (Minikube)**
- 📦 **ArgoCD**
- 🌐 **GitHub**
- 🐳 **Docker**
- 📄 **YAML (K8s manifests)**

---

## 📌 Steps Performed

1. ⚙️ **Set up Minikube on Local Machine**
2. 📥 **Installed ArgoCD in Kubernetes**
3. 📁 **Created a GitHub repo containing app manifest files**
4. 🚀 **Deployed the guestbook app using ArgoCD Application manifest**
5. 🔁 **Configured ArgoCD for automated sync (`syncPolicy.automated`)**
6. 🧪 **Tested the pipeline by changing Docker image version in `deployment.yaml`**
7. 👁️ **Verified auto-sync and rolling update via ArgoCD UI**
8. 🌍 **Application running and accessible via port-forwarding**

---

## 🧩 Conclusion

This project demonstrates how **Git** can act as the **single source of truth** in a CI/CD pipeline using ArgoCD. All Kubernetes deployments are managed **declaratively via Git**. Any update to the repo is automatically detected and synced by ArgoCD, ensuring **fast and reliable deployments**.
