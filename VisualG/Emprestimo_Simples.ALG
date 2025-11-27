algoritmo "empres"
var
 emp, par, total, val: Real

inicio
 Escreva("Valor do emprestimo:")
 Leia(emp)
 Escreva("Quantidades de parcelas")
 Leia(par)
 total<- emp * 20 / 100 + emp
 val<- total / par
 Escreva (" Voce terá que pagar por mes o valor de: ",val)
 

fimalgoritmo