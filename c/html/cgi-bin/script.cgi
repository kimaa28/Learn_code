#!/usr/bin/python3

print('Content-type:text/html\n')
from semester import Trek_FX3_Disc, Cube_nature, Liv_Alight_3, Cube_Access_WS, Woom_3, Puky_zl_18 
import cgi,cgitb
cgitb.enable()

form = cgi.FieldStorage()

vorname = form.getvalue("Vorname")
nachname = form.getvalue("Nachname")
geschlecht = form.getvalue("Geschlecht")
fahrrad = form.getvalue("fahrrad")

person = "Kunde"
Anrede= "Lieber"

if geschlecht == "man":
    Anrede = "Lieber"
    person = "Kunde"
elif geschlecht == "frau":
    Anrede = "Liebe"
    person = "Kundin"

def GE_anzeigen():
    return fahrrad_list.get(fahrrad).G_eingenschaften

vorname= vorname or person


fahrrad_list = {"Cube_Nature": Cube_nature, "Trek_FX_3_Disc": Trek_FX3_Disc, "Liv_Alight_3": Liv_Alight_3, "Cube_Access_WS": Cube_Access_WS, "Woom_3": Woom_3, "Puky_ZL_18": Puky_zl_18}



print(f"""<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Fahrrad-shop</title>
        <link rel="shortcut icon" href="../assets/images/fahrrad_logo.png">
	<link rel="stylesheet" href="../css/display.css">



</head>
<body>
<div class="result-container">
<h2 id="oben"> Hallo {Anrede} {vorname}</h2>
  <p> Sie haben sich für das Fahrrad der marke {fahrrad_list.get(fahrrad).Marke +  fahrrad_list.get(fahrrad).model} entschieden. Das ist ist wirklich schön, hierunter finden sie alles über dieses </p> 

<h3 style="font-size: 20px; padding: 10px 0px 20px">Übersicht</h3>

<p> {GE_anzeigen()}</p>

<h3 style="font-size: 20px; padding: 10px 0px 20px">Eingenschaften</h3>

<table border="1" cellpadding="10" style="width: 70%; border-collapse: collapse; font-size: 15px;">
    <thead>
        <tr>
            <th style="background-color: rgb(179, 209, 212); text-align: center; font-size: 20px;"  colspan="2">🧱Allgemeine Eigenschaften</th>
        </tr>
    </thead>
    <tbody>
        <tr><td style="background-color: white;">Marke</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).Marke}</td></tr>
        <tr><td style="background-color: lightgrey;">Modell</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).model}</td></tr>
        <tr><td style="background-color: white;">Rahmenmaterial</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).rahmenmaterial}</td></tr>
        <tr><td style="background-color: lightgrey;">Radgröße</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).radgröße}</td></tr>
        <tr><td style="background-color: white;">Gewicht</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).gewicht}</td></tr>
        <tr><td style="background-color: lightgrey;">Zulässiges Gesamtgewicht</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).zulässiges_gesamtgewicht}</td></tr>
        <tr><td style="background-color: white;">Geschlecht</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).geschlecht}</td></tr>
        <tr><td style="background-color: lightgrey;">Preis</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).preis}</td></tr>

        <tr><th style="background-color: rgb(179, 209, 212); text-align: center; font-size: 20px;" colspan="2">⚙️Antrieb & Schaltung</th></tr>

        <tr><td style="background-color: white;">Antrieb</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).antrieb}</td></tr>
        <tr><td style="background-color: lightgrey;">Kettenmodell</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).kettenmodell}</td></tr>
        <tr><td style="background-color: white;">Anzahl Gänge</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).anzahl_gaenge}</td></tr>
        <tr><td style="background-color: lightgrey;">Schaltungstyp</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).schaltungstyp}</td></tr>
        <tr><td style="background-color: white;">Schaltwerk</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).schaltwerk}</td></tr>
        <tr><td style="background-color: lightgrey;">Umwerfer</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).umwerfer}</td></tr>
        <tr><td style="background-color: white;">Kassette</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).kassette}</td></tr>

        <tr><th style="background-color: rgb(179, 209, 212); text-align: center; font-size: 20px;" colspan="2">🛑 Bremsen</th></tr>

        <tr><td style="background-color: lightgrey;">Kurbelgarnitur/Bremstyp</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).kurbelgarniturbremstyp}</td></tr>
        <tr><td style="background-color: white;">Bremse vorne</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).bremse_vorne}</td></tr>
        <tr><td style="background-color: lightgrey;">Bremse hinten</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).bremse_hinten}</td></tr>
        <tr><td style="background-color: white;">Bremsscheiben</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).bremsscheiben}</td></tr>

        <tr><th style="background-color: rgb(179, 209, 212); text-align: center; font-size: 20px;" colspan="2">🪑 Komfort & Ausstattung</th></tr>

        <tr><td style="background-color: lightgrey;">Gabel</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).gabel}</td></tr>
        <tr><td style="background-color: white;">Federweg</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).federweg}</td></tr>
        <tr><td style="background-color: lightgrey;">Lenker</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).lenker}</td></tr>
        <tr><td style="background-color: white;">Sattel</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).sattel}</td></tr>
        <tr><td style="background-color: lightgrey;">Sattelstütze</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).sattelstütze}</td></tr>
        <tr><td style="background-color: white;">Pedale</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).pedale}</td></tr>
        <tr><td style="background-color: lightgrey;">Griffe (Grips)</td><td style="background-color: lightgrey;">{fahrrad_list.get(fahrrad).grips}</td></tr>
        <tr><td style="background-color: white;">Beleuchtung</td><td style="background-color: white;">{fahrrad_list.get(fahrrad).beleuchtung}</td></tr>
    </tbody>
</table>






</div>

<footer>
    <nav>
        <br>
        <a href="mailto:kitiozan@th-brandenburg.de,muhd.danishk@gmail.com">&#128231;Contact-Us</a>
        <a href="../semester.html">🏠Home</a>
        <a href="#oben"><span class="oben">⬆️ </span> oben</a>
        <br>
    </nav>
</footer>

</body>
</html>""")


