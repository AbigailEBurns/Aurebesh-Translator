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

