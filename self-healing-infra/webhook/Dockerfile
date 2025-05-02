# webhook/Dockerfile

FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Ansible + dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends ansible python3-requests sshpass && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy code
COPY app.py restart-nginx.yml ./

CMD ["python3", "app.py"]
 
