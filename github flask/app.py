from flask import Flask,request,render_template
import requests
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    repos=[]
    username=""
    if request.method=='POST':
        username=request.form['username']
        url=f"https://api.github.com/users/{username}/repos"
        response=requests.get(url)
        if response.status_code==200:
            repos=response.json()
        else:
            repos=[]
    return render_template("index.html",username=username,repos=repos)

if __name__=="__main__":
    app.run(port=5050, debug=True)