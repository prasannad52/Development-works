from flask import Flask,render_template,request,redirect,url_for
"""
It creates an instance of the Flask calss,
which will be you r WSGI (web server gateway interface) application.
"""
### WSGI Application
app = Flask(__name__)                                

@app.route("/")
def welcome():
    return "welcome to my flask API class"

@app.route("/index",methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/form",methods = ['GET','POST'])  
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello {name}"
    return render_template("form.html")


# variable rule
@app.route("/success/<int:score>")
def success(score):
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {"score":score, "res":res}
    return render_template("result.html",results = exp)

@app.route("/submit",methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['data_science'])

        total_score = (science+maths+c+data_science)/4
    else:
        return render_template("getresult.html")
    return redirect(url_for("success",score = total_score))


if __name__=="__main__":
    app.run(debug=True)