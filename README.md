# Password Strength Checker

A simple command-line tool that evaluates password strength based on common security criteria.

## What it checks
- Length (8, 12, and 16+ characters)
- Uppercase and lowercase letters
- Numbers and special characters
- Repeated character patterns (e.g. "aaa", "111")
- Common passwords

## How to run

```bash
python3 password_checker.py
```

## Example output

```
Enter a password (or 'q' to quit): hello123

Result: Moderate (4/8)
Tips:
  - Add an uppercase letter
  - Add a special character (!@#$ etc)
```

