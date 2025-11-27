lar = float(input('Qual a largura da sua parede?'))
alt = float(input('Qual a altura?'))
area = alt * lar
s2 = area / 2
print(f'Sua parede tem a dimensao de {lar}x{alt} e sua área é de {area}m².')
print(f'Para pintar essa parede, você vai precisar de {s2 : .1f} Litros de tinta')