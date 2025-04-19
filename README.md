# ♻️ Sistema de Logística Reversa no Agronegócio

🚜 Um sistema robusto e integrado que auxilia produtores rurais a gerenciar o descarte correto de resíduos no campo, conectando-os a empresas de reciclagem parceiras através de um banco de dados Oracle. O sistema promove sustentabilidade e boas práticas no agronegócio, oferecendo funcionalidades via terminal com menus intuitivos.

---

## 🌱 Objetivo

Otimizar o processo de logística reversa no agronegócio, fornecendo aos produtores as ferramentas para:

- **Cadastrar Clientes:** Registrar informações de produtores rurais que necessitam descartar resíduos.
- **Selecionar Tipos de Resíduos:** Indicar os tipos de resíduos a serem descartados (Papelão ou Plástico).
- **Associar a Empresas de Reciclagem:** Encontrar e conectar-se a empresas de reciclagem parceiras, filtradas por tipo de resíduo e localização (atualmente São Paulo).
- **Gerar Relatórios:** Obter informações consolidadas sobre clientes cadastrados e empresas de reciclagem.
- **Armazenar Dados:** Utilizar um banco de dados Oracle para o armazenamento estruturado e eficiente de informações.
- **Operar via Terminal:** Interagir com o sistema através de um menu de linha de comando simples e direto.

---

## 🧠 Funcionalidades

### 1. Cadastro de Cliente
- Registro de informações básicas do produtor rural (nome da empresa, ramo de atuação).
- Seleção do tipo de resíduo a ser descartado (Papelão ou Plástico, com opção futura para outros).
- Registro da localização do cliente (atualmente com suporte para São Paulo).

### 2. Empresas Parceiras (Ja cadsatradass no Banco de Dados Oracle)
- As informações de empresas de reciclagem (nome, tipos de resíduos aceitos, localização, contato) são armazenadas e gerenciadas diretamente no banco de dados Oracle.

### 3. Associação de Resíduos a Empresas Parceiras
- Busca automática de empresas de reciclagem compatíveis com o tipo de resíduo do cliente e localizadas em São Paulo.
- Exibição das empresas encontradas com informações de contato.

### 4. Relatórios
- **Total de Clientes Cadastrados:** Exibe o número total de produtores rurais registrados no sistema.
- **Relatório de Empresas Parceiras:**
    - Exibe o total de empresas de reciclagem cadastradas em São Paulo.
    - Lista as empresas por tipo de resíduo que reciclam (Papelão, Plástico, ou ambos), incluindo nome, localização e contato.
    - Salva essas informações em um arquivo `relatorios.txt`.

### 5. Armazenamento
- **Banco de dados Oracle:** Utilizado para o armazenamento estruturado e persistente de dados de empresas de reciclagem parceiras e seus tipos de resíduos.
- **Arquivo JSON (`dados.json`):** Usado para armazenar informações dos clientes cadastrados.
- **Arquivo TXT (`relatorios.txt`):** Contém os relatórios gerados sobre as empresas de reciclagem.

---

## 💡 Tecnologias e Requisitos Atendidos

| Requisito              | Aplicação no Projeto                                                                 |
|------------------------|--------------------------------------------------------------------------------------|
| Subalgoritmos          | Funções modulares para cadastro de clientes, seleção de resíduos, associação de empresas, geração de relatórios e interação com o Oracle. |
| Estruturas de dados    | Listas, dicionários e tuplas para manipulação de dados.                               |
| Arquivos (JSON, TXT)   | JSON para dados de clientes e TXT para relatórios de empresas.                      |
| Banco de dados (Oracle)| Armazenamento centralizado e estruturado de dados de empresas parceiras. |

---

## 📁 Estrutura do Projeto

```bash
├── main.py                 # Ponto de entrada do sistema (menu principal)
├── core/
│   ├── clientes.py         # Funções para cadastro de clientes e seleção de resíduos
│   ├── associacao.py       # Lógica de associação entre clientes e empresas de reciclagem
│   ├── relatorios.py       # Funções para gerar relatórios de clientes e empresas
│   └── armazenamento.py    # Lógica para salvar/carregar dados de clientes em JSON
├── consumer/
│   └── consumer_oracle_sql.py # Funções para interagir com o banco de dados Oracle (consultas)
├── database/
│   └── db.py               # Conexão com o banco Oracle
├── data/
│   ├── dados.json          # Arquivo JSON com dados dos clientes salvos
│   └── relatorios.txt      # Relatório em texto gerado sobre as empresas
├── utils/
│   └── cores.py             # Cores para impressão no terminal
│
├── .env                     # Variáveis de ambiente (NÃO versionar)
├── .gitignore
├── requirements.txt
└── README.md
```

**⚙️ Como rodar o projeto localmente**

Clone o repositório:
```bash
git clone https://github.com/rsleslie/2ITAOA-CAP-6.git
cd 2ITAOA-CAP-6
```
Crie e ative o ambiente virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
Instale as dependências:
```bash
pip install -r requirements.txt
```
# ⚙️ Preparando o Banco de Dados Oracle para Teste

Para testar o sistema de logística reversa com a integração do Oracle, você precisará criar as tabelas necessárias e inserir alguns dados de exemplo no seu banco de dados. Siga os passos abaixo utilizando uma ferramenta de cliente SQL para Oracle (como SQL Developer, DBeaver, etc.).

**1. Conecte-se ao seu banco de dados Oracle.**

   Utilize as credenciais configuradas no arquivo `.env` (ORACLE_USERNAME, ORACLE_PASSWORD, ORACLE_DSN) para estabelecer uma conexão com a sua instância do Oracle.
   ```bash
ORACLE_USERNAME=RMxxxxxx
ORACLE_PASSWORD=suasenha
ORACLE_DSN=XXXX
```

**2. Crie a tabela `tipos_residuo` (se ainda não existir).**

   Execute o seguinte comando SQL para criar a tabela que armazena os tipos de resíduos:

   ```sql
   CREATE TABLE tipos_residuo (
       id_residuo NUMBER PRIMARY KEY,
       nome_residuo VARCHAR2(100)
   );

```
**3. Popule a tabela tipos_residuo com os tipos de resíduos suportados.**

   Execute os seguintes comandos SQL para inserir os dados iniciais dos tipos de resíduos:

   ```sql
INSERT INTO tipos_residuo (id_residuo, nome_residuo) VALUES (0, 'Papelão');
INSERT INTO tipos_residuo (id_residuo, nome_residuo) VALUES (1, 'Plástico');
INSERT INTO tipos_residuo (id_residuo, nome_residuo) VALUES (2, 'Papelão/Plástico');
COMMIT;

```

**4. Crie a tabela empresas_parceiras.**

   Execute o seguinte comando SQL para criar a tabela que armazena as informações das empresas de reciclagem parceiras:

   ```sql
   CREATE TABLE empresas_parceiras (
    id_empresa NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(200),
    id_residuo NUMBER,
    localizacao VARCHAR2(100),
    contato VARCHAR2(100),
    CONSTRAINT fk_residuo FOREIGN KEY (id_residuo) REFERENCES tipos_residuo(id_residuo)
);


```
**5. Popule a tabela empresas_parceiras com algumas empresas de exemplo.**

   Execute os seguintes comandos SQL para inserir dados de exemplo de empresas de reciclagem:

   ```sql
INSERT INTO empresas_parceiras (nome, id_residuo, localizacao, contato)
VALUES ('Aparas 2 Irmãos', 2, 'São Paulo - SP', '(11) 4091-3340');

INSERT INTO empresas_parceiras (nome, id_residuo, localizacao, contato)
VALUES ('Plaxo Reciclagem', 1, 'São Paulo - SP', '(11) 96363-2400');

INSERT INTO empresas_parceiras (nome, id_residuo, localizacao, contato)
VALUES ('Aparas Macedo', 2, 'Barueri - SP', '(11) 4247-2732');

INSERT INTO empresas_parceiras (nome, id_residuo, localizacao, contato)
VALUES ('Recrie Ambiental', 2, 'São Paulo - SP', '(11) 2091-8886');

INSERT INTO empresas_parceiras (nome, id_residuo, localizacao, contato)
VALUES ('Aparas Mantovani', 2, 'São Paulo - SP', '(11) 2012-0000');

COMMIT;

```

**6. Verifique a criação e o preenchimento das tabelas.**

   Você pode executar os seguintes comandos SQL para verificar se as tabelas foram criadas corretamente e se os dados foram inseridos:

   ```sql
SELECT * FROM tipos_residuo;
SELECT * FROM empresas_parceiras;

```

**Execute o sistema:**

   ```bash
python main.py
```

