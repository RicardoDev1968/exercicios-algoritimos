algoritmo "esperanca"
var
  N1, N2, M: Real
inicio
      Escreva("Primeira nota: ")
      Leia(N1)
      Escreva("Segunda nota: ")
      Leia(N2)
      M <- (N1 + N2) / 2
      Escreval (" Sua media é ", M)
      Se (M <=10) e (M >= 9) entao
         Escreval("Aproveitamento do Aluno é A")
      Senao
           Se(M <= 8.9) e (M >= 8)entao
                 Escreval("Aproveitamento do Aluno é B")
           Senao
                Se (M <= 7.9) e (M >= 7) entao
                   Escreval ("Aproveitamento do Aluno é C")
                Senao
                     Se (M <= 6.9) e (M >= 6) entao
                        Escreval ("Aproveitamento do Aluno é D")
                     Senao
                        Se (M <= 5.9) e (M >= 5) entao
                           Escreval("Aproveitamento do Aluno é E")
                        Senao
                             Escreval("Aproveitamento do Aluno é F")
                        Fimse
                     Fimse
                FimSE
           FimSE
      FimSe

fimalgoritmo