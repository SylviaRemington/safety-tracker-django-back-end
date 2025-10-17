# Safety Tracker Django Back End API

## Logo

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

## Stretch Goals 🚀

## Ahas
- **Deleting A Commit** - Learned how to delete a commit via (1) Looking up the commit number in git log, (2) Making sure it was the correct commit with git checkout a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0, (3) Going back into the main branch where my repo and commit were located, (4) Doing a hard reset to completely delete the commit (since that is where all the problems were arising) with git reset --hard HEAD~1, (5) Pushing this change through via git push origin main --force. Grateful to have learned this. There is also the ability to do a "soft" reset as well. Since I am working solo on this project, I double checked everything and then proceeded. If I were in a team, my actions would have taken into account other team members and I wouldn't have done it this way. <br><br> **Where the mistake occurred & how I corrected it:** After registering the author model, I created a foreign key and migrated it without deleting the database ahead of time & that messed all the functionality up. I tried to fix it on my own; however, best scenario after attempting this for a while was to delete the foreign key commit and go back to where I was before that. That occurred on October 16th 2025, right after I registered the author model. After that, I went through postman and all functionality to make sure it was working again before I proceeded forward (thus all the notes after that to check on functionality). <br>

<br>

- **Django Backend Simplicity In the Repetition** - Appreciate the simplicity of Django back end: e.g. where you create the project, you create the app, & add it to installed apps. And then within the app, you follow basic steps for every app: create the model/makemigrations/migrate, register it in admin.py, create serializer, create the functions in views.py, create the path in urls.py in both the app and the project, and then test it. Additionally, the first app you typically create is the Authorization which entails a bit more with creating a superuser & serializer; however, all in all, it repeats itself and makes it super simple. Additionally, if there are interrelated items, you'll need to create foreign keys as well. <br>
