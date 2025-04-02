Cloud-Based Storage System
This project is a Cloud-Based Storage System built using Flask (Python) for the backend and SQLite for database management. It provides users with a secure and easy-to-use interface to upload, manage, and retrieve files over the web.

Key Features:
User Authentication: Secure login and access control.

File Management: Upload, download, delete, and preview files.

Encryption & Security: Ensures secure file storage and access.

Database Storage: Uses SQLite to manage user and file metadata.

Logging & Error Handling: Tracks and manages system errors efficiently.

Tech Stack:
•	Backend: Flask (Python), Werkzeug (for security)
•	Database: PostgreSQL, Flask
•	Frontend: HTML, CSS, JavaScript
•	Authentication: OAuth 2.0, JWT (JSON Web Tokens)
•	Security: Flask-Login, encryption modules
•	Storage: Google cloud console

Potential Future Enhancements:
Integration with cloud storage services like AWS S3 or Google Drive.

Enhanced file sharing and collaboration features.

Improved UI/UX using modern frameworks like React or Vue.js.

Conclusion:
This system provides a secure and scalable solution for file storage and management, making it suitable for personal or business use. It serves as a strong foundation for future enhancements, including cloud integration and advanced security measures.

List of commands used to run:

Install Python and Virtual Environment: sudo apt install python3 python3-venv python3-pip -y

Install Required Python Packages: pip install -r requirements.txt

Create and Activate Virtual Environment: python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

Using Flask: export FLASK_APP=app.py   # For Linux/macOS
set FLASK_APP=app.py       # For Windows
flask run

Running the python file: python3 app.py

Tech Expert:
Krison Dmello - www.linkedin.com/in/krison-dmello-5857712aa
Sahitya Gupta - https://www.linkedin.com/in/sahitya-satyendra-gupta-9657311ab
