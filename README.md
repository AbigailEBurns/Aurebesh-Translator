# CSL Aurebesh Translator

Video Demo: [Watch Here](https://youtu.be/FOLO8NMk36Y)

The CSL Aurebesh Translator is a web application that translates text between Basic (English) and Aurebesh, the alphabet used in the Star Wars universe. This tool enhances understanding and interaction with Aurebesh, enriching the Star Wars experience.

## Project Inspiration and Purpose

The CSL Aurebesh Translator, developed as a final project for the CS50 course, demonstrates my proficiency in programming and web development. Inspired by a visit to Disney's Galactic Starcruiser, where I encountered the fictional Star Wars alphabet, Aurebesh, this tool facilitates translation between Basic (English) and Aurebesh.

Aurebesh is a letter-for-letter representation of the English alphabet. Designed to simplify translation, the tool offers a user-friendly and thematically appropriate solution for those unable to read it.

This work highlights my ability to build functional web applications using Flask, design and style user interfaces with HTML/CSS, and integrate interactive elements with JavaScript, all within a cohesive thematic framework.

## Technologies Used
  * **Programming Language:** Python
  * **Framework:** Flask
  * **Front-End Technologies:**
    * HTML
    * CSS
    * JavaScript
    * Bootstrap
  * **Libraries:**
    * `cs50`: For interacting with the Flask app.
    * `flask`: Core framework for web application development.
    * Jinja: Template engine for rendering dynamic content in Flask.
  * **Tools:**
    * `gunicorn`: WSGI HTTP server for hosting the application.
    * Aurebesh Font: For translating text into Aurebesh.

## Features
  * Basic to Aurebesh Translation: Converts English (Basic) text into Aurebesh, applying a custom font that mimics the visual style of the Star Wars universe, ensuring an immersive user experience.
  * Aurebesh to Basic Translation: Translates Aurebesh text back into English (Basic), featuring a virtual Aurebesh keyboard for seamless input, maintaining thematic consistency.
  * Error Handling: Provides user-friendly error messages with "in-universe" narrative elements, offering guidance and suggestions aligned with the Star Wars theme when invalid input or other issues arise.

## Code Overview
`app.py`
  * **Overview:** Serves as the main control for the application. Configures Flask, sets up routes, and handles requests.
  * **Routes:**
    * `/`: Renders the homepage (`index.html`).
    * `/B2A`: Handles Basic to Aurebesh translation. Processes POST requests to convert text and renders `B2A.html` with the translation.
    * `/A2B`: Handles Aurebesh to Basic translation. Processes POST requests to convert text and renders `A2B.html` with the translation.

`requirements.txt`
  * Lists dependencies required to run the application:
    * `cs50`: Library for Flask integration.
    * `flask`: Web framework.
    * `gunicorn`: Server for deployment.

## Templates
`layout.html`
  * **Purpose:** Provides the base layout for the application, including navigation and styling.
**Features:**
  * Integrates Bootstrap for responsive design.
  * Includes a navigation bar with links to translation pages.
  * Provides placeholders for other templates.

`index.html`
  * **Purpose:** Serves as the homepage of the application.
  * **Features:** Displays a welcome message and the CSL logo.

`porgs.html`
  * **Purpose:** Displays error messages.
  * **Features:** Includes a message about the error, with a Star Wars-themed explanation involving porgs, and links back to the relevant routes.

`B2A.html`
  * **Purpose:** Handles Basic to Aurebesh translation.
  * **Features:**
    * Input and output sections styled with borders.
    * Input field for text and a button to submit for translation.
    * Displays the translated Aurebesh text in a designated output section.

`A2B.html`
  * **Purpose:** Handles Aurebesh to Basic translation.
  * **Features:**
    * Input and output sections arranged for ease of use.
    * Includes a virtual Aurebesh keyboard with functionality for space and backspace.
    * JavaScript functions manage keyboard interactions and text input.

## Static Assets

`styles.css`
  * **Purpose:** Provides styling for the application, including layout and text design.
  * **Features:** Defines the appearance of text and buttons, including the Aurebesh font for translation.

`assets/`
  * `chil-porg-1.png`: Image of a porg used in the errors page. Property of The Walt Disney Company.
  * `csl-logo.png`: CSL logo used in the navigation bar and homepage. Property of The Walt Disney Company.

`fonts/`
  * `aurebeshnl.ttf`: Open-source Aurebesh font for translation functionality. Copyright (c) 2022, Vino Rodrigues - github.com/vinorodrigues, with Reserved Font Name AUREBESH.

## Relevance to Software Development
This project demonstrates my ability to:
  * **Develop dynamic web applications** using Python and Flask, showcasing back-end logic and server-side rendering.
  * **Design intuitive front-end interfaces** with HTML, CSS, Bootstrap, and JavaScript, creating user-friendly, responsive layouts.
  * **Implement interactive features** like the virtual keyboard using JavaScript to manage real-time user input.
  * **Utilize Jinja for template rendering**, enabling efficient data flow between the back-end and front-end.
  * **Apply robust input validation and error handling**, enhancing user experience by providing clear feedback and preventing application errors.
  * **Manage external libraries and tools**, such as gunicorn, to deploy and host the application in a production environment.
  * **Independently learn and integrate thematic elements**, like the Aurebesh font, aligning the project with its thematic context while maintaining functionality.
  * **Write clean, modular code** following web development best practices, ensuring maintainability and scalability.

## Reflections
This project represents my first full-scale application developed from concept to completion. It provided valuable experience in both web development and design. I am particularly proud of the translation functionality achieved through font application and the immersive design that aligns with the Star Wars universe.

Challenges included managing text length constraints to fit dynamic output areas and ensuring consistent display of the Aurebesh font across different devices. Future improvements could involve enhancing dynamic text handling and addressing potential font compatibility issues to ensure robust functionality.
