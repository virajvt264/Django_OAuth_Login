# Django OAuth Authentication System

A Django-based authentication system that allows users to log in using OAuth providers like Google, GitHub, or other third-party services. This project is ideal for developers looking to implement secure and modern login mechanisms into their Django applications.

## 🚀 Features

- User login via OAuth (e.g., Google)
- Django Allauth integration
- Secure user session management
- Redirects after login/logout
- Supports multiple providers
- Easily extendable

## 🛠️ Tech Stack

- Python 3.x
- Django 3.x/4.x
- Django Allauth
- OAuth (Google/GitHub)
- HTML/CSS (for templates)

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Set up environment variables (e.g., in .env or settings.py):

Add your Google client ID and secret.

OAuth Configuration (Example: Google)
Go to Google Cloud Console

Create a project and set up OAuth consent

Generate OAuth credentials

Add the credentials in settings.py under SOCIALACCOUNT_PROVIDERS

🙋‍♂️ Author
Viraj Tukarul

GitHub: @virajvt264

LinkedIn: https://www.linkedin.com/in/viraj-thukrul/

