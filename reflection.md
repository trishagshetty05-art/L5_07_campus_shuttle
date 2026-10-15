# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security weaknesses, code-quality problems, and formatting violations.

## 2. What did Pylint, Bandit, and Flake8 identify?

Pylint identified code-quality issues, including a mutable default argument, a broad exception handler, missing docstrings, and incorrect naming conventions. Bandit flagged the use of Python's standard pseudo-random generator. Flake8 identified formatting issues, including missing blank lines and an excessively long line.

## 3. How did static analysis improve the program?

Static analysis helped identify problems that could affect maintainability and reliability. The findings also highlighted the importance of proper exception handling, file management, documentation, and consistent coding style.

## 4. What did you learn from this lab?

I learned how to run Pylint, Bandit, and Flake8, interpret their reports, document findings, and use those findings to improve code quality and security. I also learned that static analysis can detect potential issues without executing the program. After correcting the identified issues, I reran the tools and verified that Pylint achieved a score of 10/10, Bandit reported no issues, and Flake8 reported no remaining formatting violations.
