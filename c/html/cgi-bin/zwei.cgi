#!/usr/bin/python3

print('Content-type: text/html \n')
print()
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
print(form.getvalue('count'))

anz= form.getvalue('count')

anz= int(anz)
print("""
<!DOCTYPE html>
<html lang="de">
<head>
 <meta charset="UTF-8>
 <meta name ="viewport" content="width=device-width", initial-scale=1.0">
 <title> cgi-skript </title>
</head>
<body>
<h1>Hello World! from cgi</h1>
<ul>
""")
for i in range(anz):
    print("<li>Hello World</li>")
print("""
</ul>
</body>
</html>
""")
