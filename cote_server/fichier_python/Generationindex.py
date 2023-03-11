import os #pour la lecture des fichier
import GenerationHTMLCSS
import Generationindex
def main():
    list =(os.listdir('serveur_Web/html'))
    MALISTE=[]
    for i in range(len(list)):
        try:
            if list[i].split('.')[1]=='html':
                MALISTE.append(list[i])
        except:
            pass
    file = open("serveur_Web/index.html","w")
    Head =("""
<!DOCTYPE html>
<html lang= fr-FR>
<head>
    <!--	<LINK rel=stylesheet type= text/css  href= lettre_greyc.css >-->
    <meta  charset= UTF-8  />
    <meta property= og:site_name  content= La lettre mensuelle du GREYC >
    <meta property= og:image  content= https://relpart.greyc.fr/public/motvalo/images/logo-GREYC.svg >
    <meta property= og:url  content= https://relpart.greyc.fr/public/motvalo/motvalo-3.html >
    <meta name="author" content="21903309,21907677,21908132,21911920" />
""")
    liste=("""<p>Liste de toutes les pages:</p>\n""")
    file.write(Head+liste)
    file.write("""<ul>""")
    for i in range(len(MALISTE)):
        file.write("""<li><a href=html/"""+MALISTE[i]+""">"""+MALISTE[i]+"""</a></li>\n""")
    file.write("""<ul>""")
    file.close()
