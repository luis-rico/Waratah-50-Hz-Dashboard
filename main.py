from flask import Flask, render_template
from flask import Response, jsonify
import json
import collections
app = Flask(__name__)

@app.route("/")
def hello():
    return "Sever running OK! This is to develop Waratah 50 Hz dashboard using Dc.js, crossfilter and D3.js"

@app.route('/50HzDashboard')
def Dashboard():
    return render_template("50HzDashboard.html")
	
@app.route('/50HzDashboardExper')
def DashboardExper():
    return render_template("50HzDashboardExper.html")

## research
@app.route('/stackedBarChart')
def stackedBarChart():
    return render_template("stackedBarChart.html")
	
## research
@app.route('/stackedBarChart2')
def stackedBarChart2():
    return render_template("stackedBarChart-2.html")
	
	
if __name__ == "__main__":
    app.run()