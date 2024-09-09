class Veiculo:
    def __init__(self, marca, modelo, placa, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano

    # Métodos getters and setters para os atributos privados
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_placa(self):
        return self.__placa
    def set_placa(self, placa):
        self.__placa = placa

    def get_ano(self):
        return self.__ano
    def set_ano(self, ano):
        self.__ano = ano


    def calcularTempoUso(self):
        return 2024 - self.__ano
    ## altera a formatação padrao da string da classe
    def __str__(self):
        return f'''
- Modelo: {self.__modelo}
- Marca: {self.__marca}
- Placa: {self.__placa} 
- Ano: {self.__ano}
    '''
    
meuCarro = Veiculo("Chevrolet", "Celta", "ABC-1234", 2014)