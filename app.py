from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Get the CONTRACT_ADDRESS from the environment variable
    contract_address = os.getenv("CONTRACT_ADDRESS")
    return render_template("index.html", contract_address=contract_address)

if __name__ == "__main__":
    app.run(debug=True)
