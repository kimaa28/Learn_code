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

if not os.path.exists(userfile):
    with open(userfile, "w") as f:
        pass
    os.chmod(userfile, 0o600)

def user_exists(username):
    with open(userfile, "r") as f:
        return any(line.split(":")[0] == username for line in f)

if username and password and email:
    if user_exists(username):
        msg = "Benutzername bereits vergeben!"
    else:
        with open(userfile, "a") as f:
            f.write(f"{username}:{hash_pw(password)}:{email}\n")
        msg = "Registrierung erfolgreich!"
else:
    msg = "Alle Felder sind erforderlich."

print(f"""
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Registrierung</title>
</head>
<body>
  <h1>{html.escape(msg)}</h1>
  <a href="/~lesovsky/">Zurueck</a>
</body>
</html>
""")
