from flask import Flask, render_template
app = Flask(__name__, template_folder="dist")

@app.route("/")
def hello():
    return render_template('boom.html')

if __name__ == "__main__":
    app.run()
