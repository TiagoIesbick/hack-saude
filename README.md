<p align="center">
  <img src="https://github.com/TiagoIesbick/vita-health/blob/main/client/src/assets/logos/logo-vita-no-bg.png" width="120" />
</p>
<p align="center">
    <h1 align="center">Vita</h1>
</p>
<p align="center">
    <em>Empower Your Health: Take Control of Your Medical Data</em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/license/TiagoIesbick/vita-health?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/TiagoIesbick/vita-health?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/TiagoIesbick/vita-health?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/TiagoIesbick/vita-health?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=JavaScript&logoColor=black" alt="JavaScript">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/MySQL-005C84.svg?style=flat&logo=MySQL&logoColor=white" alt="MySQL">
    <img src="https://img.shields.io/badge/GraphQL-E10098.svg?style=flat&logo=GraphQL&logoColor=white" alt="GraphQL">
    <img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat&logo=React&logoColor=black" alt="React">
    <img src="https://img.shields.io/badge/JWT-000000.svg?style=flat&logo=JSON%20web%20tokens&logoColor=white" alt="JWT">
	<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=flat&logo=dotenv&logoColor=black" alt=".ENV">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
</p>
<hr>

## 📖 Table of Contents

- [ 📍 Overview](#-overview)
- [ 📦 Features](#-features)
- [ 📂 Repository Structure](#-repository-structure)
- [ 💾 Database Structure](#-database-structure)
- [ ⚙️ Modules](#%EF%B8%8F-modules)
- [ 🚀 Getting Started](#-getting-started)
    - [ 🔧 Installation](#-installation)
    - [ 🤖 Running vita-health](#-running-vita-health)
- [ 🛣 Roadmap](#-roadmap)
- [ 👀 Comments](#-comments)

---


## 📍 Overview

This application is a medical data management system that centralizes patients' health information and allows secure sharing of this data with doctors through temporary tokens. The application aims to solve the problem of decentralization of medical data, facilitating access and management of health records in a safe and efficient way.

---


## 📦 Features

Patients and doctors can register and log in to the platform. Data such as name, email, user type (patient or doctor), and password are stored securely, and the password is encrypted before being saved in the database (fully developed). Patients can generate temporary tokens to share their medical data with specific doctors (fully developed). Doctors can access shared data using tokens provided by patients (fully developed). Access logs detail when medical records were accessed and by which doctors (fully developed). Patients can view and edit their personal information, such as date of birth and gender (fully developed). Doctors can add their specialties and license number (fully developed). Patients can upload and view their medical records, such as test results, prescriptions, etc. (part of the database has already been developed, part of the back-end and front-end to be developed). The types of medical records will be categorized for easy navigation and searching (part of the database has already been developed, part of the back-end and front-end to be developed). Patients will have visibility into who accessed their data and when (part of the database has already been developed, part of the back-end and front-end to be developed).

---


## 📂 Repository Structure

```sh
└── vita-health/
    ├── LICENSE
    ├── README.md
    ├── client
    │   ├── .gitignore
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
    │       │   ├── activeTokens.js
    │       │   ├── createUser.js
    │       │   ├── editDoctorProfile.js
    │       │   ├── editPatientProfile.js
    │       │   ├── editProfile.js
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
        │   ├── ERM_vita_health.png
        │   └── vita_health.sql
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


## 💾 Database Structure

<p align="center">
  <img src="https://github.com/TiagoIesbick/vita-health/blob/main/server/data/ERM_vita_health.png" width="600" />
</p>

---


## ⚙️ Modules

<details closed><summary>client</summary>

| File                                                                                                 | Summary                                              |
| ---                                                                                                  | ---                                                  |
| [package.json](https://github.com/TiagoIesbick/vita-health/blob/master/client/package.json)           | Defines the project's high-level dependencies, scripts, and metadata `client/package.json`      |
| [package-lock.json](https://github.com/TiagoIesbick/vita-health/blob/master/client/package-lock.json) | Locks the exact versions of all dependencies, ensuring consistent and reproducible installations `client/package-lock.json` |

</details>

<details closed><summary>client.public</summary>

| File                                                                                                | Summary                                                 |
| ---                                                                                                 | ---                                                     |
| [index.html](https://github.com/TiagoIesbick/vita-health/blob/master/client/public/index.html)       | Entry point for the application in the browser `client/public/index.html`    |
| [manifest.json](https://github.com/TiagoIesbick/vita-health/blob/master/client/public/manifest.json) | Provides information about the web application in a format that browsers and devices can understand `client/public/manifest.json` |
| [robots.txt](https://github.com/TiagoIesbick/vita-health/blob/master/client/public/robots.txt)       | Controls the behavior of search bots by specifying which parts of the site should be crawled or ignored `client/public/robots.txt`    |

</details>

<details closed><summary>client.src</summary>

| File                                                                                                       | Summary                                                   |
| ---                                                                                                        | ---                                                       |
| [reportWebVitals.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/reportWebVitals.js) | Used to measure and report application performance metrics `client/src/reportWebVitals.js` |
| [App.test.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/App.test.js)               | Used to write and run automated unit or integration tests `client/src/App.test.js`        |
| [setupTests.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/setupTests.js)           | Used to configure the testing environment before tests are run `client/src/setupTests.js`      |
| [App.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/App.js)                         | Main component that defines the structure and initial logic of the application `client/src/App.js`             |
| [index.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/index.js)                     | Responsible for rendering the application's root component on the HTML page `client/src/index.js`           |
| [index.css](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/index.css)                   | Provides global styles that apply to the entire application `client/src/index.css`          |

</details>

<details closed><summary>client.src.graphql</summary>

| File                                                                                                         | Summary                                                        |
| ---                                                                                                          | ---                                                            |
| [auth.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/graphql/auth.js)                 | Client-side authentication logic `client/src/graphql/auth.js`         |
| [apolloConfig.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/graphql/apolloConfig.js) | Apollo Client configuration `client/src/graphql/apolloConfig.js` |
| [mutations.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/graphql/mutations.js)       | Mutations to be requested to the GraphQL server `client/src/graphql/mutations.js`    |
| [queries.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/graphql/queries.js)           | Queries to be requested to the GraphQL server `client/src/graphql/queries.js`      |

</details>

<details closed><summary>client.src.utils</summary>

| File                                                                                         | Summary                                               |
| ---                                                                                          | ---                                                   |
| [utils.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/utils/utils.js) | Useful functions for the operation of the client-side of the application `client/src/utils/utils.js` |

</details>

<details closed><summary>client.src.components</summary>

| File                                                                                                                            | Summary                                                                   |
| ---                                                                                                                             | ---                                                                       |
| [activeTokens.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/activeTokens.js)                 | Active Tokens Page `client/src/components/activeTokens.js`         |
| [footer.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/footer.js)                             | Page footer `client/src/components/footer.js`               |
| [medicalRecords.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/medicalRecords.js)             | Medical Data viewed by patients `client/src/components/medicalRecords.js`       |
| [header.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/header.js)                             | Page header `client/src/components/header.js`               |
| [userBar.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/userBar.js)                           | Navigating user information `client/src/components/userBar.js`              |
| [insertToken.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/insertToken.js)                   | Page for the doctor to enter the token provided by the patient `client/src/components/insertToken.js`          |
| [home.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/home.js)                                 | Application landing page `client/src/components/home.js`                 |
| [medicalRecordsAccess.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/medicalRecordsAccess.js) | Page for the doctor to view the data released by the token provided by the patient `client/src/components/medicalRecordsAccess.js` |
| [main.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/main.js)                                 | Middle of the page `client/src/components/main.js`                 |
| [createUser.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/createUser.js)                     | Form for creating users, whether doctors or patients `client/src/components/createUser.js`           |
| [login.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/login.js)                               | Login page `client/src/components/login.js`                |
| [header.css](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/header.css)                           | Page header styling `client/src/components/header.css`              |
| [editProfile.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/editProfile.js)                   | Page that contains components for patients and doctors to edit their personal information `client/src/components/editProfile.js`          |
| [editPatientProfile.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/editPatientProfile.js)     | Component for patients to edit their personal information `client/src/components/editPatientProfile.js`   |
| [editDoctorProfile.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/editDoctorProfile.js)       | Component for doctors to edit their personal information `client/src/components/editDoctorProfile.js`    |
| [generateAccessToken.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/generateAccessToken.js)   | Page for the patient to issue the token to be provided to the doctor `client/src/components/generateAccessToken.js`  |
| [navbar.css](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/navbar.css)                           | Navigation bar styling `client/src/components/navbar.css`              |
| [navbar.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/components/navbar.js)                             | Navigation bar `client/src/components/navbar.js`               |

</details>

<details closed><summary>client.src.providers</summary>

| File                                                                                                         | Summary                                                         |
| ---                                                                                                          | ---                                                             |
| [userContext.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/providers/userContext.js) | Context data to be consumed by the client-side of the application `client/src/providers/userContext.js` |

</details>

<details closed><summary>client.src.hooks</summary>

| File                                                                                         | Summary                                               |
| ---                                                                                          | ---                                                   |
| [hooks.js](https://github.com/TiagoIesbick/vita-health/blob/master/client/src/hooks/hooks.js) | Functions to be consumed by the client-side of the application `client/src/hooks/hooks.js` |

</details>

<details closed><summary>server</summary>

| File                                                                                           | Summary                                           |
| ---                                                                                            | ---                                               |
| [resolver.py](https://github.com/TiagoIesbick/vita-health/blob/master/server/resolver.py)       | Logic for resolving mutations and queries requested from the GraphQL server `server/resolver.py`    |
| [schema.graphql](https://github.com/TiagoIesbick/vita-health/blob/master/server/schema.graphql) | GraphQL server typing and schema `server/schema.graphql` |
| [Pipfile.lock](https://github.com/TiagoIesbick/vita-health/blob/master/server/Pipfile.lock)     | Ensures reproducibility, security and efficiency in installing dependencies on the server developed with Python `server/Pipfile.lock`   |
| [server.py](https://github.com/TiagoIesbick/vita-health/blob/master/server/server.py)           | Responsible for starting and configuring the server `server/server.py`      |
| [auth.py](https://github.com/TiagoIesbick/vita-health/blob/master/server/auth.py)               | Server-side authentication logic `server/auth.py`        |
| [.env](https://github.com/TiagoIesbick/vita-health/blob/master/server/.env)                     | Environment variables `server/.env`           |
| [Pipfile](https://github.com/TiagoIesbick/vita-health/blob/master/server/Pipfile)               | Specifies the dependencies required for the project `server/Pipfile`        |

</details>

<details closed><summary>server.utils</summary>

| File                                                                                     | Summary                                           |
| ---                                                                                      | ---                                               |
| [utils.py](https://github.com/TiagoIesbick/vita-health/blob/master/server/utils/utils.py) | Useful functions for the operation of the server-side of the application `server/utils/utils.py` |

</details>

<details closed><summary>server.db</summary>

| File                                                                                                  | Summary                                                |
| ---                                                                                                   | ---                                                    |
| [connection.py](https://github.com/TiagoIesbick/vita-health/blob/master/server/db/connection.py)       | Connection to MySQL database `server/db/connection.py`    |
| [mysql_results.py](https://github.com/TiagoIesbick/vita-health/blob/master/server/db/mysql_results.py) | Executing queries and mutations in the database `server/db/mysql_results.py` |
| [mutations.py](https://github.com/TiagoIesbick/vita-health/blob/master/server/db/mutations.py)         | Logic of the mutations to be executed `server/db/mutations.py`     |
| [queries.py](https://github.com/TiagoIesbick/vita-health/blob/master/server/db/queries.py)             | Logic of the queries to be executed `server/db/queries.py`       |

</details>

<details closed><summary>server.data</summary>

| File                                                                                                  | Summary                                                |
| ---                                                                                                   | ---                                                    |
| [ERM_vita_health.png](https://github.com/TiagoIesbick/vita-health/blob/master/server/data/ERM_vita_health.png)       | ERM is a conceptual model used to describe the data that will be stored in a relational database and the relationships between that data `server/data/ERM_vita_health.png`    |
| [vita_health.sql](https://github.com/TiagoIesbick/vita-health/blob/master/server/data/vita_health.sql) | SQL script to assemble the database, including mock data `server/data/vita_health.sql` |


</details>

---


## 🚀 Getting Started

***Requirements***

Make sure you have the following dependencies installed on your system:

* **Python**: `version 3.12+`
* **MySQL**: `version 8.0+`
* **Pipenv**: `version 2023.12.1+`
* **Node**: `version v20.14.0+`

### 🔧 Installation

1. Clone the vita-health repository:

```sh
git clone https://github.com/TiagoIesbick/vita-health
```

2. Change to the project directory:

```sh
cd vita-health
```

3. Change to the server directory:

```sh
cd server
```

4. Run the following commands in the server directory:

```sh
pipenv shell
pipenv install
```

5. In the server directory, write the following command, replacing `<vita_health>` with `root` or your MySQL username:

```sh
mysql -u <vita_health> -p
```

6. Enter the requested password, according to the user you entered in the previous command.

7. Run the following command to mount the database:

```sh
source data/vita_health.sql
```

8. Exit the MySQL prompt with the following command:

```sh
exit
```

8. According to the user and password used in the MySQL prompt, update the USER and PASSWORD environment variables in the .env file:

```sh
USER=YOUR_USER
PASSWORD=YOUR_PASSWORD
```

9. Run the server in the server directory with the following command:

```sh
uvicorn server:app
```

10. The Graphql server debug will be available at the following address `http://127.0.0.1:8000/graphql/`

11. Open a new terminal and navigate to the client directory:

```sh
cd client
```

12. Run the following commands in the client directory:

```sh
npm install
npm start
```

### 🤖 Running vita-health

After these commands the server will be running on `http://127.0.0.1:8000/graphql/` and the client will be running on `http://localhost:3000/`

---


## 🛣 Roadmap

- [X] `► Log in with patient user type: john.doe@example.com, Vita_Health123`
- [X] `► Navigate to the Medical Records tab, which has an example data`
- [X] `► Navigate to the Generate Token tab`
- [X] `► Choose the date and time that the token will expire, past time will not be accepted and an error message will be displayed. To exit the calendar you need to double click outside of it`
- [X] `► Confirm the date and time and wait for the token to be displayed, which must be copied`
- [X] `► Logout from dropdown menu with logged in user's initial`
- [X] `► Log in with healthcare professional user type: jane.smith@example.com, Vita_Health123`
- [X] `► Navigate to the Insert Token tab and paste the previously generated token, if it has not expired, the medical records of the patient who generated the token will be visible`

---


## 👀 Comments

- It is possible to create new users, both patient and healthcare professional, something that can be done in the login tab in the Create an Account session, however new users will not have medical data to be displayed;
- The application runs in such a way that it saves login tokens as well as patient health data access tokens in the browser's local storage. Only the patient health data access token has an expiration date;
- The doctor will only be able to see the data of the patient who generated the token and passed it on to him, and will not have access to the data of other users;
- Each doctor's view of patient data in the period the token is active is saved in the database's TokenAccess table.
- User passwords are saved encrypted in the database;
- In the drop-down menu below the initial of the user's name there is a functionality that has not yet been implemented, namely: checking the tokens that are active.
- Regarding medical data inputs, we imagine that it will be possible for both the patient to enter data and the doctor to enter data while the token passed on is active. Furthermore, I imagine creating APIs that connect to hospitals and laboratories to automate data entry.
- The success of the application could result in the replacement of systems in use in various healthcare establishments, concentrating the data in the hands of its true owner: the patient.

[**Return**](#Top)

---
