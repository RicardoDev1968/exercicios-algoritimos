import=math

d = float(input('Quantos dias alugado?'))
km = float(input(f'Quantos Km rodados nesses {d:.0f} dias? '))
dd = d * 60
kmm = km * 0.15
print(f'Você terá que pagar {dd + kmm:.2f}R$')