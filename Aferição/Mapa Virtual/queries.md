### Lista todas as Cidades por ordem Alfabetica
```
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa_virtual/>
select ?nome where { 
    ?s :nomeCidade ?nome
} order by asc (?nome)
```

### Distribuição das cidades por distrito: lista de distritos ordenada alfabeticamente em que para cada um se indica quantas cidades tem;
```
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa_virtual/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?nomeDistrito (COUNT(?cidade) AS ?numCidades)
WHERE { 
    ?cidade rdf:type :Cidade .
    ?cidade :nomeDistrito ?nomeDistrito .
}
GROUP BY ?nomeDistrito
ORDER BY ASC(?nomeDistrito)
```

### Que cidades têm ligações diretas com Braga? (Considera Braga como origem mas também como destino)
```
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa_virtual/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?nomeCidadeLigada
WHERE {
  {
    ?braga :nomeCidade "Braga" .
    ?ligacao :temOrigem ?braga .
    ?ligacao :temDestino ?cidadeLigada .
    ?cidadeLigada :nomeCidade ?nomeCidadeLigada .
  }
  UNION
  {
    ?braga :nomeCidade "Braga" .
    ?ligacao :temDestino ?braga .
    ?ligacao :temOrigem ?cidadeLigada .
    ?cidadeLigada :nomeCidade ?nomeCidadeLigada .
  }
}
```
### Partindo de Braga, que cidades se conseguem visitar? (Apresenta uma lista de cidades ordenada alfabeticamente)
```
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa_virtual/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>«

SELECT DISTINCT ?nomeCidadeLigada
WHERE {
  ?braga :nomeCidade "Braga" .
  {
    ?ligacao :temOrigem ?braga .
    ?ligacao :temDestino ?cidadeLigada .
    ?cidadeLigada :nomeCidade ?nomeCidadeLigada .
  }
}
ORDER BY ASC(?nomeCidadeLigada)

### Através duma query CONSTRUCT cria uma ligação direta entre Braga e todas as cidades que se conseguem visitar a partir dela.

PREFIX : <http://rpcw.di.uminho.pt/2024/mapa_virtual/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

CONSTRUCT {
  ?braga :temLigacaoDireta ?cidadeLigada .
} 
WHERE {
  ?braga :nomeCidade "Braga" .
  {
    ?ligacao :temOrigem ?braga .
    ?ligacao :temDestino ?cidadeLigada .
    ?cidadeLigada :nomeCidade ?nomeCidadeLigada .
  }
}
```
### Através duma query CONSTRUCT cria uma ligação direta entre cada uma das cidades e todas as cidades que se conseguem visitar a partir dela.
```
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa_virtual/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

CONSTRUCT {
  ?cidadeOrigem :temLigacaoDireta ?cidadeDestino .
} 
WHERE {
  ?cidadeOrigem rdf:type :Cidade .
  ?cidadeDestino rdf:type :Cidade .
  ?cidadeOrigem :nomeCidade ?nomeCidadeOrigem .
  ?cidadeDestino :nomeCidade ?nomeCidadeDestino .
  
  {
    ?ligacao :temOrigem ?cidadeOrigem .
    ?ligacao :temDestino ?cidadeDestino .
  }
  UNION
  {
    ?ligacao :temDestino ?cidadeOrigem .
    ?ligacao :temOrigem ?cidadeDestino .
  }
  
  FILTER (?cidadeOrigem != ?cidadeDestino)
}
```
