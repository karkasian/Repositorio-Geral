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
        abrir_conversa(contato)     #Abrimos a conversa

        #Checamos se tem mais mensagem ou não
        cam='//*[@id="main"]/div[2]/div/div/div[2]/div'
        elemento = driver.find_element_by_xpath(cam)
        titulo=elemento.get_attribute('title')
        if (titulo == 'Carregar mensagens recentes'):
            ide=3
        else:
            ide=2

        #Precisamos saber quantas mensagens foram carregadas
        n=0
        for x in range(1,2000):
            cam='//*[@id="main"]/div[2]/div/div/div['+str(ide)+']/div['+str(x)+']'
            try:
                elemento = driver.find_element_by_xpath(cam)
                n=n+1
            except:
                break
        #E então começar a ver da ultima mensagem
        msg=[]
        for x in range(n,0,-1):
            cam='//*[@id="main"]/div[2]/div/div/div['+str(ide)+']/div['+str(x)+']/div'
            elemento = driver.find_element_by_xpath(cam)
            classe = elemento.get_attribute('class')
            if ('message-in' in classe):
                cam='//*[@id="main"]/div[2]/div/div/div['+str(ide)+']/div['+str(x)+']/div/div/div[1]/div/span'
                elemento = driver.find_element_by_xpath(cam)
                texto=elemento.text
                msg.append(texto)
            else:
                break

        return msg

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

        nvas_msgs=[]
        for contato in contatos:
            msgs=ult_msgs(contato)
            novas_msgs.append(msgs)
            
        driver.get("https://web.whatsapp.com")  #Reabrimos a pagina para não ficar em nenhuma conversa
        return nvas_msgs
