/*
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

public class controle : MonoBehaviour {

    public float velocidade;            //Controlar a velocidade de movimento
    public bool w, d, a, s;             //Se as teclas estão sendo pressionadas
    private int ww, dd, aa, ss;         //Variáveis pra ajudar no movimento

    // Use isso para inicialização
    void Start()
    {
        velocidade = 10f;               //Velocidade de movimento
        w = d = a = s = false;          //Declaramos que inicialmente as teclas não estão sendo pressionadas
    }

    // Update é chamado uma vez por frame
    void Update()
    {
        ww = dd = aa = ss = 0;                     //Assumimos valores nulos a princípio

        if (Input.GetKeyDown("w")) { w = true; }    //Se a tecla 'w' foi pressionada, salvamos true
        if (Input.GetKeyDown("d")) { d = true; }    //Idem com a tecla d
        if (Input.GetKeyDown("a")) { a = true; }    //Idem com a tecla a
        if (Input.GetKeyDown("s")) { s = true; }    //Idem com a tecla s

        if (Input.GetKeyUp("w")) { w = false; }   //Se a tecla 'w' foi solta, salvamos false
        if (Input.GetKeyUp("d")) { d = false; }    //Idem com a tecla d
        if (Input.GetKeyUp("a")) { a = false; }    //Idem com a tecla a
        if (Input.GetKeyUp("s")) { s = false; }    //Idem com a tecla s

        //Se alguma tecla está sendo pressionada, vamos mover
        if (w == true || d == true || a == true || s == true)
        {
            //Movimentação sem relação com a câmera
            //transform.Translate(velocidade * Time.deltaTime * Input.GetAxis("Horizontal"), 0f,velocidade*Time.deltaTime);

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
            //Se vamos ter movimento, assumimos um valor de deslocamento
            if (w == true) { ww = 1; }
            if (d == true) { dd = 1; }
            if (a == true) { aa = 1; }
            if (s == true) { ss = 1; }
            //Isso é a direção no mundo em que queremos nos mover:
            var direcao = frente * (ww - ss) + direita * (dd - aa);

            //Aplicamos o movimento
            transform.Translate(direcao * velocidade * Time.deltaTime);
        }
    }
}
