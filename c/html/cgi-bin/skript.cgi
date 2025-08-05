#!/usr/bin/python3

print('Content-type:text/html \n')
import cgi
import cgitb
import html

cgitb.enable()
form = cgi.FieldStorage()

vorname = form.getvalue("Vorname")
nachname = form.getvalue("Nachname")
date = form.getvalue("Geburtsdatum")
sex = form.getvalue("Geschlecht")
fahrrad = form.getvalue("fahrrad")
feedback = form.getvalue("message")

vorname= vorname or "Kunde"

fahrrad_feats = {
"Cube_Nature": "Das Cube Nature EXC ist dein perfekter Begleiter f&#252;r Alltag und Abenteuer. Der stabile Aluminiumrahmen, kombiniert mit einer sensiblen Federgabel, sorgt f&#252;r angenehmes Fahrverhalten &#8722; ob auf Asphalt oder Waldwegen. Dank der 30&#8722;Gang&#8722;Schaltung meisterst du jede Steigung m&#252;helos.\n Ideal f&#252;r: sportliche Pendler, Tourenfahrer &#38; Alltagsradler.\n Besonderheiten: hydraulische Scheibenbremsen, gro&#223;e &#220;bersetzungsbandbreite, tourentauglich.",
"Trek_FX_3_Disc": "Wenn du ein leichtes, schnelles und stylisches Bike f&#252;r den Alltag suchst, ist das FX 3 Disc genau richtig. Mit Carbon&#8722;Gabel, hochwertigen Komponenten und sportlicher Geometrie ist es ideal f&#252;r den Weg zur Arbeit und f&#252;r Fitness&#8722;Fahrten. Ideal f&#252;r: Fitness&#8722;Fans, Pendler, urbane Abenteurer. Besonderheiten: Carbon&#8722;Gabel, sportliche Leichtigkeit, Scheibenbremsen f&#252;r jede Witterung." ,
"Liv_Alight_3": "Das Liv Alight 3 ist das ideale Citybike f&#252;r stilbewusste Frauen, die Wert auf Komfort und Vielseitigkeit legen. Der leichte Alurahmen mit aufrechter Sitzposition sorgt f&#252;r ein angenehmes Fahrgef&#252;hl &#8722; ob zum Einkaufen, ins B&#252;ro oder f&#252;r eine entspannte Runde im Park. Ideal f&#252;r: urbane Alltagsfahrten, Freizeit & t&#228;gliche Erledigungen. Besonderheiten: leichtes Design, komfortable Geometrie, 3x7 Shimano&#8722;Schaltung.",
"Cube_Access_WS": "Mit dem Cube Access WS bist du flexibel unterwegs &#8722; auf der Stra&#946;e oder im leichten Gel&#228;nde.Die Federgabel schluckt Unebenheiten, und die robuste Bauweise sorgt f&#252;r Sicherheit und Fahrspa&#946; auf allen Wegen. Ideal f&#252;r: Einsteigerinnen ins Mountainbiking, aktive Pendlerinnen. Besonderheiten: 24 G&#228;nge, hydraulische Scheibenbremsen, sportlich&#252;robust.", 
"Woom_3": "Das Woom 3 wurde speziell f&#252;r Kinder ab ca. 4 Jahren entwickelt. Es ist extrem leicht, hat kindgerechte Bremshebel und bietet durch die ergonomische Rahmenform besonders hohe Sicherheit beim Fahrenlernen. Ideal f&#252;r: Kinder von 4 bis 6 Jahren. Besonderheiten: nur 5,4 kg, tiefer Einstieg, intuitive Handbremsen." ,
"Puky_ZL_18": "Das Puky ZL 18 ist ein Klassiker unter den Kinderr&#228;dern.Mit R&#252;cktrittbremse, tiefem Einstieg und Schutzblechen ist es bestens f&#252;r den Alltag ger&#252;stet &#8722; und ideal f&#252;r erste Touren zur Schule oder zum Spielplatz. Ideal f&#252;r: Kinder ab ca. 5 Jahren. Besonderheiten: R&#252;cktrittbremse, vollst&#228;ndige Sicherheitsausstattung, stabile Bauweise."
}

fahrrad_display_names = {
    "Cube_Nature": "Cube Nature",
    "Trek_FX_3_Disc": "Trek FX 3 Disc",
    "Liv_Alight_3": "Liv Alight 3",
    "Cube_Access_WS": "Cube Access WS", 
    "Woom_3": "Woom 3",
    "Puky_ZL_18": "Puky ZL 18"
}

print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fahrradshop</title>
    <link rel="stylesheet" href="../css/display.css">
</head>


<body class="body">
<div class="result-container">
    <h2>Hallo Lieber {vorname},</h2>
    <p>Sie haben sich f&#252;r das Fahrrad <strong>{fahrrad_display_names[fahrrad]}</strong> entschieden </p>

""")

if fahrrad in fahrrad_feats:
    print(fahrrad_feats.get(fahrrad))
print("</div>")
print("</body>")
print("</html>")
