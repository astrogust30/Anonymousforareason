Overview
This project implements a rule engine to evaluate user eligibility using an Abstract Syntax Tree (AST). The engine allows defining, combining, and evaluating conditional rules through an intuitive API and user interface. The application is built using Python and Flask, with SQLite for data storage.

Features
Rule Creation: Easily define rules using a straightforward syntax.
Rule Combination: Combine multiple rules into a single, optimized AST.
Rule Evaluation: Assess rules against user data to determine eligibility.
Intuitive UI: Interact with the rule engine via a web-based interface.
Persistent Storage: Store rules and their AST representations in an SQLite database.
Installation
Prerequisites
Python 3.x
Flask
Steps
Clone the Repository:

Copy
git clone https://github.com/yourusername/rule-engine-ast.git
cd rule-engine-ast
Install Dependencies:

Copy
pip install flask
Run the Application:

Copy
python app.py
Access the Application:

Open your web browser and navigate to http://localhost:5000.

Usage
Creating Rules
Navigate to the "Create a New Rule" section.
Enter a rule name and rule string, then click "Create Rule".
Combining Rules
Enter the names of the rules you want to combine, separated by commas, in the "Combine Rules" section.
The combined AST JSON will be displayed.
Evaluating Rules
Paste the combined AST JSON and user data into the respective fields in the "Evaluate Rule" section.
Click "Evaluate" to determine eligibility. The result will be displayed below the form.
Testing
Sample Rules
Rule 1: ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
Rule 2: ((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)
Sample User Data
Copy
{
  "age": 35,
  "department": "Sales",
  "salary": 60000,
  "experience": 3
}
Steps
Create Rules: Use the "Create a New Rule" form to add Rule 1 and Rule 2.
Combine Rules: Enter rule1, rule2 in the "Combine Rules" form to combine them.
Evaluate Rule: Paste the sample user data into the "User Data" field and click "Evaluate".
Expected Outcome
The sample user data should result in Eligible: True if it satisfies any of the combined rules.
Screenshots
Rule Creation
Rule Creation

Existing Rules
Existing Rules

Combine Rules
Combine Rules

Evaluate Rule
Evaluate Rule

Result
Result

Future Improvements
Enhanced UI: Develop a more interactive and visually appealing user interface.
API Documentation: Provide detailed API documentation for easier integration.
Advanced Rule Logic: Implement support for more complex rule logic and conditions.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please contact your-email@example.com.

This README template is designed to be informative and visually appealing, providing all necessary information for users to understand, install, and use your rule engine application. Adjust the content and links as needed to fit your specific project details.
