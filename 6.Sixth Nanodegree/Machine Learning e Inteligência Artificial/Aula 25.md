# Aula 25

## Harness, Skills e Agentes
* É possível automatizar usando agentes.
* Se a tarefa for repetitiva, é possível utilizar skills.
* Skill: procedimento.
  * Ensina como fazer uma coisa, especialmente algo repetitivo.
* Agente: especialista (não deve existir um agente genérico, ou seja, especialista em um tópico com um agente orquestrador).
  * Desenvolve.
  * São os agentes que disparam a skill.
* Tarefa: pedido atual.
* A primeira coisa que o agente vai ler, é o `README.md`.
* A skill tem um `frontmatter` (um template com o nome e a descrição do que ela faz), e isso fica no início, tanto na skill, como pode ficar num agent.
  * Explica quando usar, enquanto o corpo da skill explica como trabalhar.
  * A skill pode ter scripts.
  * Pastas `references/`, `scripts/` e `assets/`.
* Limitar o orquestrador para apenas mandar os outros agentes realizar, sem implementar nada.
  * Dar um "nome" para o orquestrador, assim, ao chama-lo ele ja começa a orquestração.
* Perfil do agente em `.TOML` no Codex e `.md`.
  * Da pra definir um modelo diferente para cada um, ou seja, um modelo que precisa pensar mais, usa modelos melhores, outros que são mais executores, usam outros mais simples.
    * Definido no `frontmatter`.
* Da pra usar a própria IA para criar um agente.
  * Cada subagente vai ter seu próprio nome.
* Da pra ter agentes por usuário ou de projeto.