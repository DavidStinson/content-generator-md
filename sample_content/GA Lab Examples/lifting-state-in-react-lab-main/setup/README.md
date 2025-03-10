<h1>
  <span class="headline">Lifting State in React Lab</span>
  <span class="subhead">Setup</span>
</h1>

## Setup

Open your Terminal application and navigate to your `~/code/ga/labs` directory:

```bash
cd ~/code/ga/labs
```

Create a new Vite project for your React app:

```bash
npm create vite@latest
```

You'll be prompted to choose a project name. Let's name it `lifting-state-in-react-lab`.

- Select a framework. Use the arrow keys to choose the `React` option and hit `Enter`.

- Select a variant. Again, use the arrow keys to choose `JavaScript` and hit `Enter`.

Navigate to your new project directory and install the necessary dependencies:

```bash
cd lifting-state-in-react-lab
npm i
```

Open the project's folder in your code editor:

```bash
code .
```

### Configuring ESLint

Before we begin, we need to adjust the ESLint configuration. Add the indicated rules to the `rules` object in your `eslint.config.js` file:

```javascript
    rules: {
      ...js.configs.recommended.rules,
      ...react.configs.recommended.rules,
      ...react.configs['jsx-runtime'].rules,
      ...reactHooks.configs.recommended.rules,
      'react/jsx-no-target-blank': 'off',
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
      'react/prop-types': 'off', // add this line
      'react/no-unescaped-entities': 'off', // add this line
    },
```

The first addition prevents warnings if you don't declare types for your props (which we're not), and the second prevents warnings if you use contractions within JSX.

### Running the development server

To start the development server and view our app in the browser, we'll use the following command:

```bash
npm run dev
```

You should see that `Vite` is available on port number 5173:

```plaintext
localhost:5173
```

### GitHub setup

To add this project to GitHub, initialize a Git repository:

```bash
git init
git add .
git commit -m "init commit"
```

Make a new repository on [GitHub](https://github.com/) named `lifting-state-in-react-lab`.

Link your local project to your remote GitHub repo:

```bash
git remote add origin https://github.com/<github-username>/lifting-state-in-react-lab.git
git push origin main
```

> 🚨 Do not copy the above command. It will not work. Your GitHub username will replace `<github-username>` (including the `<` and `>`) in the URL above.

## Add starter code

In this lab, we've included some starter code for you. This approach is designed to help you concentrate on learning about lifting state, without the need to focus on the initial setup, layout, or styling. Don't worry, there's still plenty of work for you to do! Your task is to build on this foundation, primarily focusing on the concept of lifting state in React.

## Clear `App.jsx`

Remove any existing code and add the following to `src/App.jsx`:

```jsx
// src/App.jsx

import './App.css';

const App = () => {
  const availableIngredients = [
    { name: 'Kaiser Bun', color: 'saddlebrown' },
    { name: 'Sesame Bun', color: 'sandybrown' },
    { name: 'Gluten Free Bun', color: 'peru' },
    { name: 'Lettuce Wrap', color: 'olivedrab' },
    { name: 'Beef Patty', color: '#3F250B' },
    { name: 'Soy Patty', color: '#3F250B' },
    { name: 'Black Bean Patty', color: '#3F250B' },
    { name: 'Chicken Patty', color: 'burlywood' },
    { name: 'Lettuce', color: 'lawngreen' },
    { name: 'Tomato', color: 'tomato' },
    { name: 'Bacon', color: 'maroon' },
    { name: 'Onion', color: 'lightyellow' },
    { name: 'Cheddar Cheese', color: '#FDE18B' },
    { name: 'Swiss Cheese', color: '#F1E1A8' },
  ];

  return (
    <main>
      <h1>Burger Stacker</h1>
      <section>
      {/* List & Stack components */}
      </section>
    </main>
  );
};

export default App;
```

## Clear `App.css`

Replace any existing code in `src/App.css` with the following:

```css
/* src/App.css */
* {
  box-sizing: border-box;
}

:root {
  line-height: 1;
  font-weight: 400;
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html,
body,
#root {
  margin: 0;
  height: 100%;
  overflow-x: hidden;
}

main {
  width: 100%;
  height: 100%;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

section {
  width: 80%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

h1 {
  text-align: center;
}

ul {
  width: 100%;
  height: 100%;

  margin: 0;
  padding: 16px;
  list-style: none;

  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

li {
  padding: 8px;
  margin-bottom: 4px;
  border-radius: 8px;
  font-weight: bold;
  text-shadow: 0px 0px 2px #000000;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

button {
  cursor: pointer;
  border-radius: 8px;
  background-color: #1a1a1a;
  border: 1px solid transparent;
}
```

## Create two new components

Run the following commands in your terminal:

```bash
mkdir src/components
mkdir src/components/IngredientList
touch src/components/IngredientList/IngredientList.jsx
mkdir src/components/BurgerStack
touch src/components/BurgerStack/BurgerStack.jsx
```

These will serve as the starting components for your burger stacking app.

### IngredientList

Add the following to `src/components/IngredientList/IngredientList.jsx`:

```jsx
// src/components/IngredientList/IngredientList.jsx

const IngredientList = (props) => {
  return <ul>// map through props.ingredients</ul>;
};

export default IngredientList;
```

### BurgerStack

Add the following to `src/components/BurgerStack/BurgerStack.jsx`:

```jsx
// src/components/BurgerStack/BurgerStack.jsx

const BurgerStack = (props) => {
  return <ul>// map through props.ingredients</ul>;
};

export default BurgerStack;
```

You're ready to go!
