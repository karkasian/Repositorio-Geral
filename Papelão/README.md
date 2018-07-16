# Papelão

Versões dos softwares utilizdas:
- Android Studio: Versão 3.1.3
  - SDK Platforms: API Level 27 (Revisão 3)
  - SDK Platform-Tools: 28.0.0
  - SDK Tools: 26.1.1
- JDK: 8.0.1710.11
- Unity: Versão 2018.1.8f1
- Node: 8.11.3

Módulos carregados no javascript:
- express: 4.16.3
- socket.io: 2.1.1

Configurações modificadas no Unity:
- Build System: Internal
- Minimum API Level: 19
- Virtual Reality SDKs: Cardboard

Assets carregados no Unity:
- GVR SDK for Unity: 1.150.0
- Socket.IO for Unity: 1.0.2

Prefabs do Cardboad utilizados:
- GvrEditorEmulator: Simular os movimentos com o celular (Alt e Ctrl) no unity
- GvrReticlePointer: Adicionar o ponto no centro da tela

Prefab do Socket.IO for Unity utilizado:
- Socket.IO - Conecta no servidor

## Modo de uso

Para essa primeira versão, ainda não é muito prático o uso. Primeiro, paraa poder usufruir do aplicativo é necessário ter todos os softwares necessários.

Então no objeto SocketIO, é necessário substituir na url o IP do computador em que você vai jogar. isto pode ser obtido utilizando o ipconfig no prompt no Windows, por exemplo.

Então, é necessário que você rode o servidor index.js através do prompt utilizando o comando 'node index.js' no prompt também.

E por fim, a partir de algum navegador, você pode acessar a página localhost:3000. Irá abrir uma página HTML em branco com o título "Papelão". Com esta página aberta, os comandos inseridos no teclado serão enviados para o aplicativo. A princípio, é possível caminhar utilizando as teclas 'w,a,s,d'.
