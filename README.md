# Certify

This project is a certificate database platform built with Django. It allows users to store certificate information and verify the authenticity of certificates using a JSON hash stored in the Ethereum Goerli blockchain.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation
1 Clone the repository:

`git clone https://github.com/ed0bus/Certify.git`


2 Change into the project directory:

`cd your-project/`

3 Set up a virtual environment:

`python -m venv env`

Activate the virtual environment:

On Windows:

`.\env\Scripts\activate`

On macOS/Linux:

`source env/bin/activate`

Install the project dependencies:

`pip install -r requirements.txt`

Perform any additional setup steps, such as configuring the Ethereum blockchain testnet connection details in the project settings (you can use Infura or Alchemy to properly connect to an external node).

## Usage

1. Start the development server:

`python manage.py runserver`


2. Open your web browser and visit `http://localhost:8000` to access the certificate database platform.

3. Use the platform to store and manage certificates. The platform allows users to view existing certificates and search for certificates using a query parameter.

4. To verify the authenticity of a certificate, enter the corresponding hash in the search bar and submit the form. The platform will check if the certificate hash exists in the Ethereum Goerli blockchain and provide the verification result.

## Features

- Store and manage certificates in a database.
- Verify the authenticity of certificates using a JSON hash stored in the Ethereum blockchain testnet.

## Contributing

Contributions are welcome! If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push the branch to your forked repository: `git push origin feature/your-feature-name`
5. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License.

---

Feel free to modify and customize this README according to your project's specific details and requirements. Include any additional information or instructions that would be helpful for others using or contributing to your certificate database platform.

If you have any further questions or need more specific guidance, feel free to ask!