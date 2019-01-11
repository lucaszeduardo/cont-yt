import time
import urllib
import json
import os
from urllib.request import urlopen

class Cores(object):
    corPadrao = "\033[0m"
    preto = "\033[0;30m"
    vermelho_bold = "\033[1;31m"
    vermelho = "\033[0;31m"
    verde = "\033[1;32m"
    marrom = "\033[0;33m"
    azul = "\033[1;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    cinzaClaro = "\033[0;37m"
    pretoCinza = "\033[1;30m"
    vermelhoClaro = "\033[1;31m"
    verdeClaro = "\033[1;32m"
    amarelo = "\033[1;33m"
    azulClaro = "\033[1;34m"
    purpleClaro = "\033[1;35m"
    cyanClaro = "\033[1;36m"
    branco = "\033[1;37m"

class Att:
    def Apikey(self):
        self.apiKey = 'SUA APIKEY AQUI'

        return self.apiKey

    def IdChannel(self):
        self.channelId = 'ID DO CANAL AQUI'

        return self.channelId

    def Connect(self):
        try:
            self.urlChannel = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + Att().IdChannel() + '&key=' + Att().Apikey()
            self.responseChannel = urlopen(self.urlChannel).read().decode('utf-8')
            self.dateChannel = json.loads(self.responseChannel)

            return self.dateChannel
        except:
            print('Error, verify ID Channel!!')

    def Subs(self):
        self.connec = Att().Connect()
        self.subs = self.connec['items'][0]['statistics']['subscriberCount']

        return self.subs
    def Views(self):
        self.connec = Att().Connect()
        self.views = self.connec['items'][0]['statistics']['viewCount']

        return self.views
    def Movies(self):
        self.connec = Att().Connect()
        self.movies = self.connec['items'][0]['statistics']['videoCount']

        return self.movies

while True:
    sub = Cores().verde + Att().Subs() + Cores().branco
    view = Cores().verde + Att().Views() + Cores().branco
    movie = Cores().verde + Att().Movies() + Cores().branco

    print ('SUBS: ' + sub)
    print ('VIEWS: ' + view)
    print ('MOVIES: ' + movie)

    time.sleep(1)
    os.system('clear')
