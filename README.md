# FC Hwasung Player Management System

A web application built with Django for managing football club players, including registration, authentication, and search functionalities.

## Features

- **User Authentication**:  
  - Login/Logout functionality with Django-admin integration.  
  - Redirects to login page if unauthorized access is attempted (e.g., incognito mode).  
- **Player Registration**:  
  - Form to register players with fields for name, nationality, position, mobile number, and date of birth.  
  - Dropdown selections for nationality and position.  
- **Search Functionality**:  
  - Search players by name, mobile number, position, nationality, or date of birth.  
- **About Page**:  
  - Displays club history and social media links (Instagram, Facebook, YouTube).  
  - Collapsible accordion sections for detailed club information.  
- **Responsive Design**:  
  - Built using Bootstrap and Font Awesome for modern styling and icons.  

## Technologies Used

- **Backend**: Python 3, Django  
- **Frontend**: Bootstrap, Font Awesome  
- **Tools**: PyCharm (IDE), GitHub (version control)  

## Installation

1. **Clone the repository**:  
   ```bash
   git clone [repository-url]
   cd project-directory

  Set up a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:

bash
pip install -r requirements.txt
Run migrations:

bash
python manage.py migrate
Start the development server:

bash
python manage.py runserver

Usage
Login Page:

Access the login page at http://localhost:8000/login.

Enter admin-created credentials (Figure 1).

Invalid credentials show "Permission Denied" (Figure 3).

Home/Register Page:

After login, users can register players via a form with dropdowns and a date picker (Figure 6, 16-17).

Search Page:

Use the navbar to search players by criteria (Figure 10, 19-21).

About Page:

View club details and social media links (Figure 7-8, 18).

Logout:

Click the logout button to return to the login page (Figure 5)

# Acknowledgments
Bootstrap: For responsive design templates.

Font Awesome: For icons used in the About page.

Django Community: For documentation and support.
