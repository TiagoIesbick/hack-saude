<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">Vita</h1>
</p>
<p align="center">
    <em>Você no controle da sua saúde</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/TiagoIesbick/hack-saude?style=flat&color=0080ff" alt="license">
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

##  Quick Links

> - [ Visão Geral](#-overview)
> - [ Características](#-features)
> - [ Estrutura do Repositório](#-repository-structure)
> - [ Módulos](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running hack-saude](#-running-hack-saude)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Visão Geral

Esta aplicação é um sistema de gerenciamento de dados médicos que centraliza informações de saúde dos pacientes e permite o compartilhamento seguro desses dados com médicos através de tokens temporários. A aplicação visa resolver o problema da descentralização dos dados médicos, facilitando o acesso e a gestão dos registros de saúde de forma segura e eficiente. `overview`

---

##  Características

Pacientes e médicos podem se registrar e fazer login na plataforma. Dados como nome, email, tipo de usuário (paciente ou médico), e senha são armazenados de forma segura, sendo que a senha é criptografada antes de ser salva no banco de dados (totalmente desenvolvido). Pacientes podem gerar tokens temporários para compartilhar seus dados médicos com médicos específicos (totalmente desenvolvido). Médicos podem acessar os dados compartilhados usando os tokens fornecidos pelos pacientes (totalmente desenvolvido). Logs de acesso detalham quando os registros médicos foram acessados e por quais médicos (totalmente desenvolvido). Pacientes poderão visualizar e editar suas informações pessoais, como data de nascimento e gênero (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida). Médicos podem adicionar suas especialidades e número de licença (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida). Pacientes podem carregar e visualizar seus registros médicos, como resultados de exames, prescrições, etc (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida). Os tipos de registros médicos serão categorizados para fácil navegação e busca (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida). Pacientes terão visibilidade sobre quem acessou seus dados e quando (parte do banco de dados já foi desenvolvida, parte do back-end e do front-end a ser denvolvida).   `features`

---

##  Repository Structure

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

##  Modules

<details closed><summary>client</summary>

| File                                                                                                 | Summary                                              |
| ---                                                                                                  | ---                                                  |
| [package.json](https://github.com/TiagoIesbick/hack-saude/blob/master/client/package.json)           | HTTP error 404 for prompt `client/package.json`      |
| [package-lock.json](https://github.com/TiagoIesbick/hack-saude/blob/master/client/package-lock.json) | HTTP error 404 for prompt `client/package-lock.json` |

</details>

<details closed><summary>client.public</summary>

| File                                                                                                | Summary                                                 |
| ---                                                                                                 | ---                                                     |
| [index.html](https://github.com/TiagoIesbick/hack-saude/blob/master/client/public/index.html)       | HTTP error 404 for prompt `client/public/index.html`    |
| [manifest.json](https://github.com/TiagoIesbick/hack-saude/blob/master/client/public/manifest.json) | HTTP error 404 for prompt `client/public/manifest.json` |
| [robots.txt](https://github.com/TiagoIesbick/hack-saude/blob/master/client/public/robots.txt)       | HTTP error 404 for prompt `client/public/robots.txt`    |

</details>

<details closed><summary>client.src</summary>

| File                                                                                                       | Summary                                                   |
| ---                                                                                                        | ---                                                       |
| [reportWebVitals.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/reportWebVitals.js) | HTTP error 404 for prompt `client/src/reportWebVitals.js` |
| [App.test.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/App.test.js)               | HTTP error 404 for prompt `client/src/App.test.js`        |
| [setupTests.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/setupTests.js)           | HTTP error 404 for prompt `client/src/setupTests.js`      |
| [App.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/App.js)                         | HTTP error 404 for prompt `client/src/App.js`             |
| [index.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/index.js)                     | HTTP error 404 for prompt `client/src/index.js`           |
| [index.css](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/index.css)                   | HTTP error 404 for prompt `client/src/index.css`          |

</details>

<details closed><summary>client.src.graphql</summary>

| File                                                                                                         | Summary                                                        |
| ---                                                                                                          | ---                                                            |
| [auth.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/graphql/auth.js)                 | HTTP error 404 for prompt `client/src/graphql/auth.js`         |
| [apolloConfig.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/graphql/apolloConfig.js) | HTTP error 404 for prompt `client/src/graphql/apolloConfig.js` |
| [mutations.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/graphql/mutations.js)       | HTTP error 404 for prompt `client/src/graphql/mutations.js`    |
| [queries.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/graphql/queries.js)           | HTTP error 404 for prompt `client/src/graphql/queries.js`      |

</details>

<details closed><summary>client.src.utils</summary>

| File                                                                                         | Summary                                               |
| ---                                                                                          | ---                                                   |
| [utils.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/utils/utils.js) | HTTP error 404 for prompt `client/src/utils/utils.js` |

</details>

<details closed><summary>client.src.components</summary>

| File                                                                                                                            | Summary                                                                   |
| ---                                                                                                                             | ---                                                                       |
| [footer.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/footer.js)                             | HTTP error 404 for prompt `client/src/components/footer.js`               |
| [medicalRecords.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/medicalRecords.js)             | HTTP error 404 for prompt `client/src/components/medicalRecords.js`       |
| [header.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/header.js)                             | HTTP error 404 for prompt `client/src/components/header.js`               |
| [userBar.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/userBar.js)                           | HTTP error 404 for prompt `client/src/components/userBar.js`              |
| [insertToken.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/insertToken.js)                   | HTTP error 404 for prompt `client/src/components/insertToken.js`          |
| [home.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/home.js)                                 | HTTP error 404 for prompt `client/src/components/home.js`                 |
| [medicalRecordsAccess.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/medicalRecordsAccess.js) | HTTP error 404 for prompt `client/src/components/medicalRecordsAccess.js` |
| [main.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/main.js)                                 | HTTP error 404 for prompt `client/src/components/main.js`                 |
| [createUser.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/createUser.js)                     | HTTP error 404 for prompt `client/src/components/createUser.js`           |
| [login.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/login.js)                               | HTTP error 404 for prompt `client/src/components/login.js`                |
| [header.css](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/header.css)                           | HTTP error 404 for prompt `client/src/components/header.css`              |
| [generateAccessToken.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/generateAccessToken.js)   | HTTP error 404 for prompt `client/src/components/generateAccessToken.js`  |
| [navbar.css](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/navbar.css)                           | HTTP error 404 for prompt `client/src/components/navbar.css`              |
| [navbar.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/components/navbar.js)                             | HTTP error 404 for prompt `client/src/components/navbar.js`               |

</details>

<details closed><summary>client.src.providers</summary>

| File                                                                                                         | Summary                                                         |
| ---                                                                                                          | ---                                                             |
| [userContext.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/providers/userContext.js) | HTTP error 404 for prompt `client/src/providers/userContext.js` |

</details>

<details closed><summary>client.src.hooks</summary>

| File                                                                                         | Summary                                               |
| ---                                                                                          | ---                                                   |
| [hooks.js](https://github.com/TiagoIesbick/hack-saude/blob/master/client/src/hooks/hooks.js) | HTTP error 404 for prompt `client/src/hooks/hooks.js` |

</details>

<details closed><summary>server</summary>

| File                                                                                           | Summary                                           |
| ---                                                                                            | ---                                               |
| [resolver.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/resolver.py)       | HTTP error 404 for prompt `server/resolver.py`    |
| [schema.graphql](https://github.com/TiagoIesbick/hack-saude/blob/master/server/schema.graphql) | HTTP error 404 for prompt `server/schema.graphql` |
| [Pipfile.lock](https://github.com/TiagoIesbick/hack-saude/blob/master/server/Pipfile.lock)     | HTTP error 404 for prompt `server/Pipfile.lock`   |
| [server.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/server.py)           | HTTP error 404 for prompt `server/server.py`      |
| [auth.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/auth.py)               | HTTP error 404 for prompt `server/auth.py`        |
| [.env](https://github.com/TiagoIesbick/hack-saude/blob/master/server/.env)                     | HTTP error 404 for prompt `server/.env`           |
| [Pipfile](https://github.com/TiagoIesbick/hack-saude/blob/master/server/Pipfile)               | HTTP error 404 for prompt `server/Pipfile`        |

</details>

<details closed><summary>server.utils</summary>

| File                                                                                     | Summary                                           |
| ---                                                                                      | ---                                               |
| [utils.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/utils/utils.py) | HTTP error 404 for prompt `server/utils/utils.py` |

</details>

<details closed><summary>server.db</summary>

| File                                                                                                  | Summary                                                |
| ---                                                                                                   | ---                                                    |
| [connection.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/db/connection.py)       | HTTP error 404 for prompt `server/db/connection.py`    |
| [mysql_results.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/db/mysql_results.py) | HTTP error 404 for prompt `server/db/mysql_results.py` |
| [mutations.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/db/mutations.py)         | HTTP error 404 for prompt `server/db/mutations.py`     |
| [queries.py](https://github.com/TiagoIesbick/hack-saude/blob/master/server/db/queries.py)             | HTTP error 404 for prompt `server/db/queries.py`       |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **JavaScript**: `version x.y.z`

###  Installation

1. Clone the hack-saude repository:

```sh
git clone https://github.com/TiagoIesbick/hack-saude
```

2. Change to the project directory:

```sh
cd hack-saude
```

3. Install the dependencies:

```sh
npm install
```

###  Running hack-saude

Use the following command to run hack-saude:

```sh
node app.js
```

###  Tests

To execute tests, run:

```sh
npm test
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/TiagoIesbick/hack-saude/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/TiagoIesbick/hack-saude/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/TiagoIesbick/hack-saude/issues)**: Submit bugs found or log feature requests for Hack-saude.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/TiagoIesbick/hack-saude
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
