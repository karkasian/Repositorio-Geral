﻿/*
PAPELÃO: Controle do personagem
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Papelão
##2018
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using SocketIO;                         //Vamos usar nosso asset do Socket

public class controle : MonoBehaviour {

    public float velocidade;            //Controlar a velocidade de movimento
    public bool w, d, a, s;             //Se as teclas estão sendo pressionadas
    private int ww, dd, aa, ss;         //Variáveis pra ajudar no movimento
    private SocketIOComponent socket;   //Vamos criar o componente

    // Use isso para inicialização
    void Start()
    {
        velocidade = 10f;               //Velocidade de movimento
        w = d = a = s = false;          //Declaramos que inicialmente as teclas não estão sendo pressionadas

        GameObject go = GameObject.Find("SocketIO");            //Buscamos nosso GameObject que é responsável pela conexão com o server
        socket = go.GetComponent<SocketIOComponent>();          //Criamos nosso comomente

        //Vamos escutar nossas tecla          // E salvar o estado
        socket.On("w", (SocketIOEvent e) => { w = e.data["estado"]; });
        socket.On("a", (SocketIOEvent e) => { a = e.data["estado"]; });
        socket.On("s", (SocketIOEvent e) => { s = e.data["estado"]; });
        socket.On("d", (SocketIOEvent e) => { d = e.data["estado"]; });
    }

    // Update é chamado uma vez por frame
    void Update()
    {
        ww = dd = aa = ss = 0;                     //Assumimos valores nulos a princípio

        //Se alguma tecla está sendo pressionada, vamos mover
        if (w == true || d == true || a == true || s == true)
        {
            //Assumindo que estamos usando apenas uma câmera:
            var camera = Camera.main;

            //Pegamos os vetores 'para frente' e 'para direita' da câmera:
            var frente = camera.transform.forward;
            var direita = camera.transform.right;

            //Projetamos os vetores no plano (y=0) e normalizamos
            frente.y = 0f;
            direita.y = 0f;
            frente.Normalize();
            direita.Normalize();
            //Se vamos ter movimento, assumimos um valor de deslocamento e consideramos falso
            if (w == true) { ww = 1; w = false; }
            if (d == true) { dd = 1; d = false; }
            if (a == true) { aa = 1; a = false; }
            if (s == true) { ss = 1; s = false; }
            //Isso é a direção no mundo em que queremos nos mover:
            var direcao = frente * (ww - ss) + direita * (dd - aa);

            //Aplicamos o movimento
            transform.Translate(direcao * velocidade * Time.deltaTime);
        }
    }
}
