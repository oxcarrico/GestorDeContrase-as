# Secure Password Generator

This Python script generates secure passwords that meet the following criteria:

- Length: 20 characters.
- Contains at least one uppercase letter, one lowercase letter, and three digits.

The script stores the generated passwords in a text file (`contraseñas.txt`) and allows the user to view all stored passwords.

## How It Works

1. **Password Generation**: 
   - The password is randomly generated using letters (uppercase and lowercase) and digits.
   - The password must contain at least one lowercase letter, one uppercase letter, and at least three digits.

2. **File Storage**: 
   - Each generated password is appended to the file `contraseñas.txt`.
   - After a password is generated, the script reads and displays all saved passwords from the file.

