# Lab 5: Static Code Analysis — Issue Report

## Project: Campus Shuttle Timetable & Fleet Tracker

### Static Analysis Tools
- Pylint
- Bandit
- Flake8

### Issue Table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Code quality / Bug | 11 | The `logs=[]` default list can be shared between function calls. | Change the default to `None` and initialize a new list inside the function. |
| Broad exception handler | Code quality / Bug | 29 | A bare `except:` catches unexpected errors and can hide problems. | Catch only the expected exception types and handle them appropriately. |
| Insecure random generator warning | Security | 35 | Bandit reports that `random.choice()` is not suitable for security-sensitive randomness. | Replace it with a suitable alternative or document why cryptographic randomness is unnecessary for driver assignment. |
| File handling without context managers | Code quality | 39–43 | Files are opened and closed manually, so exceptions could leave files open. | Use `with open(...)` context managers. |
| Incorrect function naming | Code style | 33 | `assignDriver` does not follow the conventional Python snake_case naming style. | Rename it to `assign_driver`. |
| Unused function argument | Code quality | 33 | The `route_id` argument is not used in the function. | Remove the unused argument or use it meaningfully. |
| Missing blank lines | Formatting | Multiple | Flake8 reports E302 and E305 because the required blank lines around functions are missing. | Add the required blank lines. |
| Excessive line length | Formatting | 13 | Flake8 reports E501 because a line exceeds 79 characters. | Split the line or use an f-string with suitable formatting. |
| Missing docstrings | Documentation | Multiple | Pylint reports missing module, function, or method docstrings. | Add concise docstrings describing the purpose of the module and functions. |
| Route lookup after deletion | Functional bug | 55–58 | The program removes route R3 and later attempts to calculate its average, causing a `KeyError`. | Validate route existence before accessing it or change the program flow to avoid accessing a deleted route. |

## Conclusion

Pylint, Bandit, and Flake8 identified code-quality, security, formatting, and functional issues in the original shuttle tracker. The identified issues were addressed, and the tools were rerun to verify the corrections. Pylint achieved a score of 10.00/10, Bandit reported no issues, and Flake8 reported no remaining formatting violations.