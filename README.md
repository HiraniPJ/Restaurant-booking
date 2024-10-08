
# Mint Restaurant Reservation System

## Scope

Mint Restaurant Reservation System is a web-based application developed to streamline the booking and reservation process for Mint Restaurant. The system allows users to create accounts, book tables, view, edit, or delete their reservations, and manage reservations efficiently. It also provides restaurant administrators the ability to manage available tables.

The project is implemented using the Django framework and includes functionalities such as user authentication, form validation, and reservation management.

------

## Project Aims

The goal of the project is to build a fully functioning restaurant booking system that:

  1. Allows users to create accounts.
  2. Enables users to book, view, edit, and cancel reservations.
  3. Prevents double booking for the same table at the same time.
  4. Provides an admin interface to manage the restaurant bookings.
  5. Is easily extendable for future features, such as adding payment options or special requests.

---------

## User Stories & Epics

### Epic 1: User Account Management
- As a user, I want to create an account, so I can manage my reservations.
- As a user, I want to log in and log out of my account, so my information remains private and secure.
- As a user, I want to receive validation messages if I make a mistake during signup, so I can correct the issues.

### Epic 2: Reservation System
- As a user, I want to view available tables and book one for a specific date and time, so I can ensure my spot at the restaurant.
- As a user, I want to view a summary of all my bookings, so I can keep track of my reservations.
- As a user, I want to edit or cancel my reservations, so I can make adjustments if my plans change.
- As a user, I want to receive validation messages if I make a mistake while booking, so I can correct the issues before submission.

### Epic 3: Admin Table Management
- As an admin, I want to manage the available tables (add, edit, or delete tables), so I can control the table availability for the restaurant.
- As an admin, I want to view all reservations, so I can manage customer bookings.

### Epic 4: Form Validation
- As a user, I want to be informed when required fields are missing, so I know what needs to be corrected.
- As an admin, I want the form to reject invalid data (e.g., negative guests), so that bookings are made properly.

### Epic 5: Testing and Quality Assurance
- As a developer, I want unit tests to verify the functionality of the app, so that any future changes can be validated.
- As a developer, I want to ensure coverage for critical functions such as user signup, login, and reservation processes.

-----------

## Technologies Used

  1. **Django:** The main web framework used for building the backend and managing the database.
  2. **PostgreSQL:** The database system used for storing reservations and user data.
  3. **HTML5 & CSS3:** Used for structuring and styling the frontend.
  4. **Bootstrap:** Used to create a responsive and mobile-friendly interface.
  5. **Python:** The programming language used for the backend.
  6. **Gunicorn:** WSGI HTTP server used for deployment.
  7. **Heroku:** Cloud platform used for deployment.
  8. **Git:** For version control and code collaboration.
  9. **Gitpod:** An online integrated development environment (IDE) for development.
  10. **GitHub:** For managing the project repository and tracking issues with GitHub Issues.

----------

## Conclusion

The **Mint Restaurant Reservation System** is a scalable, user-friendly platform for managing table reservations. It was built to streamline the booking process and provide a better experience for both users and restaurant staff. The system has been tested to ensure quality and is flexible for future enhancements such as calendar views, payment integrations, and administrative features.

This project is a foundation that can be expanded as the needs of Mint Restaurant grow.