# Aula 4

## Gerenciamento de Memória
* É uma das funções mais críticas do SO, pois garante que os processos tenham o acesso adequado à memória RAM, otimizando a utilização dos recursos disponíveis.
* A memória RAM é temporário e de altíssima velocidade, e é volátil, ou seja, apaga ao desligar o sistema.
* A memória virtual é uma técnica que utiliza parte do disco rígido (ou SSD) como uma extensão temporária caso a RAM fique cheia.
  * O sistema transfere dados inativos para esse espaço no disco (arquivos de paginação ou swap).
  * Pode deixar o computador mais lento.
* O processo acha que a memória é continua, mas a mesma tem a suas páginas espalhadas pela RAM e até no disco.
  * Pois que se comunica com a RAM física é somente o SO, os aplicativos não fazem ideia do tamanho ou do endereçamento.
* A RAM não guarda o processo inteiro junto, mas sim em páginas que ficam espalhadas em diferentes posições de memória.
* Cada processo tem acesso apenas à quantidade necessária de memória para a sua execução.

### Estratégias para Gerenciamento de Memória

#### Particionamento Contíguo
* A memória é dividida em segmentos contíguos (perto um do outro) para cada processo.
* Pode ser fixo ou dinâmico.
* No dinâmico o tamanho varia de acordo com a entrada e saída dos processo na memória.

#### Paginação
* A memória é dividia em blocos de tamanho fixo, chamadas páginas.
* Carrega apenas as páginas necessárias para o processo.
* Bibliotecas em comum que são usadas por vários processos, podem ser carregadas em apenas uma página e acessada pelos processos que necessitam. (Shared Pages)

#### Segmentação
* A memória é dividida em segmentos de tamanhos variados com base na estrutura lógica do programa.
* Ajuda a otimizar a alocação, pois cada segmento pode ter um tamanho adequado às necessidades do programa.
* Ou seja, o código pode ter o seu segmento, e os dados e a pilha outro.

#### Memória Virtual
* Permite que programas sejam carregados mesmo que estejam parcialmente carregados na memória principal.
* A memória virtual utiliza o disco para armazenar dados que não estão atualmente na RAM, permitindo que os programas utilizam mais memoria do que está fisicamente disponível.

#### Técnicas Avançadas
* Swapping
  * Retira o processo da RAM e manda pro disco.
* Compactação de Memória
  * Reorganiza os dados na memória para eliminar espaços vazios.
  * Raramente utilizada devido ao alto custo computacional.

### Memória Primaria
* É composta pro componentes como RAM, cache e processador.
* Armazenamento temporário dos dados e programas em execução.
* É volátil, ou seja, os dados são perdidos quando a energia é desligada.
* Rápido acesso.

### Memória Secundária
* Refere-se ao armazenamento permanente de dados, utilizando HDs, SSDs e dispositivos removíveis como pendrives.
* É mais lenta que a primária.
* Não volátil, visto que os dados são persistidos ao desligar.

### Cache
* Memória muito rápida usada pela CPU para acessar dados mais rapidamente.
* Fica dentro ou próxima da CPU, e guarda dados sendo usados com frequência, evitando que a CPU vá até a RAM toda hora.
  * É um atalho de memória.
* Dividida em 3 nívies:
  * L1
    * A mais rápida.
    * Menor tamanho.
    * Fica dentro do núcleo da CPU.
    * O que a CPU está usando agora.
  * L2
    * Um pouco maior
    * Um pouco mais lenta
    * Apoia a L1.
  * L3
    * A maior de todas.
    * Compartilhada entre núcleos.
    * Mais lenta que as outras.
    * É uma reserva rápida antes da RAM.

### Memória Virtual
* Combina a RAM com um espaço no disco rígido, conhecido como arquivo de paginação ou swap.
  * A paginação virtual é enviada para um frame da memória física.
* Usado quando a RAM está cheia.
* A transferência dos dados para o disco é chamada de paginação.
* Como principais funções:
  * Permite a extensão de memória.
  * Cada processo opera em seus próprio espaço de endereçamento, impedindo que cada processo acessa a memoria de outro.
  * O SO gerencia automaticamente o que deve ser mantido na RAM e o que pode ser movido para o disco.

### Fragmentação
* Acontece quando a memória fica "quebrada em pedaços" e isso dificulta o uso eficiente.
* Ou seja, quando tem espaço livre mas está mal distribuído.
* Tipos de Fragmentação:
  * Externa
    * O problema está entre os blocos
    * Tem espaço livre mas está espalhado em vários pedaços.
  * Interna
    * O problema está dentro do bloco.
    * O processo recebe mais espaço do que precisava, e sobra espaço desperdiçado dentro dele.
* Isso pode acontecer por:
  * Particionamento dinâmico: gera fragmentação externa.
  * Particionamento fixo: gera fragmentação interna.
  * Paginação: Resolve o problema da externa, mas pode ter interna.
  * Segmentação: Pode ter fragmentação externa.