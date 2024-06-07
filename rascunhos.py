#importa o módulo
from modulo import calcular_quadrilatero, calcular_triangulo #importa apenas funções específicas
import modulo #importa o módulo completo
#calcular a área de um quadrilátero
#entrada de dados
b = int(input('Informe o valor da base:'))
h = int(input('Informe o valor da altura: '))

#calcula a área do quadrilátero
int(f'Área do quadrilátero: {calcular_quadrilatero(b, h)}.')

#calcula a área do triângulo 
print(f'Área do triângulo: {calcular_triangulo(b, h)}')

#calcula a área de um circulo 
#entrada de dados
r = float(input('Infome o valor do raio: '))

#exibe a área da circunferência
print(f'Área do círculo: {modulo.calcular_circulo(r)}.')

