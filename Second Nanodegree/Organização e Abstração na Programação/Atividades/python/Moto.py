from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas

    def get_cilindradas(self):
        return self.__cilindradas
    def set_cilindradas(self, cilindradas):
        self.__cilindradas = cilindradas
    
moto = Moto("Honda", "Biz", "123", 2015, 220)
moto.partidaeletrica = True
print(moto)