# Tkinter Pwncheck

A simple Tkinter-based Python 3 GUI for the [haveibeenpwned.com](haveibeenpwned.com) Pwned Passwords API. Lets you input a password and query if it has been exposed in data breaches. Useful if you don't feel comfortable typing all your sensitive passwords into a random web page to check if they're unsafe.

[Only the first 5 characters of the SHA-1 hash of the password](https://haveibeenpwned.com/API/v2#SearchingPwnedPasswordsByRange) are sent to the API, so your password never leaves your computer.

## Usage

Run pwnceck.py with a Python 3 interpreter, e.g.
`python pcheck.py`. You might need to install Tkinter for your environment (on Ubuntu or similar, `sudo apt install python3-tk`).

## License

This program is licensed under the MIT license.

The data by haveibeenpwned.com is licensed under CC-BY-4.0.
