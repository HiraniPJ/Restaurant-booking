
# Mint Restaurant Reservation System

## Scope

Click the link to view the live app [Mint Restaurant](https://mint-restaurant-app-e407d965e4db.herokuapp.com/)

Mint Restaurant Reservation System is a web-based application developed to streamline the booking and reservation process for Mint Restaurant. The system allows users to create accounts, book tables, view, edit, or delete their reservations, and manage reservations efficiently. It also provides restaurant administrators the ability to manage available tables.

The project is implemented using the Django framework and includes functionalities such as user authentication, form validation, and reservation management.

------

##Contents
* [About Mint Restaurant](#Introduction) 
* [How To Use It](#how-to-use-it)
* [User Story](#User-Stories)
* [Design](#Design)
* [ERD](#ERD)
* [Wireframes](#Wireframes)
* [Features](#features)
    * [Existing Features](#Existing-Features)
    * [Future Refactor](#Future-Refactor)
    * [Future Features](#future-features)
* [Technologies Used](technologies-used)
* [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [User Story Testing](#user-story-testing)
    * [Validator](#validatiors)
* [Solved Bugs](#solved-bugs)
* [Deployment](#Deployment-Incomplete!!!)
    * [Cloning & Forking](#cloning--forking)
    * [Local Deployment](#local-deployment)
    * [Remote Deployment](#remote-deployment)
    * [Google Sheets](#google-sheet)
* [Credits / Acknowledgements](#credits--acknowledgement)


------
## Project Aims

The goal of the project is to build a fully functioning restaurant booking system that:

- Allow users to create accounts, log in, and manage reservations.
- Provide a user-friendly interface to book tables at a restaurant.
- Enable users to view, edit, and delete their reservations easily.
- Build a scalable and reliable system using Django and PostgreSQL.
- Offer features like responsive design for various devices.
- Ensure the app is secure, with user authentication and data protection.

---------

## How to Use It
Mint Restaurant can be easily used through the following steps:

1. Create an account: Sign up with a username, email, and password to get started.
2. Login: After signing up, log in to access reservation features.
3. Make a reservation: Navigate to the reservation page and choose an available table to book.
4. View your reservations: Check the "My Reservations" page to see a list of your current and upcoming bookings.
5. Edit a reservation: Modify the details of a reservation via the "Edit Reservation" link.
6. Cancel a reservation: Use the "Delete Reservation" button to cancel a reservation.
7. Logout: Logout securely using the link in the navigation bar.

-----
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
## Design

## ERD

## Wireframes
### Home Page
<details> <summary>Click to view</summary> <img src="img_src_link_here" alt="Home Page Wireframe"> </details>

### Reservation Page
<details> <summary>Click to view</summary> <img src="img_src_link_here" alt="Reservation Page Wireframe"> </details>

-------------
## Features
### Existing Features
- **Account Management:** Users can sign up, log in, and log out securely using Django’s authentication system.
- **Make a Reservation:** Users can select a table, choose a date and time, and submit a reservation request.
- **View/Edit/Delete Reservations:** Users can view all their bookings, edit the details, or delete them if they no longer need the reservation.
- **Responsive Design:** The website is fully responsive, offering a seamless experience across mobile, tablet, and desktop devices.

### Future Refactor
- **Reservation Time Validation:** Future updates may include time slot management to avoid overlapping reservations.
- **Profile Management:** Implement a user profile page to allow users to update their contact details and preferences.

### Future Features
- **Notifications:** Implement email notifications for reservation confirmations, changes, and reminders.
- **Admin Panel for Restaurant Owners:** A feature for restaurant owners to view, manage, and approve reservations.
- **Reservation Availability Check:** Add features that allow users to see real-time availability of tables.
---------------

## Technologies Used

- **HTML5:** For structuring the content.
- **CSS3 (Bootstrap):** For styling and layout.
- **Python & Django:** For backend logic and user authentication.
- **PostgreSQL:** For storing reservation data.
- **JavaScript (jQuery):** For client-side interactivity and form validation.
- **Cloudinary:** For managing static files and media (e.g., restaurant images).

----------

## Testing
For detailed information on testing, refer to the Testing.md file.

## Manual Testing
### Home Page
|Test	|Outcome	|Evidence|
|Logo and navigation links work correctly|	Pass|	Clicking the logo redirects to the homepage, navigation links work properly.|
|Reservation form displays correctly on various devices|	Pass|	Tested on different screen sizes, form elements display consistently.|
|User login and logout functionality|	Pass|	Tested the login and logout process for multiple users.|

### Reservation Page
|Test	|Outcome	|Evidence|
|User can submit a valid reservation	|Pass	|Form validation ensures that all required fields are filled before submission.|
|User can edit and delete their reservation|	Pass|	Edit and delete functionality works as expected.|

## User Story Testing
Each user story has been successfully tested. Below are some examples:

User Story: "I want to make a reservation easily."
Result: Pass – Users can make a reservation using the dedicated form, and the booking is stored in the database.

User Story: "I want to log out securely."
Result: Pass – Logout functionality works correctly and redirects the user to the homepage.

## Validators
HTML5: No issues detected.
CSS3: No issues detected with the W3C CSS Validator.
Python (PEP8): Passed with no major issues.
JavaScript (JSHint): All scripts validated successfully.

--------------- 

## Solved Bugs
Cloudinary Image Upload Bug:
Fixed by ensuring request.FILES is correctly handled in the form submission.
Reservation Deletion Bug:
Users were unable to delete reservations due to a missing CSRF token. This was resolved by adding {% csrf_token %} to the delete form.

---------------
## Deployment
### Cloning & Forking
#### Forking the Repository
Navigate to the repository on GitHub.
Click on the "Fork" button in the top right corner.
You will now have a copy of the repository under your GitHub account.

#### Cloning the Repository
Click on the "Code" button.
Copy the repository link (either via HTTPS or SSH).
In your terminal, run git clone <repo-link> to download the repository to your local machine.

## Local Deployment
Clone the repository from GitHub.
Install dependencies by running pip install -r requirements.txt.
Set up a .env file with environment variables like SECRET_KEY, DATABASE_URL, and CLOUDINARY_URL.
Run the Django development server using python manage.py runserver.

## Remote Deployment
Sign in to Heroku and create a new app.
Add the necessary environment variables (SECRET_KEY, DATABASE_URL, CLOUDINARY_URL) to the app’s configuration.
Connect the app to your GitHub repository and deploy it via the Heroku dashboard.

## Credits / Acknowledgements
#### Code References
Django Documentation: Django
Bootstrap Documentation: Bootstrap

#### Media Credits
All icons: Font Awesome
Restaurant banner images: Unsplash

#### Acknowledgements
Special thanks to my mentor and colleagues for their support and guidance during the development of this project.

---------------
## Conclusion

The **Mint Restaurant Reservation System** is a scalable, user-friendly platform for managing table reservations. It was built to streamline the booking process and provide a better experience for both users and restaurant staff. The system has been tested to ensure quality and is flexible for future enhancements such as calendar views, payment integrations, and administrative features.

This project is a foundation that can be expanded as the needs of Mint Restaurant grow.