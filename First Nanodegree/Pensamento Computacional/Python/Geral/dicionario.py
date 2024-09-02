from os import system

system("cls")

pessoa = {
    "nome": "pablo",
    "idade": 24,
    "jogos": {
        "nintendo": {"mario", "zelda", "pokemon"},
        "ubisoft": {"ac", "division"}
    }
}

pessoa["jogos"]["sony"] = "god of war"

print(pessoa["jogos"]["sony"])