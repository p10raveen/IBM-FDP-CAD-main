from flask import Flask,url_for,redirect,request
from flask import render_template
import ibm_db

app = Flask(__name__) 

conn=ibm_db.connect("DATABASE=bludb; HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud; PORT=32286;PROTOCOL=TCPIP;USERNAME=trd17134; PASSWORD=AVovDmEgKjAUBaQf; SECURITY=SSL;  SSLServerCercertificate=DigiCertGlobalRootCA.crt","","") 
rc = ibm_db.active(conn)
print(rc)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        uname = request.form['username']
        pword = request.form['password']
        print(uname,pword)

        sql = 'SELECT * FROM REGISTER WHERE USERNAME=? AND PASSWORD=?'
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,uname)
        ibm_db.bind_param(stmt,2,pword)
        ibm_db.execute(stmt)
        out = ibm_db.fetch_assoc(stmt)
        print(out)
        if out==False:
            msg = "Invalid Credentials"
            return render_template("login.html",login_message=msg)
        else:
            role = out['ROLE']
            if role==0:
               return render_template("adminProfile1.html",name=out['NAME']) 
            elif role==1:
                return render_template("facultyProfile.html") 
            elif role==2:
                return render_template("studentProfile.html") 
    return render_template("login.html")

@app.route('/registration',methods=["GET","POST"])
def registration():
    if request.method=="POST":
        name = request.form['name']
        uname = request.form['username']
        email = request.form['email']
        pword = request.form['password']
        role = int(request.form['role'])

        sql = 'INSERT INTO REGISTER VALUES(?,?,?,?,?)'
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,name)
        ibm_db.bind_param(stmt,2,uname)
        ibm_db.bind_param(stmt,3,email)
        ibm_db.bind_param(stmt,4,pword)
        ibm_db.bind_param(stmt,5,role)
        ibm_db.execute(stmt)
        
    return render_template("adminProfile1.html")

if __name__ == "__main__":
    app.run(debug= True)