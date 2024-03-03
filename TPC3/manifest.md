# Dataset Mapa_Virtual

Este trabalho tem como objetivo analisar, modelar e representar um conjunto de dados relacionados a um Mapa Virtual. O dataset inclui informações Cidades e as suas ligações.

## Etapas Realizadas 

### -> Criação de uma ontologia no Protégé a partir do dataset 

Foi criado um ficheiro MapaProtege.ttl a partir do Protégé.

### -> Script de Povoamento da Ontologia

De seguida, foi elaborada um script (pyMapa.py) para popular a ontologia com os dados do dataset. Esse script assegura que todas as instâncias e relações sejam corretamente representadas na ontologia. (sendo criado o Mapa.ttl)

### -> Criação da Ontologia

Foi desenvolvida uma ontologia para representar de forma estruturada e semântica as entidades presentes no dataset:

- **Classes:** Cidade, Ligacao.
- **Object Properties:** temDestino, temOrigem.
- **Data Properties:** idCidade, idLigacao, nomeCidade, numPopulacao, temDescricao, nomeDistrito, temDistancia.

### -> Especficação das queries

Foram especificadas umas queries que estão no ficheiro queries.txt.

