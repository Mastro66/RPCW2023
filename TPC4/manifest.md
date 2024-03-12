# Dataset Tabela-Periodica

O propósito deste trabalho é desenvolver um projeto web que faça uso de dados provenientes de um repositório GraphDB, após a criação e carregamento do arquivo TTL correspondente. A aplicação visa oferecer páginas interativas relacionadas a elementos químicos e grupos, explorando as capacidades proporcionadas pelo GraphDB.

## Etapas Realizadas 

### -> Criação de um Repositório no GraphDB

Comecei por criar um repositório no GraphDB através da utilização de um ficheiro TTL contendo informações acerca da tabela periódica.

### ->  Páginas Web

Em seguida, foram desenvolvidas seis páginas web distintas:

/index: Página inicial que oferece a opção de navegar tanto para a página de grupos quanto para a dos elementos.

/elementos: Página que apresenta informações como nome, símbolo, número atômico, número de grupo e nome do grupo para cada elemento. Inclui links de redireção no nome do elemento e no grupo.

/grupos: Página que lista o nome e número de cada grupo.

/grupo/<número do grupo> | /grupo/<nome do grupo>: Página dedicada a apresentar informações sobre os elementos de um grupo específico, como nome, símbolo e número atômico de cada elemento.

/elemento/<nome do elemento>: Página que fornece informações detalhadas sobre um elemento específico, incluindo nome, símbolo, número atômico, peso atômico, cor, número do grupo, nome do grupo e período.

/empty: Nas situações em que as páginas não contêm informações específicas, a estrutura padrão da página empty.html é empregue para assegurar uma experiência consistente para o utilizador, indicando que a página encontra-se vazia neste momento.

### -> Criação da Ontologia

Comece por garantir que possui um repositório no GraphDB com o nome "tabelaPeriodica" e faça o upload do ficheiro "tabela-periodica.ttl" para esse repositório. Além disso, é fundamental ter a biblioteca ```Flask``` para Python instalada.
A partir deste momento, a página web principal estará disponível em ```localhost:7200```.

