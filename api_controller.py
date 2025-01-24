from flask import Flask, request, jsonify
from user_manual_agent import UserManualAgent

app = Flask(__name__)
agent = UserManualAgent()

@app.route('/query', methods=['POST'])
def query_agent():
    data = request.json
    if not data or 'query' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    query = data['query']
    try:
        result = agent.query(query, stream=False)
        return jsonify({'result': result.response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()