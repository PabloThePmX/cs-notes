# Aula 28

## Infraestrutura, Deploy e Entrega
* Testar localmente primeiro, em um container.
* Sistemas de deploy gratuitos tem condições e limites.
* O frontend pode ser:
  * Estático.
  * Servidor / SSR.
  * Funções.
* Uma SPA estática e uma aplicação com SSR tem necessidades diferentes.
* Algumas para hospedagem: Vercel, Cloudflare, GitHub Pages.
  * Vercel no modo hobby não pode ser usado para uso comercial.
    * Mas é gratuito.
* Quando uma opção gratuita faz sentido:
  * Protótipo, projeto acadêmico, cliente real (mas cuidar pois no hobby pode dar problema).
* O backend pode ficar em sistemas:
  * PaaS.
  * Serverless.
  * Infra própria.
    * VM / VPS.
      * Ex.: DigitalOcean, Hetzner, Lightsail, Hostinger.
* Algumas hospedagens: Render, Railway, Heroku, AWS.
* Guardar arquivos em um storage durável.
  * Banco não é storage de arquivos.
* Algumas opções de banco: Supabase, Neon, Atlas e Amazon RDS.
* Algumas opções de storage: Supabase Storage, Cloudflare R2 e o Amazon S3.
  * O S3 é cobrado pelo upload e download.
* Usar o cache para acelerar as consultas.
  * Pode ser mais demorado para gravar, mas aumenta a velocidade de leitura.
* Cache em dados pouco usados, dados de PK, que nunca mudam.
* Cache precisa ter uma validade, pois ele precisa expirar.
* O cache não é a fonte de verdade.
* Algumas alternativas: Memória local, Upstash Redis, serviço gerenciado.
* Nem todo o projeto precisa de cache.
* O CloudAMQP Free é um servidor de mensageria gratuito.
* As opções mais conhecidas para autenticação: Supabase Auth e Firebase.
* Gateways de pagamento com: Stripe, Asaas, AbacatePay, MercadoPago.
  * API gratuita não significa transação gratuita.
  * No AbacatePay, existe um `.txt` para um agente no link `/llms.txt`.
* Pensar quanto um usuário vai custar para nós.
* A entrega com `CI/CD`, a entrega rápida, uma esteira de entrega.
  * O próprio github possui isso.
* Pipeline: GitHub Actions, a partir de um evento.
  * Ao receber um evento, chama o CI para testar e gerar o build, e depois vai para o CD para publicar a versão.
    * Se falhar, não envia.
* Ambiente local, homologação e produção.
  * Os documentos de segredo não devem ir ao navegador ou repositório.
* Incidentes: Um problema muito crítico.
* Ferramentas para verificar o produto: UptimeRobot, Sentry Free, Grafana Cloud.
  * Defina um para cada tipo de verificação.
* Importante ter ferramentas para rollback.