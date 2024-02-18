# goit-algo-hw-02

This repository contains Python code for two tasks:

1. Request Handling System Simulation
2. Palindrome Checker Function

## Task 1: Request Handling System Simulation

### Description
This task involves simulating a request handling system where requests are generated automatically and processed sequentially, mimicking the operation of a service center.

### Implementation
The Python code utilizes a queue data structure (`Queue` from the `queue` module) to manage the requests. Two main functions are implemented:
- `generate_request()`: Generates new requests and adds them to the queue.
- `process_request()`: Processes requests by removing them from the queue.

The main program continuously executes these functions, simulating a continuous flow of new requests and their processing.

## Task 2: Palindrome Checker Function

### Description
The second task involves developing a function that takes a string as input, adds its characters to a deque data structure (`deque` from the `collections` module), and then compares characters from both ends of the deque to determine if the string is a palindrome.

### Implementation
The Python function `is_palindrome()` converts the input string to lowercase and removes spaces to ensure case insensitivity and handling of whitespace. It then creates a deque from the characters of the string and compares characters from both ends until the deque has one or no characters left. If all characters match, the function returns `True`, indicating that the input string is a palindrome; otherwise, it returns `False`.

## Usage
To use these functionalities:
1. Ensure you have Python installed on your system.
2. Copy the provided code snippets into your Python environment or files.
3. Call the appropriate functions (`generate_request()` and `process_request()` for Task 1, `is_palindrome()` for Task 2) with suitable input parameters.


