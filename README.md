# Even Odd Checker

A simple Flask web application that checks whether a given number is even or odd.

## Description

Even Odd Checker is a minimalist web application built with Flask that allows users to input a number and instantly determine if it's even or odd. The application features a clean, modern UI with a responsive design.

## Features

- Clean and intuitive user interface
- Real-time number validation (accepts only numeric input)
- Instant even/odd determination
- Responsive design with custom styling
- Runs locally on port 5001

## Project Structure

```
Even Odd Checker/
├── app.py                 # Main Flask application
├── README.md              # This file
├── static/
│   ├── style.css          # Stylesheet for the application
│   └── images/            # Image assets (favicon, logo)
└── templates/
    └── index.html         # HTML template for the web page
```

## Installation

1. **Clone or download the project folder**

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install flask
   ```

## Running the Application

1. Activate the virtual environment (if you created one):

   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:5001
   ```

## Usage

1. Enter any number in the input field
2. Click the "Check" button
3. The application will display whether the number is even or odd

## Technologies Used

- **Python 3** - Backend programming language
- **Flask** - Python web framework
- **HTML5** - Markup language for web pages
- **CSS3** - Styling and layout

## Dependencies

- Flask - Web framework for Python

Install with: `pip install flask`

## Author

Created as a simple demonstration of Flask web application development.

## License

This project is open source and available under the MIT License.
