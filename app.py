from flask import Flask, send_file, request
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/download')
def download_game():
    dir_path = request.args.get('dir')
    zip_file = request.args.get('zip')
    game_path = os.path.join(dir_path, zip_file)

    return send_file(game_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

