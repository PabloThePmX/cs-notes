# Aula 29

* Usar o Eclipse EE
* Criar um package no eclipse.
  * A convenção de nomenclatura seria a reversa do domínio da empresa, ou seja, `minhaempresa.com` seria `com.minhaempresa`, ou `br.com.minhaempresa`
  * Possível ter pacotes dentro de outros.
    * Geralmente tem um pacote inicial, e outros sub pacotes.
      * O `protected` é um modificador de acesso usado para permitir o acesso por sub pacotes (sub classes).
  * Sub pacote `utils` com os utilitários do projeto.
    * Os sub pacotes precisam ser importados na classe que vai utiliza-los.
* O package é uma estrutura de pastas, cada ponto é um diretório.
* Tudo que for `java.lang` não precisa importar.

## Arquitetura Monolítica
* Tudo em um bloco só, no mesmo sistema.
* Não recomendado para projetos mais complexos.
  * Se um sistema falhou, afeta a todos os sistemas.

## Arquitetura de Camadas
* Separa um sistema monolítico em camadas.
  * UI, Services (regras de negócio) e Data Access Layer (repositórios).
  * Cada um pode ser um pacote diferente.
    * Mesmo que os projetos no C#.
* Se alinha bem com padrões, como o MVC e SOLID.

## Arquitetura Cliente Servidor
* Separa o back e o front em dois projetos
  * Servidor - back.
  * Cliente - front.
* O protocolo HTTP é cliente (que é o navegador, a aplicação, etc) e o servidor é o backend, ou seja, toda a internet é funciona assim.
* Cada elemento usado no html que esteja em algum outro local, vai fazer uma requisição para busca-lo.
  * Requisição para o css, imagens, apis, scripts, etc.
  * O cliente (navegador) que vai fazer essas requisições, ou seja, ele que vai solicitar as informações.
* O swagger é a documentação da API. 
* O cliente faz um fetch para o servidor.
* A comunicação entre os dois costuma ser HTTP.

## Arquitetura MicroServiços (o mais utilizado, geralmente em médios ou grandes projetos)
* É dividido em vários projetos menores.
  * Possível trabalhar em cada serviço individualmente.
* Tem uma (ou várias) api de entrada (api gateway), que vai chamar o microsserviço desejado.
* Cada microsserviço é como um projeto diferente, portanto cada um pode ter uma linguagem, ou um banco específico.
* O cliente (o front) é um só sempre.
  * Mas pode ter front pra mobile, web, android, ios, etc.