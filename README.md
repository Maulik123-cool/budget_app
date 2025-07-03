# budget_app
Budget Buddy is an easy-to-use app that helps you keep track of your money. You can quickly add your income and expenses, organize them by category, and see all your transactions in one place. It’s like having a personal assistant that helps you save smarter and spend wiser

![image](https://github.com/user-attachments/assets/3e4ddd3f-044c-4e43-941b-e87ae1c90fa6)
![image](https://github.com/user-attachments/assets/89b85751-7001-4e2a-bdde-552c75f9242a)
![image](https://github.com/user-attachments/assets/3c5a43a9-a254-4c90-a383-9a2cea7a2d74)

# IMPORTANT 
always remmber to put the code into vs code and go to http://127.0.0.1:5000/dashboard the you can play the app the code should be running into vs code

## Features

- Add income and expenses with description, amount, type, and category  
- View a list of all your transactions  
- Simple and clean user interface  
- Easy to run locally on your computer

## How to Run Locally

### Prerequisites

- Python installed ([Download here](https://www.python.org/downloads/))  
- Basic command line knowledge  

### Steps

1. Download or clone this repository.  
2. Open your terminal or PowerShell and navigate to the project folder:

# Demo link 
1. Click the demo link
2. then copy and paste in the browser for the app to be downloaded and working 

 # How It Works

- You open the app in your browser.
- The homepage welcomes you and gives a button to enter the dashboard.
- On the dashboard, you fill out a form to add a new transaction:
  - **Description** (e.g., "Groceries", "Salary")
  - **Amount** (how much money)
  - **Type** (Income or Expense)
  - **Category** (e.g., Food, Rent, Entertainment)
- When you submit, the app saves the data into a small database.
- Below the form, you see a list of all your past transactions with details.
- This way, you can easily monitor your cash flow and spending habits.

# Technologies Used

- **Python**: For the backend logic using the Flask framework.
- **Flask**: A lightweight web framework to create routes, handle requests, and render HTML pages.
- **SQLite**: A simple database to store transactions in a file locally.
- **HTML & CSS**: To create the user interface, forms, and style the pages.
- **Jinja2 Templates**: Flask’s built-in templating engine to dynamically generate HTML based on data.

# How It Works Under the Hood

- When you start the app (`python app.py`), Flask creates the web server.
- The app checks for a database and creates the transactions table if it doesn’t exist.
- When you visit `/`, it shows the homepage.
- When you visit `/dashboard`, the app fetches all transactions from the database and shows them.
- When you submit the form on `/dashboard`, Flask receives the data, inserts it into the database, then reloads the page with updated data.
- The template engine fills the transaction list dynamically every time.

 # Future Ideas

- Add user login for personal accounts.
- Show spending charts with JavaScript libraries like Chart.js.
- Set monthly saving goals with alerts.
- Add the ability to edit or delete transactions.
- Responsive design for mobile use.
