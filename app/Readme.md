# CRUD Microservice for Categories

Este microserviço fornece uma API CRUD para a tabela `categories` do banco de dados PostgreSQL. Ele permite criar, ler, atualizar e deletar categorias.
Este repositório deve ser clonado pelos Alunos da UniFaat para trabalharem os outros aspectos da Aplicação.

## Configuração

1. **Banco de Dados**: Certifique-se de que o banco de dados PostgreSQL está configurado e rodando. 
<br>O script SQL `northwind.sql` na pasta InfraBD contém a definição da tabela `categories`.<br>
Para inicializar a infra e o Banco Postgre sega o Readme.md de Infra [clicando aqui](../InfraBD/Readme.md)

2. **Parâmetros de Conexão**: Configure os parâmetros de conexão ao banco de dados no arquivo `paramsBD.yml` localizado em `app/Util/`.

```yaml
# Util/paramsBD.yml
db_name: "your_db_name"
db_user: "your_db_user"
db_password: "your_db_password"
db_host: "your_db_host"
db_port: "your_db_port"
```
<br>

## Execução
**Instalar Dependências:** 
Certifique-se de que você tem o Flask e psycopg2 instalados. Você pode instalar as dependências usando pip:
```sh
pip install -r requirements.txt
```

**Rodar o Microserviço:** 
Navegue até o diretório raiz do projeto e execute o seguinte comando para iniciar o servidor Flask:
```sh
export FLASK_APP=Sistema.crudCateg
flask run --host=0.0.0.0 --port=5000
```
Endpoints
Criar Categoria
- URL: /categories
- Método: POST
- Corpo da Requisição:
```json
{
    "category_id": [Código da Categoria],
    "category_name": "[Nome da Categoria]",
    "description": "[Descrição da categoria]",
    "picture": [imagem]
}
```
### Ler Categoria

- **URL**: `/categories/<int:category_id>`
- **Método**: `GET`
- **Exemplo de `curl`**:
  ```sh
  curl -X GET http://localhost:5000/categories/1
  ```

### Atualizar Categoria

- **URL**: `/categories/<int:category_id>`
- **Método**: `PUT`
- **Corpo da Requisição**:
  ```json
  {
      "category_name": "Beverages",
      "description": "Soft drinks, coffees, teas, beers, and ales",
      "picture": null
  }
  ```
- **Exemplo de `curl`**:
  ```sh
  curl -X PUT http://localhost:5000/categories/1 \
  -H "Content-Type: application/json" \
  -d '{
      "category_name": "Beverages",
      "description": "Soft drinks, coffees, teas, beers, and ales",
      "picture": null
  }'
  ```

### Deletar Categoria

- **URL**: `/categories/<int:category_id>`
- **Método**: `DELETE`
- **Exemplo de `curl`**:
  ```sh
  curl -X DELETE http://localhost:5000/categories/1
  ```
## Testes Unitários
O arquivo test_crudCateg.py cobre os seguintes casos de teste para o crudCateg.py:
1. test_create_category_success: Testa a criação bem-sucedida de uma categoria.
2. test_create_category_db_failure: Testa a falha na criação de uma categoria devido a problemas de conexão com o banco de dados.
3. test_read_category_success: Testa a leitura bem-sucedida de uma categoria.
4. test_read_category_not_found: Testa a leitura de uma categoria que não existe.

Para executar os testes, você pode usar o seguinte comando:

```sh
pytest test_crudCateg.py
```