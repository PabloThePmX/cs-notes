from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas

    def get_cilindradas(self):
        return self.__cilindradas
    def set_cilindradas(self, cilindradas):
        self.__cilindradas = cilindradas
    
    def __str__(self):
        # pega o valor retornado desse método da classe pai
        retorno = super().__str__()
        # altera o valor
        return f'''
{retorno} 
- Cilindradas: {self.__cilindradas}'''