

## Description
This is a simple Python script that attempts to crack an Instagram account password using brute force or a provided password list.

## Features
- Allows users to specify an Instagram username.
- Supports both brute force and password list modes.
- Flexible character set and password length options.
- Saves found passwords to a file for future reference.
- Provides elapsed time for the cracking process.

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the script using Python: `InstaSneak.py`.
4. Follow the on-screen prompts to input the Instagram username and choose the cracking mode.
5. If using a password list, specify the path to the password list file.
6. Wait for the script to crack the password. If found, it will be displayed on the screen and saved to a file.

## Example
```bash
$ python InstaSneak.py
Enter the Instagram username: example_user
Do you want to use a password list? (yes/no): yes
Enter the path to the password list file: passwords.txt

=========================================
|        InstaSneak Password Cracker    |
=========================================

Cracking...
=======================================
Password found: 123456
=======================================
Elapsed time: 10.53 seconds
