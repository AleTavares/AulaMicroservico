## Propósito

Este repositório foi criado para ensinar os alunos da UniFAAT a trabalharem com microserviços em Python, além de implementar um sistema de observabilidade focado no monitoramento do banco de dados utilizando ferramentas modernas como Prometheus, Grafana e PostgreSQL Exporter.

## Estrutura do Projeto

├── InfraBD/  <!-- Contém os arquivos Docker para subir o Banco de Dados --><br>
│ ├── northwind.sql <!-- SQL utilizado para criar o Banco e as tabelas utilizadas no projeto --><br> 
│ ├── Dockerfile <!-- Arquivo Docker para inicializar o PostgreSQL --><br>
│ └── [Readme.md](InfraBD/Readme.md) <!-- Instruções para inicializar o banco no Docker --><br>
├── app/ <!-- Pasta com o projeto Python --><br>
│ ├── Util/ <!-- Utilitários e módulos Python --><br>
│ │ ├── bd.py <!-- Arquivo Python com função para conectar no Banco de Dados --><br>
│ │ └── paramsBD.yml <!-- Arquivo com as configurações para conexão com o Banco de Dados --><br>
│ ├── crudCateg.py <!-- Microserviço de CRUD de Categorias --><br>
│ ├── test_crudCateg.py <!-- Arquivo Python com os testes unitários --><br>
│ └── [Readme.md](app/Readme.md) <!-- Instruções para inicializar o APP --><br>
├── prometheus/ <!-- Configuração do Prometheus --><br>
│ ├── prometheus.yml <!-- Arquivo de configuração do Prometheus --><br>
│ └── Dockerfile <!-- Dockerfile para o Prometheus --><br>
├── grafana/ <!-- Configuração do Grafana --><br>
│ └── Dockerfile <!-- Dockerfile para o Grafana --><br>
├── docker-compose.yml <!-- Define a configuração para os serviços: db, Prometheus, Grafana e PostgreSQL Exporter --><br>
└── Readme.md <!-- Arquivo com instruções gerais --><br>

## Como Rodar o Docker-Compose

Para rodar o projeto utilizando o Docker-Compose, siga os passos abaixo:

1. Certifique-se de que você tem o Docker e o Docker-Compose instalados na sua máquina:
    ```sh
    docker --version
    docker-compose --version
    ```

2. No diretório raiz do projeto, execute o seguinte comando para parar e remover quaisquer contêineres existentes:
    ```sh
    docker-compose down
    ```

3. Remova o volume de dados do PostgreSQL (se necessário):
    ```sh
    docker volume rm AulaMicroservico_postgres_data
    ```

4. Execute o comando para iniciar os contêineres com o Docker-Compose:
    ```sh
    docker-compose up --build
    ```

5. Acesse os serviços:
    - **Prometheus**: [http://localhost:9090](http://localhost:9090)
    - **Grafana**: [http://localhost:3000](http://localhost:3000)

## Configurando o Grafana para Monitorar o Banco de Dados

1. Acesse o Grafana em [http://localhost:3000](http://localhost:3000).
2. Faça login com as credenciais padrão:
   - **Usuário**: `admin`
   - **Senha**: `admin`
3. Adicione uma nova fonte de dados:
   - Vá para **Configuration > Data Sources**.
   - Clique em **Add data source**.
   - Escolha **Prometheus**.
   - Configure o URL como `http://prometheus:9090` e clique em **Save & Test**.
4. Importe um dashboard para o PostgreSQL Exporter:
   - Vá para **Dashboards > Import**.
   - Use o ID de um dashboard público, como **9628** (PostgreSQL Exporter Overview).
   - Configure a fonte de dados como `Prometheus`.

## Observabilidade no Projeto

O projeto implementa um sistema de observabilidade focado no banco de dados com os seguintes componentes:
- **Prometheus**: Coleta métricas do PostgreSQL Exporter.
- **Grafana**: Exibe dashboards com métricas do banco de dados.
- **PostgreSQL Exporter**: Exporta métricas do banco de dados PostgreSQL.

## Volumes Persistentes

- **PostgreSQL**: `postgres_data`
- **Grafana**: `grafana_data`

## Rede

Todos os serviços estão conectados à rede `monitoring_network` para facilitar a comunicação.

## Observações

- Certifique-se de que as portas necessárias (9090, 3000, 9187) estejam disponíveis no host.
- Personalize as configurações no arquivo `docker-compose.yml` conforme necessário.