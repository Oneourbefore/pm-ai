from flask import Flask, render_template, jsonify, request
from sum_model import summarize_model
from flask_cors import CORS
import torch

app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def index():
    return render_template('index.html')

# def summarize():
#     text = request.args.get('text')
#     summary = sum_model(text)
#     return jsonify(summary)

@app.route('/gsummarize', methods=['POST'])
def gsummarize():
	try:
		data = request.get_json(force=True)
		print(data)
		context = data['text']
		print(context)
		gsum = summarize_model(context)
		print(gsum)
		response = jsonify({'gsum': gsum})

	except Exception as e:
		response = jsonify({'error': str(e)})	
	return response

if __name__ == '__main__':
    app.run('127.0.0.1', port=8000, debug=True)
