<h1>
  <span class="headline">Mastering React Hooks</span>
  <span class="subhead">Unleash the Power of React Hooks</span>
</h1>

![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

| Title                 | Type     | Duration | Author |
|---                    |---       |---       |---     |
| Mastering React Hooks | Lesson   | 3 hours  | [Your Name] |

**Learning objectives:** By the end of this lesson, students will be able to:

- Understand the core concepts of React Hooks
- Implement basic React Hooks functionality
- Debug common issues with React Hooks

> 🛠️ **Lesson Summary**: I think a large portion of the problems with this lesson are due to the topic scope. Hooks are a *huge* topic with a lot of complexity, and each hook has specific reasons for using it. Ensuring that students understand why they would use a specific hooks is **more important than their actual implementation in code**.
>
> Because of this, we don't have a specific **React Hooks** lesson in SEB, and instead split this subject into multiple lessons that are delivered over the course of ~a week. This allows students to learn about the different hooks in a more digestible way, and also gives them time to practice and implement each one in isolation, giving them context for why they would use a specific hook to accomplish a goal. For example:
>
> - **`useState`** is covered in [React State Management](https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-state-management/canvas-landing-pages/seb.html)
> - **`useEffect`** is covered in [Fetching Data in React](https://pages.git.generalassemb.ly/modular-curriculum-all-courses/fetching-data-in-react/canvas-landing-pages/seb.html)
>
> All of that said, there are other fundamental problems with this lesson addressed below.

## Introduction (10 mins)

React Hooks were introduced in React 16.8, and they revolutionized the way we develop React applications. Hooks allow you to use state and other React features without writing class components, making your code more concise and easier to maintain.

> 📚 *Hooks are functions that let you "hook into" React state and lifecycle features from function components. Hooks don't work inside classes — they let you use React without classes.*

In this lesson, we'll explore the core concepts of React Hooks and learn how to implement them in your React projects. We'll also cover some common issues and debugging techniques for Hooks.

> 🛠️ Issues in this section:
>
> - A third of this section is spent on talking about irrelevant details such as Class components and when Hooks were added to React instead of actually introducing Hooks.
> - Another third of this section is spent telling students what the lesson covers when the learning objectives are already doing that.
> - Vital details and terms are glossed over such as: **React state**, **lifecycle features**.
>   - For comparison, check out **[React State Management's Concepts microlesson](https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-state-management/concepts/)**. This entire microlesson focuses on the concept of state and how it works in React.

### Why This Matters

Mastering React Hooks is crucial for modern React development. Hooks simplify the code, making it more readable and maintainable. They also enable better code reusability through custom Hooks. With the increasing adoption of React Hooks in the industry, having a solid understanding of this concept will make you a more competitive and efficient React developer.

> 🛠️ This is where we're supposed to be telling students *why* "Mastering React Hooks is crucial for modern React development." (yay filler statements), but we never actually do that.
>
> Connecting back to industry is fine as a sub-item here, but when talking about the why we should be more focused on *why hooks matter in React* not *why hooks help you get a job*.

## The Core Hooks (30 mins)

React provides several built-in Hooks that cover the most common use cases. Let's explore the core Hooks and their usage.

### useState Hook

The `useState` Hook allows you to add state to functional components. It returns an array with two elements: the current state value and a function to update that state.

```jsx
// !! 🛠️ We don't need to import React from 'react' here
import React, { useState } from 'react';

// This is a poorly named component.
const Example = () => {
  // 🛠️ We never explain what this syntax is or why we use it.
  // Array destructuring is likely a new concept for students since it's not
  // widely used in JavaScript.

  // Why did we name these variables `count` and `setCount`?
  
  // Why do we pass `0` to the `useState()` function?
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
  // 🛠️ This is a lot of code to add at once - we should start with the most
  // simple implementation (display the state variable) then add the button to
  // manipulate the state variable in another step.
  // We never explain the `onClick` event handler, how it works, or why we need
  // to provide it with an anonymous function.
};
```

> 📚 *The `useState` Hook is a function that takes the initial state as an argument and returns an array with two elements: the current state value and a function to update that state.*

> 🛠️ Half of this callout restates the copy above. For context, the microlesson that is equivalent to this section is [here](https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-state-management/the-use-state-hook/).

#### Try it out

1. Create a new React project using `create-react-app`.
2. Create a functional component that uses the `useState` Hook to manage a counter.
3. Render the current count and a button to increment the count.
4. Observe how the component's state updates when you click the button.

> This exercise is very poorly constructed.
>
> 1. We should use the existing project to have students build this (beside the point, but CRA is also deprecated).
> 2. The activity itself is exactly what we show them in the example above.

### useEffect Hook

The `useEffect` Hook allows you to perform side effects in functional components. It's similar to the `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` lifecycle methods in class components.

> 🛠️ These sentences are factually incorrect, and create a bad false equivalence in student's minds.
>
> The `useEffect` hook allows you to [synchronize a component with an external system](https://react.dev/reference/react/useEffect) and [should *not* be used to perform side effects](https://react.dev/learn/you-might-not-need-an-effect).
>
> Regardless, there is no background here at all. What is a side effect? Why do we need to use `useEffect()`?

```jsx
import React, { useState, useEffect } from 'react';

const Example = () => {
  const [data, setData] = useState([]);

  // 🛠️ This establishes an unsustainable pattern for fetching data from
  // within a component.
  useEffect(() => {
    // Fetch data from an API
    fetch('/api/data')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <ul>
      {data.map((item) => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
  // 🛠️ Again, this is a lot of code to add at once. We should step through
  // this, starting with the `fetch()` call, then add the `useEffect()`, then
  // finally put the data into state with a `useState()` variable.

  // This code will also not work as written. We haven't set up an API at 
  // `/api/data`.
};
```

> 📚 *The `useEffect` Hook takes two arguments: a function to run after every render (the effect), and an optional array of dependencies. If the array is empty, the effect will run only once, similar to `componentDidMount`.*

> 🛠️ What happens when the array isn't empty?

#### Try it out

1. Modify the previous example to fetch data from an API using the `useEffect` Hook.
2. Display the fetched data in a list.
3. Experiment with different dependency arrays and observe the effect's behavior.

> 🛠️ This exercise is poorly constructed - these are kind of "draw the owl"-like steps.

### useContext Hook

> 🛠️ This is probably one of the better explanations, but it's still missing a lot of meaningful information. What does it mean to "consume context"?
>
> Also, if `useEffect()` wasn't already information overload, this definitely is - we don't even cover this in week 1 of React.
>
> This is a poor example of how to `useContext()` is actually implemented. Typically, you'd create a context component and wrap your app in it, then use the `useContext()` hook to access the context value in child components. This example is more of a "how to use the context API" than a "how to use the useContext() hook".

The `useContext` Hook allows you to consume context in functional components, eliminating the need for prop drilling or render prop patterns.

```jsx
import React, { createContext, useState, useContext } from 'react';

const ThemeContext = createContext();

const Example = () => {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <div>
        <Button />
        <Theme />
      </div>
    </ThemeContext.Provider>
  );
};

const Button = () => {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <button
      onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
      style={{ backgroundColor: theme === 'light' ? 'white' : 'black' }}
    >
      Toggle Theme
    </button>
  );
};

const Theme = () => {
  const { theme } = useContext(ThemeContext);

  return <p>Current theme: {theme}</p>;
};
```

> 📚 *The `useContext` Hook allows you to subscribe to React context without introducing nesting through a render prop or higher-order component.*

> 🛠️ So much jargon, where are the real words? What does it mean to "subscribe to React context?" what is "nesting" or a "render prop" or a "higher-order component"?

#### Try it out

1. Create a new context using the `createContext` function.
2. Implement a theme switcher using the `useContext` Hook to consume the theme context in different components.
3. Experiment with updating the context value and observe the changes in the components.

> 🛠️ This exercise is a re-hash of the thing we just did.

## Custom Hooks (30 mins)

> 🛠️ If `useContext()` goes too far this definitely does - not going to review the actual content here.

In addition to the built-in Hooks, you can create your own custom Hooks to encapsulate reusable stateful logic. Custom Hooks allow you to extract component logic into reusable functions.

```jsx
import { useState, useEffect } from 'react';

const useLocalStorage = (key, initialValue) => {
  const [state, setState] = useState(() => {
    const storedValue = window.localStorage.getItem(key);
    return storedValue ? JSON.parse(storedValue) : initialValue;
  });

  useEffect(() => {
    window.localStorage.setItem(key, JSON.stringify(state));
  }, [key, state]);

  return [state, setState];
};

const Example = () => {
  const [value, setValue] = useLocalStorage('my-key', '');

  return (
    <div>
      <input
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      <p>Value from localStorage: {value}</p>
    </div>
  );
};
```

> 📚 *Custom Hooks are JavaScript functions that use React's built-in Hooks under the hood. They allow you to extract and reuse stateful logic across multiple components.*

#### Try it out

1. Create a custom Hook called `useLocalStorage` that manages state with local storage.
2. Use the `useLocalStorage` Hook in a component to store and retrieve data from local storage.
3. Experiment with different keys and initial values, and observe the behavior.

## Debugging Hooks (30 mins)

While Hooks simplify React development, they can also introduce new challenges and potential bugs. Let's explore some common issues and debugging techniques for Hooks.

### Rules of Hooks

React Hooks have two main rules:

1. **Only call Hooks at the top level.** Don't call Hooks inside loops, conditions, or nested functions.
2. **Only call Hooks from React function components.** Don't call Hooks from regular JavaScript functions.

Violating these rules can lead to bugs and inconsistent behavior in your application.

> 📚 *React relies on the order in which Hooks are called to maintain the state between renders. If you violate the rules of Hooks, React won't be able to correctly associate the state with the corresponding Hook calls.*

> 🛠️ This section is good!! That said, the callout is not true, React does not rely on the order in which Hooks are called to maintain the state between renders.

#### Try it out

1. Create a component that violates the rules of Hooks (e.g., call a Hook inside a loop or condition).
2. Observe the warning messages in the console and the incorrect behavior of the component.
3. Fix the code by following the rules of Hooks.

> 🛠️ This is a good exercise!!

### Exhaustive Dependencies

When using the `useEffect` Hook, it's crucial to ensure that the dependency array includes all values from the component scope that could change and cause the effect to re-run. Failing to do so can lead to stale state or unnecessary re-renders.

```jsx
const Example = () => {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  useEffect(() => {
    // This effect will only re-run when the count changes
    // Potential issue: The effect may use a stale value of `name`
    console.log(`Count is ${count}, name is ${name}`);
  }, [count]);

  return (
    <div>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};
```

> 📚 *When you use an effect, it's important to include all values from the component scope that could change and cause the effect to re-run. This includes props, state, and any functions that are defined inside the component.*

> 🛠️ This is a good thing to talk about, but should have been with the `useEffect()` section above!
>
> That said, this is a poor example - there is no need for a `useEffect()` here at all and introduces anti-patterns. We should *only* use `useEffect()` to sync with external systems, not carry out work in React.

#### Try it out

1. Create a component with multiple state variables and an effect that depends on one of them.
2. Observe the potential issue of using stale state in the effect.
3. Fix the issue by adding the missing dependencies to the dependency array.

### Lint Rules

To help catch potential issues with Hooks, you can use the `eslint-plugin-react-hooks` plugin, which provides lint rules for Hooks. This plugin automatically checks for violations of the rules of Hooks and exhaustive dependencies.

> 🛠️ We use vite, so this isn't a crazy rabbit hole, but it absolutely could be if we didn't. However, these settings are already covered by the default `...reactHooks.configs.recommended.rules` vite comes with out of the box. I like this section, but would probably pivot it to talk about that instead. Finally, what file is this?

```json
{
  "plugins": ["react-hooks"],
  "rules": {
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": "warn"
  }
}
```

> 📚 *The `eslint-plugin-react-hooks` plugin is an ESLint plugin that enforces the rules of Hooks and helps catch potential issues with dependencies in the `useEffect` Hook.*

#### Try it out

1. Install the `eslint-plugin-react-hooks` plugin in your project.
2. Configure the plugin in your ESLint configuration file.
3. Introduce violations of the rules of Hooks or missing dependencies in your code.
4. Observe the lint warnings and fix the issues accordingly.

> 🛠️ Again, this is SUCH a rabbit hole to go down if you're not already using eslint in a project. There are a LOT of missing steps here.

## Conclusion (10 mins)

In this lesson, we explored the core concepts of React Hooks, learned how to implement basic Hooks functionality, and covered debugging techniques for common issues. Hooks have become an essential part of modern React development, and mastering them will make you a more efficient and effective React developer.

### Why This Matters

React Hooks are widely adopted in the industry, and proficiency in using them is a valuable skill for any React developer. By understanding Hooks, you can write more concise and maintainable code, leverage code reusability through custom Hooks, and stay up-to-date with the latest React best practices.

### Additional Resources

- [React Hooks Documentation](https://reactjs.org/docs/hooks-intro.html)
- [React Hooks Cheatsheet](https://react-hooks-cheatsheet.com/)
- [Debugging React Hooks](https://reactjs.org/docs/hooks-rules.html)
- [ESLint Plugin for React Hooks](https://www.npmjs.com/package/eslint-plugin-react-hooks)

> 🛠️ Two of these link to the legacy React docs that are not being maintained. The links might also be better if they were used within the appropriate context throughout the lesson instead of just being here at the end.

![React Hooks Diagram](https://i.imgur.com/2LRbFxY.png)
*Diagram illustrating the core React Hooks*

![React Hooks Flow](https://i.imgur.com/iB9eFoH.png)
*Flowchart representing the flow of React Hooks*

> 🛠️ Not sure what these images were supposed to be.
