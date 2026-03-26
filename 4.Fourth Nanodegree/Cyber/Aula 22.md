# Aula 22

* Pentest é um teste para encontrar vulnerabilidades em sistemas.
  * Existe uma metodologia, mas não precisa exatamente seguir ela.
    * Conforme for fazendo, vai adquirindo o conhecimento.
  
## Normas e Padrões do Pentest
* OWASP para web
  * O Top 10 tem as vulnerabilidades mais comuns da web.
* NIST é tipo a ISO.
* PTES para os padrões de pentest.
* OSSTMM é um manual de metodologia e testes.
* ISO 27001 é o SGSI.
  * A segurança da informação não está dentro da TI em si.
* PCI DSS para proteger dados do cartão e transações financeiras.
* CWE/SANS possui uma lista dos erros mais perigosos de software.
* ISSAF é um framework para pentest, um guia.
* MITRE ATT&CK possui todas as táticas e técnicas de ataque.

## Tipos de Pentest
* Black-box
  * O pentester não terá conhecimento prévio da infra do cliente.
  * Simula com exatidão o ataque externo
* Grey-box
  * O pentester tem conhecimentos parciais da infraestrutura, como pontos críticos.
* White-Box
  * O pentester tem todas as informações do sistema e infraestrutura.
  * É o mais barato e rápido.
  * Simula um ataque interno.

## Fases do PTES
* Preparação e planejamento.
  * São definidos os objetivos do teste de penetração.
  * Define o escopo do teste.
  * Obter autorização.
  * Documentar tudo.
* Coleta de informações.
  * Reúne as informações sobre o alvo, que podem ser úteis no planejamento do teste de penetração.
  * Podem ser coletadas de fontes públicas ou privadas.
  * Ferramentas para ser usadas podem ser o OSINT, Google Dorks, Censys, Github Dorks, SpiderFoot, etc.
* Análise de ameaças.
  * Identifica as possíveis ameaças.
* Testes de vulnerabilidade.
  * São identificadas as vulnerabilidades dos alvos.
  * O objetivo é encontrar vulnerabilidades que podem ser exploradas.
  * Ferramentas para fazer a análise: Nmap, Nessus, Burp Suite, etc.
* Exploração.
  * Ganhar acesso não autorizado ao sistema.
  * Algumas ferramentas podem ser: Metasploit, Mimikatz, SQLMap, Rubeus, Social-Engineer Toolkit (clonagem de site), etc.
* Pós exploração.
  * Quando foi conseguido o acesso a máquina.
  * Ferramentas para usar: Bloodhound, PowerSploit, Xmind, etc.
* Relatório.
  * Documenta e descreve as atividades que foram e não foram realizadas.
  * Um mais técnico, e o outro mais amplo para que a empresa possa entender.
  * Ferramentas como OpenVAS, CherryTree, etc.