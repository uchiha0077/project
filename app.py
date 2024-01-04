import os
from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Get the absolute path of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')
    # return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    convo_id = data.get('convo_id')
    message=data.get('message')

    # Construct absolute paths for the Python scripts
    # script_path = os.path.join(current_script_path, 'bridge_script.py')

    # Call your_other_script.py with the username and password as arguments
    # result = 
    # print(script_path)
    print(username,password,"from app.py",convo_id,message)
    subprocess.run(['python', 'a.py', username, password,convo_id,message])
    return 

    # if result.returncode == 0:
    #     return jsonify({'result': result.stdout})
    # else:
    #     return jsonify({'error': result.stderr})


if __name__ == '__main__':
    app.run(debug=True)
