import os
from flask import Flask, render_template
from flask_cors import CORS

app  = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins":"*"}})

@app.route('/')
def index():
    return render_template('index.html')

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()