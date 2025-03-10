<h1>
  <span class="headline">Lifting State in React Lab</span>
  <span class="subhead">Create a Reusable <code>Ingredient</code> Component</span>
</h1>

## Component thought

Reusing components by making them more abstract and able to be used across various situations is a core concept of React. Complete the below exercises to help accomplish better reusability.

1. Create a component called `Ingredient` that can be reused by both `src/components/IngredientList/IngredientList.jsx` and `src/components/BurgerStack/BurgerStack.jsx`. It should display the `name` of a single ingredient, and conditionally render the add or remove button based on its parent.

2. Apply conditional rendering within `src/components/BurgerStack/BurgerStack.jsx`, so that a message of 'No Ingredients' is displayed if there are no ingredients in the `stack`.
