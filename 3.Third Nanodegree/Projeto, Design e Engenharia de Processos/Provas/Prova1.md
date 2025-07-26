# Prova 1

## Surgimento da Engenharia de Software
* O termo surgiu em 1960, com o intuito de equiparar o desenvolvimento de softwares e outras engenharias. O termo foi adotado pela NATO.
* Criado para padronizar o desenvolvimento, pois na época estavam sendo feito diversos sistemas, em que grande parte eram feitos com baixa qualidade.
* Ajudou na criação das metodologias.

## MVP
* Se trata do conceito de criação de um projeto que engloba o mínimo possível, apenas para demonstrar a função principal do produto.

## Diagrama de Casos de Uso
* Busca demonstrar de forma visual e clara, a interação dos usuários (atores) e o sistema, destacando as funcionalidades principais que o sistema oferece.
* O sistema é representado por um retângulo, e dentro dele vai ter os casos de uso, e o ator fica fora dele, pois estara usando o sistema.
  * Atores são classes (Pessoa, Banco, etc).
  * Ator primário (à direita) é aquele que inicia a utilização do sistema, enquanto o secundário (à esquerda), reage a essa utilização (por exemplo, o usuário pede ao banco algo).
* O caso de uso é uma ação (sempre em verbo).
* Tipo de associação inclusão representa uma ação complementar obrigatória de algum caso de uso.
  * Representado por uma linha tracejada do caso de uso base ate o caso de uso incluído, com a escrita `<<include>>`.
* O tipo de associação de extensão só ocorre se alguns critérios acontecerem (opcional).
  * Representado por uma linha tracejada, saindo do caso de uso opcional até o base, com a escrita `<<extends>>`.
* A generalização é a herança dos casos de uso.

## Fluxograma
* Ele deve ser lido de cima para baixo, e da esquerda para a direita.
* Deixar simples.
* Simbologia:
  * Retângulo: Uma operação ou ação.
  * Losango: Decisão ou bifurcação.
  * Elipse: Usado para indicar o início ou fim do processo.
  * Existem vários outros.

## História do Usuário
* Uma descrição simples de uma funcionalidade do sistema contada do ponto de vista do usuário.
* Destacando **Como**, **eu quero** e **para**
  * Como eu quero fazer algo para ter esse resultado.

## Requisitos Funcionais e Não Funcionais
* Os requisitos funcionais descrevem o que o sistema DEVE FAZER, ou seja, comportamentos.
  * Descrevem funcionalidades e serviços.
* Os requisitos não funcionais descrevem como o sistema DEVE SE COMPORTAR, focando na qualidade, desempenho e restrições do sistema.
  * Descrevem qualidades e caraterísticas.

## Regras de Negócio
* Definem a política, procedimentos e restrições do softwares, a fim de obedecer as necessidades da organização.
* Devem ser alinhadas com o cliente antes mesmo de iniciar o desenvolvimento.

## Ciclo de vida de um software
* É representado por um círculo contendo cada parte do ciclo de vida de um software.
* A ordem seria: Planejamento, Análise, Design, Desenvolvimento, Testes, Implantação e Manutenção.

## Modelos de Desenvolvimento
* O waterfall é um modelo tradicional e sequencial (linear), ou seja, algo precisa estar pronto para que o proximo comece.
* O SCRUM (e o Kanban) é um modelo ágil, que busca trabalhar de forma circular, pois ele sempre está em constante atualização.

## Scrum
* Sprint é a etapa de desenvolvimento, e esse desenvolvimento vai se basear no backlog feito, onde nele vai ter as coisas que precisam ser feitas.
* Papéis:
  * O Scrum Master vai guiar a equipe de desenvolvimento.
  * O Product Owner vai estar falando diretamente com o cliente, e repassando essas informações para o SM.
  * O time desenvolvimento vai ser responsável por realizar as tarefas definidas.
* Três perguntas chaves da daily: O que eu fiz, o que vou fazer e se existe algum impedimento.
* O Kanban pode ser usado para mostrar as atualizações do sprint.
  
## Princípios de Design
* SOLID
  * S de única responsabilidade.
  * O de permitir extensão sem alterar o que já existe (aberto/fechado).
  * L permite que uma classe pai seja substituída por uma classe filha sem que quebre o sistema.
  * I diz que as interfaces devem ser bem específicas, evitando que demande de implementações que o usuário não utilize.
  * D diz que não podemos depender de algo concreto, e sim de uma abstração dela (chamar uma interface ao invés de uma instancia).
* DRY diz que não é pra ficar repetindo código.
* KISS diz para deixarmos tudo o mais simples possível.
* YAGNI diz que devemos apenas priorizar o que sabemos que é necessário.
* Padrões de design são formas de melhorar o design de um software.
-----------
* ### Anotações feitas a partir do que o prof falou:
  * Como começou o design de software, e como surgiu a engenharia, arquitetura etc.
    * OTAN
    * Padronização
  * Saber o que é MVP.
    * Dizer se o produto é MVP ou não.
  * Diagramas de caso de uso
    * Interpretar os campos que faltam.
    * Ver vídeo.
  * Diagrama de classe e fluxo de dados nao cai, mas sim o fluxograma
    * O que cada forma geométrica significa, ordem de leitura, etc.
  * História do usuário.
    * Como, eu quero, para.
  * Diferenciar requisitos funcionais e não funcionais.
  * Regras de negocio, saber diferenciar elas de outras especificações.
  * Papéis no SCRUM.
    * Lembrar de CIO e CEO.
  * O que é backlog
  * Relatórios, qual a importância, etc.
  * O que é o gráfico Gantt
  * Tipos de protótipos
    * Wireframe, alta e baixa fidelidade
  * Ciclo de vida do software, apenas decorar o círculo.
    * O que engloba cada processo.
  * Metodologias de desenvolvimento
    * Diferença entre waterfall, e SCRUM etc.
    * O que é cada uma delas.
    * Processos de scrum.
  * SOLID
    * Saber diferenciar entre eles.
  * Princípios de Design.
    * DRY, KISS, YAGNI.