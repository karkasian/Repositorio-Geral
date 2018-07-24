# WhatsApp FAPI

Queremos integrar o WhatsApp com o nosso bot para Discord, para isso desenvolvemos este projeto. Ele se chama WhatsApp FAPI (WhatsApp Falso API), pois n�o existe de fato um API para o WhatsApp, uma alternativa segura, � utilizar uma automatiza��o do navegador e automatizar a intera��o com o [Web WhatsApp](https://web.whatsapp.com).

WebDriver � uma ferramente aberta para automatizar testes em diferentes navegadores. Eu estou utilizando o [ChromeDriver](http://chromedriver.chromium.org/home) que implementa o WebDriver no Google Chrome, e a biblioteca [Selenium](http://selenium-python.readthedocs.io/installation.html) que � um API para utilizar o WebDriver.

Limita��es conhecidas:
- Lerdo;
- S� envia e recebe textos;
- N�o pode ter dois n�meros com o mesmo nome;
- N�o funciona com grupos;
- Desenvolvido para lidar com conversas j� existentes;
- Desenvolvido para contatos na agenda.

Anota��es:
- Revisar a necessidade e os tempos de espera (time.sleep(segundos)).