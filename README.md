# MyShop Automation Project

This project automates the main user flow of the demo website [http://www.automationpractice.pl](http://www.automationpractice.pl) using Playwright, Pytest, and Allure.

## Technologies Used

- Playwright (Python)
- Pytest
- Allure for test reporting
- Page Object Model (POM) structure with explicit selectors and reusable page methods

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
├── tests/                 
│   ├── test_flow.py
│   └── test_invalid_login.py
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
- Login with invalid credentials (negative test)
- Search for a product
- Open product and select color
- Add to cart
- Remove from cart
- Assert UI and URL validation throughout the flow

## Improvements & Conventions

- Page Object Model structured without `@dataclass`
- All selectors declared at the top of each page class
- Enhanced assertions with screenshots and Allure integration
- Timeout values centralized via `BROWSER_CONFIG`
- Error handling and validation at each critical step

## Author

Created by Boaz Yashar
