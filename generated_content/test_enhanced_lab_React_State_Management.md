Here is a lab on React State Management, following the provided format and guidelines:

![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

| Title | Type | Duration | Author |
| --- | --- | --- | --- |
| React State Management Lab | Lab | 8 hours | [Your Name] |

## Learning Objectives

By the end of this lab, you will be able to:

- Build a functional React application that demonstrates proper state management
- Implement key features of React state management, including state lifting and passing data between components
- Test and debug a React state management implementation
- Understand the importance of state management in building complex user interfaces

## Overview

In this multi-day lab, you will build a task management application using React and proper state management techniques. The application will allow users to create, update, and delete tasks, as well as mark tasks as complete. You will learn how to lift state to a common ancestor component and pass data between components efficiently.

### User Stories

- As a user, I want to be able to create a new task.
- As a user, I want to be able to view a list of all my tasks.
- As a user, I want to be able to mark a task as complete.
- As a user, I want to be able to edit an existing task.
- As a user, I want to be able to delete a task.

## Day 1: Setting up the Project

### Step 1: Create a new React project

1. Open your terminal and navigate to the directory where you want to create your project.
2. Run the following command to create a new React project using Create React App:

```bash
npx create-react-app task-manager
```

3. Once the project is created, navigate into the project directory:

```bash
cd task-manager
```

4. Start the development server:

```bash
npm start
```

This will open the React application in your default browser at `http://localhost:3000`.

### Step 2: Understand the project structure

Take a moment to explore the project structure and familiarize yourself with the files and folders. The `src` folder is where you will be working on your React components and managing the application state.

### Step 3: Plan the component structure

Before starting to code, it's essential to plan the component structure for your application. Based on the user stories, you might need components like `TaskList`, `TaskForm`, `TaskItem`, and a parent component to manage the state.

> 💡 It's a good practice to sketch out the component hierarchy and data flow before writing any code.

![Component Hierarchy Diagram](./assets/component-hierarchy.png)

In this diagram, the `App` component is the parent component that will manage the state of tasks. The `TaskList` component will render a list of `TaskItem` components, and the `TaskForm` component will allow users to create and edit tasks.

## Day 2: Building the TaskForm Component

### Step 1: Create the TaskForm component

1. In the `src` folder, create a new file called `TaskForm.js`.
2. Import the necessary dependencies and create a functional component called `TaskForm`:

```jsx
import React, { useState } from 'react';

const TaskForm = () => {
  // Component code goes here
  return (
    <div>
      <h2>Add Task</h2>
      {/* Form fields go here */}
    </div>
  );
};

export default TaskForm;
```

### Step 2: Add form fields

1. Inside the `TaskForm` component, create state variables for the task title and description using the `useState` hook:

```jsx
const [title, setTitle] = useState('');
const [description, setDescription] = useState('');
```

2. Add input fields for the task title and description, and bind them to the corresponding state variables:

```jsx
<input
  type="text"
  placeholder="Task Title"
  value={title}
  onChange={(e) => setTitle(e.target.value)}
/>
<textarea
  placeholder="Task Description"
  value={description}
  onChange={(e) => setDescription(e.target.value)}
></textarea>
```

### Step 3: Add form submission handler

1. Create a function to handle form submission:

```jsx
const handleSubmit = (e) => {
  e.preventDefault();
  // Form submission logic goes here
  setTitle('');
  setDescription('');
};
```

2. Add an `onSubmit` handler to the form:

```jsx
<form onSubmit={handleSubmit}>
  {/* Form fields go here */}
  <button type="submit">Add Task</button>
</form>
```

### Step 4: Test the TaskForm component

1. In the `App.js` file, import the `TaskForm` component:

```jsx
import TaskForm from './TaskForm';
```

2. Render the `TaskForm` component inside the `App` component:

```jsx
function App() {
  return (
    <div>
      <TaskForm />
    </div>
  );
}
```

3. Start the development server and test the `TaskForm` component by adding tasks and observing the console output.

<details>
<summary>Hint: Handling form submission</summary>
When the form is submitted, you should log the task title and description to the console for now. Later, you will pass this data to the parent component to update the task list.
</details>

```jsx
const handleSubmit = (e) => {
  e.preventDefault();
  console.log('Task Title:', title);
  console.log('Task Description:', description);
  setTitle('');
  setDescription('');
};
```

### Checkpoint 🚩

At this point, you should have a working `TaskForm` component that allows users to input task details and logs the form data to the console when submitted.

## Day 3: Managing State in the Parent Component

### Step 1: Lift state to the parent component

1. In the `App.js` file, create a state variable to hold the tasks:

```jsx
const [tasks, setTasks] = useState([]);
```

2. Create a function to add a new task to the task list:

```jsx
const addTask = (newTask) => {
  setTasks([...tasks, newTask]);
};
```

3. Pass the `addTask` function as a prop to the `TaskForm` component:

```jsx
<TaskForm addTask={addTask} />
```

### Step 2: Update the TaskForm component

1. In the `TaskForm.js` file, import the `addTask` prop:

```jsx
const TaskForm = ({ addTask }) => { ... }
```

2. Update the `handleSubmit` function to create a new task object and pass it to the `addTask` function:

```jsx
const handleSubmit = (e) => {
  e.preventDefault();
  const newTask = { id: Date.now(), title, description, completed: false };
  addTask(newTask);
  setTitle('');
  setDescription('');
};
```

### Step 3: Create the TaskList component

1. In the `src` folder, create a new file called `TaskList.js`.
2. Import the necessary dependencies and create a functional component called `TaskList`:

```jsx
import React from 'react';

const TaskList = ({ tasks }) => {
  return (
    <div>
      <h2>Task List</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <h3>{task.title}</h3>
            <p>{task.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
```

### Step 4: Render the TaskList component

1. In the `App.js` file, import the `TaskList` component:

```jsx
import TaskList from './TaskList';
```

2. Render the `TaskList` component and pass the `tasks` state as a prop:

```jsx
<div>
  <TaskForm addTask={addTask} />
  <TaskList tasks={tasks} />
</div>
```

### Checkpoint 🚩

At this point, you should be able to create new tasks using the `TaskForm` component, and the tasks should be displayed in the `TaskList` component.

<details>
<summary>Hint: Debugging state management issues</summary>
If you encounter any issues with state management, make sure to check the following:

- Are you properly lifting state to the parent component?
- Are you passing the correct props to the child components?
- Are you updating state correctly using the state setter function?
- Are you using the correct unique key for mapping over arrays?
</details>

![Task Manager App](./assets/task-manager-app.png)

## Day 4: Implementing Task Completion and Deletion

### Step 1: Add task completion functionality

1. In the `TaskList.js` file, add a checkbox input for each task item:

```jsx
<li key={task.id}>
  <input
    type="checkbox"
    checked={task.completed}
    onChange={() => handleTaskCompletion(task.id)}
  />
  <h3>{task.title}</h3>
  <p>{task.description}</p>
</li>
```

2. In the `App.js` file, create a function to handle task completion:

```jsx
const handleTaskCompletion = (taskId) => {
  setTasks(
    tasks.map((task) =>
      task.id === taskId ? { ...task, completed: !task.completed } : task
    )
  );
};
```

3. Pass the `handleTaskCompletion` function as a prop to the `TaskList` component:

```jsx
<TaskList tasks={tasks} handleTaskCompletion={handleTaskCompletion} />
```

4. In the `TaskList.js` file, import the `handleTaskCompletion` prop and use it as the `onChange` handler for the checkbox input.

### Step 2: Add task deletion functionality

1. In the `TaskList.js` file, add a delete button for each task item:

```jsx
<li key={task.id}>
  <input
    type="checkbox"
    checked={task.completed}
    onChange={() => handleTaskCompletion(task.id)}
  />
  <h3>{task.title}</h3>
  <p>{task.description}</p>
  <button onClick={() => handleTaskDeletion(task.id)}>Delete</button>
</li>
```

2. In the `App.js` file, create a function to handle task deletion:

```jsx
const handleTaskDeletion = (taskId) => {
  setTasks(tasks.filter((task) => task.id !== taskId));
};
```

3. Pass the `handleTaskDeletion` function as a prop to the `TaskList` component:

```jsx
<TaskList
  tasks={tasks}
  handleTaskCompletion={handleTaskCompletion}
  handleTaskDeletion={handleTaskDeletion}
/>
```

4. In the `TaskList.js` file, import the `handleTaskDeletion` prop and use it as the `onClick` handler for the delete button.

### Checkpoint 🚩

At this point, you should be able to mark tasks as complete by checking the checkbox and delete tasks by clicking the delete button.

## Day 5: Implementing Task Editing

### Step 1: Create the TaskEditForm component

1. In the `src` folder, create a new file called `TaskEditForm.js`.
2. Import the necessary dependencies and create a functional component called `TaskEditForm`:

```jsx
import React, { useState } from 'react';

const TaskEditForm = ({ task, updateTask, cancelEdit }) => {
  const [editedTitle, setEditedTitle] = useState(task.title);
  const [editedDescription, setEditedDescription] = useState(task.description);

  const handleSubmit = (e) => {
    e.preventDefault();
    const updatedTask = { ...task, title: editedTitle, description: editedDescription };
    updateTask(updatedTask);
    cancelEdit();
  };

  return (
    <div>
      <h3>Edit Task</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={editedTitle}
          onChange={(e) => setEditedTitle(e.target.value)}
        />
        <textarea
          value={editedDescription}
          onChange={(e) => setEditedDescription(e.target.value)}
        ></textarea>
        <button type="submit">Save</button>
        <button type="button" onClick={cancelEdit}>
          Cancel
        </button>
      </form>
    </div>
  );
};

export default TaskEditForm;
```

### Step 2: Update the TaskList component

1. In the `TaskList.js` file, import the `TaskEditForm` component:

```jsx
import TaskEditForm from './TaskEditForm';
```

2. Add state to track the task being edited:

```jsx
const [editingTask, setEditingTask] = useState(null);
```

3. Create a function to handle task editing:

```jsx
const handleTaskEdit = (task) => {
  setEditingTask(task);
};
```

4. Create a function to handle task update:

```jsx
const handleTaskUpdate = (updatedTask) => {
  updateTask(updatedTask);
  setEditingTask(null);
};
```

5. Create a function to cancel task editing:

```jsx
const cancelEdit = () => {
  setEditingTask(null);
};
```

6. Update the task item rendering to include an edit button and conditionally render the `TaskEditForm` component when a task is being edited:

```jsx
<ul>
  {tasks.map((task) => (
    <li key={task.id}>
      {editingTask && editingTask.id === task.id ? (
        <TaskEditForm
          task={task}
          updateTask={handleTaskUpdate}
          cancelEdit={cancelEdit}
        />
      ) : (
        <>
          <input
            type="checkbox"
            checked={task.completed}
            onChange={() => handleTaskCompletion(task.id)}
          />
          <h3>{task.title}</h3>
          <p>{task.description}</p>
          <button onClick={() => handleTaskEdit(task)}>Edit</button>
          <button onClick={() => handleTaskDeletion(task.id)}>Delete</button>
        </>
      )}
    </li>
  ))}
</ul>
```

### Step 3: Update the App component

1. In the `App.js` file, create a function to handle task updates:

```jsx
const updateTask = (updatedTask) => {
  setTasks(tasks.map((task) => (task.id === updatedTask.id ? updatedTask : task)));
};
```

2. Pass the `updateTask` function as a prop to the `TaskList` component:

```jsx
<TaskList
  tasks={tasks}
  handleTaskCompletion={handleTaskCompletion}
  handleTaskDeletion={handleTaskDeletion}
  updateTask={updateTask}
/>
```

### Checkpoint 🚩

At this point, you should be able to edit tasks by clicking the "Edit" button, which will display the `TaskEditForm` component. After making changes and clicking "Save," the task list should be updated with the edited task details.

<details>
<summary>Hint: Handling task editing</summary>
When editing a task, make sure to:

- Set the `editingTask` state to the task being edited
- Pass the `editingTask` and `updateTask` function as props to the `TaskEditForm` component
- Update the `editingTask` state to `null` after saving the changes or canceling the edit
</details>

## Submission Instructions

Once you have completed the lab, commit your changes and push your code to a GitHub repository. Then, submit the link to your repository to the instructional team for review.

## Why This Matters

State management is a crucial aspect of building complex user interfaces with React. Proper state management techniques, such as lifting state and passing data between components, ensure that your application's data flow is efficient and predictable. This lab has prepared you to handle state management in real-world scenarios, where you may need to build applications with multiple components that interact with each other and share data.

By completing this lab, you have gained hands-on experience with:

- Lifting state to a common ancestor component
- Passing data as