from flask import Flask, render_template, send_from_directory
app = Flask(__name__, template_folder="frontend/build/",static_url_path='')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('frontend/build/static/', path)

if __name__ == "__main__":
    app.run()
