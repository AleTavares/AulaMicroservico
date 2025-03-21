## Propósito

Este Repositorio foi criado para ensinar os alunos da UniFAAT a trabalharem com microserviço em Python.

## Estrutura do Projeto

├── InfraBD/  <!-- Contem a os arquivos docker para subir o Banco de Dados --><br>
│ ├── northwind.sql <!-- SQL utilizado para criar o Banco e as tabelas utilizadas no projeto --><br> 
│ ├── Dockerfile <!-- arquivo docker para inicializar o postgre --><br>
│ └── [Readme.md](InfraBD/Readme.md) <!--  Instruções para inicializar o banco no docker --><br>
├── app/ <!-- Pasta com o projeto python --><br>
│ ├── Util/ <!-- Utilitários e modulos Python --><br>
│ │ ├── bd.py <!-- Arquivo python com função para conectar no Banco de Dados --><br>
│ │ └── paramsBD.yml <!-- Arquico com as configurações para conexão com o Banco de Dados --><br>
│ ├── crudCateg.py <!-- MicroServiso de CRUD de Categorias --><br>
│ ├── test_crudCateg.py <!-- Arquivo Python com os Testes unitários --><br>
│ └── [Readme.md](app/Readme.md) <!-- Instruções para inicializar o APP --><br>
├── docker-compose.yml <!-- define a configuração para dois serviços: app e db. --><br>
├── Dockerfile <!-- define a configuração para construir uma imagem Docker para uma aplicação Flask. --><br>
└── Readme.md <!-- Arquivo com instruções gerais --><br>

## Como Rodar o Docker-Compose

Para rodar o projeto utilizando o Docker-Compose, siga os passos abaixo:

1. Certifique-se de que você tem o Docker e o Docker-Compose instalados na sua máquina.
```sh
docker --version
``` 
```sh
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

5. O serviço Flask estará disponível em `http://localhost:5000` e o banco de dados PostgreSQL estará disponível na porta `3000`.

>[!NOTE]
> Esses passos irão construir e iniciar os contêineres definidos no `docker-compose.yml`, garantindo que o ambiente esteja configurado corretamente.