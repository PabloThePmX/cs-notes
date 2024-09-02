# Aula 6

* Não colocar print nas funções, pois essa função pode ser chamada por aplicações externas que não possuem o print como comando, portanto, usar o return.
* Usar o from, pra pegar funções de outros arquivos.
```python
# se estiver na mesma pasta
from funcoes import funcao1, funcao2
# se estiver em outra pasta
from pasta.funcoes import funcao1, funcao2
# se quiser importar tudo
import pasta.funcoes
    ## e quando for chamar:
    pasta.funcoes.funcao1()
```
* `pychache.pyc` é um binário com o compilado que deve ser executado (`.pyc` é python compiler).