# REST e Mensageria

1. A Api REST segue o design de arquitetura REST (conjunto de restrições) e é baseada no protocolo HTTP (cliente servidor). Dessa forma, é possível realizar requisições para URL, especificando seu método (GET, POST, PUT, DELETE, etc) e esses métodos são responsáveis por se comunicar com um outro fim, para tratar dados.

    **Vantagens:** Escalável, Flexível, Independente, Segurança, etc.

    **Desvantagens:** Pode ser difícil de trabalhar sem uma documentação (Swagger), caso não rodar localmente, pois a conexões lentas com a internet (latência) podem atrapalhar as requisições, comunicação naturalmente síncrona.

    **Casos de Uso:** Envio de informações entre uma aplicação web e o backend, comunicação com serviços cloud e microsserviços.
    
    **Microsserviços:** É possível usar APIs REST para se comunicar entre microsserviços, para isso precisamos fazer uma chamada a um método via interface que por sua vez vai ser uma abstração de um cliente que vai fazer uma requisição ao endpoint do microsserviço que lhe foi designado, no java, podemos usar o FeignClient e o Eureka para descobrir os microsserviços que estão rodando.

2. A mensageria é uma abordagem de desenvolvimento usando mensagens para estabelecer comunicações entre aplicações, usando um Message Broker. Esse MOM é um servidor idealizado unicamente para processar e suportar o envio/recebimento, redirecionamento e também a monitoria das mensagens compartilhadas entre os sistemas integrados por mensagem. O protocolo AMPQ por sua vez costuma ser usado com o broker RabbitMQ. Existem vários modelos de integração (a forma vai funcionar a comunicação). Em resumo, ele envia "mensagens", que são estrutura de dados, para os microsserviços de forma assíncrona, e o serviço que vai enviar, não precisa saber se o serviço que vai consumir está ativo no momento, pois fica como se fosse em uma "fila de espera", e o serviço as consome apenas quando ele for reativado.

    **Vantagens:** A aplicação produtora da mensagem não precisa se preocupar se a aplicação consumidora está disponível no momento do envio, baixo acoplamento na integração entre sistemas, deixando a comunicação assíncrona, é possível tentar consumir a mensagem mesmo após uma falha, devido a mesma estar enfileirada no Broker, etc.

    **Desvantagens:** Mais complexo, não é muito adequado em modelos que dependem mais de comunicações síncronas.

    **Casos de Uso:** Envio de notificações e emails, processamento de pedidos em e-commerce.
    
    **Microsserviços:** Usando o event sourcing, as mudanças no estado do sistema são registradas como eventos imutáveis que são enviados e consumidos por diferentes microsserviços. Por exemplo, quando um pedido é criado, o serviço de pedidos emite um evento “PedidoCriado”. Outros microsserviços, como o de faturamento ou o de estoque, podem reagir a esse evento e executar suas próprias ações, mantendo o sistema desacoplado e reativo.