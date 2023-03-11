import lecture_Rubrique
import lecture_xlsx
def GenerationHTMLCSS(Date):
    file = open("serveur_Web/html/"+Date+".html","a")
    file.write("""
<body>
	<aside>
		<a href= http://www.greyc.fr/  target= _blank >
			<img alt= GREYC  src= https://relpart.greyc.fr/public/motvalo/images/logo-GREYC.svg  title= GREYC >
		</a>
		<a href= https://www.unicaen.fr/  target= _blank >
			<img alt= UNICAEN  src= https://relpart.greyc.fr/public/motvalo/images/icone_UNICAEN.png  title= UNICAEN >
		</a>
		<a href= https://www.ensicaen.fr/  target= _blank >
			<img alt= ENSICAEN  src= https://relpart.greyc.fr/public/motvalo/images/icone_ENSICAEN.png  title= ENSICAEN >
		</a>
		<a href= https://www.cnrs.fr/  target= _blank >
			<img alt= CNRS  src= https://relpart.greyc.fr/public/motvalo/images/icone_CNRS.png  title= CNRS >
		</a>

	</aside>""")



    file.write("""
    <header><h1>Actualités du GREYC"""+Date+"""</h1></header>""")

    Liste_Rubrique=lecture_Rubrique.lecture_fueilles()
    Data=lecture_xlsx.rangement()
    Couple_Valeur=[]
    for i in range(len(Liste_Rubrique)):
        Couple_Valeur.append([Liste_Rubrique[i]])

    for i in range(len(Data)):
        for j in range(len(Liste_Rubrique)):
            if Data[i][2]==Liste_Rubrique[j]:
                del Data[i][2]
                variable=Data[i]
                Couple_Valeur[j].append(variable)
    value=0
    for i in range(len(Couple_Valeur)):
        if len(Couple_Valeur[i]) <=1:
            pass
        else:
            file.write("""
        <section>""")
            for j in range(len(Couple_Valeur[i])):
                if isinstance(Couple_Valeur[i][j], str):
                    valeur=Couple_Valeur[i][j]
                    file.write("""
            <h2>"""+Couple_Valeur[i][j]+"""</h2>""")
                else:
                    salut=Couple_Valeur[i][j]
                    #print(salut[0])
                    file.write("""
                    <article>""")
                    file.write("""
                        <h3>"""+salut[2]+"""</h3>""")
                    file.write("""
                        <p>"""+salut[3]+"""</p>""")
                    if isinstance(salut[4], str):
                        file.write("""
                            <p><a href="""+salut[4]+""">"""+salut[4]+"""</a></p>""")
                    file.write("""
                        <p>"""+salut[0]+"""</p>""")
                    file.write("""
                    </article>""")
            file.write("""
            </section>""")
    file.write("""
	<footer>
	<p>
		<a href= http://www.greyc.fr/  target= _blank >GREYC UMR CNRS 6072<br>Laboratoire en Sciences du Numérique, Caen</a>
	</p>
	</footer>
</body>
</html>""")
    file.close()
