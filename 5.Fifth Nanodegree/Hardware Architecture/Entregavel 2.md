# Bloco 1 — Cálculo de média e aprovação

* Mário Bernardo Balen (1136196)
* Pablo Henrique Strücker Sarturi (1136331)

## Objetivo Geral
O objetivo dessa rotina é carregar três notas armazenadas em memória, realizar o cálculo da média aritmética e verificar, através de uma comparação lógica, se o aluno atingiu a nota mínima necessária para aprovação.

## Explicações

| Instrução | Operandos        | Tipo de instrução      | Modo de endereço provável           |
|------------|-------------------|-------------------------|--------------------------------------|
| LOAD       | R1, [1000]        | Movimentação de dados   | Registrador e Memória               |
| LOAD       | R2, [1004]        | Movimentação de dados   | Registrador e Memória               |
| LOAD       | R3, [1008]        | Movimentação de dados   | Registrador e Memória               |
| ADD        | R4, R1, R2        | Aritmética              | Registrador                         |
| ADD        | R4, R4, R3        | Aritmética              | Registrador                         |
| MOV        | R5, #3            | Movimentação de dados   | Registrador e Imediato              |
| DIV        | R6, R4, R5        | Aritmética              | Registrador                         |
| STORE      | [1012], R6        | Movimentação de dados   | Memória e Registrador               |
| CMP        | R6, #7            | Aritmética              | Registrador e Imediato              |
| BGE        | APROVADO          | Controle de fluxo       | Indireto                            |
| MOV        | R7, #0            | Movimentação de dados   | Registrador e Imediato              |
| JMP        | FIM               | Controle de fluxo       | Indireto                            |
| APROVADO   |                   |                         |                                     |
| MOV        | R7, #1            | Movimentação de dados   | Registrador e Imediato              |
| FIM        |                   |                         |                                     |
| STORE      | [1016], R7        | Movimentação de dados   | Memória e Registrador               |

## Código Equivalente

```c#
using System;
					
public class Program
{
	public static void Main()
	{
		if(GetStudentGrade())
			Console.WriteLine("Aprovado");
		else
			Console.WriteLine("Reprovado");
	}
	
	private static bool GetStudentGrade() 
	{
		Console.Write("Digite a nota 1: ");
		float.TryParse(Console.ReadLine(), out float R1);
		Console.Write("Digite a nota 2: ");
		float.TryParse(Console.ReadLine(), out float R2);
		Console.Write("Digite a nota 3: ");
		float.TryParse(Console.ReadLine(), out float R3);
		
		float finalGrade = (R1 + R2 + R3)/3;
		
		Console.WriteLine($"\nNota Final {finalGrade:F2}\n");
		
		return finalGrade >= 7;
	}
}
```

## Conclusão
Concluímos que mesmo uma tarefa relativamente simples, como calcular a média de um aluno e determinar sua aprovação, exige a utilização de diferentes tipos de instruções em baixo nível, incluindo movimentação de dados, operações aritméticas, comparações lógicas e controle de fluxo.

