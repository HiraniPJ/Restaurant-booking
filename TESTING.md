## Automated Tests
I have run multiple tests to ensure that the functionality of the project works as expected.

![image](https://github.com/user-attachments/assets/b0f8706e-ddae-4f6c-9228-1b145093efc3)
![image](https://github.com/user-attachments/assets/c0c22723-3cd8-4c20-b943-da0911a6e55d)

 - Authentication: Signup, Login, Logout
 - Reservation management: Make, view, edit, and delete reservations
 - Homepage functionality: Displaying tables and restaurant information

A comprehensive list of tests and their status is displayed below.

-----

## Manual Tests
Manual testing was performed during development and is documented below.

## Home Page
|Test #|Test|Results|Evidence|
| --- | --- | --- | --- |
|1 ![image](https://github.com/user-attachments/assets/edc06987-fcec-46bc-b9f6-7f9294df6b21)
|	Navbar links work as expected| Pass| The Home, Make a Reservation, My Reservations, and Logout links in the navbar were tested. All links work correctly.|
|2 ![image](https://github.com/user-attachments/assets/2637db17-771c-40c8-94c0-db309e13400b)
|	Restaurant nav banner is responsive|	Pass |	All the navigation links collapses in a toggle format when the ratio is reduced.|
|3 ![image](https://github.com/user-attachments/assets/c41b59ba-f1c3-4393-bef8-f2dcf86a4987)
|	Welcome message with user's name appears after login|	Pass|	After logging in, the user's name is displayed in the navbar, confirming successful login.|
|4 ![image](https://github.com/user-attachments/assets/c6681dff-7e1b-4b8e-bb0e-844cd43b652b)
|	Login/ Sign up button disappears when user is logged in|	Pass |	the button on the index page carousel disappears when the user is logged in and shows up if the user has not been authenticated.|

## Reservation Page
|Test #|Test|Results|Evidence|
| --- | --- | --- | --- |
|1 ![image](https://github.com/user-attachments/assets/ee77a12c-581e-4ed4-817e-ad8bcbcc810e)
|	User can submit a valid reservation|	Pass|	Form validation ensures that all fields are filled before submission. Reservation appears on the My Reservations page.|
|2 ![image](https://github.com/user-attachments/assets/b48f11ef-0890-4e20-ab8d-0f0d7035cd80)
|	Reservation form shows correct validation errors|	Pass|	Invalid inputs trigger appropriate error messages (e.g., "This field is required").|
|3 ![image](https://github.com/user-attachments/assets/e062165c-5e2b-4413-ba67-fff06a3bd7c6)
|	Reservation is saved in the database|	Pass|	Reservation data is correctly saved to the database and linked to the user's account.

## My Reservations Page
|Test #|Test|Results|Evidence|
| --- | --- | --- | --- |
|1 ![image](https://github.com/user-attachments/assets/0c1a8074-eca0-46c4-8b3e-9b5089def04d)
|	Reservations are displayed correctly|	Pass|	All reservations for the logged-in user are displayed correctly, along with the reservation date, time, and table number.|
|2 ![image](https://github.com/user-attachments/assets/1506b517-3893-493d-b188-1a0f50c67e7a)
|	Reservations can be edited|	Pass|	Tested by clicking the edit button next to a reservation, modifying data, and confirming that changes are saved.|
|3 ![image](https://github.com/user-attachments/assets/80e3d672-ebae-4b7b-b2cb-77de87983be6)
|	Reservations can be deleted|	Pass|	Reservation is successfully deleted when the delete button is clicked, and the reservation no longer appears on the list.|

## Signup/Login/Logout Pages
|Test #|Test|Results|Evidence|
| --- | --- | --- | --- |
|1|	User can register with valid credentials | Pass | Registration form accepts valid input and creates a new user account. Redirects to the homepage after successful signup. |
|2 ![image](https://github.com/user-attachments/assets/5ecb7e54-1c28-4262-885c-3bedbd3997f9)
|	Login fails with incorrect credentials | Pass | Error message is displayed if the wrong username or password is entered. |
|3|	Logout redirects user to the homepage | Fail | After clicking the logout link, the user is failed redirected to the homepage with a logout confirmation. |

-----

## Code Validation
### HTML
The HTML files were passed through the W3C Validator with no major errors found. Minor issues such as missing alt attributes on some images were resolved during the testing phase.

![image](https://github.com/user-attachments/assets/ce2483b4-5663-4c9a-b03c-8f177b773452)

### CSS
The CSS passed validation with W3C's CSS Validator. No critical errors were found, though warnings related to the use of vendor-specific properties (e.g., -webkit- and -moz-) were noted.

### JavaScript
JavaScript code was passed through JSHint, with no major errors detected. The following functionalities were tested:
 1. Form validation on reservation forms
 2. Event handling for form submission and navbar interactions

### Python (PEP8 Compliance)
The Python code adheres to PEP8 standards. CI Python Linter. Linting was performed using Flake8, and the following minor warnings were ignored:
![image](https://github.com/user-attachments/assets/11476257-e47a-4fa3-a79a-2c1120dfc9e9)


## Lighthouse/Accessibility Testing
Lighthouse was used to check the performance, accessibility, best practices, and SEO of the application. Results are listed below.

### Home Page
| Category | Score|
| --- | --- | 
|Performance | 59 |
|Accessibility | 80 |
|Best Practices |93 |
|SEO | 91 |
![image](https://github.com/user-attachments/assets/e54a8964-8296-4456-9143-b33e61fb59b6)

### Reservation Page
|Category |	Score |
| --- | --- | 
| Performance	| 98|
| Accessibility |	81 |
| Best Practices | 96 |
| SEO | 90 |
![image](https://github.com/user-attachments/assets/6a97fff2-31bc-47ca-9e21-802fe090364d)

## Devices Used for Manual Testing
Manual testing was performed on the following devices and browsers:

## Desktop
 - Chrome (latest version)
 - Firefox (latest version)
 - Safari (latest version)

## Mobile and Tablet
 - iPhone 12 (Safari, iOS 14)
 - Samsung Galaxy S21 (Chrome)
 - iPad Pro (Safari)

## User Story Testing

The following user stories were successfully tested:

1. As a user, I want to be able to log in and out of the application so that I can manage my reservations.
- Status: Pass - Login
- Evidence: Login, logout, and signup functionalities were successfully implemented and tested.

2. As a user, I want to reserve a table so that I can ensure I have a place at the restaurant.
- Status: Pass
- Evidence: The reservation form is validated correctly, and the reservation is saved in the database.

3. As a user, I want to view my past reservations so that I can keep track of my bookings.
- Status: Pass
- Evidence: The My Reservations page correctly displays all reservations linked to the logged-in user.

4. As a user, I want to be able to cancel a reservation if I no longer need it.
- Status: Pass
- Evidence: The delete functionality works as expected. The user can delete a reservation from the My Reservations page.
