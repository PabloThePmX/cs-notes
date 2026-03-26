# Aula 3

* Digital Ocean.
* Cuidar com a dependência do provedor.
  * Não conseguir sair da mesma nuvem, pois a aplicação usa alguma ferramenta específica daquele provedor.

## Tipos de Serviços
* SaaS (System as a Service)
  * Só usa, paga e usa, ou seja, vem tudo pronto.
  * Quem contrata não gerencia nada relacionado a estrutura.
* PaaS (Platform as a Service)
  * Usado para hospedar.
  * Oferece um ambiente sob demanda.
* IaaS (Infrastructure as a Service)
  * Dependendo pode ser o mais barato de todos, pois depende do usuário para configura-lo.
  * Elimina um data center.
  * Custo com hardware reduzido.
* Melhor começar com PaaS, e se crescer mudar para IaaS.
* Em alguns casos, vale a pena usar o SaaS estrategicamente, ao menos pra quebrar um galho.
* Um SaaS fica mais difícil de manter pois varias empresas usam exatamente o mesmo serviço.
  * Se subir um update, vai ser pra todos.
    * Porém cada cliente pode ter uma feature especifica (tratado com flags).
* Data lake.
* AWS Elastic Beanstalk.
* Cache do servidor e browser.
  * No browser: Local storage e session storage.
* Escala vertical: So escala um servidor.
* Escala horizontal: Escala servidores ("servidor de um lado pro outro").

## Tipos de Nuvem
* Pública: Qualquer um pode contratar
* Privada: Recurso interno das empresas.
* Híbrido: Junta as duas.
* O servidor que processa, não é o mesmo que armazena.
  * Por isso que se ele estragar, os dados não serão perdidos.

## Migração para nuvem
* Complexidade, custos, segurança, disponibilidade e gerenciamento de mudanças.
* SLA (Service Level Agreement) é um contrato entre o fornecedor de TI (nuvem) e o cliente.
  * Tem uma informação de quantos % o sistema vai estar fora no ano, portanto, só da pra reclamar se passar desse tempo.