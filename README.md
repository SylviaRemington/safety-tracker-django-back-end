# Safety Tracker Django Back End API
**I've created a Django/Python API using Django Rest Framework (DRF), with 5 data entities (users, stories, authors, comments, check-ins, and more for stretch targets) which exposes its endpoints so it can be consumed from any front end application (like react.js).**

Next up, I will be creating a front end to complete building my first Django API & React Frontend full stack application! Woot woot! <br> **...Currently, in progress...**

<hr>

### Encountering errors of deployment with backend - Luke was troubleshooting with me today (10/26) for 1.5 hours. He will be looking over my repo to determine what else needs to be done to deploy. 
### **Update** 
- **I needed to delete all the heroku updates that we did to settings.py from my GitHub Repo so that my backend could function again and interact with my frontend for project week. Below is what I had to delete from my repo and local so that things would work again.**
- **Deleted settings.py deleted static file to the top to reset. And I have taken screenshots of these commits prior to deleting. I have them on my local computer. (See Image Below From GitHub)**

<hr>

<img width="1208" height="651" alt="Deleted Commits From Repo - from deleted static file to the top - 2025-10-26 at 1 13 31 PM" src="https://github.com/user-attachments/assets/d0d35f38-0268-4f85-8dcb-35c27c0fcef3" />

<br>

<hr>

## Logo
<img width="611" height="572" alt="Screenshot 2025-10-18 at 4 59 50 AM" src="https://github.com/user-attachments/assets/52ff486f-75cb-4e9b-942f-fdda15bad912" />


## Link to:
- Front End Github Repo
- View Site: Back End Repo Link
- Trello Planning Materials & Excalidraw Wireframes & Lucid ERDs (Planning Materials)
- Deployed App

## Information/Inspiration

## Features

## Tech Stack

## Attributions/Resources

## Rough Drafts - screenshots of wireframes & tree set ups

## Future Enhancements / Next Steps
- Patterns / Graphs Functionality
- Self Care / Calming Actions / Wellbeing Tips

## Stretch Goals 🚀

## Ahas / Additional Awareness
- **Deleting A Commit** - Learned how to delete a commit via (1) Looking up the commit number in git log, (2) Making sure it was the correct commit with git checkout a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0, (3) Going back into the main branch where my repo and commit were located, (4) Doing a hard reset to completely delete the commit (since that is where all the problems were arising) with git reset --hard HEAD~1, (5) Pushing this change through via git push origin main --force. Grateful to have learned this. There is also the ability to do a "soft" reset as well. Since I am working solo on this project, I double checked everything and then proceeded. If I were in a team, my actions would have taken into account other team members and I wouldn't have done it this way. <br><br> **Where the mistake occurred & how I corrected it:** After registering the author model, I created a foreign key and migrated it without deleting the database ahead of time & that messed all the functionality up. I tried to fix it on my own; however, best scenario after attempting this for a while was to delete the foreign key commit and go back to where I was before that. That occurred on October 16th 2025, right after I registered the author model. After that, I went through postman and all functionality to make sure it was working again before I proceeded forward (thus all the notes after that to check on functionality). <br>

<br>

- **Django Backend Simplicity In the Repetition** - Appreciate the simplicity of Django back end: e.g. where you create the project, you create the app, & add it to installed apps. And then within the app, you follow basic steps for every app: create the model/makemigrations/migrate, register it in admin.py, create serializer, create the functions in views.py, create the path in urls.py in both the app and the project, and then test it. Additionally, the first app you typically create is the Authorization which entails a bit more with creating a superuser & serializer; however, all in all, it repeats itself and makes it super simple. Additionally, if there are interrelated items, you'll need to create foreign keys as well. <br>

<br>

- **Order of Installed Apps** - Researched this and learned that the common Django best practices for INSTALLED_APPS order is: **(1)Django built-in apps** first, **(2)then third party apps** like **corsheaders** & **rest_framework**, and **(3)then custom apps** go last to avoid overriding Django's defaults.
