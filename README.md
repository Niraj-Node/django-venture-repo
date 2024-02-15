# Django Venture Repository

Welcome to my Django learning repository where I've documented the steps and concepts I've learned while working on Django Framework.

## Learnings from Calculator App

### 1. Setting up the Project

```python
django-admin startproject myproject
```

### 2. Creating an App

```python
python manage.py startapp calculator
```

In Django, an app is a self-contained module that houses related functionalities. The startapp command is used to create a new app, and in this case, the app is named "calculator." This command creates a directory with the app name and sets up the basic structure for the app.

### 3. Adding the App to Installed Apps & URLs in Main App

- Adding an app to the INSTALLED_APPS list in Django's settings.py file is a crucial step for integrating the app into the project. This informs Django about the existence of the app and enables the use of its functionalities.
- Additionally, to handle the app's URLs, you need to configure both project-level and app-level URL patterns. In the project's urls.py, use the include function to reference the app's URLs, specifying the path where the app's views should be accessible.

This comprehensive approach ensures proper app integration and URL routing within a Django project.

### 4. Defining URLs in App

Edit the calculator/urls.py file to define URL patterns for the calculator app. This involves mapping URLs to views within the app. URL patterns determine how requests are routed to specific views, enabling the app to respond to different endpoints.

### 5. Views and Templates

In calculator/views.py, create functions to handle the application's logic and render templates. Views process incoming requests and return HTTP responses. Templates, typically stored in the templates directory, contain the HTML structure and presentation logic.

### 6. Template Inheritance

Implement template inheritance to enhance code reusability and maintain a consistent look across pages. By creating a base template that contains common elements (header, footer, etc.), other templates can extend this base template. This ensures a uniform structure and appearance throughout the application.

### 7. Using CSS

Create a static folder within the calculator app and add CSS files for styling. By updating the STATICFILES_DIRS in myproject/settings.py, Django is informed about additional locations to look for static files. This allows the inclusion of custom CSS files for styling the web pages.

### 8. Integrating Bootstrap 5 with Django

Bootstrap is an open-source front-end framework developed by Twitter. It is a collection of HTML, CSS, and JavaScript tools and components designed to simplify the process of building responsive and visually appealing web pages.

```bash
pip install django-bootstrap-v5
```

- Add 'bootstrap5' in the INSTALLED_APPS list in settings.py file.

- Add below 3 lines in the <head> section of your html file (the file in which you want to use bootstrap)

1. {% load bootstrap5 %}
2. {% bootstrap_css %}
3. {% bootstrap_javascript %}

## Learnings from Registration App

### 1. Creating a Form in forms.py:

In register_form/forms.py, you define a form using Django's built-in forms module. In Django's forms module, forms.Form is a class that serves as the base class for creating forms. It provides a way to define the structure and behavior of a form in a Python class.

When you create a subclass of forms.Form, you define the fields of the form as attributes of that class. Each attribute represents a form field, and its type determines the type of input the field will accept.

In Django's forms module, CharField, EmailField, ChoiceField, DateField, and TextArea are all classes, not functions. They are predefined field types that you can use to define the structure and validation rules for form fields in your Django application.

### 2. OOP Concepts in forms.py:

- Class: The RegistrationForm class is defined, encapsulating the form's structure and behavior.
  Inheritance: forms.Form is inherited, utilizing Django's form functionalities.
- Encapsulation: Form fields (e.g., username, email, password) are encapsulated within the form class.
- Abstraction: The form class abstracts away the complexities of form processing.
- Composition: Forms can be composed of multiple fields, each serving a specific purpose within the overall registration process.

### 3. Rendering HTML with Form Fields:

Render HTML pages in views with additional data processed from the form.
In your HTML template (register.html), you can access form fields like {{ form.username }}, {{ form.email }}, etc.

## Learning from "model_auth" App

### User Form in Django

- The NewUserForm is a custom form class in Django designed to facilitate the creation of new user accounts with enhanced features. It builds upon the built-in UserCreationForm class from the django.contrib.auth.forms module, extending its functionality to include an email address during user registration.

- The form's Meta class specifies the model to be used (User) and the fields to be included in the form, such as username, email, and password.

#### Custom Save Method:

- The save method first calls the parent class's save method with commit set to False, allowing modifications to the user object before it is saved to the database.
- It retrieves the email value from the cleaned data and assigns it to the user object.
- If commit is set to True, indicating that the form data should be saved to the database, the user object is saved.

- The save method is overridden to ensure that the user's email address is properly stored in the database. If commit is set to True, indicating that the form data should be saved to the database, the user object is saved.

### User Model in Django

- The "model_auth" app leverages the built-in User model provided by Django for handling user authentication and authorization. This model is located in the django.contrib.auth.models module.

- The User model includes several fields designed to store essential user information:

```text
- username: A unique identifier for the user. It must be unique across the system.
- password: Stores the user's password in a secure, hashed format.
- email: An optional field to store the user's email address. While not required, it's commonly used for communication purposes.
- first_name: Stores the user's first name.
- last_name: Stores the user's last name.
- is_active: A boolean field indicating whether the user account is active. Inactive users typically cannot log in.
- is_staff: A boolean field indicating whether the user is a staff member. Staff members usually have access to administrative functions.
- is_superuser: A boolean field indicating whether the user has superuser privileges. Superusers have full access to the system and all its functionalities.
- date_joined: Stores the date and time when the user account was created.
```

### AuthenticationForm Class

The AuthenticationForm class, residing in the django.contrib.auth.forms module, is a crucial component used for handling user authentication.

### Custom Fields Implementation in User Form

For a detailed demonstration of implementing custom fields in a Django user form, you can explore the following GitHub repository:

[User Model with Custom Fields](https://github.com/baxi099/django-lab/tree/main/user_model_with_custom_fields)

## Model Registration and Admin Panel

### Model Registration:

In Django, models are essentially the representation of your application's data structure. Before you can interact with your models through Django's admin interface, you need to register them.

To register a model, navigate to the admin.py file within your Django app directory. Inside this file, you can import your models and then register them using the admin.site.register() method. This allows Django to recognize your models and provide administrative functionalities for them.

```python
# File: admin.py
from django.contrib import admin
from .models import YourModelName

admin.site.register(YourModelName)
```

Admin Panel:
Django provides a powerful built-in admin panel that allows you to manage your application's data easily. Once your models are registered, you can access the admin panel by running your Django server (python manage.py runserver) and navigating to http://localhost:8000/admin in your web browser.

The admin panel allows you to perform various CRUD (Create, Read, Update, Delete) operations on your data without having to write custom views or forms. You can customize the admin panel to suit your application's needs by creating admin classes for your models.

Example of customizing the admin panel:

```python
# File: admin.py
from django.contrib import admin
from .models import YourModelName

class YourModelNameAdmin(admin.ModelAdmin):
list_display = ['field1', 'field2', 'field3'] # Customize displayed fields
search_fields = ['field1', 'field2'] # Add search functionality

admin.site.register(YourModelName, YourModelNameAdmin)
```

Replace field1, field2, etc. with the actual field names of your model.

By customizing the admin panel, you can enhance the usability and efficiency of managing your application's data during development and production stag

## Database Migrations:

Database migrations are essential when making changes to your Django models. They allow you to propagate changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

To create migrations, run the following commands in your terminal.

```bash
python manage.py makemigrations
python manage.py migrate
```

The makemigrations command creates migration files based on the changes detected in your models. The migrate command applies those migrations to the database, making the necessary changes to the schema.

Make sure to run these commands whenever you make changes to your models to keep your database schema synchronized with your Django models.
