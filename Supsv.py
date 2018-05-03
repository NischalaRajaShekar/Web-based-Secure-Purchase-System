from flask import Flask, request, render_template, redirect, url_for
import MySQLdb
import os
import rsa
import _pickle as cPickle
from werkzeug import secure_filename

UPLOAD_FOLDER = 'C:\\Users\\nisch\\Documents\\SJSU\\CMPE 209\\Project\\Supervisor'
ALLOWED_EXTENSIONS = set(['txt','pdf','png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/authenticate_po',methods=['POST','GET'])
def authenticate_po():
    print ("inside file upload'")
    if request.method == 'POST':
        print ("inside post file upload")
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(file)
            return 'file uploaded successfully'
    print ("before render return")
    return render_template('authenticate_po.html')

    
@app.route('/wrong_credentials',methods=['GET'])
def wrong_credentials():
    return render_template('wrong_credentials.html')

#email and pwd verification
@app.route('/verify/<mail>/<password>')
def verify_pw(mail,password):
    if (mail == "supervisor.spcenter@gmail.com" and password == "sup@209"):
        return redirect(url_for('authenticate_po'))
    else:
        print ("pwd wrong")
        return redirect(url_for('wrong_credentials'))    

#Login Page, enter email and password
@app.route("/",methods=['POST','GET'])
def home():
    print ("enter")
    if request.method == 'POST':
        email = request.form['EmailID']
        pw = request.form['Password']
        print (email, " ", pw)
        return redirect(url_for('verify_pw', mail = email, password=pw))
    return render_template('login.html')        

if __name__ == '__main__':
    app.run()
