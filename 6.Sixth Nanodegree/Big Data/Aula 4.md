# Aula 4

* MongoDB não tem join.
* ETL -> Extração de dados (no python, usa-se `numpy` e `pandas`).
* Star Schema: Usado em data warehouse, agrega dados e manda para outro banco ou apenas uma tabela (tudo relacional).
  * Evita fazer vários joins, pois os dados vão estar prontos para serem buscados.
* Linha do tempo: Data Warehouse -> Data Lake -> Data Lakehouse.
* O Data Lake guarda os dados, visto que o armazenamento ficou mais barato, tornando isso possível.
  * Todos os tipos de formato de dados, de várias origens.
  * É um object storage, tipo o S3.
    * Sem hierarquia de pastas, para que não precise ter recursividade ao realizar as buscas.
* O Data Lakehouse adiciona uma camada de meta dados e governança, contendo informações de onde veio, qualidade, quem atualizou, etc.
* Apache Airflow.