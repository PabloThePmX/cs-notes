import os
import random
import time
import datetime
horarioInicial = time.time()
os.system("cls")
print("Horário Atual", datetime.datetime.now())
print(random.randint(0,100))
horarioFinal = time.time()
print("Tempo de Execução:", (horarioFinal - horarioInicial))
