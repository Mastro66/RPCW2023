# Conversor XML para TTL

Este trabalho de casa envolve a utilização de uma ontologia simples sobre famílias, que inclui informações básicas como o nome de uma pessoa e propriedades de objeto como `temPai` e `temMae`. O desafio proposto é enriquecer essa ontologia com dados de um ficheiro XML que detalha a genealogia de figuras bíblicas.

Para este efeito, entre as duas opções disponíveis — `biblia.xml` e `royal.xml` —, optou-se pelo ficheiro `biblia.xml`. Este contém informações sobre a genealogia de várias personagens bíblicas.

A leitura do ficheiro XML é realizada utilizando a  biblioteca ```xml.etree.ElementTree```, e a adição de informações à ontologia é efetuada através da concatenação direta de strings ao ficheiro `familia.ttl`.

O script desenvolvido foi testado com sucesso e a ontologia resultante foi verificada utilizando o software Protegé.

