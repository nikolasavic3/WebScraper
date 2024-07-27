# WebScraper

## Description
This is a Python-based web scraping script designed to extract various information from websites, including links, email addresses, host references, and image counts.

## Features
- Extracts all href links from the webpage
- Finds and lists email addresses
- Counts references to different hosts
- Counts the number of images on the webpage
- User-friendly command-line interface

## Requirements
- Python 3.x
- Standard Python libraries (no external dependencies required):
  - urllib
  - re

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/nikolasavic3/WebScraper.git
   ```
2. Navigate to the project directory:
   ```
   cd WebScraper
   ```

## Usage
Run the script using Python:
```
python webscraper.py
```
When prompted, enter the URL of the website you want to scrape (without 'https://'). For example:
```
Enter the url of website you want to access:
www.example.com
```

## Output
The script will print the following information to the console:
- List of all href links found on the page
- List of email addresses found on the page
- Number of references to each host
- Total number of images on the page

## Limitations
- The script assumes 'https://' protocol for all URLs
- May not handle complex webpage structures or dynamically loaded content
- Does not follow links or scrape multiple pages

## Future Improvements
- Add support for 'http://' protocol
- Implement deeper crawling to follow links
- Export results to a file for easier analysis
- Add error handling for invalid URLs or connection issues

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Disclaimer
This tool is for educational purposes only. Be sure to read and comply with the terms of service of any website you scrape. Respect robots.txt files and implement appropriate rate limiting to avoid overloading servers.
