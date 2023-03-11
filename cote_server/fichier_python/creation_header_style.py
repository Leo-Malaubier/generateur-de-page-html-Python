import os #pour la lecture des fichier
import GenerationHTMLCSS
import Generationindex
import conversio_csv
def main(date,destination):
    file = open("serveur_Web/html/"+date+".html","w")
    Head =("""
<!DOCTYPE html>
<html lang= fr-FR>
<head>
    <!--	<LINK rel=stylesheet type= text/css  href= lettre_greyc.css >-->
    <meta  charset= UTF-8  />
    """)

    variable=date+" Lettre d'actualites du GREYC"
    TitreHead=('<title>'+variable+'</title>')

    Head2=("""
    <!-- a modifier l'ors de la génération client -->
    <link rel="stylesheet" href="style/screen.css" />

    <meta property= og:site_name  content= La lettre mensuelle du GREYC >
    <meta property= og:image  content= https://relpart.greyc.fr/public/motvalo/images/logo-GREYC.svg >
    <meta property= og:url  content= https://relpart.greyc.fr/public/motvalo/motvalo-3.html >
    <meta name= author  content= greyc S.SChÃ¼pp AMACC CODAG ELEC IMAGE MAD SAFE SAR DDA ADMINISTRATIF  />
    <meta name="author" content="21903309,21907677,21908132,21911920" />
""")

    style="\n"
    if destination =='client':
        with open("../HTML/style/screen.css","r") as page:
            style="<style>"+page.read()+"\n</style>\n</head>"

    else:
        style="</head>"


    file.write(Head+TitreHead+Head2+style)
    file.close()
    GenerationHTMLCSS.GenerationHTMLCSS(date)
    Generationindex.main()
    transfer=conversio_csv.Conversion(date)
    transfer.suppression()
