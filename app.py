from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Video Player!"

@app.route('/watch/<video_id>')
def watch(video_id):
    return render_template('watch.html', video_id=video_id)

@app.route('/static/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory('static/videos', filename)

if __name__ == "__main__":
    app.run(debug=True)
