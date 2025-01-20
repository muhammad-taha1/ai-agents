from flask import Flask, request, jsonify
from user_manual_agent import UserManualAgent

app = Flask(__name__)

agent = UserManualAgent()

@app.route('/query', methods=['POST'])
def query():
    question = request.json['question']
    response = agent.query(question)
    return response.response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)