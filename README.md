# MyShop Automation Project

This project automates the main user flow of the demo website [http://www.automationpractice.pl](http://www.automationpractice.pl) using Playwright, Pytest, and Allure.

## Technologies Used

- Playwright (Python)
- Pytest
- Allure for test reporting
- Page Object Model (POM) structure

## Project Structure

```
MyShop/
├── config/                 # Configuration settings
│   └── test_config.py
├── pages/                 # Page object classes
│   ├── registration_page.py
│   ├── login_page.py
│   ├── home_page.py
│   └── cart_page.py
├── tests/                 # Test cases
│   └── test_flow.py
├── utils/                 # Utility functions
│   └── helpers.py
├── conftest.py            # Shared pytest fixtures
├── requirements.txt
├── README.md
```

## Getting Started

1. Create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
# or
source .venv/bin/activate  # macOS/Linux
```

2. Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

3. Run tests with Allure:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

Make sure Allure is installed on your system: https://docs.qameta.io/allure/

## Test Coverage

- Register new user
- Login with valid credentials
- Search for a product
- Open product and select color
- Add to cart
- Remove from cart
- Validate navigation and expected behavior

## Author

Created by Boaz Yashar