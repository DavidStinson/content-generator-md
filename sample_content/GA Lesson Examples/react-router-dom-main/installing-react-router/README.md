<h1>
  <span class="headline">React Router DOM</span>
  <span class="subhead">Installing React Router</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to install React Router and add it to their React application.

## Installation

To add React Router, the first step is installing the package.

Begin by installing the [`react-router`](https://www.npmjs.com/package/react-router) package using npm:

```bash
npm i react-router
```

### Setting up React Router

With `react-router` installed, the next step is to set it up in our project.

We'll start by importing `BrowserRouter` in our entry file, (`src/main.jsx`). `BrowserRouter` is a component in React Router that enables navigation. It allows your app to update the URL and display different pages without reloading the whole page.

Add the following import to `src/main.jsx`:

```jsx
// src/main.jsx

import { BrowserRouter } from 'react-router';
```

Next, wrap the `<App />` component with `<BrowserRouter>`:

```jsx
// src/main.jsx

// Nest the App component inside the BrowserRouter component to enable routing:
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
```

> 💡 By wrapping `BrowserRouter` around the `App` component, it ensures that routing functionality is available within the `App` component tree.

Congratulations! You've successfully integrated React Router into your React application. With this setup, you're now ready to define routes and build a dynamic, navigable single-page application.

> 🧠 React Router has great documentation - most of the code and steps on this page are taken directly from this [Installation documentation](https://reactrouter.com/start/library/installation).
>
> You will want to stay within the **Library** documentation as you're getting started. Most of the other documentation is for the React Router framework, which we will not use in this course.
