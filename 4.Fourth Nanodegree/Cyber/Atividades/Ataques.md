<div style="text-align: right"><i>Cyber Security</i></div>
<div style="text-align: right"><i>Prof. Vitalino Pitt | Luciano Ferretto</i></div>

# Ataques Cibernéticos

* Alex Rodrigues Gonçalves (1136919)
* Gabriel Hanel (1135926)
* Mário Bernardo Balen (1136196)
* Pablo Henrique Strücker Sarturi (1136331)

## Ativos

### **Sony (PSN)**
Em 2011 um ataque deixou os serviços da PSN (Serviço online do PlayStation 3) fora por cerca de 1 mês, afetando 77 milhões de usuários e causando um prejuízo de cerca de $171 milhões de dólares para a Sony. Os responsáveis pelo ataque, o grupo Anonymous (que negou responsabilidade) explorou falhas de injeção de SQL, visto que a Sony estava rodando servidores web desatualizados e vulneráveis. Dentro do servidor, o grupo extraiu dados do usuários (possivelmente até cartões de crédito) e a Sony levou quase uma semana para perceber o ataque.

**Taxonomia do Ataque:** 
* *Atacantes:* Invasores.
* *Ferramentas:* Toolkit e Script.
* *Vulnerabilidade:* Configuração/Manutenção.
* *Ação:* Roubo de Recursos.
* *Alvo:* Dados dos Usuários.
* *Resultado:* Obtenção de Recursos de Usuários e Serviço Indisponível.
* *Objetivo:* Dano e provavelmente ganho financeiro.

**Como prevenir:** Atualizar os servidores para utilizar versões mais recentes com patches de segurança, bem como monitorar com maior precisão os acessos indevidos no servidor.

---------

### **NotPetya**
O NotPetya foi um malware que surgiu em 2017 e foi responsável por um extenso ataque cibernético ocorrido na Ucrânia (em decorrência do conflito com a Rússia), ele se disfarçava de ransomware, mas na verdade tinha o objetivo de apagar dados e tornar sistemas inutilizáveis. Ele se espalhou inicialmente via atualização comprometida do software contábil MeDoc e explorou vulnerabilidades do Windows (EternalBlue) para se propagar lateralmente. Ele é um wiper, ou seja, um malware que sobrescreve e destrói arquivos e registros do disco, sem deixar possibilidade de recuperação. O ataque afetou empresas globais como Maersk, Merck e FedEx, paralisando operações e causando prejuízos bilionários.

**Taxonomia do Ataque:** 
* *Atacantes:* Espiões e Terroristas.
* *Ferramentas:* Programa em uma ferramenta distribuída.
* *Vulnerabilidade:* Configuração.
* *Ação:* Varredura total dos dados.
* *Alvo:* Computador e Rede.
* *Resultado:* Corrupção da Informação.
* *Objetivo:* Ganho Político e Dano.

**Como prevenir:** Um malware dentro de uma atualização de um aplicativo terceiro é bem difícil de ser detectado, visto que vem de um software confiável, porém, seria possível mitigar buscando informar aos usuários o quanto antes, bem como tirar do ar a atualização assim que fosse detectado.

## Passivos

### **Community Health Center (CHC)**
Em janeiro de 2025, a CHC confirmou acesso não autorizado e o vazamento de dados de mais de 1 milhão de pacientes. Por ser recente, não temos certeza de como o acesso aconteceu, mas os possíveis modos de ataque incluem: uso de credenciais comprometidas, exploração de vulnerabilidades em aplicações (SQLi, RCE), malware/backdoor com acesso indevido a backups/buckets públicos. Os impactos incluem exposição de dados pessoais e médicos, risco de fraude, perda de confiança e obrigações legais.

**Taxonomia do Ataque:** 
* *Atacantes:* Hackers.
* *Ferramentas:* Comando executado por usuário, programa ou ferramenta distribuída.
* *Vulnerabilidade:* Configuração.
* *Ação:* Roubo.
* *Alvo:* Dados.
* *Resultado:* Corrupção de Informação e roubo de recursos.
* *Objetivo:* Ganhos financeiros (provavelmente). 

**Como prevenir:** Por ser uma instituição com informações sensíveis, a rede e os computadores devem estar totalmente protegidos e monitorados, para que qualquer alteração no sistema possa ser detectada o quanto antes, além de que, sistemas como esses não podem rodar versões desatualizadas de softwares, bem como, devem funcionar apenas con versões consolidadas desses softwares, pois as versões consolidadas (LTS) já passaram por extensos testes.

---------

### [**Espionagem de Ativistas e Jornalistas**](https://www.cnnbrasil.com.br/internacional/investigacao-aponta-que-spyware-espionou-jornalistas-e-ativistas-em-todo-o-mundo/) 
Trinta e sete smartphones de jornalistas e ativistas foram visados por um spyware de nível miliar licenciado por uma empresa israelense. Em 2021 foi detectado que o spyware Pegasus estava sendo usado para perseguir e vazar dados de inimigos políticos de países de forte censura. A empresa responsável negou haver vendido o sistema para outros além de agencias de inteligência. Esse spyware é projetado para contornar facilmente medidas de privacidade típicas de smartphones, atacando-os sem nenhum alerta aos usuários. O Pegasus costuma se propagar via links de SMS, bem como mensagens sem notificação, que acabam infectando o telefone sem mesmo que haja qualquer interação com o mesmo (zero clicks).

**Taxonomia do Ataque:** 
* *Atacantes:* Espiões.
* *Ferramentas:* Programa.
* *Vulnerabilidade:* Design de segurança dos smartphones.
* *Ação:* Bypass.
* *Alvo:* Dados e contas.
* *Resultado:* Roubo de informações. 
* *Objetivo:* Ganho politico.

**Como prevenir:** Por se tratar de um software poderoso que é capaz de se infiltrar sem nenhum alarde, acaba sendo mais difícil providenciar alguma forma de prevenção, mas pode-se mitigar usando telefones temporários (no caso de perseguidos políticos e afins).