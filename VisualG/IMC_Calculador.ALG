algoritmo "IMX"
var
M, A, IMC: Real
inicio
      Escreva("Massa:")
      Leia(M)
      Escreva("Altura")
      Leia(A)
      IMC <- M / (A ^ 2)
      Escreval("IMC:", IMC)
      Se (IMC < 17) entao
         Escreval (" Você esta muito abaixo do peso")
      Senao
         Se (IMC >= 17) e (IMC < 18.5) entao
            Escreval("Abaixo do Peso")
         Senao
              Se (IMC>=18.5) e (IMC<25) entao
                 Escreval("Voce esta no peso ideal")
              Senao
                   Se (IMC>= 25) e (IMC < 30) entao
                      Escreval("Sobrepeso")
                   Senao
                        Se (IMC >= 30) e (IMC < 35) entao
                           Escreval("Obesidade")
                        Senao
                             Se (IMC >= 35) e (IMC < 40) entao
                                Escreval("Obesidade Severa")
                             Senao
                                  Escreval ("Obesidade Morbita ")
                             Fimse
                        Fimse
                   Fimse
              FimSE
         FimSe
      FimSe
fimalgoritmo