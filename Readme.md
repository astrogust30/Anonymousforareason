<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="200" height="200"/>
</div>


##  About

Welcome to my project, an engine that evaluates rules using an AST. This application determines user eligibility based on attributes like age, department, income, spending habits, and more. It leverages an AST to represent conditional logic, allowing for dynamic creation, combination, and modification of these rules.


## Table of Content  <div id="header" align="center">
  <img src="https://media.giphy.com/media/Qo2dupDib32rkTY4hX/giphy.gif?cid=ecf05e47viopwlm7lo1gou3g05zpjr1edr7jzyf2pqpv70ny&ep=v1_gifs_related&rid=giphy.gif&ct=s" width="100"/>
</div>

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Design Choices](#design-choices)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [Build Instructions and Design Choices](#build-instructions-and-design-choices)
- [License](#license)
- [Contact Information](#contact-information)

## Introduction

This project implements a rule engine using an Abstract Syntax Tree (AST) to evaluate user eligibility based on dynamic rules. It consists of:

- **Backend**: Python application using Flask for the API layer.
- **Frontend**: HTML templates styled with Bootstrap for a modern UI.
- **Database**: SQLite for storing rules and application metadata.

## Features

- **Create Rules**: Define new eligibility rules using a simple syntax.
- **Combine Rules**: Merge multiple rules into a single optimized AST.
- **Evaluate Rules**: Assess user data against combined rules to determine eligibility.
- **Modify Rules**: Update existing rules dynamically.
- **Error Handling**: Robust error management for invalid inputs.
- **Attribute Validation**: Ensures attributes used in rules are part of a predefined catalog.
- **Modern UI**: User-friendly interface with a modern look using Bootstrap and Font Awesome.

## Technologies Used

- **Python 3.8+**
- **Flask**: Web framework for the API and server.
- **SQLite**: Lightweight database for storing rules.
- **Bootstrap**: For responsive and modern UI components.
- **jQuery**: Simplifies JavaScript interactions.
- **Font Awesome**: Provides icons for enhancing UI.

## Design Choices

- **AST Representation**: The rules are parsed into an Abstract Syntax Tree to allow for efficient evaluation and manipulation.
- **Optimization of Rules**: Redundant conditions are minimized when combining rules to enhance performance.
- **Web Interface**: A user-friendly UI is provided for interacting with the rule engine without the need for direct API calls.
- **Separation of Concerns**: The code is organized into separate modules for parsing, evaluation, and API endpoints.
- **Error Handling**: Implemented comprehensive error handling to manage invalid inputs and operations.
- **Attribute Catalog**: Validates attributes against a predefined catalog to ensure consistency.

## Prerequisites

- **Python 3.8 or higher**
- **pip**: Package installer for Python

 <div id="header" align="center">
  <img src="https://media.giphy.com/media/jzuSsejVh8EYRfdOTz/giphy.gif?cid=ecf05e47vbyg4kvtrcv9fhy38lkc9a67y8tp03v7oy8xcfbt&ep=v1_gifs_related&rid=giphy.gif&ct=s" width="300" height="300"/>
</div>


## Usage

### Create a New Rule
1. On the Rule Engine homepage, use the form to enter a unique rule name and a valid rule string.
2. Click on "Create Rule" to save the rule.

### Combine Rules
1. Enter the names of the rules you wish to combine, separated by commas (e.g., `rule1, rule2`).
2. Click on "Combine Rules" to merge them.
3. The combined AST JSON will appear in the Evaluate Rule section.

### Evaluate Rule
1. Provide user data in JSON format in the User Data field.
2. Click on "Evaluate" to assess eligibility.
3. The result will display whether the user is eligible based on the combined rule.

## API Endpoints

### POST /api/rules
- **Description**: Creates a new rule.
- **Parameters**:
  - `name`: Unique name for the rule.
  - `rule_string`: The rule logic in string format.
- **Response**:
  - `201 Created`: Rule created successfully.
  - `400 Bad Request`: Error message.

### POST /api/rules/combine
- **Description**: Combines multiple rules into one.
- **Parameters**:
  - `rule_names`: List of rule names to combine.
- **Response**:
  - `200 OK`: Combined AST JSON.
  - `400 Bad Request`: Error message.

### POST /api/evaluate
- **Description**: Evaluates user data against the combined rule.
- **Parameters**:
  - `ast_json`: The combined AST in JSON format.
  - `user_data`: User attributes in JSON format.
- **Response**:
  - `200 OK`: Eligibility result.
  - `400 Bad Request`: Error message.

## Dependencies

- **Flask**: Install with `pip install flask`
- **Flask-Session**: Install with `pip install flask-session`
- **Bootstrap**: Included via CDN in templates.
- **jQuery**: Included via CDN in templates.
- **Font Awesome**: Included via CDN in templates.
- All Python dependencies are listed in `requirements.txt`.

## Build Instructions and Design Choices

### Build Instructions

#### Set Up Environment
- Use a virtual environment to manage dependencies.
- Install required packages using `requirements.txt`.

#### Initialize the Application
- The database initializes on the first run.
- Run `app.py` to start the Flask server.

#### Access the Application
- Open `http://localhost:5000` in a web browser.

### Design Choices

- **AST Implementation**: Utilized an AST to parse and represent rules, allowing for dynamic creation, combination, and modification.
- **Optimized Rule Combination**: Implemented a function to optimize and combine multiple rules into a single AST, minimizing redundant checks.
- **Modern UI with Bootstrap**: Adopted Bootstrap for a responsive and modern user interface. Included Font Awesome icons to enhance visual appeal.
- **API Layer**: Created RESTful API endpoints using Flask to interact with the rule engine programmatically.
- **Database Choice**: Chose SQLite for simplicity and ease of setup, suitable for development and lightweight applications.
- **Error Handling and Validation**: Implemented comprehensive error handling for invalid inputs. Validated attributes against a predefined catalog to ensure consistency.

## File Structure

