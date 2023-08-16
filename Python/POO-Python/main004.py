from escritor import Escritor
from caneta import Caneta
from maquina import MaquinaDeEscrever 

escritor = Escritor('Silas')
print(escritor.nome)
caneta = Caneta('Bic')
print(caneta.marca)
maquina = MaquinaDeEscrever('2023')

escritor.ferramenta = caneta

escritor.ferramenta.escrever()
escritor.ferramenta.maquina()