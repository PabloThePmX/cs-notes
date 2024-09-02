# História da Computação
### ENIAC
“Computador eletrônico” que usaria válvulas eletrônicas no lugar de componentes mecânicos.

### EDVAC
Von Neumann introduziu as ideias de neurocientistas que tinham desenvolvido uma teoria das operações lógicas do cérebro (daí vem o termo “memória” em computação.
* Foi nesse momento que surgiu o modelo de Von Neumann, que separava o computador em 3 partes:
  * Memória Principal, CPU e Equipamentos de entrada/saída (input e output)
    * A memória é enviada para a CPU, e a CPU manda isso para os dispositivos, e vice versa.

* Anos depois, surgiram os PCs de mesa, sendo um dos primeiros, o MAC.

# Organização de Computadores

### Modelo de Von Neumann
Focando no modelo em si:
  1. Memória armazenaria não apenas dados numéricos, mas também as instruções de operação.
  2. Unidade Aritmética realizaria os cálculos
  3. Um “órgão” de Entrada permitiria a transferência de programas e dados para a memória
  4. Um “órgão” de Saída armazenaria os resultados da computação.
  5. Uma unidade de controle coordenaria as operações.

* ### Partes do Modelo
   * Unidade de Controle (Está dentro da CPU)
        * Serve para fornecer sinais de controle: 
            * Gerenciar o fluxo interno de dados e o instante preciso em que ocorrem as transferências entre uma unidade e outra; 

            * Seleção de dados para entrada; 

            * Ativação de memória; 

            * Seleção de uma operação;
    * Unidade Operacional (Está dentro da CPU)
      * Também conhecida como bloco operacional (Datapath); 
      * Componentes: 
        * ULA
        * registradores de uso geral e específico
        * Barramentos. 
        * Unidade Lógica e Aritmética (ULA) - Realiza operações lógicas e aritméticas;
    * Memórias
      * Memória principal:  memória usada para armazenar os programas enquanto eles estão sendo executados. 
        * As DRAMs (Dynamic Random Access Memory) são utilizadas como memórias principais.
      * Memória secundária: usada para armazenar programas entre as execuções. Os discos magnéticos são utilizados para essa função. São também chamados de discos rígidos, winchester ou HD (Hard Disc). 

### Hierarquia de Memórias
Ela visa manter os dados utilizados mais próximos da CPU, consistindo em múltiplos níveis de memória com diferentes velocidades e tamanhos.
* Na ordem de mais perto (alto da pirâmide) da CPU temos:
  * Registradores
  * Memoria Cache
    * Usam SRAMs (Static Random Access Memory. As SRAMs são mais rápidas que as DRAMs, mas são mais caras e possuem menor capacidade de  armazenamento para a mesma área de silício.
  * Memoria Principal
  * Memoria Secundaria
    * HDs, portanto, salva quando desliga.
> Lembrando que quanto mais perto da CPU, maior o custo, a velocidade, e menor a capacidade

### Dado, informação e conhecimento
* **Dados** são códigos que constituem a matéria prima da informação.
* **Informação** são esses dados tratados.
* O **conhecimento** é o que tiramos da informação, que fica em nossa mente. (quando a informação é processada em nossa mente)

# Sistemas Operacionais
O sistema operacional faz o controle e o meio termo entre as aplicações e o hardware. (tradutor). O kernel é a parte central do SO, e é ele o responsável por fazer esse meio entre o hardware e o software.
* Temos interfaces de comando e gráficas para poder se comunicar com o SO.
* Cinco gerações de SO
  * Somente na quarte geração tivemos interfaces gráficas.

# Redes
Redes é um Sistema constituído pela interligação de dois ou mais computadores e seus periféricos, com o objetivo de comunicação compartilhamento e intercambio de dados. A rede é o conjunto entre software e hardware.
* Componentes
  * Hardware: PCs, roteadores, etc.
  * Software: TCP/IP, HTTPS, email, etc
* Protocolos:
  * Toda atividade de comunicação na Internet é governada por protocolos Protocolos definem regras que:
    * Estabelecem os formatos e a ordem das mensagens.
    * As ações a serem tomadas na transmissão e recepção das mensagens.

### Estrutura da Rede
* Borda da rede: aplicações e hospedeiros
* Núcleo da rede: roteadores e rede.
* Redes de acesso (o meio físico): enlaces (fios) de comunicação.

### Protocolos
* TCP/IP: Handshake, PC pede a solicitação da rede e recebe
* UDP: Para salvar coisas quando a rede ficou offline por certo período
* HTTPS: Conexão segura
* FTP: Transferência segura
* SMTP: Envio de emails

### Formas de Transferir Dados
* Comutação de circuitos: usa um canal dedicado para a conexão
ex: dirigir com uma rota fixa
* Comutação de pacotes: dados enviados em “blocos” discretos
ex: dirigir com mudança de rotar dinamicamente

# Segurança

# Backups