# nayepankh-volunteer-management system
A web-based Volunteer Management System developed for NayePankh Foundation to simplify volunteer registration and administration.

## Overview
This application enables volunteers to register for social initiatives while providing administrators with a secure dashboard to manage and monitor volunteer data.
The project was built as part of the internship assignment for NayePankh Foundation.

## Features
* Volunteer registration form
* Duplicate email validation
* Admin login and logout functionality
* Session-based authentication
* Protected admin dashboard
* View all registered volunteers
* Search volunteers by name, city, or skills
* Dashboard statistics
* Flash messages for successful actions and errors
* Responsive user interface
* Active navigation bar highlighting the current page

## Tech Stack
### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Backend
* Python
* Flask

### Database
* MySQL
* MySQL Connector for Python

## Project Structure
```text
nayepankh-volunteer-management/
│
|-- app.py
|-- database.py
|-- database.sql
|-- requirements.txt
|-- README.md
│
|-- static/
│   |-- style.css
│
|-- templates/
    |-- home.html
    |-- about.html
    |-- register.html
    |-- admin_login.html
    |-- dashboard.html
    |-- volunteers.html
```

## Installation and Setup
### 1. Clone the repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/nayepankh-volunteer-management.git
```

### 2. Navigate to the project directory
```bash
cd nayepankh-volunteer-management
```

### 3. Create a virtual environment (optional)
```bash
python -m venv venv
```

Activate the virtual environment:
#### Windows
```bash
venv\Scripts\activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure the database
* Create a MySQL database named:

```text
nayepankh_db
```

* Import and execute the queries provided in `database.sql`.
* Update the database credentials in `database.py`:
```python
host = "localhost"
user = "your_mysql_username"
password = "your_mysql_password"
database = "nayepankh_db"
```

### 6. Run the application
```bash
python app.py
```

Open your browser and visit:
```text
http://127.0.0.1:5000
```

## Admin Access
Create an admin record in the database before logging in.

Example:
```sql
INSERT INTO admins (username, password)
VALUES ('admin', 'admin123');
```

## Security Notes

* Do not store real database credentials in public repositories.
* Keep sensitive information inside environment variables or a `.env` file.

## Future Improvements
* Password hashing using bcrypt
* Role-based access control
* Email notifications
* Volunteer profile management
* Data export to CSV or Excel
* Analytics dashboard with charts

## Author
**Aryan Chaudhary**

## License
This project was created for educational and internship evaluation purposes.
