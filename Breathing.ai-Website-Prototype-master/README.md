# Breathing.ai-Website-Prototype
This is a rough draft for the web application that will allow users to detect and view their heart-rate based on colors and fonts they observe

------------------


This is a prototype for the web application we are currently trying to work on, the prototype is not fully complete and is a mockup of what the actual one should look and behave like. There are several functionalities that still need to be added, for some of these tasks we require additional assistance. These problems will be addressed later on in the README, for now we will go through what we have and how the actual application should work.


## STEPS: 
1. When you first run the web application, you are greeted with a login screen. As of now the login screen does not store any input so click “continue as a guest”. The purpose of the login screen for the final product is to allow for the user to have their data, on their heart rate, stored and be accessible to both us and the user. 
2. After “continuing as a guest” you are taken to the “Start” page, this will be the beginning of the test.
3. Next, the directions page should appear, where  if you hover over the circles you will be able to see the steps of the entire process. Click “Begin”
4. The camera page will open up prompting the user to give access to the camera. The purpose of this page for now is to give an idea of what should happen, the camera opens and locks on to your face, at that point, a green channel, focused on your forehead, is able to view sensitive photodiodes to detect the amount of blood flowing through your skin. 
5. Next, users observe a series of five colors in random order. This process should last up to a minute in the final version, but for now it is 25 seconds long. We will update the colors based research showing us which colors have the most impact on heart rate. Our (UX team)
6. The following page is a simple buffer page to let the user know that the next portion of the simulation is about to start. 
7. This test observes the change in the user heart rate after observing five different fonts in random order, the timing is the same as above.
8. The next page is the preference page. Users are able to rate colors and fonts they found most calming on a scale of 1-5 (5 = most liked). This information will be used to allow the users to compare their choices to the actual results of the test (Will be shown in the Results page -- not complete).



## PROBLEMS/THINGS WE NEED HELP WITH:

Some of the problems we are facing are: 
* Finding a way to actually use the camera to analyze the users BPM
    * One of the two approaches to this problem is using JavaScript to take pictures and store them so that we can use        Python/Flask backend on the server side to analyze pictures we have taken. To learn more on how this might work, you can speak to the researchers on our team. 
    * The second approach would be to replicate the code we have in python already and write it up in JavaScript so we can do everything on the client side, since python cannot be run on the client side. (Insert link to python code and unity)
* The first method brings up another issue we are having which is setting Up Python and Flask
    *To use python with a database a web framework must be implemented. We tried implementing flask but were not able to since the python file was too complex. We need someone to help us with that portion since we are stuck on it. 
* Help Setting up Database
    * Use the Google Firebase to store images (from client side) and sent back to the server side to be analyzed (if we use python code)







## Task We Are Still Working On, Need To Modify/Finish:
- [ ] Results Page
  * Two Column Layout: 
    * First showing the result of preferences   
    * Second showing the BPM for each color
- [ ] Modify Preference/Questions Page: “Which Color Did YOU Find Most Calming”
   * Want to store the users answers so we can preview them in the results page
- [ ] User Authentication
   * Users can login using their Google account
   * Users can create new user credentials 



**We will further update the readme with updates, also if things are not too clear to understand at the moment. We will update the readme to include the link to the desktop version of the site where you will be able to view the python code**

