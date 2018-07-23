from selenium import webdriver                          #Biblioteca de automatização de tarefas no navegador
from selenium.webdriver.common.keys import Keys         #Importa os atalhos de teclas do Selenium
from PIL import Image                                   #Biblioteca para tratamento de imagem
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

#Função pra gerar o QR  code
def gerar_qr():
        nimg='qr.png'                           #Nome da imagem a ser salvo
        driver.get_screenshot_as_file(nimg)     #Screenshot do navegador
        im = Image.open(nimg)                   #Abre a imagem
        im.crop((676,152,940,416)).save(nimg)     #Corta a imagem 
        return

#Função para abrir a conversa
def abrir_conversa(contato):
        #contato   - Quem vamos abrir as mensagens
        #Dicionário com os XPath
        caminho='//*[@id="side"]/div[2]/div/label/input'        #Caminho para "Procurar ou começar uma nova conversa"
        elemento = driver.find_element_by_xpath(caminho)        #Pegamos o elemento onde procuramos uma nova conversa
        elemento.clear()                                        #Limpamos caso tenha alguma pesquisa antiga
        elemento.send_keys(contato)                             #Digitamos o destinatário
        time.sleep( 5 )                                         #Esperamos para fazer a busca
        for x in range(1,17):   #Checar os possíveis 16 resultados
                caminho='//*[@id="pane-side"]/div/div/div/div['+str(x)+']/div/div/div[2]/div[1]/div[1]/span/span'       #Caminho para o nome do contato
                #//*[@id="pane-side"]/div/div/div/div[4]/div/div/div[2]/div[1]/div[1]/span
                try:                                                                                                    #Tentamos checar o resultado
                        elemento = driver.find_element_by_xpath(caminho)                                                #Pegamos o elemento
                        if (elemento.get_attribute('title')==contato):                                                  #Comparamos o nome com o nosso objetivo
                                caminho='//*[@id="pane-side"]/div/div/div/div['+str(x)+']/div/div'                      #Se for, salvamos o caminho pro elemento do resultado
                                break                                                                                   #E saímos do for
                except:                                                                                                 #Se não funcionar
                        pass                                                                                            #Tentamos o próximo resultado
        elemento = driver.find_element_by_xpath(caminho)                        #Pegamos o elemento
        elemento.click()                                                        #Clicamos
        caminho='//*[@id="side"]/div[2]/div/button'                             #Caminho para o botão de voltar
        elemento = driver.find_element_by_xpath(caminho)                        #Pegamos o elemento
        elemento.click()                                                        #Clicamos
        return

#Função para enviar mensagem
def enviar_msg(destinatario,msg):
        #destinatario   - Quem vai receber a mensagem
        #msg            - Mensagem a ser enviada

        abrir_conversa(destinatario)                                            #Abrimos a conversa de quem vamos enviar
        caminho='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'               #Caminho da conversa
        elemento = driver.find_element_by_xpath(caminho)                        #Selecionamos o campo da mensagem
        elemento.clear()                                                        #Limpamos caso tenha alguma coisa antiga
        elemento.send_keys(msg,Keys.ENTER)                                      #Enviamos a mensagem
        return

#Função para lermos as ultimas mensagens enviadas de algum contato:
def ult_msgs(contato):
        abrir_conversa(contato)
        return

#Função para checar se tem novas mensagens não lidas
def novas_msgs():
        contatos=[]             #Onde vamos guardar quem nos enviou as mensagens não lidas
        for x in range(1,17):   #Checar os últimos 16 contatos na lista de conversas
                try:            #Checamos se tem mensagem nova
                        caminho='//*[@id="pane-side"]/div/div/div/div['+str(x)+']/div/div/div[2]/div[2]/div[2]/span[1]/div/span'        #Caminho para a quantidade de mensagens novas
                        elemento = driver.find_element_by_xpath(caminho)                                                                #Verificamos se existe o elemento
                        caminho='//*[@id="pane-side"]/div/div/div/div['+str(x)+']/div/div/div[2]/div[1]/div[1]/span/span'               #Caminho para o nome do contato
                        elemento = driver.find_element_by_xpath(caminho)                                                                #Pegamos o elemento
                        contatos.append(elemento.get_attribute('title'))                                                                #Salvamos o nome
                except:         #Se não existe o elemento de novas mensagens do contato
                        pass    #Passamos e checamos todas as novas mensagens na lista
                        #break  #Paramos e pegamos so até ter uma mensagem já lida
        return contatos

##PROBLEMAS
##Maximo 16 novas mensagens de conversas diferentes
##Envia e recebe só textos
##Só funciona com contatos na agenda
##Não pode ter contatos com nomes repetidos
##Não otimizado para grupos
##Só testado com conversas já existentes
