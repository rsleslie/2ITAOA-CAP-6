# ♻️ Sistema de Logística Reversa no Agronegócio

🚜 Um sistema simples e funcional que auxilia produtores rurais a registrar, organizar e acompanhar o descarte correto de resíduos no campo, promovendo sustentabilidade e boas práticas no agronegócio.

---

## 🌱 Objetivo

Facilitar o processo de logística reversa no agronegócio, permitindo que produtores:

- Cadastrem resíduos e materiais descartáveis
- Informem locais/empresas de coleta e reaproveitamento
- Acompanhem prazos e histórico de descarte
- Gerem relatórios úteis com base nos dados
- Usem o sistema via terminal, com menus simples e diretos

---

## 🧠 Funcionalidades

### 1. Cadastro de Resíduos
- Tipo (embalagem, restos de safra, máquina quebrada, etc)
- Quantidade
- Data do descarte
- Destinação correta (reciclagem, compostagem, incineração...)

### 2. Cadastro de Pontos de Coleta ou Empresas Parceiras
- Nome da empresa
- Tipo de resíduo aceito
- Localização

### 3. Associação Automática
- Sugestão de empresas compatíveis com o tipo de resíduo informado

### 4. Relatórios
- Total de resíduos por tipo
- Histórico completo de descartes
- Empresas mais utilizadas

### 5. Armazenamento
- `.json` com todos os dados salvos
- `.txt` com relatórios e resumos
- Banco de dados SQLite com estrutura completa para consultas

---

## 💡 Tecnologias e Requisitos Atendidos

| Requisito              | Aplicação no Projeto                                     |
|------------------------|----------------------------------------------------------|
| Subalgoritmos          | Funções de cadastro, consulta, relatórios e associação  |
| Estruturas de dados    | Listas, dicionários e tuplas                            |
| Arquivos (JSON, TXT)   | Dados salvos em JSON e relatórios em TXT                |
| Banco de dados (Oracle)| Registro completo e estruturado                         |

---

## 📁 Estrutura do Projeto

```bash
├── main.py                 # Ponto de entrada do sistema (menu principal)
├── core/
│   ├── residuos.py         # Funções para cadastro e consulta de resíduos
│   ├── empresas.py         # Funções para cadastro de empresas/parceiras
│   ├── associacao.py       # Lógica de associação entre resíduos e empresas
│   ├── relatorios.py       # Funções para gerar e salvar relatórios
│   └── armazenamento.py    # Lógica para salvar/carregar JSON e .txt
├── database/
│   └── db.py               # conexão com o banco Oracle
├── data/
│   ├── dados.json          # Arquivo JSON com dados salvos
│   ├── relatorio.txt       # Relatório em texto gerado
│   └── banco.db            # Banco de dados SQLite
├── utils/
│   ├── cores.py             # cores para impressão no terminal
│   └── validacoes.py       # Funções auxiliares (ex: validar datas, tipos)
├── .env                     # variáveis de ambiente (NÃO versionar)
├── .gitignore          
├── requirements.txt
└── README.md
```
---

## ⚙️ Como rodar o projeto localmente

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
Crie um arquivo .env na raiz com as credenciais do banco Oracle:
```bash
DB_USER=RMxxxxxx
DB_PASSWORD=suasenha
DB_DSN=XXXX
```
Execute o sistema:
```bash
python main.py
```