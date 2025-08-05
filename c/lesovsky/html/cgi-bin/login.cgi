#!/usr/bin/python3
print('Content-type: text/html \n')
# -*- coding: utf-8 -*-
import cgi
import html
import hashlib
import os


form = cgi.FieldStorage()
username = form.getfirst("username", "").strip()
password = form.getfirst("password", "").strip()
email = form.getfirst("email", "").strip()

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

userfile = "/homes/students/lesovsky/html/cgi-bin/users.txt"

def check_login(username, password, email):
    if not os.path.exists(userfile):
        return False
    with open(userfile, "r") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) != 3:
                continue
            stored_user, stored_hash, stored_email = parts
            if stored_user == username and stored_hash == hash_pw(password) and stored_email == email:
                return True
    return False

if username and password and email:
    if check_login(username, password, email):
        msg = "Login erfolgreich!"
    else:
        msg = "Benutzername, Passwort oder E-Mail falsch."
else:
    msg = "Alle Felder sind erforderlich."

print(f"""
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
</head>
<body>
  <h1>{html.escape(msg)}</h1>
  <a href="/~lesovsky/">Zurueck</a>
</body>
</html>
""")
