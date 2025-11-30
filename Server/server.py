# server.py
from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXT = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

index_html = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Uploaded Screenshot</title>
  <style> body { font-family: Arial, sans-serif; text-align:center; } img { max-width: 90vw; max-height: 80vh; border: 1px solid #ccc; } </style>
  <script>
    function refreshImage() {
      const img = document.getElementById("latest");
      const ts = new Date().getTime();
      img.src = "/static/uploads/latest.png?t=" + ts;
    }
    setInterval(refreshImage, 10000); // refresh every 30 sec
    window.onload = refreshImage;
  </script>
</head>
<body>
  <h1>Latest uploaded screenshot</h1>
  <img id="latest" src="/static/uploads/latest.png" alt="No screenshot yet" />
  <p>Page refreshes every 30 seconds.</p>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(index_html)

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return "No file part", 400
    f = request.files['file']
    if f.filename == "":
        return "No selected file", 400
    filename = secure_filename(f.filename)
    ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
    if ext not in ALLOWED_EXT:
        return "File type not allowed", 400
    # always save as latest.png to simplify display
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], "latest.png")
    f.save(save_path)
    return "OK", 200

if __name__ == "__main__":
    # for demo only. In production use a real WSGI server.
    app.run(host="0.0.0.0", port=5000)
