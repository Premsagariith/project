from flask import Flask,redirect,url_for,render_template

#app= Flask(__name__)
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template("prem.html", content="Testing")
    
@app.route("/<name>")
def user(name):
    return f"Hey! how are you {name}?"
    
#@app.route("/admin")
#def admin():
#    return redirect(url_for("home"))
    

if __name__=="__main__":
    app.run(debug=True)
