## WhatsApp FAPI

Esse projeto se chama WhatsApp FAPI (WhatsApp Falso API), pois não existe de fato um API para o WhatsApp, uma alternativa segura, é utilizar uma automatização do navegador e automatizar a interação com o [Web WhatsApp](https://web.whatsapp.com).

WebDriver é uma ferramente aberta para automatizar testes em diferentes navegadores. Eu estou utilizando o [ChromeDriver](http://chromedriver.chromium.org/home) que implementa o WebDriver no Google Chrome, e a biblioteca [Selenium](http://selenium-python.readthedocs.io/installation.html) que é um API para utilizar o WebDriver.

Limitações conhecidas:
- Máximo de 16 novas mensagens de conversas diferentes por vez;
- Envia e recebe só textos;
- Só funciona com contatos na agenda;
- Não pode ter dois números com o mesmo nome;
- Não funciona com grupos;
