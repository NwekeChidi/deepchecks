# DEEPCHECKS BACKEND ASSESSMENT

This project attempts to solve the assesment problem which involves building a system that can log LLM interactions, calculate various metrics on these interactions and alert the user when specific conditions are met on these metrics.

---

### Libraries/Frameworks Used

- Flask
- psycopg2-binary
- Flask-SQLAlchemy

---

### Database

- PostgreSQL

---

### Project Structure

```
.
├── models
│   ├── __init__.py
|   ├── log_alerts.py
├── scripts
│   ├── destory.sh
|   ├── startup.sh
├── utils
│   ├── __init__.py
|   ├── calculateMetrics.py
│   ├── db.py
├── .gitignore
├── app.py
├── deepchecks.csv
├── Dockerfile
├── docker-compose.yml
├── todo.md
├── requirements.txt
└── README.md
```

- `models` Contains the data models
- `scripts` Contains the bash scripts for starting up and terminating the project
- `utils` Contains the utility files and functions
- `app.py` Entry point for Flask Application
- `Dockerfile` and `docker-compose.yml` Docker containerization configurations
- `deepchecks.csv` Sample test file

---

### Getting Started

To successfully initialize and spin up this project, you need:

> - Docker Account
> - docker cli
> - python

- _Step 1:_ Clone the repository
- _Step 2:_ Ensure you in the right directory `/deepchecks`
- _Step 3:_ Run the command `./scripts/startup.sh`. This script spins up the docker containers. Might require authentication if you are not already signed in to you docker account

---

### Postman Documentation

[`API Documentation`](https://documenter.getpostman.com/view/19837110/2sA3dygVmr)

---

### Cleanup

You can terminate and remove the running containers by running the command `./scripts/destroy.sh`
