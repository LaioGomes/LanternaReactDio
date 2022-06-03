from gettext import find
from re import findall
import requests

from bs4 import BeautifulSoup

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()


content = ' '


def extrair_info(url):
    print('Extraindo Notícias...')
    cnt = ' '
    cnt += ('<b>Principais notícias do dia</b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('a', attrs={'class':'title'})):
        cnt += ((str(i+1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text!='More' else ' ')
        #print(tag.prettify), findall('span', attrs ={'class' : 'sitestr'})
    return(cnt)

cnt = extrair_info('https://br.investing.com/news/')
content += cnt
content += ("<br>--------------------------------------<br>")
content += ('<br><br>Fim da Mensagem')


print('Escrevendo email')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'laiolvat.kiss@gmail.com'
TO = 'lorryansilva@gmail.com'
PASS = 'Billion@ire640'

#fp = open(file_name, 'rb)
#Create a text/plain messege
#msg = MIMEText(' ')
msg = MIMEMultipart()

#msg.add_header('Content-Disposition', 'attachment', filename='empty.txt)
msg['Subject'] = 'Principais notícias do dia [Automated Email]' + ' ' + str(now.day) + str(now.month) + '/' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
#fp.close()

print('Iniciando Servidor...')

server = smtplib.SMTP(SERVER, PORT)
#server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(0)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email enviado...')

server.quit()

