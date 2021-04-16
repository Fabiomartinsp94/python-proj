from time import sleep 
from datetime import datetime
import requests
from seleniumwire import webdriver as wd #pip install selenium
from selenium.webdriver.chrome.options import Options #mostrando que o driver do selenium vai ser o chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import filecmp
from random import randint
from colorama import init
from termcolor import colored



# importar todos os plugins antes

def get_sec(time_str):
    "Get Seconds from time."
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
 
def alterar_posicao(posicao):
    global pagina
    global driver
    if posicao >= 30:
        pagina = pagina + 1
        driver.get(urlrank_base.format(pagina)) #formatar na hora pra mudar a pagina // chamar a string formatada para uso
        print(colored("página" + str(pagina), 'green'))
        return 1
    else:
        return posicao + 1

def escolher_e_atacar(posicao):
    global driver
    while True:

        inimigo = driver.find_element_by_xpath('/html/body/section[2]/div[2]/table/tbody/tr[{}]/td[1]/a'.format(posicao))
        inimigo.click()
        atacar = driver.find_element_by_xpath('/html/body/section[1]/div/div[2]/div[2]/div[2]/form/button')
        atacar.click()

        if "battle-log" in driver.current_url:

            driver.execute_script("window.history.go(-2)")
            print(colored(str(datetime.now()) + " , " + "Aguardando 10, sucesso" + str(posicao),"blue", "on_white"))
            sleep(randint(600, 630))
            posicao = alterar_posicao(posicao)
            continue

        if "anti-bot" in driver.current_url:
            for i in range(1, 5):
                for r in driver.requests:          
                    if f"anti-bot-img.png?pos={i}" in r.url:   
                        with open(fr'C:\Users\dir\Desktop\web-s\Anti-bot/tmp{i}.png', "wb") as file:  #wb = write bytes
                            file.write(r.response.body) #pedindo pra ver os bytes da imagem
            valores = []
            for r in range (1, 5):
                for i in range (1, 10):
                    if filecmp.cmp(fr'C:\Users\dir\Desktop\web-s\Anti-bot/tmp{r}.png', fr'C:\Users\dir\Desktop\web-s\Anti-bot/{i}.png'):
                        valores.append(i)
                        break
            if len(valores) != 4:
                print("ERRO NO ANTI BOT")
                exit()
            valor_final = ""
            for n in valores:
                valor_final += str(n)
            del driver.requests
            caixaab = driver.find_element_by_xpath('//*[@id="id_number"]')
            caixaab.send_keys(valor_final + '\n')
            driver.execute_script("window.history.go(-3)")
        
        else:
            driver.execute_script("window.history.go(-2)")
            print("falha" + str(posicao))
            posicao = alterar_posicao(posicao)
            continue


#######################################################################
init(autoreset=True)

url = "" #variável chamada url

pagina = 35
urlrank_base = "" 
urlrank = urlrank_base.format(pagina)
print(urlrank)

option = Options()
#option.add_argument("user-data-dir=C:/Users/dir/Desktop/web-s") #selecionando a pasta que as opções do navegador vai salvar
option.headless = True #deixar o navegador escondido (true) ou mostrar as operações (false)
driver = wd.Chrome("C:/Users/dir/Desktop/web-s/chromedriver", options=option) 
driver.implicitly_wait(60)

driver.get(url) 

email = 'email@email.com'
senha = 'password'

login = driver.find_element_by_id("id_email")
login.send_keys(email)

loginpass = driver.find_element_by_id("id_password")
loginpass.send_keys(senha)

botao = driver.find_element_by_xpath('//*[@id="landing"]/div/div[2]/form/div/button')
botao.click()
driver.get(urlrank)

try:
    chat = driver.find_element_by_xpath('//*[@id="chatControls"]/a[5]').click()
except:
    pass
 

escolher_e_atacar(1)