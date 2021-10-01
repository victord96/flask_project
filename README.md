# Flask Project

I have created a project based on Python with Flask microframework implementation and Firestore Gcloud as BBDD.

My goal is to create a "to do" application that helps the user writing tasks to be done, like some kind of online notepad.

The app is divided in two main parts:

1. Login

2. Main menu

## Login

when you enter the page, the web ask your username and password, and compares it with data of the database.

If you don´t have an account, you can register it going to /signup url

I make this part with LoginForms, that is a flask feature, and if the page check that is correct, it redirects to the main program.

## Main menu

Here the program greets you and show your ip (this doesn´t have a lot of sense, but I make it to prove Flask requests)

But the main feature, and the purpose of this web, is just below.

Down you can add tasks to do, edit them or delete directly. It opperate on the database and remains after you logout or exit the app.

Finally, you can logout with the link inside the navbar, that it's called "logout"
