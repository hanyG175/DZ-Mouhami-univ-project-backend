# Lawyer Hiring Website Backend

This repository contains the backend code for a lawyer hiring website built with Django. It leverages REST APIs to manage lawyer data, appointments, reviews, and categories, and also demonstrates how to scrape data for lawyers and their profiles. The backend integrates with external services (e.g., for geocoding) and is structured for easy extension and maintenance.

---

## Features
- **User Authentication**: Sign up, log in, and log out using custom user models.
- **Lawyers Management**: Create, read, update, and delete lawyers and their detailed profiles.
- **Reviews**: Allow clients to leave reviews for lawyers.
- **Appointments**: Schedule and manage appointments with lawyers.
- **Categories**: Categorize lawyers by their specializations.
- **Location/Coordinates**: Geocode addresses to retrieve latitude and longitude using an external API (Nominatim).

---

## Project Structure


- **authentication**: Handles user authentication logic (e.g., sign up, login, logout).
- **backend**: Could include main settings and configuration for Django.
- **build**: Build artifacts or deployment-related scripts (if any).
- **lawyers**: Contains the Django app for managing lawyer data, views, models, and serializers.
- **media**: Stores uploaded media files (e.g., lawyer profile pictures).
- **scraper**: Contains scripts or modules for scraping lawyer data.
- **source**: Additional source files or utilities.
- **manage.py**: Django’s CLI utility for running server, migrations, etc.
- **Makefile / make.bat**: Automates certain tasks (e.g., running tests, migrations, or server).

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/lawyer-hiring-backend.git
   cd lawyer-hiring-backend
2. **Create and activate a virtual environment (recommended)**:
  ```bash
  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. **Install dependencies:**
   ```pip install django djangorestframework django-filter geopy requests```
4. **Apply migrations:**
   ``python manage.py migrate``
5. Run the development server:
   ``python manage.py runserver``
   The server should be accessible at http://127.0.0.1:8000/.

---

## Usage & Endpoints
Below is a brief overview of the key endpoints defined in lawyers/urls.py. You can interact with these endpoints using tools like Postman or cURL.

### Lawyers

- GET /lawyers/: Retrieve all lawyers.
- POST /lawyers/: Create a new lawyer.
- GET /lawyers/<int:pk>/: Retrieve a specific lawyer by ID.
- PUT /lawyers/<int:pk>/: Update a specific lawyer by ID.
- DELETE /lawyers/<int:pk>/: Delete a specific lawyer by ID.

### Lawyer Profiles

- GET /profiles/: Retrieve all lawyer profiles.
- POST /profiles/: Create a new lawyer profile.
- GET /profile/<int:pk>/: Retrieve a lawyer profile by the associated lawyer ID.
- PUT /profile/<int:pk>/: Update a lawyer profile.
- DELETE /profile/<int:pk>/: Delete a lawyer profile.

### Categories

- GET /categories/: Retrieve all categories.
- POST /categories/: Create a new category.
- GET /categories/<int:pk>/: Retrieve a specific category.
- PUT /categories/<int:pk>/: Update a category.
- DELETE /categories/<int:pk>/: Delete a category.

### Reviews

- GET /lawyers/<int:pk>/reviews/: Retrieve all reviews for a specific lawyer.
- POST /lawyers/<int:pk>/reviews/: Create a review for a lawyer.
- GET /lawyers/<int:pk>/reviews/<review_id>: Retrieve a specific review.
- PUT /lawyers/<int:pk>/reviews/<review_id>: Update a review.
- DELETE /lawyers/<int:pk>/reviews/<review_id>: Delete a review.

### Appointments

- GET /lawyers/<int:pk>/appointments/: Retrieve all appointments for a specific lawyer.
- POST /lawyers/<int:pk>/appointments/: Create an appointment for a lawyer.
- GET /lawyers/<int:pk>/appointments/<app_id>: Retrieve a specific appointment.
- PUT /lawyers/<int:pk>/appointments/<app_id>: Update an appointment.
- DELETE /lawyers/<int:pk>/appointments/<app_id>: Delete an appointment.

### Coordinates

- GET /get_coordinates/?address=<your_address>: Retrieves the latitude and longitude for the given address using the Nominatim API.

### Authentication

- POST /signup/: Register a new client user.
- POST /user_login/: Log in a user with email and password.
- POST /user_logout/: Log out the currently authenticated user.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as you wish.

