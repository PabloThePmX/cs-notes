from Veiculo import Veiculo
from Moto import Moto

meuCarro = Veiculo("Chevrolet", "Celta", "ABC-1234", 2014)

moto = Moto("Honda", "Biz", "123", 2015, 220)
# cria a prop dentro da classe "automaticamente"
moto.partidaeletrica = True
print(moto)