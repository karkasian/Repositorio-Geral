/*
PAPELÃO: Servidor
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Papelão
##2018
*/

var app = require('express')();         //Framework web minimalista
var http = require('http').Server(app); //Permite transferir dados via HTTP
var io = require('socket.io')(http);    //Permite comunicação bi-direcional

//Redirecionamos o cliente que conectar nosso servidor pra pagina index.html
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

//Dos clientes conectados
io.on('connection', function(socket){
  //Informamos o usuário se conectou
  console.log('Usuário conectado.');

  //Recebemos o estado das estados
  socket.on('w', function(estado){
    console.log('w: ',estado);
    //E emitimos pra todos clientes
    io.emit('w', estado);
    });

  socket.on('a', function(estado){
    console.log('a: ',estado);
    io.emit('a', estado);
    });

  socket.on('s', function(estado){
    console.log('s: ',estado);
    io.emit('s', estado);
    });

  socket.on('d', function(estado){
    console.log('d: ',estado);
    io.emit('d', estado);
    });

});

//Vamos ouvir na porta 300
http.listen(3000, function(){
  console.log('Ouvindo na porta:3000');
});
