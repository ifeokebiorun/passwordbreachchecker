# Password Breach Checker

A command-line tool that checks whether a password has appeared in known
data breaches and scores its overall strength.

## How it works

This tool uses the [HaveIBeenPwned Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords),
which implements **k-anonymity** to protect user privacy. Instead of sending
a full password (or even its full hash) to a third party, the tool:

1. Hashes the password locally using SHA-1
2. Sends only the first 5 characters of the hash to the API
3. Receives a list of all breached hashes matching that prefix
4. Checks locally whether the full hash appears in that list

This means the real password — and even the full hash — never leaves your machine.

## Features

- Checks password against billions of breached credentials
- Scores password strength based on length and character variety
- Gives specific suggestions for improving weak passwords

## Usage

\`\`\`
pip3 install requests
python3 checker.py
\`\`\`

## Built with

- Python
- [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3)

## What I learned

- Implementing k-anonymity for privacy-preserving API calls
- Working with hashing (SHA-1) and HTTP requests in Python
- Designing basic security heuristics for password strength
