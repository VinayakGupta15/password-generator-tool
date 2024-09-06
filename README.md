# Password Generator Tool

## Project Overview

This Password Generator Tool is a Python-based application designed to help users create strong and customizable passwords. The tool allows users to specify the password length and the types of characters (lowercase, uppercase, digits, special characters) they want to include. By providing flexibility in character selection, this tool generates secure and random passwords that meet a variety of security requirements.

### Features

- **Customizable Password Length:** Users can specify the desired length of the password.
- **Character Type Selection:** Users can choose to include lowercase letters, uppercase letters, numbers, and special characters.
- **Random and Secure:** The tool generates a completely random password based on the selected criteria.
- **Interactive User Interface:** The tool interacts with the user through the terminal, making it simple and intuitive to use.
- **Error Handling:** The tool ensures that at least one character type is selected, and raises an error if none are chosen.

## Getting Started

### Prerequisites

- Python 3.x must be installed on your system.

### Installation

1. **Clone the Repository**  
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/VinayakGupta15/password-generator-tool.git
   ```

2. **Navigate to the Project Directory**  
   Move to the project folder where the script is located:
   ```bash
   cd password-generator-tool
   ```

3. **Run the Script**  
   You can run the password generator script using the following command:
   ```bash
   python3 password-generator.py
   ```

## Usage

1. **Start the Script:** When you run the script, you will be prompted to enter the desired length of your password.

2. **Character Preferences:** The script will ask whether you want to include different types of characters (lowercase letters, uppercase letters, digits, and special characters). You can respond with 'y' (yes) or 'n' (no) for each option.

3. **Generated Password:** After you input your preferences, the script will generate and display a secure password based on the provided criteria.

### Example

```bash
Enter the desired password length: 12
Include lowercase letters? (y/n): y
Include uppercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): n
Generated password: aBcD3FgH9Lm2
```
