# Genesis Regression Test Framework

This repository contains code written in Python using [pytest](https://docs.pytest.org/) (test automation framework) and [Allure](https://github.com/allure-framework) framework for report generation. The framework is designed to automate genesis regression tests, ensuring its functionality and reliability over time.
## Getting Started

### Clone the Repository

To get started, you need to clone the repository to your local machine. Open your terminal (or command prompt) and run the following command:

```bash
git clone https://github.com/your-username/your-repo.git

Replace your-username with your GitHub username and your-repo with the name of your repository.
```

### Setup Virtual Environment
It's recommended to create a virtual environment to isolate your project's dependencies. You can do this using Python's built-in venv module.

For Mac Users
Open a terminal.

Navigate to your project's directory:

```bash
cd path/to/your-repo
```
Create a virtual environment:
```bash
python3 -m venv venv
```
Activate the virtual environment:
```bash
source venv/bin/activate
```
For Windows Users
Open a command prompt.

Navigate to your project's directory:

```shell
cd path\to\your-repo
```
Create a virtual environment:
```shell
python -m venv venv
```
Activate the virtual environment:
```shell
.\venv\Scripts\activate
```
Install Dependencies
Once the virtual environment is activated, you can install the required dependencies for the framework. In your project's directory, run:

```shell
pip install -r requirements.txt
```
This command will install all the necessary Python packages listed in the requirements.txt file.

Execute Tests
With the virtual environment activated and dependencies installed, you can now execute tests using pytest.

Navigate to your project's test directory:
```shell
cd tests
```
Run the tests using pytest:
```shell
pytest
```
This command will discover and execute all the test cases in the project. You'll see the test results in the terminal, including any failures or errors.
If you want to run the tests with allure reporting enabled sequentially, use:
```shell
pytest --alluredir=allure && allure serve $base_dir/allure

```
If you want to run tests in parallel and with allure reporting enabled , use:
```shell
pytest -n $number_of_parallel_runs --alluredir=allure && allure serve $base_dir/allure

```