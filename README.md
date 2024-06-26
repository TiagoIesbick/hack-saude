<p align="center">
  <img src="https://github.com/TiagoIesbick/hack-saude/blob/main/client/src/assets/logos/logo-vita-no-bg.png" width="120" />
</p>
<p align="center">
    <h1 align="center">Vita</h1>
</p>
<p align="center">
    <em>Você no controle da sua saúde</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/TiagoIesbick/hack-saude?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/TiagoIesbick/hack-saude?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/TiagoIesbick/hack-saude?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Desenvolvido com os softwares e ferramentas abaixo.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=flat&logo=dotenv&logoColor=black" alt=".ENV">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/GraphQL-E10098.svg?style=flat&logo=GraphQL&logoColor=white" alt="GraphQL">
	<img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat&logo=React&logoColor=black" alt="React">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

## 📖 Sumário

- [ 📍 Visão Geral](#-visão-geral)
- [ 📦 Características](#-características)
- [ 📂 Estrutura do Repositório](#-estrutura-do-repositório)
- [ 💾 Estrutura do Banco de Dados](#-estrutura-do-banco-de-dados)
- [ ⚙️ Módulos](#%EF%B8%8F-módulos)
- [ 🚀 Começando](#-começando)
    - [ 🔧 Instalação](#-instalação)
    - [ 🤖 Rodando hack-saude](#-rodando-hack-saude)
- [ 🛣 Roadmap do projeto](#-roadmap-do-projeto)
- [ 👀 Observações](#-observações)

---


## 📍 Visão Geral

Esta aplicação é um sistema de gerenciamento de dados médicos que centraliza informações de saúde dos pacientes e permite o compartilhamento seguro desses dados com médicos através de tokens temporários. A aplicação visa resolver o problema da descentralização dos dados médicos, facilitando o acesso e a gestão dos registros de saúde de forma segura e eficiente.

---


## 📦 Características

Pacientes e médicos podem se registrar e fazer login na plataforma. Dados como nome, email, tipo de usuário (paciente ou médico), e senha são armazenados de forma segura, sendo que a senha é criptografada antes de ser salva no banco de dados (totalmente desenvolvido). Pacientes podem gerar tokens temporários para compartilhar seus dados médicos com médicos específicos (totalmente desenvolvido). Médicos podem acessar os dados compartilhados usando os tokens fornecidos pelos pacientes (totalmente desenvolvido). Logs de acesso detalham quando os registros médicos foram acessados e por quais médicos (totalmente desenvolvido). Pacientes poderão visualizar e editar suas informações pessoais, como data de nascimento e gênero (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida). Médicos podem adicionar suas especialidades e número de licença (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida). Pacientes podem carregar e visualizar seus registros médicos, como resultados de exames, prescrições, etc (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida). Os tipos de registros médicos serão categorizados para fácil navegação e busca (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida). Pacientes terão visibilidade sobre quem acessou seus dados e quando (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida).

---


## 📂 Estrutura do Repositório

```sh
└── hack-saude/
    ├── README.md
    ├── client
    │   ├── .gitignore
    │   ├── README.md
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── public
    │   │   ├── favicon.ico
    │   │   ├── index.html
    │   │   ├── logo-vita-192.jpg
    │   │   ├── logo-vita-512.jpg
    │   │   ├── manifest.json
    │   │   └── robots.txt
    │   └── src
    │       ├── App.js
    │       ├── App.test.js
    │       ├── assets
    │       │   ├── images
    │       │   │   └── home.jfif
    │       │   └── logos
    │       │       ├── logo-vita-no-bg.png
    │       │       └── logo-vita.jpg
    │       ├── components
    │       │   ├── createUser.js
    │       │   ├── footer.js
    │       │   ├── generateAccessToken.js
    │       │   ├── header.css
    │       │   ├── header.js
    │       │   ├── home.js
    │       │   ├── insertToken.js
    │       │   ├── login.js
    │       │   ├── main.js
    │       │   ├── medicalRecords.js
    │       │   ├── medicalRecordsAccess.js
    │       │   ├── navbar.css
    │       │   ├── navbar.js
    │       │   └── userBar.js
    │       ├── graphql
    │       │   ├── apolloConfig.js
    │       │   ├── auth.js
    │       │   ├── mutations.js
    │       │   └── queries.js
    │       ├── hooks
    │       │   └── hooks.js
    │       ├── index.css
    │       ├── index.js
    │       ├── providers
    │       │   └── userContext.js
    │       ├── reportWebVitals.js
    │       ├── setupTests.js
    │       └── utils
    │           └── utils.js
    └── server
        ├── .env
        ├── Pipfile
        ├── Pipfile.lock
        ├── auth.py
        ├── data
        │   ├── ERM_hack_saude.png
        │   └── hack_saude.sql
        ├── db
        │   ├── connection.py
        │   ├── mutations.py
        │   ├── mysql_results.py
        │   └── queries.py
        ├── resolver.py
        ├── schema.graphql
        ├── server.py
        └── utils
            └── utils.py
```

---


## 💾 Estrutura do Banco de Dados

<p align="center">
  <img src="https://github.com/TiagoIesbick/hack-saude/blob/main/server/data/ERM_hack_saude.png" width="600" />
</p>

---


## ⚙️ Módulos

<details closed><summary>client</summary>

| File                                                                                                 | Summary                                              |
| ---                                                                                                  | ---                                                  |
| [package.json](https://github.com/TiagoIesbick/hack-saude/blob/master/client/package.json)           | Define as dependências de alto nível do projeto, scripts, e metadados. `client/package.json`      |
| [package-lock.json](https://github.com/TiagoIesbick/hack-saude/blob/master/client/package-lock.json) | Bloqueia as versões exatas de todas as dependências, garantindo instalações consistentes e reprodutíveis. `client/package-lock.json` |

</details>

<details closed><summary>client.public</summary>

| File                                                                                                | Summary                                                 |
| ---                                                                                                 | ---                                                     |
| [index.html](https://github.com/TiagoIesbick/hack-saude/blob/master/client/public/index.html)       | Ponto de entrada para a aplicação no navegador `client/public/index.html`    |
| [manifest.json](https://github.com/TiagoIesbick/hack-saude/blob/master/client/public/manifest.json) | Fornece informações sobre o aplicativo web em um formato que os navegadores e dispositivos podem entender `client/public/manifest.json` |
| [robots.txt](https://github.com/TiagoIesbick/hack-saude/blob/master/client/public/robots.txt)       | Controla o comportamento de bots de busca, especificando quais partes do site devem ser rastreadas ou ignoradas. `client/public/robots.txt`    |

</details>

<details closed><summary>client.src</summary>

| File                                                                                                       | Summary                                                   |
| ---                                                                                                        | ---                                                       |
| [reportWebVitals.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/reportWebVitals.js) | Utilizado para medir e reportar métricas de performance da aplicação `client/src/reportWebVitals.js` |
| [App.test.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/App.test.js)               | Utilizado para escrever e executar testes automatizados de unidade ou integração `client/src/App.test.js`        |
| [setupTests.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/setupTests.js)           | Utilizado para configurar o ambiente de testes antes que os testes sejam executados `client/src/setupTests.js`      |
| [App.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/App.js)                         | Componente principal que define a estrutura e a lógica inicial da aplicação `client/src/App.js`             |
| [index.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/index.js)                     | Responsável por renderizar o componente raiz da aplicação na página HTML `client/src/index.js`           |
| [index.css](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/index.css)                   | Fornece estilos globais que se aplicam a toda a aplicação. `client/src/index.css`          |

</details>

<details closed><summary>client.src.graphql</summary>

| File                                                                                                         | Summary                                                        |
| ---                                                                                                          | ---                                                            |
| [auth.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/graphql/auth.js)                 | Lógica de autenticação na parte do cliente `client/src/graphql/auth.js`         |
| [apolloConfig.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/graphql/apolloConfig.js) | Configuração do Apollo Client `client/src/graphql/apolloConfig.js` |
| [mutations.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/graphql/mutations.js)       | Mutações a serem executadas pelo servidor GraphQL `client/src/graphql/mutations.js`    |
| [queries.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/graphql/queries.js)           | Consultas a serem executadas pelo servidor GraphQL `client/src/graphql/queries.js`      |

</details>

<details closed><summary>client.src.utils</summary>

| File                                                                                         | Summary                                               |
| ---                                                                                          | ---                                                   |
| [utils.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/utils/utils.js) | Funções úteis para o funcionamento da aplicação `client/src/utils/utils.js` |

</details>

<details closed><summary>client.src.components</summary>

| File                                                                                                                            | Summary                                                                   |
| ---                                                                                                                             | ---                                                                       |
| [footer.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/footer.js)                             | Rodapé da página `client/src/components/footer.js`               |
| [medicalRecords.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/medicalRecords.js)             | Dados Médicos visualizados pelos pacientes `client/src/components/medicalRecords.js`       |
| [header.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/header.js)                             | Topo da página `client/src/components/header.js`               |
| [userBar.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/userBar.js)                           | Navegação pelas informações do usuário `client/src/components/userBar.js`              |
| [insertToken.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/insertToken.js)                   | Página para o médico inserir o token fornecido pelo paciente `client/src/components/insertToken.js`          |
| [home.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/home.js)                                 | Página de entrada da aplicação `client/src/components/home.js`                 |
| [medicalRecordsAccess.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/medicalRecordsAccess.js) | Página para o médico visualizar os dados liberados pelo token fornecido pelo paciente `client/src/components/medicalRecordsAccess.js` |
| [main.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/main.js)                                 | Meio da página `client/src/components/main.js`                 |
| [createUser.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/createUser.js)                     | Formulário para criação de usuários, sejam médicos ou pacientes `client/src/components/createUser.js`           |
| [login.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/login.js)                               | Página para efetuar o login `client/src/components/login.js`                |
| [header.css](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/header.css)                           | Estilização do topo da página `client/src/components/header.css`              |
| [generateAccessToken.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/generateAccessToken.js)   | Página para o paciente emitir o token a sr fornecido ao médico `client/src/components/generateAccessToken.js`  |
| [navbar.css](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/navbar.css)                           | Estilização da barra de navegação `client/src/components/navbar.css`              |
| [navbar.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/navbar.js)                             | Barra de navegação `client/src/components/navbar.js`               |

</details>

<details closed><summary>client.src.providers</summary>

| File                                                                                                         | Summary                                                         |
| ---                                                                                                          | ---                                                             |
| [userContext.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/providers/userContext.js) | Dados de contexto a serem consumidos pela aplicação `client/src/providers/userContext.js` |

</details>

<details closed><summary>client.src.hooks</summary>

| File                                                                                         | Summary                                               |
| ---                                                                                          | ---                                                   |
| [hooks.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/hooks/hooks.js) | Funções a serem consumidas pela aplicação `client/src/hooks/hooks.js` |

</details>

<details closed><summary>server</summary>

| File                                                                                           | Summary                                           |
| ---                                                                                            | ---                                               |
| [resolver.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/resolver.py)       | Lógica de resolução das mutações e consultas feitas ao servidor GraphQL `server/resolver.py`    |
| [schema.graphql](https://github.com/TiagoIesbick/hack-saude/blob/master/server/schema.graphql) | Tipagem e esquema do servidor GraphQL `server/schema.graphql` |
| [Pipfile.lock](https://github.com/TiagoIesbick/hack-saude/blob/master/server/Pipfile.lock)     | Garante a reprodutibilidade, a segurança e a eficiência nas instalações de dependências no sevidor desenvolvido com Python `server/Pipfile.lock`   |
| [server.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/server.py)           |  Responsável por iniciar e configurar o servidor `server/server.py`      |
| [auth.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/auth.py)               | Lógica de autenticação pela parte do servidor `server/auth.py`        |
| [.env](https://github.com/TiagoIesbick/hack-saude/blob/master/server/.env)                     | Variáveis de ambiente `server/.env`           |
| [Pipfile](https://github.com/TiagoIesbick/hack-saude/blob/master/server/Pipfile)               | Especifica as dependências necessárias para o projeto `server/Pipfile`        |

</details>

<details closed><summary>server.utils</summary>

| File                                                                                     | Summary                                           |
| ---                                                                                      | ---                                               |
| [utils.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/utils/utils.py) | Funcções úteis para a lógica do servidor `server/utils/utils.py` |

</details>

<details closed><summary>server.db</summary>

| File                                                                                                  | Summary                                                |
| ---                                                                                                   | ---                                                    |
| [connection.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/db/connection.py)       | Conexão com o banco de dados MySQL `server/db/connection.py`    |
| [mysql_results.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/db/mysql_results.py) | Execução de consultas e mutações no banco de dados `server/db/mysql_results.py` |
| [mutations.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/db/mutations.py)         | Lógica das mutações a serem executadas `server/db/mutations.py`     |
| [queries.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/db/queries.py)             | Lógica das consultas a serem executadas `server/db/queries.py`       |

</details>

<details closed><summary>server.data</summary>

| File                                                                                                  | Summary                                                |
| ---                                                                                                   | ---                                                    |
| [ERM_hack_saude.png](https://github.com/TiagoIesbick/hack-saude/blob/master/server/data/ERM_hack_saude.png)       | O ERM é um modelo conceitual usado para descrever os dados que serão armazenados em um banco de dados relacional e as relações entre esses dados. `server/data/ERM_hack_saude.png`    |
| [hack_saude.sql](https://github.com/TiagoIesbick/hack-saude/blob/master/server/data/hack_saude.sql) | Script SQL para montar o banco de dados, incluindo dados para testes `server/data/hack_saude.sql` |


</details>

---


## 🚀 Começando

***Requisitos***

Certifique-se de ter as seguintes dependências instaladas em seu sistema:

* **Python**: `version 3.12+`
* **MySQL**: `version 8.0+`
* **Pipenv**: `version 2023.12.1+`
* **Node**: `version v20.14.0+`

### 🔧 Instalação

1. Clone o repositório hack-saude:

```sh
git clone https://github.com/TiagoIesbick/hack-saude
```

2. Mude para o diretório do projeto:

```sh
cd hack-saude
```

3. Mude para o diretório server:

```sh
cd server
```

4. Rode os seguintes comandos no diretório server:

```sh
pipenv shell
pipenv install
```

5. Abra o prompt MySQL no diretório server da seguinte forma, troque `hack_saude` por `root` ou pelo seu nome de usuário no MySQL:

```sh
mysql -u hack_saude -p
```

6. Insira a senha solicitada, conforme o usuário que passou no comando anterior.

7. Rode o seguinte comando para montar o banco de dados:

```sh
source data/hack_saude.sql
```

8. Saia do prompt do MySQL com o seguinte comando:

```sh
exit
```

8. De acordo com o usuário e a senha utilizados no prompt do MySQL, atualize as variáveis de ambiente USER e PASSWORD do arquivo .env:

```sh
USER=SEU_USUÁRIO
PASSWORD=SUA_SENHA
```

9. Rode o servidor no diretório server com o seguinte comando:

```sh
uvicorn server:app
```

10. O debug do servidor Graphql ficará disponível no seguinte endereço `http://127.0.0.1:8000/graphql/`

11. Abra um novo terminal e navegue para o diretório client:

```sh
cd client
```

12. Rode os seguintes comandos no diretório client:

```sh
npm install
npm start
```

### 🤖 Rodando hack-saude

Após tais comandos o servidor estará rodando em `http://127.0.0.1:8000/graphql/` e o cliente estará rodando em `http://localhost:3000/`

---


## 🛣 Roadmap do projeto

- [X] `► Fazer Login com usuário paciente: john.doe@example.com, senha Password123 `
- [X] `► Navegar para aba Dados Médicos, a qual possui um dado de exemplo`
- [X] `► Navegar para a aba Gerar Token de Acesso`
- [X] `► Escolher data e hora que o token irá expirar, sendo que tempo passado não será aceito e será exibida mensagem de erro. Para sair do calendário é preciso dar dois cliques fora dele`
- [X] `► Confirmar o horário e aguardar a exibição do token, o qual deverá ser copiado`
- [X] `► Fazer logout no menu suspenso com a inicial do usuário logado`
- [X] `► Fazer login com usário profissional da saúde:  jane.smith@example.com, senha Password123`
- [X] `► Navegar para a aba Inserir Token e colar o token gerado anteriormente, caso ele não tenha expirado, ficarão visíveis os dados médicos do paciente que gerou o token`

---


## 👀 Observações

- É possível criar novos usuários, tanto do tipo paciente, quanto do tipo profissional de saúde, algo que pode ser feito na aba login na sessão Crie uma Conta, contudo novos usuários não irão possuir dados médicos a serem exibidos;
- A aplicação roda de uma maneira em que salva tokens de login, bem como de acesso a dados de saúde do paciente em Local Storage do navegador, sendo que o token de login não expira, apenas o de acesso a dados de saúde do paciente;
- O médico só poderá ver os dados do paciente que gerou o token e o repassou a ele, não tendo acesso aos dados dos demais usuários;
- Cada visualização do médico aos dados do paciente no período em que o token está ativo é salvo na tabela TokenAccess do banco de dados.
- As senhas dos usuários são salvas de maneira criptografada no banco de dados;
- No menu suspenso abaixo da inicial do nome do usuário há duas funcionalidades que ainda serão implementadas, a saber: editar o perfil do usuário e consultar os tokens que estão ativos.
- Sobre os inputs de dados médicos, imagina-se que será possível tanto o paciente inserir dados, quanto o médico inserir dados enquanto o token repassado estiver ativo. Além disso, imagina-se criar API's que se conectem com hospitais e laboratórios, a fim de automatizar a entrada de dados, sendo que o sucesso da aplicação poderá acarretar na substituição dos sistemas em uso nos diversos estabelicimentos de saúde, concentrando os dados na mão de seu real proprietário: o paciente.

[**Voltar**](#Top)

---
