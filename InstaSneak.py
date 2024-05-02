import itertools
import requests
import time

def generate_passwords(characters, length):
    return (''.join(candidate)
            for candidate in itertools.product(characters, repeat=length))

def check_password(username, password):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    return response.status_code == 200

def load_password_list(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def save_password_found(password):
    with open("passwords_found.txt", "a") as file:
        file.write(password + "\n")

def main():
    print("=========================================")
    print("|        InstaSneak Password Cracker    |")
    print("=========================================")
    print()

    username = input("Enter the Instagram username: ")
    use_password_list = input("Do you want to use a password list? (yes/no): ").lower()

    if use_password_list == 'yes':
        password_list_file = input("Enter the path to the password list file: ")
        passwords = load_password_list(password_list_file)
    else:
        character_set = input("Enter the character set to use for passwords (e.g., abc123): ")
        password_length = int(input("Enter the password length: "))
        passwords = generate_passwords(character_set, password_length)

    print("\nCracking...")
    print("=======================================")
    
    start_time = time.time()

    found = False
    for password in passwords:
        if check_password(username, password):
            print(f"Password found: {password}")
            save_password_found(password)
            found = True
            break

    if not found:
        print("Password not found in the list.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("=======================================")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
