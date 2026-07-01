# Tinder Automation

A Python automation project built with **Selenium WebDriver** that automates interactions on the TinDog web application. The bot performs the complete login flow using Facebook authentication, handles cookie consent dialogs and pop-ups, and automates profile likes.

## Features

* Automated login to TinDog
* Facebook authentication workflow
* Automatic browser window switching
* Handles cookie consent dialogs
* Handles match pop-ups
* Uses explicit waits for reliable automation
* Scrolls elements into view before interaction
* Modular helper functions for improved readability

## Technologies Used

* Python 3
* Selenium WebDriver
* Google Chrome
* ChromeDriver

## Project Structure

```text
.
├── main.py              # Main automation script
├── requirements.txt     # Project dependencies (optional)
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/Tinder-Automation.git
```

2. Navigate to the project directory:

```bash
cd Tinder-Automation
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, install Selenium manually:

```bash
pip install selenium
```

4. Download a ChromeDriver version compatible with your installed version of Google Chrome, or use Selenium Manager (supported in recent Selenium releases).

## Usage

1. Update the login credentials in the script.

2. Run the program:

```bash
python main.py
```

The automation will:

* Open the TinDog website.
* Log in using Facebook.
* Accept cookie permissions.
* Automatically like profiles.
* Handle match pop-ups when they appear.

## Learning Outcomes

This project demonstrates practical experience with:

* Selenium WebDriver
* Browser automation
* Explicit waits
* Window and tab switching
* Handling dynamic web elements
* Working with pop-ups and dialogs
* CSS Selectors and XPath
* Exception handling in Selenium

## Future Improvements

* Store credentials securely using environment variables
* Add logging for better debugging
* Implement Page Object Model (POM)
* Add configurable number of likes
* Improve handling of unexpected pop-ups
* Support multiple browsers

## Disclaimer

This project was created for **educational purposes** to practice Selenium automation. Ensure that any automation complies with the website's Terms of Service before use.
