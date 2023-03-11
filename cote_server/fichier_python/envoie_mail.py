 ## Importation des modules  https://latutotheque.fr/charlometre/tutoriels/informatique/comment-envoyer-un-email-avec-python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

Fromadd = "biboop.bot@gmail.com"
Toadd = "21903309@etu.unicaen.fr"    ##  Spécification des destinataires
message = MIMEMultipart()    ## Création de l'objet "message"
message['From'] = Fromadd    ## Spécification de l'expéditeur
message['To'] = Toadd    ## Attache du destinataire à l'objet "message"
message['Subject'] = "Page mensuelle"    ## Spécification de l'objet de votre mail
msg = "La page de ce mois si est en pièce jointe"    ## Message à envoyer
message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))    ## Attache du message à l'objet "message", et encodage en UTF-8

nom_fichier = "serveur_Web/html/Juin_2022.html"    ## Spécification du nom de la pièce jointe
piece = open(nom_fichier, "rb")    ## Ouverture du fichier
part = MIMEBase('application', 'octet-stream')    ## Encodage de la pièce jointe en Base64
part.set_payload((piece).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
message.attach(part)    ## Attache de la pièce jointe à l'objet "message"

serveur = smtplib.SMTP('smtp.gmail.com', 587)    ## Connexion au serveur sortant (en précisant son nom et son port)
serveur.starttls()    ## Spécification de la sécurisation
serveur.login(Fromadd, "fdtmibncumlvwdgd")    ## Authentification
texte= message.as_string().encode('utf-8')    ## Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
serveur.sendmail(Fromadd, Toadd, texte)    ## Envoi du mail
serveur.quit()    ## Déconnexion du serveur
