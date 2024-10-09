## Automated Tests
I have run multiple tests to ensure that the functionality of the project works as expected.

Ran 22 tests with 2 failures and 0 errors.
These tests cover key views such as:

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
|1|	Navbar links work as expected| Pass| The Home, Make a Reservation, My Reservations, and Logout links in the navbar were tested. All links work correctly.|
|2|	Restaurant banner image is responsive|	Pass|	Banner image tested on multiple screen sizes. It maintains its aspect ratio and is displayed correctly.|
|3|	Welcome message with user's name appears after login|	Pass|	After logging in, the user's name is displayed in the navbar, confirming successful login.|
|4|	Footer links work as expected|	Pass|	Social media links in the footer navigate to external pages as expected.|

## Reservation Page
|Test #|Test|Results|Evidence|
| --- | --- | --- | --- |
|1|	User can submit a valid reservation|	Pass|	Form validation ensures that all fields are filled before submission. Reservation appears on the My Reservations page.|
|2|	Reservation form shows correct validation errors|	Pass|	Invalid inputs trigger appropriate error messages (e.g., "This field is required").|
|3|	Reservation is saved in the database|	Pass|	Reservation data is correctly saved to the database and linked to the user's account.

## My Reservations Page
|Test #|Test|Results|Evidence|
| --- | --- | --- | --- |
|1|	Reservations are displayed correctly|	Pass|	All reservations for the logged-in user are displayed correctly, along with the reservation date, time, and table number.|
|2|	Reservations can be edited|	Pass|	Tested by clicking the edit button next to a reservation, modifying data, and confirming that changes are saved.|
|3|	Reservations can be deleted|	Pass|	Reservation is successfully deleted when the delete button is clicked, and the reservation no longer appears on the list.|

## Signup/Login/Logout Pages
|Test #|Test|Results|Evidence|
| --- | --- | --- | --- |
|1|	User can register with valid credentials | Pass | Registration form accepts valid input and creates a new user account. Redirects to the homepage after successful signup. |
|2|	Login fails with incorrect credentials | Pass | Error message is displayed if the wrong username or password is entered. |
|3|	Logout redirects user to the homepage | Pass | After clicking the logout link, the user is redirected to the homepage with a logout confirmation. |

-----

## Code Validation
### HTML
The HTML files were passed through the W3C Validator with no major errors found. Minor issues such as missing alt attributes on some images were resolved during the testing phase.

### CSS
The CSS passed validation with W3C's CSS Validator. No critical errors were found, though warnings related to the use of vendor-specific properties (e.g., -webkit- and -moz-) were noted.

### JavaScript
JavaScript code was passed through JSHint, with no major errors detected. The following functionalities were tested:
 1. Form validation on reservation forms
 2. Event handling for form submission and navbar interactions

### Python (PEP8 Compliance)
The Python code adheres to PEP8 standards. Linting was performed using Flake8, and the following minor warnings were ignored:
 - Lines exceeding 80 characters (handled via line breaks)
 - Unused variables (reserved for potential future features)

## Lighthouse/Accessibility Testing
Lighthouse was used to check the performance, accessibility, best practices, and SEO of the application. Results are listed below.

### Home Page
| Category | Score|
| --- | --- | 
|Performance | 90 |
|Accessibility | 98 |
|Best Practices | 95 |
|SEO | 100
### Reservation Page
|Category |	Score |
| --- | --- | 
| Performance	| 85 |
| Accessibility |	100 |
| Best Practices | 90 |
| SEO | 95 |

#### Screenshots from Lighthouse results:

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
- Status: Pass
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
