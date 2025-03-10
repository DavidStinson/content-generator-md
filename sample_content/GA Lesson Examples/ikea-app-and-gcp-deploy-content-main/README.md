# IKEA Express API / React / GitHub Actions / Google Cloud Deploy


### In this repo
- [Google Cloud Overview](./gcp-walkthrough.md)
- [Build Node/Express App](./build-express-app.md)
- [Testing With Postman](./testing-with-postman.md)
- [Build React App](./build-react-app.md)
- [Deploy to GCP](./deploy-to-gcp.md)
- [Deploy to GCP with Github Actions](./deploy-to-gcp-github-actions.md)

## Other repos
- [IKEA Users App Complete](https://git.generalassemb.ly/marcwright-rem/ikea-users-app)
- [GCP Deployed App](https://ikea-users-app-alem6gcnna-uc.a.run.app/)
- [Public GitHub IKEA Users App](https://github.com/marcwright/ikea-users-app)

<!-- # INSTRUCTIONS TO CREATE NODE

## CREATE REACT VITE APP

1. `mkdir pirate-app-08012024`
1. `npm create vite@latest`
2. Project Name: `react-app`
3. React - Javascript
4. Run these

	```
	cd pirate-app-08012024
	npm install
	npm run dev
	```

5. `code .`
6. make a change to `src/App.tsx` and app will rebuild
7. `cd react-app` and `npm run build` will create a dist directory to deploy

<br>

## CREATE EXPRESS APP server side

- send static html/js/css to browser
- Create api for react app to call for data

1. Go up one directory
2. `npm init -y`
3. `npm install express nodemon cors`
3. `touch index.js`
4. Add code to `index.js`

 ```js
 const express = require('express');
 const cors = require('cors');
 const app = express();
 app.use(cors());
 app.use(express.json());
 app.use(express.static("react-app/dist"));
 
 
 app.get("/api/pirates/:id", (req, res) => {
     const id = req.params.id;
     const pirate = getPirate(id);
     if (!pirate) {
       res.status(404).send(`Pirate ${id} not found`);
     } else {
       res.send({ data: pirate });
     }
   });
 function getPirate(id) {
     const pirates = [
       { id: 1, name: "Blackbeard", active: true, country: "England" },
       { id: 2, name: "Anne Bonny", active: true, country: "Ireland" },
       { id: 3, name: "Calico Jack", active: false, country: "England" },
       { id: 4, name: "Bartholomew Roberts", active: true, country: "Wales" },
       { id: 5, name: "Mary Read", active: false, country: "England" },
     ];
     return pirates.find((pirate) => pirate.id == id);
   }
 
 const port = process.env.PORT || 8080;
 app.listen(port, async () => {
   console.log(`Server started at ${port}`);
 }); 
 ```

5. Add a `start` command to `package.json`

 ```js
   "scripts": {
     "test": "echo \"Error: no test specified\" && exit 1",
     "start": "nodemon index.js" 
   }, 
 ```

1. The server should start on port 8080 and we should see the `dist` folder.
1. Try `http://localhost:8080/api/pirates/3` and you should get JSON back.

NOTE - if you make a change to the files, you'll see it on `localhost:5173`, but not on `localhost:8080` since it's serving the static `dist` folder.

<br>

## DEPLOY TO GCP

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a New Project
3. Using Cloud Run which is serverless, only billed when someone sends a request.
4. In GCP CLI - `gcloud auth login`
5. `gcloud config set project PROJECT_ID`
6. Deploy to Cloud Run and define what service should be called: `gcloud run deploy pirate-service-0801`. Note - make sure you're in the parent directory.
7. A few APIs are not yet enabled. Click yes.

 ```js
 The following APIs are not enabled on project [pirate-app-project-08012024]:
        artifactregistry.googleapis.com // makes it easy to rollback to previous revisions
        cloudbuild.googleapis.com
        run.googleapis.com
 ```

1. Choose the region closest to you.
2. Choose yes for next 2 questions. _Cloud Build question should only com up the first time._
3. Deployment can take 3 minutes
4. When it's done the URL should give you the same response as locally: `https://pirate-service-0801-js6e7clajq-uc.a.run.app/api/pirates/3`

<br>

## Add SQL Lite

1. In the root directory: `npm install sequelize cors sqlite3`
2. Add this to `index.js`

 ```js
 const { Sequelize, Model, DataTypes } = require('sequelize');
 const cors = require("cors");

  ...
  
 app.use(cors())
 
  ...
  
 // Create Sequelize instance
 const sequelize = new Sequelize({
   dialect: 'sqlite',
   storage: './database.sqlite'
 });
 
  ...
  
 // Define User model
 class User extends Model {}
 User.init({
   name: DataTypes.STRING,
   email: DataTypes.STRING,
   password: DataTypes.STRING
 }, { sequelize, modelName: 'user' });
 
 // Sync models with database
 sequelize.sync();

 app.get('/api/seeds', async (req, res) => {


   const users = [
     { name: "John Doe", email: "john@example.com", password: "password1" },
     { name: "Jane Smith", email: "jane@example.com", password: "password2" },
     { name: "Mike Johnson", email: "mike@example.com", password: "password3" },
     { name: "Sarah Williams", email: "sarah@example.com", password: "password4" },
     { name: "David Brown", email: "david@example.com", password: "password5" }
   ];
   users.forEach(u => User.create(u));
   // const users = await User.findAll();
   res.json(users);
 }); 

 app.post('/api/users', async (req, res) => {
   const user = await User.create(req.body);
   res.json(user);
 });
 
 
 // CRUD routes for User model
 app.get('/api/users', async (req, res) => {
   const users = await User.findAll();
   res.json(users);
 });
 
 app.get('/api/users/:id', async (req, res) => {
   const user = await User.findByPk(req.params.id);
   res.json(user);
 });
 ```

1. `cd` into `react-app` and `npm run dev`.
2. Then, `cd` into the root and run `npm run start`
2. Run `http://localhost:8080/api/seeds` then `http://localhost:8080/api/users`

<br>

## Push to GitHub

1. Create a new repo and push
2. SHOW GITHUB ACTIONS - Search for "google" and "Deploy to Cloud Run from Source"
3. Click configure
3. Get these from GCP Project and Cloud Run:

 ```js
 env:
   PROJECT_ID: react-pirate-app-431121 # TODO: update Google Cloud project id
   SERVICE: pirate-app # TODO: update Cloud Run service name
   REGION: us-central1 # TODO: update Cloud Run service region
   ENVIRONMENT: production
    ```
  
4. Add these under `steps` and `name: Checkout`:

 ```js
 - name: Install Dependencies
  working-directory: ./react-app
  run: npm install
 
 - name: Build React App
  working-directory: ./react-app
  run: npm run build
 ```

1. In the file uncomment the Alternative option for authentication:

 ```yaml
 # NOTE: Alternative option - authentication via credentials json
 - name: Google Auth
  id: auth
  uses: 'google-github-actions/auth@v0'
  with:
  credentials_json: '${{ secrets.GCP_CREDENTIALS }}'
 ```

#### Finished yml

```yaml
# This workflow will deploy source code on Cloud Run when a commit is pushed to
# the "main" branch.
#
# To configure this workflow:
#
# 1. Enable the following Google Cloud APIs:
#
#    - Artifact Registry (artifactregistry.googleapis.com)
#    - Cloud Build (cloudbuild.googleapis.com)
#    - Cloud Run (run.googleapis.com)
#    - IAM Credentials API (iamcredentials.googleapis.com)
#
#    You can learn more about enabling APIs at
#    https://support.google.com/googleapi/answer/6158841.
#
# 2. Create and configure a Workload Identity Provider for GitHub:
#    https://github.com/google-github-actions/auth#preferred-direct-workload-identity-federation.
#
#    Depending on how you authenticate, you will need to grant an IAM principal
#    permissions on Google Cloud:
#
#    - Artifact Registry Administrator (roles/artifactregistry.admin)
#    - Cloud Run Source Developer (roles/run.sourceDeveloper)
#
#    You can learn more about setting IAM permissions at
#    https://cloud.google.com/iam/docs/manage-access-other-resources.
#
# 3. Change the values in the "env" block to match your values.

name: 'Deploy to Cloud Run from Source'

on:
  push:
    branches: ['main']

env:
  PROJECT_ID: 'ikea-08202024' # TODO: update to your Google Cloud project ID
  REGION: 'europe-west1' # TODO: update to your region
  SERVICE: 'ikea-08202024' # TODO: update to your service name

jobs:
  deploy:
    runs-on: 'ubuntu-latest'

    permissions:
      contents: 'read'
      id-token: 'write'

    steps:
      - name: 'Checkout'
        uses: 'actions/checkout@692973e3d937129bcbf40652eb9f2f61becf3332' # actions/checkout@v4
      
      - name: 'Install Dependencies'
        working-directory: ./react-app
        run: npm install

      - name: 'Build React App'
        working-directory: ./react-app
        run: npm run build

      - name: 'Google Auth'
        id: auth
        uses: 'google-github-actions/auth@v0'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run'
        uses: 'google-github-actions/deploy-cloudrun@33553064113a37d688aa6937bacbdc481580be17' # google-github-actions/deploy-cloudrun@v2
        with:
          service: '${{ env.SERVICE }}'
          region: '${{ env.REGION }}'
          # NOTE: If using a different source folder, update the image name below:
          source: './'

      # If required, use the Cloud Run URL output in later steps
      - name: 'Show output'
        run: |-
          echo ${{ steps.deploy.outputs.url }}
```

1. Comment the seciton above it where it mentions Workload Identity Provider.
2. Get GCP_CREDENTIALS from `Service Account -> Permissions -> Keys` -> Add the entire downloaded JSON file to GH
5. In your GitHub repo, Go add `Settings -> Secrets and variables -> Actions (GCP_PROJECT_ID, GCP_CREDENTIALS)`
6. Change things to v2
7. Commit changes then git pull
8. Make changes - add, commit and push and watch GH Actions. -->
