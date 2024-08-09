# JobScraper Flask App

A Flask web application that scrapes job listings from RemoteOK and Wanted.co.kr based on a keyword search. The application provides the ability to search for jobs by keyword (specific language or framework), view results, and export them to a CSV file.

## Features

- **Search for Jobs:** Enter a keyword to search for relevant job listings.
- **View Job Listings:** See job details - title, company, location, reward, and a direct link to apply.
- **Export Results:** Export search results to a CSV file.

## Requirements

- Python 3.10 or later
- Playwright (for dynamic scraping)
- BeautifulSoup (for parsing HTML)
- Flask (for the web application)
- Requests (for making HTTP requests)

## Installation

1. Clone the repository:

   git clone https://github.com/username/JobScraper.git
   cd JobScraper

2. Set up a virtual environment and install dependencies:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt

3. Set up Playwright:

    playwright install

## Usage

1. Run the Flask app:
    python main.py

2. Open your browser, enter a keyword to search for jobs.

3. View the search results and export them to a CSV file if desired.
