# WFAPI

Queremos integrar o WhatsApp com o nosso bot para Discord, para isso desenvolvemos este projeto. Ele se chama WFAPI (WhatsApp Falso API), pois não existe de fato um API para o WhatsApp, uma alternativa segura, é utilizar uma automatização do navegador e automatizar a interação com o [Web WhatsApp](https://web.whatsapp.com).

WebDriver é uma ferramente aberta para automatizar testes em diferentes navegadores. Eu estou utilizando o [ChromeDriver](http://chromedriver.chromium.org/home) que implementa o WebDriver no Google Chrome, e a biblioteca [Selenium](http://selenium-python.readthedocs.io/installation.html) que é um API para utilizar o WebDriver.

Para rodar, é necessário definir o caminho pro <code>chromedriver.exe</code> nas variáveis de ambiente, ou colocar na mesma pasta do código.

Limitações conhecidas:
- Lerdo;
- Só envia e recebe textos;
- Não pode ter dois números com o mesmo nome;
- Não funciona com grupos;
- Desenvolvido para lidar com conversas já existentes;
- Desenvolvido para contatos na agenda.

Anotações:
- Revisar a necessidade e os tempos de espera (time.sleep(segundos));
- Possívelmente dá erro ao minimizar o navegador.

## Funções importantes

<code>gerar_qr()</code>

Salva o QR Code da página inicial do Web WhatsApp com o nome 'qr.png'. Caso não esteja na página inicial, salva o recorte da tela na posição equivalente de onde estaria o mesmo.

Obs.: As dimensões do recorte foram baseadas nos teste no meu navegador, em outro computador, provavelmente deve ser adaptado.

<code>abrir_conversa_pesquisa(contato)</code>

Abre uma conversa com o contato utilizando o recurso de pesquisa disponível.

Obs.: Foi o primeiro método que testei, não recomendo utilizar, mas mantive o código caso tenha interesse futuro em aprimorá-lo e talvez usar para outro fim.

<code>abrir_conversa(contato)</code>

Mesmo propósito que a função anterior, mas utiliza o recurso de 'nova conversa' para isso.

<code>enviar_msg(destinatario,msg)</code>

Envia a mensagem para o contato destinatário.

<code>ult_msgs(contato)</code>

Exibe as últimas mensagens recebidas de um contato, ele retorna todas mensagens até encontrar a última que você enviou, indepdente das datas. Ex.:
<pre>
Você: Oi
Contato: Oi
Contato: Tudo bem?
</pre>
A função retornaria <code>[[Tudo bem?],[Oi]]</code>, não importando o intervalo de tempo entre as últimas mensagens.

<code>novas_msgs()</code>

Checa se tem novas mensagens e de quem são as novas mensagens, então se há alguma nova mensagem, exibe as últimas mensagens recebidas do contato em questão.

<code>checar_msgs()</code> e <code>iniciar_wfapi()</code> 

A primeira função simplesmente cria um loop infinito para ficar checando se há novas mensagens, e a segunda função invoca esta em plano de fundo.
