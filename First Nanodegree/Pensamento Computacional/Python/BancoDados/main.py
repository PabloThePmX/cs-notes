try:
    arquivo = open("bd.atitus", "w", encoding="utf-8") #w, r, a (write, read, append)
    arquivo.write("oi")
    arquivo.close()
except Exception as error:
    print(error)