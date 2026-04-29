# Aula 13

## Hierarquia de Memória

* Memória principal (DRAM) e secundária.
* Um programa não acessa todo o seu código e dados ao mesmo tempo.
  * Ele usa cada vez um, como cache, principal e secundária.
  * Faz a memória parecer maior.
* Os registradores são os menores e mais rápido, depois vem a cache, principal e secundária.
  * Quando maior a velocidade, maior o custo e menor a capacidade.
* Os dados contidos num nível mais próximo do processador são sempre um sub-conjunto dos dados contidos no nível anterior.
  * O nível mais baixo contém a totalidade dos dados.
  
### Cache
* Usam SRAMs, que são mais rápidas que as DRAMs.
* Existem 3: L1, L2 e L3.
  * Sendo a L1 a mais proxima ao processador, e a L3 é menos rápida pois compartilha con todas as threads.
* Tempo de acesso de 0,5 a 5ns.
* Um `hit` é quando o processador pede por um dado, e o mesmo existe na cache.
  * E o `miss` é quando não tem.
    * Quando ele busca, não encontra e busca na memória primeira e/ou secundária, ele muda para `hit`.
* O tempo de hit é o tempo de acesso com sucesso a cache
* Penalidade de miss é o tempo de transferência do dado para a cache.

## Com funciona a Cache?
* Memória pequena ao lado do processador.
* Mapeamento Direto: Cada bloco pode ser colado em uma única posição na cache.
  * Pode ser colocado em qualquer lugar.
* Totalmente Associativo: Cada bloco pode ser colocado em qualquer posição na cache.
  * Só pode ser colocado em um local, encontroado pelo resto de 12/8 (12 % 8).
    * Falado melhor abaixo.
* Parcialmente Associativo: Cada bloco pode ser colocado em um conjunto restrito de posições dentro da cache.
  * Também verifica com o calculo, mas os blocos são separados em conjuntos, portanto ficaria 12 % 4.
  * Sempre que falar em conjuntos ou sets, vai ser esse.
  * Primeiro o conjunto precisa ser mapeado.4
* Para encontrar um bloco correspondente a um endereço:
  * Usar a fórmula: Endereço do bloco MÓDULO Número de blocos da cache.
    * Pegar o endereço e dividir pelo tamanho de bytes de cada bloco, para encontrar o tamanho do bloco.
    * Ex.: 
    ```
    32 blocos
    16 bytes
    1392 endereço

    1392/16 = 87

    87 % 32 = 23 <- posição que vai estar na cache
    ```
* Quando acontece um miss, o processador congela o seu funcionamento (stall), até que a memória cache busque no nível anterior o dado requisitado.
* Se a cache ta cheia, existe as seguintes estratégias para substituição de bloco:
  * **Aleatório**.
  * **Menos recentemente usado (LRU)**.
  * **Primeiro a entrar, primeiro a sair (FIFO)**.
* Para escrever na memória, é necessário mandar primeiro para o cache, e depois para a memória.
  * Existem duas formas de escrita:
    * **Write-Through:** Consiste em sempre escrever na cache e na memória principal, garantindo dados consistentes.
    * **Write-Back:** É escrita somente na cache, e só é escrito no nível inferior quando o mesmo precisar ser retirado da cache.