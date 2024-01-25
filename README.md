# Django Venture Repository

Welcome to my Django learning repository where I've documented the steps and concepts I've learned while working on Django Framework.

## Learnings from Calculator App

### 1. Setting up the Project

```bash
django-admin startproject myproject
```

### 2. Creating an App

```bash
python manage.py startapp calculator
```

In Django, an app is a self-contained module that houses related functionalities. The startapp command is used to create a new app, and in this case, the app is named "calculator." This command creates a directory with the app name and sets up the basic structure for the app.

### 3. Adding the App to Installed Apps & URLs in Main App

Adding an app to the INSTALLED_APPS list in Django's settings.py file is a crucial step for integrating the app into the project. This informs Django about the existence of the app and enables the use of its functionalities. Additionally, to handle the app's URLs, you need to configure both project-level and app-level URL patterns. In the project's urls.py, use the include function to reference the app's URLs, specifying the path where the app's views should be accessible. This comprehensive approach ensures proper app integration and URL routing within a Django project.

### 4. Defining URLs in App

Edit the calculator/urls.py file to define URL patterns for the calculator app. This involves mapping URLs to views within the app. URL patterns determine how requests are routed to specific views, enabling the app to respond to different endpoints.

### 5. Views and Templates

In calculator/views.py, create functions to handle the application's logic and render templates. Views process incoming requests and return HTTP responses. Templates, typically stored in the templates directory, contain the HTML structure and presentation logic.

### 6. Using CSS

Create a static folder within the calculator app and add CSS files for styling. By updating the STATICFILES_DIRS in myproject/settings.py, Django is informed about additional locations to look for static files. This allows the inclusion of custom CSS files for styling the web pages.

### 7. Template Inheritance

Implement template inheritance to enhance code reusability and maintain a consistent look across pages. By creating a base template that contains common elements (header, footer, etc.), other templates can extend this base template. This ensures a uniform structure and appearance throughout the application.

## Learnings from Registration App

### 1. Creating a Form in forms.py:

In register_app/forms.py, you define a form using Django's built-in forms module.

### 2. OOP Concepts in forms.py:

Class: The RegistrationForm class is defined, encapsulating the form's structure and behavior.
Inheritance: forms.Form is inherited, utilizing Django's form functionalities.
Encapsulation: Form fields (e.g., username, email, password) are encapsulated within the form class.
Abstraction: The form class abstracts away the complexities of form processing.
Composition: Forms can be composed of multiple fields, each serving a specific purpose within the overall registration process.

### 3. Handling Forms in Views:

In register_app/views.py, you handle user input and validation.

### 4. Rendering HTML with Data:

Render HTML pages in views with additional data processed from the form.
In your HTML template (registration/register.html), you can access form fields like {{ form.username }}, {{ form.email }}, etc.
