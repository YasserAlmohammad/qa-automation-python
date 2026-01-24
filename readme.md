[![Python tests](https://github.com/YasserAlmohammad/qa-automation-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/YasserAlmohammad/qa-automation-python/actions/workflows/python-tests.yml)

[![API tests](https://github.com/YasserAlmohammad/qa-automation-python/actions/workflows/api-tests.yml/badge.svg)](https://github.com/YasserAlmohammad/qa-automation-python/actions/workflows/api-tests.yml)
# QA Automation (Python + pytest)

This repository is a **learning and practice project** for QA automation using **Python**, **pytest**, and **GitHub Actions**.  
It demonstrates how to write, structure, and run automated tests locally and in CI.

---




## Setup
```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1  #activate vm
pip install -r requirements.txt #install dependencies
pytest -q #run tests

## Project structure
qa-automation-python/
├── src/ # application / utility code
│ └── utils.py
├── tests/ # automated tests
│ ├── test_utils.py # unit-style tests
│ └── test_api_users.py # API tests
├── pytest.ini # pytest configuration
├── requirements.txt # project dependencies
└── README.md
└── .github/
    └──  workflows/
            └── python-tests.yml # CI for github

## 🔍 What this project demonstrates

- Python-based test automation with **pytest**
- Unit-style tests for application logic
- API tests using the **requests** library
- Use of **fixtures** for shared test setup
- Use of **parametrized tests** for multiple input scenarios
- Testing of **positive and negative cases** (e.g. errors, timeouts)
- **Continuous Integration (CI)** with GitHub Actions
