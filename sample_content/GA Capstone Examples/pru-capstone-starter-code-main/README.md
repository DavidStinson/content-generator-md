# Capstone Starter Code

## Submitting your project

**Project is due on Friday of Week 4**

[Link to Capstone Requirements PDF](./assets/Capstone-Project-Guidelines.pdf)

Please **fork** and **clone** this repo. To submit your work, please submit a Pull Request with your full name on this repo. You will also present your application during class.

[Pull Request Instructions](https://git.generalassemb.ly/ModernEngineering/start-here/#submitting-your-work-via-pull-request)

_Note: The use of this starter code is optional! Feel free to build your own app from scratch as you see fit._

## Requirements

You will develop a new full-stack application that leverages all the technologies covered in the course. Prudential has asked that you build an application with a financial theme (e.g. budget tracker app, bill tracker app, etc.). All code will be submitted to your fork of this GitHub repository on GA’s GitHub Enterprise servers. 

[The grading rubric can be found in the Capstone Requirements PDF here](./assets/Capstone-Project-Guidelines.pdf)

- Data Model:
   - Implement and use a PostgreSQL database for storage
   - Demonstrate your API can write to and read from the database
- API Endpoints:
   - Using Express, implement working API endpoints corresponding to CRUD operations
- React User Interface:
   - CRUD operations are accessible to a user from a React front-end
   - _Styling will not be part of the evaluation_
   - _React Router does not need to be included_
- Testing:
   - 3 Jest Unit tests on the React app
   - 3 Jest Unit tests on the Express app
   - 1 End-to-End browser test with Selenium
- Containerization:
   - Create 3 Dockerfiles (backend, db, frontend) to containerize your application
   - 
_Note: Reach Out To Instructors To Show Passing Tests Before Proceeding To Containerization._

## Reference Links

Refer to previous lessons to guide you as you build out your full-stack application.

- Backend
   - [Express Todo Api Lesson](https://git.generalassemb.ly/ModernEngineering/express-to-do-api)
   - [Testing Express With Supertest](https://git.generalassemb.ly/ModernEngineering/todo-express-api-testing-with-supertest)
- Frontend
   - [Connect React frontend to Express API backen](https://git.generalassemb.ly/ModernEngineering/full-stack-react)
   - [React Jest Testing](https://git.generalassemb.ly/ModernEngineering/jest-react-lab)
   - [Testing React With Jest Walkthrough](https://git.generalassemb.ly/ModernEngineering/testing-react-with-jest-walkthrough)
- Full-stack
   - [Selenium Walkthrough](https://git.generalassemb.ly/ModernEngineering/selenium-walkthrough)
   - [Dockerize Todo App](https://git.generalassemb.ly/ModernEngineering/dockerize-to-do-app)

## Getting Started

### Backend Express API

1. `cd backend`
1. `npm i`
1. `npm run start` will start the server on port 3001

<br>

### Database

- Use the `backend/db/capstone.sql` file to create the schema in your database.
- Run the `db/capstone.sql` file to create the database, table and data: `psql -U postgres -d name_of_your_app_db < db/capstone.sql`

  _Note 1: If you're asked, the default password for the `postgres` user is either `password` or `postgres`_

  _Note 2: In `index.js`, you have 2 `pool` variables: one for local development and one when you build your backend `Dockerfile`

<br>

### React Frontend

1. `cd frontend`
1. `npm i`
1. `npm run start` will start the server on port 3000

## Presentations

Presentations will start on Thursday on a volunteers-first basis. Those who do not present on Thursday will have to present on Friday. Everyone will be asked to share their screen and demo their app. Each person will have 3-5 minutes including Q&A.

We ask that you demo the following:

- Run `sudo docker ps` to show that you have running Docker containers for the DB, backend, and frontend.
- Demo that you can Create, Read, Update and Delete on a resource.
- What are the biggest challenges and biggest wins from your capstone app?
- Give shoutouts to any peers that helped you out throughout capstone week.

_NOTE: In the interest of time, you are not required to demo your test suites, but you should still have working frontend, backend, and end-to-end tests in your repo.

## Squads

We've assigned everyone to an instructor so that we get more familiar with individual apps and better provide assistance. Here is when we'll check in.

1. We will check into the main room at 9am EST for attendance. Afterward, we'll split up into squads (in breakouts) for a standup. Here you can address:
   - What you've completed so far?
   - What you plan to work on that day
   - Any blockers

1. We will also have a 1:30pm EST check in after lunch in the Zoom chat each day for attendance.

1. We'll meet in the main room at 4:30pm EST each day for the daily exit ticket. For question "10. Any other general questions or comments to share?", please briefly let us know the following:
   - What did you accomplish today?
   - Did you hit any blockers?
   - What’s your plan for tomorrow?

### Squad Assignments

#### Ben
- Akash
- Srivalya
- Arun
- Richard
- Ellen
- Lisa
- Grant
- Joe
- Jason

#### Mario
- Alpesh
- Bradley
- Srinivas
- Lino
- Razvan
- Ed
- Karen
- Greg

#### Troy
- Arpita
- Sangeetha
- Priyank
- Brent
- Joel
- Juhi
- Harish
- Henri
- Ken
