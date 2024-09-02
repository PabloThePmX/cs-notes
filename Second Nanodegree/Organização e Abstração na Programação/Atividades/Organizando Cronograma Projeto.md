# Software para auxiliar pessoas com Desvio de Foco (assim como eu)
O propósito deste sistema será de auxiliar pessoas que assim como eu, possuem uma certa dificuldade para focar nas tarefas. Essa aplicação web tentará dar dicas para o usuário em cada momento em que ele relate alguma adversidade.

## Modelo Cascata
* **Requisitos**: Realizar pesquisas com pessoas que sofrem com isso, para tentar buscar padrões, e entender como eles se sentiriam caso recebessem ajuda diretamente pelo sistema.
* **Planejamento**: A partir da pesquisa, definir como será o fluxo da aplicação, e quanto tempo e dinheiro custará, visto que já temos as informações da persona e quais as necessidades deles.
* **Modelagem**:
  * Banco: Além das tabelas da aplicação em si, idealizar tabelas específicas para salvar o progresso e escolhas de cada usuário.
  * Classes: Definir quais as classes serão necessárias para deixar o backend funcionando.
* **Desenvolvimento**: Desenvolver primeiro o backend usando ASP.NET Core com o C#, e para desenvolver o front, utilizar o Figma para criar a UI e um framework como Angular para desenvolver. Documentar cada processo envolvido durante o desenvolvimento.
* **Testes**: Fazer testes unitários para cadastros em tabelas mais cruciais, e as outras deixar apenas que o time de QA teste manualmente.
* **Implantação**: Será hospedado na Azure, e o domínio será comprado para utilizar um nome mais fácil no link.
* **Manutenção**: Aos poucos ir criando mais testes unitários, e ir aumentando a documentação para que qualquer programador possa entender o que o código estará fazendo. Usuários poderão relatar bugs para serem corrigidos.
  
## Modelo Espiral
* ### Início (Início do Espiral - Processo mais devagar)
  * **Requisitos**: Verificar quem vai ser a persona, e o que vai ser feito para auxilia-los com a falta de foco.
  * **Planejamento**: Planejar essa etapa inicial do projeto, verificando quais as tabelas e quais telas serão necessárias. Definir as linguagens que serão usadas (ASP.NET e o framework Angular)
  * **Modelagem**: Análise e criação das tabelas necessárias no banco, para o cadastro do usuário e dicas. Verificar também quais as classes vão ser necessárias para ter o backend funcionando.
  * **Desenvolvimento**: Desenvolvimento das telas principais, do banco e das classes, documentando cada passo. 
  * **Protótipo**: Mostrar para a gerência como o projeto está sendo realizado.
  * **Revisão dos requisitos com a equipe gerencial**: Após essa primeira etapa, revisar com a equipe gerencial se está tudo de acordo com o que havia sido planejado.
* ### Meio (Processo normal)
  * **Planejamento**: Planejar como serão feitas as rotinas mais "secundárias" do frontend, como por exemplo o acompanhamento da evolução do usuário, além de verificar se está tudo andando conforme o prazo.
  * **Desenvolvimento**: Desenvolvimento das rotinas secundárias.
  * **Protótipo**: Envio do novo protótipo para a gerência.
  * **Avaliação da Gerencia da Empresa**: Reunião para definir quais as mudanças serão necessárias depois da avaliação do protótipo. 
* ### Fim (Processo rápido)
  * **Planejamento**: Sprint final, verificando quais foram as mudanças propostas pela gerência, e como podemos encaixar estas alterações dentro do prazo.
  * **Desenvolvimento**: Desenvolvendo as mudanças que o setor de gerência pediu. Criação de Unit Tests para testar automaticamente as rotinas.
  * **Implantação**: Implantação no servidor da Azure, criação dos processos para atualizar automaticamente a aplicação quando for enviada para a branch main. Criação do banco de dados na nuvem. Compra do domínio para o site.
  * **Testes**: Testando a aplicação final na nuvem.
  * **Manutenção**: Verificando se a documentação está em dia. Designando parte do time para trabalhar na correção de bugs que vai ser reportada pelos usuários.