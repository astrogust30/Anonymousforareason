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

### **How to Run the Application**

1. **Install Dependencies**:
    
    ```bash
    pip install flask
    
    ```
    
2. **Run the Application**:
    
    ```bash
    python app.py
    
    ```
    
3. **Access the UI**:
    - Open a web browser and navigate to **`http://localhost:5000`**.
4. **Interact with the Rule Engine**:
    - **Create Rules**: Use the form to create new rules by providing a name and a rule string.
    - **View Rules**: Existing rules will be listed on the page.
    - **Combine Rules**: Enter rule names (comma-separated) to combine them.
    - **Evaluate Rules**: Provide the combined AST JSON and user data to evaluate eligibility.

### **Testing the Application**

### **Sample Rules**

- **Rule 1**:
    
    ```
    ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
    
    ```
    
- **Rule 2**:
    
    ```
    ((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)
    
    ```
    

### **Sample User Data**

```json
{
  "age": 35,
  "department": "Sales",
  "salary": 60000,
  "experience": 3
}

```

### **Steps:**

1. **Create Rules**:
    - Use the "Create a New Rule" form to add Rule 1 and Rule 2 with names **`rule1`** and **`rule2`** respectively.
2. **Combine Rules**:
    - Enter **`rule1, rule2`** in the "Combine Rules" form to combine them.
    - The combined AST JSON will be displayed in the "Evaluate Rule" section.
3. **Evaluate Rule**:
    - Paste the sample user data into the "User Data" field.
    - Click "Evaluate" to check if the user is eligible based on the combined rule.
    - The result will be displayed below the form.

### **Expected Outcome**

- The sample user data should result in **`Eligible: True`** if it satisfies any of the combined rules.

### Design Choices

- **AST Implementation**: Utilized an AST to parse and represent rules, allowing for dynamic creation, combination, and modification.
- **Optimized Rule Combination**: Implemented a function to optimize and combine multiple rules into a single AST, minimizing redundant checks.
- **Modern UI with Bootstrap**: Adopted Bootstrap for a responsive and modern user interface. Included Font Awesome icons to enhance visual appeal.
- **API Layer**: Created RESTful API endpoints using Flask to interact with the rule engine programmatically.
- **Database Choice**: Chose SQLite for simplicity and ease of setup, suitable for development and lightweight applications.
- **Error Handling and Validation**: Implemented comprehensive error handling for invalid inputs. Validated attributes against a predefined catalog to ensure consistency.

## File Structure
 ```sh
root/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
└── rules.db
```

## Details of Key Files

- **app.py**: The main Flask application file containing:
  - Route Definitions: Defines the endpoints for creating rules, combining rules, and evaluating rules.
  - AST Functions: Contains functions for tokenizing, parsing, and evaluating rules represented as ASTs.
  - Database Functions: Manages the creation of the database and interactions with the rules table.

- **templates/index.html**: The HTML template for the user interface, providing forms and displays for:
  - Creating Rules
  - Combining Rules
  - Evaluating Rules

- **static/css/style.css**: Custom CSS styles to enhance the visual appeal of the application, including:
  - Layout and Spacing
  - Color Scheme
  - Responsive Design

- **static/js/app.js**: Custom JavaScript for client-side interactivity and AJAX calls, handling:
  - Form Submissions
  - API Requests
  - Result Display

## License

All rights reserved with khushisharmasre30@gmail.com

## Contact Information

For any questions or suggestions, please open an issue or contact the repository owner.

## Additional Notes

- **Security**: Remember to set a strong `secret_key` in `app.py` for session management if sessions are used.
- **Extensibility**: The system is designed to be easily extendable for additional features or integration with other systems.
- **Testing**: Test the application thoroughly with different rule combinations and user data to ensure reliability.

