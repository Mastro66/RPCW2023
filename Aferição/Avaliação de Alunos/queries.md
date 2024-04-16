## Queries SPARQL

```sql

# 1 Quantos alunos estão registados? (inteiro)

PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select (count(distinct ?s) as ?count) where { 
    ?s rdf:type :Aluno .
} 
```
```sql

# 2 Quantos alunos frequentam o curso "LCC"? (inteiro)

PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select (count(distinct ?aluno) as ?count) where { 
    ?aluno rdf:type :Aluno ;
            :curso "LCC" .
}

```

```sql
# 3 Que alunos tiveram nota positiva no exame de época normal? (lista ordenada alfabeticamente por nome com: idAluno, nome, curso, nota do exame)

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.org/exam#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>

SELECT ?idAluno ?nome ?curso ?notaNormal
WHERE {
    ?idAluno rdf:type :Aluno ;
            :temExame ?exame ;
    		:nome ?nome ;
            :curso ?curso .
    ?exame :exameNormal ?notaNormal .
    
    FILTER (?notaNormal >= 10) .
}
ORDER BY ?nome

```

```sql

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
# 4 Qual a distribuição dos alunos pelas notas do projeto? (lista com: nota e número de alunos que obtiveram essa nota)

select ?notaProjeto (count (?aluno) as ?nAlunos ) where {
    ?aluno rdf:type :Aluno ;
    		:projeto ?notaProjeto .
} GROUP BY (?notaProjeto)

```

```sql
# 5 Quais os alunos mais trabalhadores durante o semestre? (lista ordenada por ordem decrescente do total: idAluno, nome, curso, total = somatório dos resultados dos TPC)

PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT distinct ?nome ?idAluno ?curso (SUM(?nota) AS ?total) WHERE {
  ?idAluno rdf:type :Aluno ;
           :nome ?nome ;
           :curso ?curso ;
           :temTPC ?tpc .
  ?tpc :nota ?nota .
} 
GROUP BY ?idAluno ?nome ?curso
ORDER BY DESC(?total)

```

```sql

# 6 Qual a distribuição dos alunos pelos vários cursos? (lista de cursos, ordenada alfabeticamente por curso, com: curso, número de alunos nesse curso)

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
select ?curso (count (?aluno) as ?nAlunos ) where {
    ?aluno rdf:type :Aluno ;
    		:curso ?curso .
} GROUP BY (?curso)
ORDER BY (?curso)

```

