<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
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

 <div id="header" align="center">
  <img src="https://media.giphy.com/media/jzuSsejVh8EYRfdOTz/giphy.gif?cid=ecf05e47vbyg4kvtrcv9fhy38lkc9a67y8tp03v7oy8xcfbt&ep=v1_gifs_related&rid=giphy.gif&ct=s" width="100"/>
</div>

- **AST Representation**: The rules are parsed into an Abstract Syntax Tree to allow for efficient evaluation and manipulation.
- **Optimization of Rules**: Redundant conditions are minimized when combining rules to enhance performance.
- **Web Interface**: A user-friendly UI is provided for interacting with the rule engine without the need for direct API calls.
- **Separation of Concerns**: The code is organized into separate modules for parsing, evaluation, and API endpoints.
- **Error Handling**: Implemented comprehensive error handling to manage invalid inputs and operations.
- **Attribute Catalog**: Validates attributes against a predefined catalog to ensure consistency.

## Prerequisites

- **Python 3.8 or higher**
- **pip**: Package installer for Python

