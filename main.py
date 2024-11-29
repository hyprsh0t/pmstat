import os
from flask import Flask as f, request as r



app = f(__name__)

@app.route('/')
def main():
    return """
    <h1>Hello, Welcome to Proxbox</h1>
    <p>Please check the proxbox documentation on GitHub to see what you want to do.</p>
    <p></p>
    <p>Blessings!</p>
"""



app.run(port=9090, debug=True)
