# Aurebesh-Translator

Aurebesh Translator

Video Demo:  <URL HERE>
Description: A web app that translates basic (english) to Aurebesh, and Aurebesh to Basic.

TODO Your README.md file should be minimally multiple paragraphs in length, and should explain what your project is, what each of the files you wrote for the project contains and does, and if you debated certain design choices, explaining why you made them. Ensure you allocate sufficient time and energy to writing a README.md that documents your project thoroughly. Be proud of it! If it is too short, the system will reject it.


I recently was fortunate enough to get to go on Disney's Galactic Starcruiser.  It is a 2 day, fully immersive and interactive, theatrical experience where you become a character in the Star Wars universe and live out the events that happen on your Starcruiser the Halcyon, making choices along the way that shape your journey.

In preperation for this journey, I learned to read Aurebesh, the alphabet that often appears in Star Wars. It is not it's own language, but simply a letter for letter conversion of the english alphabet, where A is one symbol, B another symbol, and so on.

Although Aurebesh is a fairly easy language to learn to read, it is harder to write and not everyone has the time to learn it. Due to this experience I was inspired to create this translation app to translate from both basic to aurebesh and aurebesh to basic.

APP.PY
The main controls for the app. 
flask and ncessary functionality are imported at the top of the page. it is then configured as a flask app. 
I define the "/" route as the home page which directs to the index.html template. 
"/B2A" is the next route defined with GET and POST parameters. If the request is get it will render the B2A =.html template. If the request is post, it will save the text as the basic_text variable and check to make sure that the user has entered text and that the text is not too long. The limit on the length of the text is to make sure that the text fits properly in the 'output' box in both desktop and mobile views. If the user does not input text or if the text is too long, the it will renger the porgs.html temlate which shows an error. If the user has entered the text correctly, it will pass the basic_text variable to the B2A.html template, which will display it in a jinja template in the 'output' section. The Aurebesh font is applied to it as a css class which causes the translation
the "/A2B" route is applied similarly, the main difference being that it checks for a different length of text. This is becasue basic characters takes up less space than the aurebesh characters.

REQUIREMENTS.TXT
cs50 to require the cs50 library
flask is required for it to run
gunicord required for it to be hosted on render

TEMPLATES

LAYOUT.HTML
This dictates the layout for the whole app. I inport bootstrap for both Css and html. I connect the css style sheet to this page so that design choice i make in css will be reflected throughout the app. I establish the title as well as creating a jinja placeholde for the titles from the other pages.

I establish a navbar, although the only component is the 'brand'. I incorporat the img of the CSL logo into the word 'Translator' in place of the letter 'o'

I create two buttons to navigate the app. one that takes the user to the page to tranlate basic into aurebesh and another that takes the user to the page to translate aurebesh into basic. the Basic to aurebesh button links to the previously defined "/B2A" route and the Aurebesh to basic button links to the "/A2B" route

last I create a place holder for the other html template to fit into when called.

INDEX.HTML

this is essentialy the homepage. It links into the layout html template. It displayes a simple welcome message that is 'in universe' from Chandrilla Star Lines. It also includes the img of the CSL logo.

PORGS.HTML

This is the error page. It show a message informing the user that there has been an issue, and suggest a couple of things that may have caused the error. The message is also 'in universe' and inplicates creatues known as 'Porgs' in the issues the app has encounterd, as well as including an img of a porg. It also links into the layout template and is called by both the "/B2A" and "/A2B" routes depending on the actions of the user.

B2A.HTML

This is the page that provides Basic to aurebesh translation. It connects with the layout template. Using fieldset and legend, I created a text in border effect for both the input and output sections. First is the input section. here the is an input field for a user to type the text they want translated. there is a button for them to click when they are reaey for their text to be translated by calling the "/B2A" route. when the users text is passed back from the "/B2A" it goes to the jinja placeholder in the 'output' section. The aurebesh class is applied which changes the font to Aurbesh creating the translation. the text in aurbesh is displayed in the output section.

A2B.HTML

this is the page that provides Aurebesh to basic translation. for this page i swapped the input and output sections so that output was at the top. I relized this would be the best design for the user, since the aurebesh keyboard has pushed the output section for far down the page. it made send to have the translation be more immidiatly visable after they submitted it.

similarly to the B2A.html page, I used fieldset and legend to created a text in border effect for both the input and output sections. I also used a jinja template to display the users text when it is translated, but this time, i do not apply the aurebesh class, so it displays in basic. 

Like in B2A there is a input field where the users desired text will appear, however this time they will type it using the virtual keyboard and the text will be displayed in aurebesh. there is another button that the user will use when they are ready for their text to be translated, which will call the "/A2B" route.

below the input field are two buttons, space and delete. these allow the user to either delete a character if they make a mistake, or input a space if they are inputting multiple words.

I created a virtual aurebesh keyboard on this page, since most people don't have an aurebesh keyboard of their own and users would need a way to type those symbols. I organised it in sections with alphabet in the first, numbers in the second, and punctuation in the third.

The final componenet of this template is the javascript. It has three components. the first makes it so that when the user clicks one of the buttons in the aurebesh keyboard it will appear in the input field. the second and third borth create the functionality for the space and delete buttons. 

STATIC

STYLE.CSS
all the css for the app. includes design for the over all look of the app, as well as all the text, buttons and input. the design elements for fieldset and legend are particularly important as they enable the text in border effect seen in the input and output sections. I also import the Aurebesh font which enabes the translations.

ASSETS

CHIL-PORG-1.PNG
an image of a porg used on the porgs.html template

CSLLOGOW.PNG
the csl logo used in the navbar and the index.html template

FONTS

AUREBESHNL.TTF
an open source font that enables the translation function of the app.
Copyright (c) 2022, Vino Rodrigues - github.com/vinorodrigues, with Reserved Font Name AUREBESH.
