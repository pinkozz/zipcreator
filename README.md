# Biggest-number
This is a program that returns the biggest number of a text file

# Table of contents
• [Features](https://github.com/pinkozz/zipcreator#features)

• [Installation](https://github.com/pinkozz/zipcreator#installation)

• [Usage](https://github.com/pinkozz/zipcreator#usage)

• [Contributing](https://github.com/pinkozz/zipcreator#contributing)

• [License](https://github.com/pinkozz/zipcreator#license)

# Features
• Easy-to-use and extendable program

• Makes a zip file

• Makes a compressed version of the entered file inside the zip file

# Installation
1. Clone this repository to your local machine using this command:
   
   ```shell
   git clone https://github.com/pinkozz/zipcreator
   ```
2. Navigate to project folder:
   
   ```shell
   cd zipcreator
   ```
3. Once you have installed the program open the main.py file and change 'YOUR_ZIP_FILENAME.zip' to your own filename:
   
   ```shell
   newZip = zipfile.ZipFile('YOUR_ZIP_FILENAME.zip', 'w')
   ```

4. Then change 'test' to your own file you want to compress (You can test the program by entering 'test.txt'. It is a text file made for this purpose!):

    ```shell
    newZip.write('test', compress_type=zipfile.ZIP_DEFLATED)
    ```

5. Run the program:

   ```shell
   python main.py
   ```

# Usage
Once the program is up and running, it will create a new zip file with compressed file inside it. That zip file will be created and visible in current working directory

# Contributing
Contributions to the zipcreator are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository.
6. Submit a pull request to the main repository.

Please ensure that your contributions align with the project's coding style, guidelines, and licensing.

# License
The zipcreator is open-source software released under the MIT License.

Feel free to customize this guide page based on your specific bot implementation and project requirements.