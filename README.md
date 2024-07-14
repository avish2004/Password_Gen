# Password Generator

This repository contains a Python script for generating strong passwords. The generated passwords include a mix of uppercase and lowercase letters, digits, and special characters, ensuring a high level of security.

## Features

- Generates a strong password of a specified length (default is 12 characters).
- Ensures the password contains at least one special character.
- Ensures the password contains at least two digits.
- Utilizes the `secrets` module for secure random password generation.

## Installation

To run the script, you need to have Python installed on your system. This script is compatible with Python 3.x.

## Usage

You can use the script directly from the command line or integrate it into your own projects. 

### Command Line

1. Clone the repository:

```bash
git clone https://github.com/yourusername/password-generator.git            (enter your username instead of yourusername)
cd password-generator

2. Run the script:
```bash
python create_pw.py


### Integration
You can also import the `create_pw` function into your own projects:
from create_pw import create_pw

# Generate a password with the default length of 12 characters
password = create_pw()
print(password)

# Generate a password with a custom length
custom_length_password = create_pw(pw_length=16)
print(custom_length_password)

## Customization
You can customize the length of the password by passing the desired length as an argument to the `create_pw` function:
create_pw(pw_length=16)


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact me at adityaavishwakarma@gmail.com.
