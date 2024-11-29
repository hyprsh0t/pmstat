import os
from flask import Flask as f, request as r



app = f(__name__)

@app.route('/')
def main():
    return """
    <h1>Hello, Welcome to Proxbox </h1>
    <p>Please check the proxbox documentation on GitHub to see what you want to do.</p>
    <p></p>
    <p>Blessings!</p>
"""

@app.route('/', methods=['GET'])
def getInfo(response):
    information = {
        "name": str(),
        "cpuName": str(),
        "memory": str(),
        "disk": str(),
        "network": str(),
        "networkInterface": str(),
        "ip": str(),
        "os": str(),
        "osVersion": str(),
        "osDistribution": str(),
        "gpuName": str(),
        "gpuMemory": str(),
        "gpuDriverVersion": str(),
        "gpuDriverName": str(),
        "gpuDriverDate": str(),
        "gpuTemperature": str(),
        "cpuFrequency": str(),
        "cpuLoad": str(),
        "cpuCores": str(),
        "cpuThreads": str(),
        "cpuUsage": str(),
        "cpuVoltage": str(),
        "cpuPower": str(),
        "cpuTemperature": str(),
    }



app.run(port=9090, debug=True)
