# # Crie um script para verificar o preço de produtos em sites e enviar alertas.
# # Dificuldade: Intermediário
# # Documentação: BeautifulSoup

import os
from time import sleep
import requests
from bs4 import BeautifulSoup as BS

try: 
    link = 'https://www.kabum.com.br/produto/256732/headset-gamer-razer-kaira-x-console-e-pc-drivers-50mm-p2-preto-e-verde-rz04-03970100-r3u1'
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"}
    requisicao = requests.get(link, headers=headers)
    code = BS(requisicao.text, 'html.parser')
    pesquisa = code.find('h4', class_='sc-5492faee-2')
    os.system('cls')
    print(f'O valor do Headset Gamer Razer Kaira X na Kabum está saindo atualmente por: {pesquisa.getText()}')
except KeyboardInterrupt:
    print(f'Você cancelou a pesquisa!')
except Exception as err: 
    print(f'Algo deu errado. Erro: {err}')