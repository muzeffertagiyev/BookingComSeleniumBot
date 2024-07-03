# Booking.com Selenium Bot

## Overview

This project is a Selenium bot that automates the process of searching for hotels on Booking.com, applying filters, sorting the results, and sending a detailed report via email. The bot is capable of selecting the destination, dates, and number of adults, applying star rating filters, sorting results by price (lowest first), and then generating a report of the hotel options. This report includes the hotel's name, price, score, and a direct link to the hotel page.

## Features

- **Automated Hotel Search**: Input destination, check-in/check-out dates, and number of adults.
- **Filters and Sorting**: Apply star rating filters and sort results by price (lowest first).
- **Detailed Report**: Generate and send an email report with hotel details including name, price, score, and link.
- **Pop-up Handling**: Automatically dismisses cookie and login pop-ups.
- **Customizable Currency**: Change the currency for displayed prices.

## Demo Video
 
https://github.com/muzeffertagiyev/BOOKING_COM_SELENIUM_BOT/assets/75939608/9ddf78ae-d36d-46a3-841b-2398f6c0d988




## Usage

1. **Run the Bot**
    ```bash
    python run.py
    ```

2. **Follow the Prompts**
    - Enter the city name.
    - Enter check-in and check-out dates (format: yyyy-mm-dd).
    - Enter the number of adults.
    - Enter your email address to receive the report.

3. **Example Interaction**
    ```bash
    Where do you go? (city name): New York
    Check in date(yyyy-mm-dd): 2024-07-21
    Check out date(yyyy-mm-dd): 2024-07-24
    Number of people: 2
    Please add your email: example@example.com
    ```

## Project Structure

- `booking_filtration.py`: Contains the `BookingFiltration` class for applying filters and sorting results.
- `booking_report.py`: Contains the `BookingReport` class for extracting hotel details and preparing the report.
- `booking.py`: Contains the main `Booking` class for handling the overall automation workflow.
- `constants.py`: Stores constant values such as the base URL.
- `mail.py`: Contains the `EmailSend` class for sending the email report.
- `run.py`: The entry point of the bot, handles user interaction and runs the automation.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.


## Contact

For any inquiries or issues, please contact me via:
- [LinkedIn](https://www.linkedin.com/in/muzaffar-taghiyev/)
- Email: muzaffar.taghiyev@gmail.com



