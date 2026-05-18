# Maior Valor

* Mário Bernardo Balen (1136196)
* Pablo Henrique Strücker Sarturi (1136331)

## Analisando a Função
| Item                              |  Resposta |
|-----------------------------------|-----------|
| Função escolhida                  | Maior Valor 
| Entradas                          | a & b     |
| Saída / retorno                   | O maior valor, podendo ser a ou b |
| Responsabilidade                  | Encontrar o maior valor entre dois números inteiros  |
| Retorna em todos os caminhos?     |   Sim     |
| Representa lógica combinacional?  |   Sim     |
| Uso provável na architecture      |   `maior_valor <= maior(1, 8)` |

## Refatoração
```vhdl
function maior(a, b : bit) 
    return bit is
begin
    return a when a > b else b;
end function;
```
Usando na architecture:
```vhdl
maior_valor_ab <= maior(a, b);
maior_valor_cd <= maior(c, d);
```

## Questões

1. **Por que uma função em VHDL deve ter uma responsabilidade clara?**

    Pois o VHDL não é uma linguagem tão simples, portanto, é melhor separar em pequenas lógicas com responsabilidades claras, e por isso o uso de funções pode se tornar ainda mais úteis.

2. **Qual a diferença entre usar uma função e usar um process com clock?**
   
    Uma função em VHDL normalmente representa lógica combinacional, retornando um valor imediatamente a partir das entradas. 
    Já um process com clock representa lógica sequencial, onde os valores são atualizados somente na borda do clock, permitindo armazenamento de estado em registradores ou flip-flops.

3. **Por que uma função não deve ser usada para guardar estado?**
   
    A função deve ser relativamente simples, sendo usada apenas para realizar lógicas e cálculos combinacionais que serão retornados a partir dos parâmetros de entrada.

4. **Quando faz sentido colocar uma função em um package?**

    Quando é uma função que poderá ser reutilizada por outras entidades ou architectures, permitindo uma melhor organização e estruturação do projeto.

5. **A função melhora o hardware ou melhora principalmente a organização do código?**
   
   É possível considerar que ambos. Visto que ao melhorar a organização de códigos, conseguimos separar e encontrar pontos de melhora, que consequentemente podem melhorar a simulação, a síntese, a manutenção e o hardware final.