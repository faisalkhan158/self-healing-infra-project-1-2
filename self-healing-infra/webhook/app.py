from flask import Flask, request
import subprocess
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", json.dumps(data, indent=2))

    # You can customize this logic based on the alert name
    if data["alerts"][0]["status"] == "firing":
        print("⚠️ Alert is firing! Executing Ansible playbook...")
        subprocess.run(["ansible-playbook", "restart-nginx.yml"])

    return 'Webhook received!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
 
