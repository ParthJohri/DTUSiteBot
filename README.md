# 🚀 DTUSiteBot - A Subject Registration Bot

This is a Python bot that automates the process of subject registration on a website. It uses Selenium WebDriver to interact with the website and perform the registration. The bot reads subject codes and credentials from text files, allowing you to easily registers you for the subject.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ParthJohri/DTUSiteBot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DTUSiteBot
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Update `subjects.txt` file:

   Open the `subjects.txt` file and replace the existing subject codes with your desired subject codes. Each subject code should be on a new line.

2. Update `credentials.txt` file:

   Open the `credentials.txt` file and replace the existing credentials with your own. The file should contain your username on the first line and your password on the second line.

## Usage

1. Make sure you are in the project directory.

2. Run the bot:

   ```bash
   python main.py or python3 main.py
   ```

   The bot will start the subject registration process using the provided subject codes and credentials. It will log any errors or notifications to a log file in the `logs` directory, therefore create a logs folder in the directory.

3. Monitor the bot:

   You can monitor the bot's progress by checking the log file generated in the `logs` directory. The log file will provide information about any errors encountered during the registration process.

4. Customize the bot:

   If you want to modify the behavior of the bot or add additional features, you can edit the `main.py` file. Make sure to test your changes thoroughly before running the bot.

---

Feel free to customize the README file based on your specific requirements or preferences.
