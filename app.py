# app.py

import re
import json
import sqlite3
from flask import Flask, request, jsonify, render_template
from collections import defaultdict

app = Flask(__name__)

# Define valid attributes for validation
VALID_ATTRIBUTES = {'age', 'department', 'salary', 'experience'}

# Node class to represent the AST
class Node:
    def __init__(self, node_type, operator=None, attribute=None, value=None, left=None, right=None):
        self.node_type = node_type  # 'operator' or 'condition'
        self.operator = operator    # e.g., 'AND', 'OR', '>', '<', '==', '!='
        self.attribute = attribute  # e.g., 'age', 'department'
        self.value = value          # e.g., 30, 'Sales'
        self.left = left            # Left child Node
        self.right = right          # Right child Node

    def to_dict(self):
        return {
            'node_type': self.node_type,
            'operator': self.operator,
            'attribute': self.attribute,
            'value': self.value,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None
        }

    @staticmethod
    def from_dict(d):
        if d is None:
            return None
        node = Node(
            node_type=d['node_type'],
            operator=d['operator'],
            attribute=d['attribute'],
            value=d['value'],
            left=Node.from_dict(d['left']),
            right=Node.from_dict(d['right'])
        )
        return node

# Tokenizer function
def tokenize(rule_string):
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),      # Integer or decimal number
        ('AND',      r'AND'),
        ('OR',       r'OR'),
        ('NOT',      r'NOT'),
        ('OP',       r'>=|<=|!=|==|>|<|='),  # Comparison operators
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('STRING',   r"'[^']*'|\"[^\"]*\""),  # Quoted string
        ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),  # Identifiers
        ('SKIP',     r'[ \t]+'),  # Skip over spaces and tabs
        ('MISMATCH', r'.'),       # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line = rule_string
    pos = 0
    tokens = []
    mo = get_token(line)
    while mo is not None:
        kind = mo.lastgroup
        value = mo.group()
        if kind in ('NUMBER', 'AND', 'OR', 'NOT', 'OP', 'LPAREN', 'RPAREN', 'STRING', 'ID'):
            tokens.append((kind, value))
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r} at position {pos}')
        pos = mo.end()
        mo = get_token(line, pos)
    if pos != len(line):
        raise RuntimeError(f'Unexpected character {line[pos]!r} at position {pos}')
    return tokens

# Parser class
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def lookahead(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        else:
            return ('EOF', None)

    def consume(self, expected_type=None):
        token = self.lookahead()
        if expected_type and token[0] != expected_type:
            raise RuntimeError(f'Expected token {expected_type}, got {token[0]}')
        self.pos += 1
        return token

    def parse(self):
        node = self.expr()
        if self.pos != len(self.tokens):
            raise RuntimeError('Unexpected tokens at the end')
        return node

    def expr(self):
        node = self.term()
        while self.lookahead()[0] == 'OR':
            self.consume('OR')
            right = self.term()
            node = Node(node_type='operator', operator='OR', left=node, right=right)
        return node

    def term(self):
        node = self.factor()
        while self.lookahead()[0] == 'AND':
            self.consume('AND')
            right = self.factor()
            node = Node(node_type='operator', operator='AND', left=node, right=right)
        return node

    def factor(self):
        token = self.lookahead()
        if token[0] == 'NOT':
            self.consume('NOT')
            node = self.factor()
            node = Node(node_type='operator', operator='NOT', left=node)
            return node
        elif token[0] == 'LPAREN':
            self.consume('LPAREN')
            node = self.expr()
            self.consume('RPAREN')
            return node
        else:
            node = self.condition()
            return node

    def condition(self):
        token = self.lookahead()
        if token[0] == 'ID':
            attribute = self.consume('ID')[1]
            if attribute not in VALID_ATTRIBUTES:
                raise RuntimeError(f'Invalid attribute {attribute}')
            op_token = self.lookahead()
            if op_token[0] == 'OP':
                operator = self.consume('OP')[1]
                if operator == '=':
                    operator = '=='
            else:
                raise RuntimeError(f'Expected operator, got {op_token[0]}')
            value_token = self.lookahead()
            if value_token[0] == 'NUMBER':
                value = float(self.consume('NUMBER')[1])
            elif value_token[0] == 'STRING':
                value = self.consume('STRING')[1]
                # Remove quotes
                if value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                elif value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
            elif value_token[0] == 'ID':
                # Unquoted string
                value = self.consume('ID')[1]
            else:
                raise RuntimeError(f'Expected value, got {value_token[0]}')
            node = Node(node_type='condition', attribute=attribute, operator=operator, value=value)
            return node
        else:
            raise RuntimeError(f'Expected ID, got {token[0]}')

# Function to create a rule
def create_rule(rule_string):
    tokens = tokenize(rule_string)
    parser = Parser(tokens)
    ast = parser.parse()
    return ast

# Function to optimize and combine multiple rules into a single AST
def combine_rules(rule_strings):
    # Collect all conditions
    condition_map = defaultdict(set)
    operator_nodes = []

    for rule_string in rule_strings:
        ast = create_rule(rule_string)
        extract_conditions(ast, condition_map)
        operator_nodes.append(ast)

    # Build optimized AST
    optimized_ast = build_optimized_ast(condition_map)
    return optimized_ast

def extract_conditions(node, condition_map):
    if node is None:
        return
    if node.node_type == 'condition':
        key = (node.attribute, node.operator, node.value)
        condition_map[key].add(node)
    else:
        extract_conditions(node.left, condition_map)
        extract_conditions(node.right, condition_map)

def build_optimized_ast(condition_map):
    # Remove redundant conditions
    unique_conditions = [list(nodes)[0] for nodes in condition_map.values()]
    # Combine conditions with OR
    if not unique_conditions:
        return None
    node = unique_conditions[0]
    for cond in unique_conditions[1:]:
        node = Node(node_type='operator', operator='OR', left=node, right=cond)
    return node

# Function to evaluate the AST against data
def evaluate_ast(node, data):
    if node.node_type == 'condition':
        attribute = node.attribute
        operator = node.operator
        value = node.value
        data_value = data.get(attribute)
        if data_value is None:
            raise RuntimeError(f'Missing attribute {attribute} in data')
        # Perform the comparison
        try:
            if operator == '==':
                return data_value == value
            elif operator == '!=':
                return data_value != value
            elif operator == '>':
                return data_value > value
            elif operator == '<':
                return data_value < value
            elif operator == '>=':
                return data_value >= value
            elif operator == '<=':
                return data_value <= value
            else:
                raise RuntimeError(f'Unknown operator {operator}')
        except TypeError:
            raise RuntimeError(f'Type mismatch for attribute {attribute}')
    elif node.node_type == 'operator':
        operator = node.operator
        if operator == 'AND':
            return evaluate_ast(node.left, data) and evaluate_ast(node.right, data)
        elif operator == 'OR':
            return evaluate_ast(node.left, data) or evaluate_ast(node.right, data)
        elif operator == 'NOT':
            return not evaluate_ast(node.left, data)
        else:
            raise RuntimeError(f'Unknown operator {operator}')
    else:
        raise RuntimeError(f'Unknown node type {node.node_type}')

# Function to evaluate the rule
def evaluate_rule(ast_json, data):
    # Reconstruct the AST from JSON
    ast = Node.from_dict(ast_json)
    return evaluate_ast(ast, data)

# Database functions
def create_database():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            rule_string TEXT,
            ast_json TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_rule(name, rule_string, ast_json):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO rules (name, rule_string, ast_json) VALUES (?, ?, ?)', (name, rule_string, json.dumps(ast_json)))
    conn.commit()
    conn.close()

def get_rule_by_name(name):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('SELECT rule_string, ast_json FROM rules WHERE name = ?', (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result
    else:
        return None

def get_all_rules():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, rule_string FROM rules')
    result = cursor.fetchall()
    conn.close()
    return result

# Flask API endpoints

@app.route('/')
def index():
    rules = get_all_rules()
    return render_template('index.html', rules=rules)

@app.route('/api/rules', methods=['POST'])
def api_create_rule():
    data = request.json
    rule_string = data.get('rule_string')
    name = data.get('name')
    if not rule_string or not name:
        return jsonify({'error': 'Missing rule_string or name'}), 400
    try:
        ast = create_rule(rule_string)
        ast_json = ast.to_dict()
        store_rule(name, rule_string, ast_json)
        return jsonify({'message': 'Rule created successfully'}), 201
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/rules/combine', methods=['POST'])
def api_combine_rules():
    data = request.json
    rule_names = data.get('rule_names')
    if not rule_names or not isinstance(rule_names, list):
        return jsonify({'error': 'Invalid rule_names'}), 400
    rule_strings = []
    for name in rule_names:
        rule = get_rule_by_name(name)
        if rule:
            rule_strings.append(rule[0])
        else:
            return jsonify({'error': f'Rule {name} not found'}), 404
    try:
        combined_ast = combine_rules(rule_strings)
        combined_ast_json = combined_ast.to_dict()
        return jsonify({'ast_json': combined_ast_json}), 200
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/evaluate', methods=['POST'])
def api_evaluate_rule():
    data = request.json
    ast_json = data.get('ast_json')
    user_data = data.get('user_data')
    if not ast_json or not user_data:
        return jsonify({'error': 'Missing ast_json or user_data'}), 400
    try:
        result = evaluate_rule(ast_json, user_data)
        return jsonify({'eligible': result}), 200
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 400



# Main execution
if __name__ == '__main__':
    create_database()
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
