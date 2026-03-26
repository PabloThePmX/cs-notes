# Aula 6

* Default Gateway.
  * Vai pedir para o roteador para se comunicar com algum servidor.
  * `route print` para mostrar as rotas.
  * O mundo externo só ve até o roteador.
* IPv4 privado (local) e público.
  * Público é o que sai pra internet (roteável).
    * Aquele que aparece no `meuip.com`
  * Qualquer IP que começa com 10, é privado.
  * Várias conexões locais podem estar em apenas um IP público.
* NAT - Network Address Translation
  * Traduz os IPs privados para endereços públicos.
  * Coloca em uma tabela.
* O roteador precisa estar na mesma rede do host.
  * O roteador tem duas interfaces, uma que está conectada na rede privada e outro na pública.
* ICMP -  Internet Control Message Protocol.
  * Tem duas versões (IPv4 e IPv6).
  * A principal função dele é relatório de erros e informações
  * Não é usado pra trafegar dados.
  * Verificar se existe comunicação.
* Roteamento dinâmico e estático.
* Usar o `tracert -d <URL>` para rastrear as rotas para aquele site específico.
  * Também usa o ICMP.
  * Um dos roteadores pode ter o ICMP bloqueado.

## IPv6
* Usa endereços 128 bits.
* Já vem embutido com maior segurança.
* Dividido em 8 conjuntos de 16 bits.
* Hexadecimal.
* Abreviação
  * Pode omitir o 0 a esquerda.
  * Quando tem vários 0, da pra colocar só um
  * Quando tem vários conjuntos de 0 juntos, da pra usar `::`.
    * Só da pra fazer uma vez por IP.
* Geralmente se usa máscara cheia (múltiplos de 4 para facilitar).
* O `localhost` em ipv6 é `::1`.
* Também usa NAT.

## Transporte
* Responsável por gerenciar a comunicação de ponta a ponta.
* Porta de comunicação.
* Existem portas padrões.
  * São as 1023 pra baixo, que são consideradas portas baixas.
  * A padrão pra HTTP é a 80.
  * Só da pra simular usando usuário admin.
* Portas altas da pra fazer servidor sem ser admin.
* A partir da 40mil é dinâmica ou privada.
  * Quando o cliente inicia o serviço.
* TCP, UDP e SCTP.
  * O udp prioriza velocidade, já o TCP prioriza a ordem e a garantia dos dados.
  * O udp é mais comum em streaming/jogos e é usado para VOIP.
    * É mais simples.
  * O TCP tem um controle de fluxo.
    * O cabeçalho é bem maior.
    * Usa Three-Way Handshake.
      * Três pacotes apenas para fechar a conexão.
    * Faz a fragmentação dependendo do tamanho do meio físico.
      * Cria frames.
      * Tem diferença na forma que ele fragmenta, no IPv4 ele fragmente tudo de uma vez, no IPv6 ele ve qual o menor meio físico e fragmente de acordo com ele.