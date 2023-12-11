from flask import Flask, send_from_directory, render_template_string, abort
import os
import re

app = Flask(__name__)

@app.route('/<path:filename>')
def serve_file(filename):
    # Check for malicious characters in the filename
    if re.search(r'(~|//|\.\.)', filename):
        abort(403)  # Forbidden

    # Construct the full path to the file
    file_path = os.path.join(app.root_path, 'templates', filename)

    # Check if the file exists and is a file (not a directory)
    if os.path.isfile(file_path):
        return send_from_directory(os.path.join(app.root_path, 'templates'), filename)
    else:
        abort(404)  # Not Found

@app.errorhandler(403)
def forbidden(error):
    return render_template_string(open("templates/403.html").read()), 403

@app.errorhandler(404)
def not_found(error):
    return render_template_string(open("templates/404.html").read()), 404

@app.route("/")
def hello():
    return "IT492 docker demo!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
