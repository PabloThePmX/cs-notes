# Aula 23

* Fluxograma para resolver problemas complexos.
* Parar e planejar o projeto.
* Máquina de Estados.
  * Existe um diagrama só para isso.
* Backend deve ter as verificações também, e não só apenas no front.
* Microservices
  * Separar rotinas em vários sistemas que se comunicam entre si.
  * Evita que algum erro ou instabilidade interfira em outros serviços.
  * Grandes sistemas funcionam assim.

### Diagrama de caso de uso:
* Como dividir responsabilidades.
* Utilizar a UML (Linguagem de Modelagem Unificada).
  * É uma linguagem pois segue padrões.
  * Tipos de diagramas da UML:
    * Estruturais.
    * Comportamentais.
    * Interação.
* Caracteristicas:
  * Caso de uso, agente/ator e relacionamento.
    * Ex: Cliente e sistema são os atores.
    * Os casos de uso são os requisitos.
* Linha reta sólida é apenas quando o ator interage com o caso de uso.
* Linha pontilhada é o relacionamento entre os casos de uso.
* O `extends` na linha significa que é opcional (apenas entre casos de uso).
* O `include` na linha significa que é obrigatório (apenas entre casos de uso).
* A flecha na linha, significa quem está agindo em quem, e que não haverá resposta.
* Separando rotinas, isolando elas.
  * Dentro de cada rotina, podemos definir o resumo, atores, pré e pós condições.
  * Bem como os fluxos dessa rotina.
* Algumas ferramentas:
  * Drawio
  * Astah Community
* Ser específico apenas para coisas mais importantes e principaís.
* Para fazer os relacionamentos, é possível pensar que, para fazer determinado requisito, é preciso usar esse outro requisito.
  * Quase como uma ação e consequência.