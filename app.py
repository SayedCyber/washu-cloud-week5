@app.route('/health')
def health():
    return "Healthy", 200
def home():
    return jsonify({
        "message": "Hello from WashU Week 5 - CI/CD Pipeline!",
        "platform": "ECS Fargate via GitHub Actions",
        "course": "Containers and Serverless",
        "version": "2.0"
    })
