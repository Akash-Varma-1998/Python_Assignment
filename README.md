# Python_Assignment
Python Assignment | Test Assignment Using Python-Django MVT
<!-- Brief description of My Project. -->

<!-- Table of Contents :  -->
    - Project Overview
    - Installation

<!-- Project Overview -->
    "Purpose"
    
  The purpose of this project is to create a web application for managing a blog platform. The platform allows users to view all blogs and also provides functionality for registered users to create, update, and delete their own blogs.

    "Key Features"
    
  User Authentication: 
    Users can register, log in, and log out securely.

  Blog Management:
    Admin Panel: An admin user can manage all blogs, including creating, updating, and deleting any blog posts.
    User-specific Blogs: Registered users can create, update, and delete their own blog posts. They can only manage their own content.

  Blog Viewing:
    All Blogs: Users (both registered and non-registered) can view all blog posts on the platform.
    User-specific Blogs: Registered users can also view their own blogs separately from the main blog listing

  Technologies Used:
    Django: Framework for building the web application and managing data using MVT.
    HTML/CSS/JavaScript: For Development for user interface and interactions.
    SQLite: Database management for storing blog posts and user information.
    Django Templates: Render dynamic content and display blog posts on the frontend.
    Django Forms/Bootstrap: Handle form submissions for creating and updating blog posts.
    User Authentication: Utilize Django's built-in authentication system for user registration, login, and logout functionalities.

  Project Structure:
    Models: Define models for blog posts and user profiles.
    Views: Implement views for rendering blog posts, user-specific content, and admin functionalities.
    Templates: Create HTML templates for displaying blog posts, forms, and user interfaces.
    Forms: Define forms for creating and updating blog posts.
    Static Files: Store CSS, JavaScript, and media files for styling and functionality.
    Admin Panel: Customize the admin interface for blog management by admins.
    URLs: Configure URL patterns for routing requests to the appropriate views.

  <!-- Installation -->

  Clone the repository -
    git clone https://github.com/Akashuvarma/Python_Assignment.git
    cd Python_Assignment/
    python -m venv venv
    source venv\Scripts\activate <!-- If macOS/Linux -->
    venv\Scripts\activate <!-- If Windows -->
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

    ""Open your web browser and go to http://127.0.0.1:8000/ or the appropriate URL.""