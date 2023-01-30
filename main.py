import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL="https://www.matchendirect.fr/live-score/etoile-du-sahel-esperance.html"
headers={"user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'}
sender_mail='azizjouini906@gmail.com'
reciever_mail='jouini.hammadi@yahoo.com'
sender_pass='zmryjqrkxvsuxtsn'

page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,'html.parser')


team1=soup.find_all("a",{"href":"/equipe/etoile-du-sahel.html","title":"Étoile Sahel"})[1].get_text()
team2=soup.find_all("a",{"href":"/equipe/es-tunis.html","title":"ES Tunis"})[1].get_text()
time_match=str(soup.find_all("div",{"class":"status"})[0].get_text())
score1=str(soup.find_all("span",{"class":"score"})[0].get_text())
score2=str(soup.find_all("span",{"class":"score"})[1].get_text())
   


def send_email():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_mail,sender_pass)
    subject='match ESS VS EST'
    msg=f"subject: {subject} \n\n match status {team1} {team2} \n\n {score1} {score2} \n\n time:{time_match} "  

    server.sendmail(
        sender_mail,
        sender_mail,
        msg.encode('utf-8')
    )
    server.quit()
    print('email sent!')

while(True):
    send_email()
    time.sleep(60*8)

