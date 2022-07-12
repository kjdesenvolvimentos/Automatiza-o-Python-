#importar as bibliotecas
from selenium import webdriver
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#navegar pelo whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

#Definir contatos e grupos e mensagem a ser enviada
contatos = ['JoyDev']
mensagem = 'Olá esse foi um teste de automação em Phyton'
#buscar contatos/grupos
def buscar_contatos(contatos):
    #campo de pesquisa 'copyable-text selectable-text' 
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contatos)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    #campo de mensagem privada 'copyable-text selectable-text'
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    time.sleep(3)

#enviar mensagem para o contato/grupo
for contatos in contatos:
    buscar_contatos(contatos)
    enviar_mensagem(mensagem)




