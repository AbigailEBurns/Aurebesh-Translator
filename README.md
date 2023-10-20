# Aurebesh-Translator

Aurebesh Translator

Video Demo:  <URL HERE>
Description: A web app that translates Basic (English) to Aurebesh, and Aurebesh to Basic.

I recently visited Disney's Galactic Starcruiser. It is a 2 day, fully immersive and interactive, theatrical experience where you become a character in the Star Wars universe and live out the events that happen on the Starcruiser Halcyon, making choices along the way that shape your journey.

In preparation for this journey, I learned to read Aurebesh, the alphabet that often appears in Star Wars. It is important to note that it is not its own language, but simply a letter for letter conversion of the English alphabet, where A is one symbol, B another symbol, and so on. It is also important to note that English is knows as Basic in the Star Wars universe

Although Aurebesh is fairly easy to learn to read, it is harder to write and not everyone has the time or desire to learn it. I was inspired to create this translator by my experience preparing for and experiencing the Halcyon as an understanding of Aurebesh enriched my time there and has given me a depper understanding of the Star Wars universe since then.

APP.PY
This is the main control for the app. 

Flask and other necessary functionalites, such as request and render_template, are imported at the top of the page. It is then configured as a flask app. 

I define the "/" route as the home page which directs to the index.html template and defines it as the homepage for the app.

"/B2A" is the next route defined, with GET and POST parameters. If the request is GET it will render the B2A.html template. If the request is POST, it will save the text as the basic_text variable and check to make sure that the user has entered text and that the text is not too long. The limit on the length of the text is to make sure that the text fits properly in the 'output' box in both desktop and mobile views. If the user does not input text or if the text is too long, then it will render the porgs.html template which shows an error. If the user has entered the text correctly, it will pass the basic_text variable to the B2A.html template, which will display it in a Jinja placeholder in the 'Output' section. The Aurebesh font is applied to it as a CSS class which causes the translation.

The "/A2B" route is applied similarly, the main difference being that it checks for a different length of text. This is because basic characters take up less space than the Aurebesh characters. It also saves the user input in a different variable and the Aurebesh class is not applied when passed to the jinja placeholder.

REQUIREMENTS.TXT
These are the elements required to run the app:
cs50 to require the cs50 library
flask is required for it to run
gunicord required for it to be hosted on render

TEMPLATES

LAYOUT.HTML
This dictates the layout for the whole app. I import bootstrap for both CSS and HTML. I connect the CSS style sheet to this page so that design choices I make in CSS will be reflected throughout the app. I establish the title as well as creating a Jinja placeholder for the titles from the other pages.

I establish a navbar, although the only component is the 'brand'. I incorporate the img of the CSL logo into the word 'Translator' in place of the letter 'o'. clicking on the 'brand' will follow the '/' route and return the user to the homepage.

Next I create two buttons to navigate the app. One that follows the '/B2A' route and takes the user to the page that translates Basic into Aurebesh. The other follows the '/A2B' route and takes the user to the page to translate Aurebesh into Basic.

Lastly, I created a place holder for the other html template to fit into when called.

INDEX.HTML

This is the homepage and is called by the '/' route. It links into the layout html template. It displays a simple 'in universe' welcome message from Chandrilla Star Lines that utilizes the <h1>, <h3>. and <p> tags . It also includes the img of the CSL logo.

PORGS.HTML

This is the error page. It show a message informing the user that there has been an issue, and suggests a couple of things that may have caused the error. The message is also 'in universe' and implicates creatures known as 'Porgs' in the issues the app has encountered, as well as including an img of a Porg. It  links into the layout template and is called by both the "/B2A" and "/A2B" routes depending on the actions of the user.

B2A.HTML

This is the page that provides Basic to Aurebesh translation. It links with the layout template. 

Using fieldset and legend, I created a text in border effect for both the input and output sections. 

At the top is the Input section. There is an input field for a user to type the text they want translated and there is a button for them to click when they are ready for their text to be translated. When clicked it calls the POST branch of the "/B2A" route. 

When the users’ text is passed back from "/B2A" it goes to the Jinja placeholder in the Output section. The Aurebesh class is applied which changes the font to Aurebesh creating the translation. The text in Aurebesh is displayed in the Output section at the bottom of the page.

A2B.HTML

This is the page that provides Aurebesh to Basic translation. For this page I swapped the input and output sections so that output was at the top. I realized this would be the best design for the user, since the Aurebesh keyboard had pushed the output section so far down the page. It made sense to have the translation be more visible immediatly after they submitted it.

Similarly, to the B2A.html page, I used fieldset and legend to create a text in border effect for both the input and output sections. I also used a Jinja template in the Output section to display the users’ text when it is translated, but this time I do not apply the Aurebesh class, so it displays in Basic. 

Like in B2A there is an input field where the users desired text will appear, however this time they will type it using the virtual keyboard and the text will be displayed in Aurebesh. There is also a 'Translate' submit button that the user will use when they are ready for their text to be translated, which will call the POST branch of the"/A2B" route.

Below the input field are two buttons, 'Space' and 'Backspace'. These allow the user to either delete a character if they make a mistake or input a space if they are inputting multiple words to be translated. They work by calling the JavaScript at the bottom of the page.

Next I created a virtual Aurebesh keyboard. Most people don't have an Aurebesh keyboard of their own and users would need a way to type Aurebesh symbols. I organized it in sections with alphabet in the first, numbers in the second, and punctuation in the third. This was to make the most likely typed characters more acessible at the top.

The final component of this template is the JavaScript. It has three functions. The first connects the buttons of the aurebesh keyboard with the input box, so that the characters the user types will appear in the input box. The second and third create the functionality for the delete and space buttons respectivly. 

STATIC

STYLE.CSS
The CSS stylesheet for the app. Includes design for the overall look of the app, as well as all the text, buttons and input. The design elements for fieldset and legend are particularly important as they enable the text in border effect seen in the input and output sections. I also import the Aurebesh font which enables the translation functionality.

ASSETS

CHIL-PORG-1.PNG
An image of a Porg used on the porgs.html template. Property of the Walt Disney Company

CSLLOGOW.PNG
The CSL logo used in the navbar and the index.html template. Property of the Walt Disney Company

FONTS

AUREBESHNL.TTF
An open-source font that enables the translation function of the app.
Copyright (c) 2022, Vino Rodrigues - github.com/vinorodrigues, with Reserved Font Name AUREBESH.

REFLECTIONS

Overall, I am quite pleased with how this project turned out. It is the first thing I have ever thought of and built from start to finish by myself. It was a huge learning experience, particularly when it came to CSS which I have learned is not my favorite. 

I am really pleased with how I handled the translation functionality with using a font. I feel this is a very simple yet effective solution. I also really enjoyed designing the app to look like something that might exist within the world of Star Wars and be available to CSL passengers. It was also very gratifying building my own keyboard and getting it to function like a keyboard!

The part of the code I am least satisfied with is how I had to limit the characters a user could enter to ensure that it would fit within the output box in both desktop and mobile views. I am sure there are better ways to handle this sort of thing more dynamically, but I couldn’t figure them out for this project. I hope in the future I can come up with a better implementation. I also have concerns that if something happens to the Aurebesh font (if a user’s device is unable to display it properly) then the entire functionality of the app is messed up. 
