# UrbanServe API

API RESTful desenvolvida para o gerenciamento de serviços, usuários e localizações, com persistência de dados e armazenamento de arquivos via Supabase.

## Instalação e Execução

### Pré-requisitos
* Python 3.
* Supabase (URL e Service Role Key).

### Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/fastapi-supabase-services.git](https://github.com/seu-usuario/fastapi-supabase-services.git)
    cd fastapi-supabase-services
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Variáveis de Ambiente:**
    Crie um arquivo `.env` em `/src` com as seguintes chaves:

    ```env
    SUPABASE_URL=sua_url_aqui
    SUPABASE_SERVICE_KEY=sua_chave_service_role_aqui
    ```

### Execução

Inicie o servidor de desenvolvimento:

```bash
fastapi dev ./src/main.py