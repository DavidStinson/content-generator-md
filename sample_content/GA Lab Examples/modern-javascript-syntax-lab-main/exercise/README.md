<h1>
  <span class="headline">Modern JavaScript Syntax Lab</span>
  <span class="subhead">Exercise</span>
</h1>

## Introduction

Over the last decade, JavaScript has seen significant changes in its syntax to make it more user-friendly, responding to developers' needs. These updates have become standard in popular frameworks like React, Vue, and Angular.

These changes primarily enhance coding efficiency rather than add new functionality to the language.

## Learning goals

This lab is your opportunity to dive into modern JavaScript syntax. Understanding this contemporary style is beneficial, but a solid grasp of traditional JavaScript is essential. It lays a strong foundation not only for JavaScript but also for learning other programming languages. Remember, not all languages offer such syntax shortcuts.

As a developer, you will encounter languages with unique characteristics, but many, including JavaScript, share foundational concepts. Mastering modern JavaScript syntax without relying on it as a crutch is crucial. This approach ensures you're well-prepared to adapt to different programming languages without starting from scratch.

## Lab structure

Each **Review section** will briefly explain of a modern JavaScript concept, followed by an **exercise** to complete.

## Review: The `map()` iterator method of arrays

An array's [`map()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) returns a new array with the results of calling a function on every element in an existing array.

Put another way, `map()` creates a new array where each element in the original array has been *transformed* by the action specified in the `map()` method's callback function without altering the original array.

Take a look at the example below:

```javascript
const flavors = ['vanilla', 'chocolate', 'strawberry'];

const iceCreamFlavors = flavors.map((flavor) => {
  return `${flavor} ice cream`;
});

console.log(iceCreamFlavors); 
// Prints: ['vanilla ice cream', 'chocolate ice cream', 'strawberry ice cream']
```

In this example, we've used the `map()` method is used to iterate over `flavors` to generate `iceCreamFlavors`. Each element in `iceCreamFlavors` is the result of appending `' ice cream'` to the end of a string element in `flavors`.

The `map()` method will call upon the provided function for every element in `flavors`. When called upon, the function receives the current element being processed as an argument. The value returned from the function is added to the new array.

> 💡 `map()` returns a **new array** with altered values. It does *not* change the original array.

### Exercise 1: Applying `map()`

```javascript
// ! Exercise 1:
// a. Use the `map()` method to iterate over the provided `nums` array
//
// b. Use the callback function of the `map()` method you wrote to
//    create a new array where each value is multiplied by 2.
//    Name the new array `numsTimesTwo`.
//
// c. Console log the new array.
//
// Starting code (don't modify this):

const nums = [13, 87, 2, 89, 12, 4, 90, 63];

// Your code here:

```

## Review: Array destructuring

Array destructuring in JavaScript is a way of unpacking the elements of an array. With array destructuring, we can extract elements from an array and store them in variables with a single line of code.

When we destructure an array, the elements are matched positionally with the variables we define, meaning the order in which we declare variables corresponds with the order of elements in the array.

```javascript
const petsArray = ['Rover', 'Snuffles', 'Toto', 'Spot'];

const [firstPet, secondPet] = petsArray;

console.log(firstPet);
// Prints: 'Rover'
console.log(secondPet);
// Prints: 'Snuffles'

// Equivalent in traditional bracket notation:
console.log(petsArray[0]);
// Prints: 'Rover'
console.log(petsArray[1]);
// Prints: 'Snuffles'
```

In the example above, the first two elements of `petsArray` are unpacked into `firstPet` and `secondPet`.

> 💡 You have complete control of the variable names!

### Exercise 2: Array destructuring

```javascript
// ! Exercise 2:
// a. Given the provided `pizzaToppings` array, use destructuring to extract 
//    the first and second values and place them into variables. Name the 
//    variable that corresponds to the first value `firstIngredient`. Name the 
//    variable that corresponds to the second value `secondIngredient`.
//
// b. Console log the `firstIngredient` and `secondIngredient` variables.
//
// Starting code (don't modify this):

const pizzaToppings = ['Pineapple', 'Olives', 'Anchovies'];

// Your code here:

```

## Review: Object destructuring

Destructuring can also be applied to objects. With object destructuring, we can extract properties from an object. Instead of accessing properties through dot or bracket notation, the values of specific properties in an object can be assigned to variables.

```javascript
const person = {
  name: 'Alex',
  role: 'Software Engineer',
};

// Object destructuring:
const { name, role } = person;

console.log(name);
// Prints: 'Alex'
console.log(role);
// Prints: 'Software Engineer'

// Equivalent in traditional dot notation:
console.log(person.name); 
// Prints: 'Alex'
console.log(person.role); 
// Prints: 'Software Engineer'
```

In the example above, the `person` object is deconstructed to extract the `name` and `role` properties. This approach allows us to access the values of `name` and `role` without using dot notation for each property.

> 🚨 Unlike array destructuring, where elements are matched based on their position, the variables created in object destructuring, such as `const { name, role }`, must match the names of existing properties in the object.

### Exercise 3: Destructuring objects

```javascript
// ! Exercise 3:
// a. Given the provided `car` object, use destructuring to create two
//    variables: `make` and `model` that will hold the respective values.
//
// b. Console log the `make` and `model` variables.
//
// Starting code (don't modify this):

const car = {
  make: 'Audi',
  model: 'Q5',
};

// Your code here:

```

## Review: Applying the spread operator on arrays

The spread operator (`...`) allows us to duplicate or combine arrays. Instead of manually copying elements from one array to another using loops, the spread operator allows us to copy the elements of one array into another directly.

```javascript
const originalArray = [1, 2, 3];
const duplicateArray = [...originalArray];

console.log(duplicateArray); 
// Prints: [1, 2, 3]
```

In the example above, `duplicateArray` is an entirely separate array produced by copying the contents of `originalArray`.

This means that if the `duplicateArray` is modified, those changes won't be reflected in the `originalArray`:

```javascript
duplicateArray.push(4); 
// Using spread created a *copy* of the `originalArray`
// Changing it doesn't also change `originalArray`

console.log(duplicateArray); 
// Prints: [1, 2, 3, 4]
console.log(originalArray); 
// Prints: [1, 2, 3]
```

This differs from simply assigning one array to another, which only creates a *reference*, not a *copy*:

```javascript
const originalArray = [1, 2, 3];
const referenceArray = originalArray; 
// referenceArray a reference to originalArray (not a copy)

referenceArray.push(4); 
// This means modifying `referenceArray` also modifies `originalArray`

console.log(referenceArray); 
// Prints: [1, 2, 3, 4]
console.log(originalArray);
// Prints: [1, 2, 3, 4]
```

The spread operator prevents this issue by ensuring the new array is an independent copy that shares no references with the original. This can be useful when we need to maintain the immutability of the original array.

The spread operator can also merge multiple arrays into one array:

```javascript
const fruits = ['apple', 'orange', 'banana'];
const vegetables = ['broccoli', 'carrot', 'spinach'];

const fruitsAndVegetables = [...fruits, ...vegetables];

console.log(fruitsAndVegetables); 
// Prints: ['apple', 'orange', 'banana', 'broccoli', 'carrot', 'spinach']
```

> 🚨 When merging multiple arrays, be sure to include the spread operator. Not doing so can result in unintentional nesting.

### Exercise 4: Applying the spread operator on arrays

```javascript
// ! Exercise 4: 
// a. Duplicate the provided `morePizzaToppings` array using the spread 
//    operator and assign it to a variable named `uncontroversialPizzaToppings`.
// 
// b. Console log the `uncontroversialPizzaToppings` variable.
//
// Starting code (don't modify this):

const morePizzaToppings = ['Cheese', 'Sauce'];

// Your code here:

```

## Review: Applying the spread operator on objects

The spread operator can also be used to copy objects:

```javascript
const originalObject = {
  foo: 'Hello',
  bar: 100,
};

const clonedObject = { ...originalObject };
console.log('Clone: ', clonedObject); 
// Prints: { foo: 'Hello', bar: 100 }
```

In the example above, we can see how the properties of `originalObject` have been copied over into a new object called `clonedObject`.

The use of the spread operator here differs significantly from direct assignment:

```javascript
const originalObject = {
  foo: 'Hello',
  bar: 100,
};

const clonedObject = originalObject;
clonedObject.foo = 'Goodbye';

console.log(originalObject); 
// Prints: { foo: 'Goodbye', bar: 100 }
```

The example above demonstrates a pitfall of attempting to clone an object **without the spread operator**. When `clonedObject` is assigned `originalObject` directly, it doesn't create a new, independent object. This behavior is identical to not using the spread operator to duplicate an array.

Instead, `clonedObject` becomes a reference to `originalObject`. This means any changes made to `clonedObject` also affect `originalObject`, as they both point to the same data.

Like with arrays, this issue can be remedied when we apply the spread operator:

```javascript
const originalObject = {
  foo: 'Hello',
  bar: 100,
};

// Copy the properties of `originalObject`:
const clonedObject = { ...originalObject };

// Update the properties of `clonedObject`:
clonedObject.foo = 'Goodbye';
clonedObject.bar = 0;

console.log('Original: ', originalObject);
// Prints: { foo: 'Hello', bar: 100 }
console.log('Clone: ', clonedObject);
// Prints: { foo: 'Goodbye', bar: 0 }
```

With the spread operator, `clonedObject` is a brand new object with a separate copy of the data from `originalObject`. Now, modifying `clonedObject` will not impact the `originalObject`

### Exercise 5: Applying the spread operator on objects

```javascript
// ! Exercise 5:
// a. Duplicate the provided `anotherCar` object and spread its values into a 
//    new variable named `myCar`.
//
// b. Change the `make` and `model` properties of the `myCar` object to new 
//    values.
//
// c. Console log both objects and observe the results.
//
// Starting code (don't modify this):

const anotherCar = {
  make: 'Toyota',
  model: 'RAV4',
};

// Your code here:

```

## Review: Dynamic keys in objects

Variables and expressions can be used as dynamic keys in an object by using bracket notation. Dynamic keys can be used to create, access, and modify properties in an object. Dynamic keys enhance our ability to access data.

This approach is handy in scenarios where key names are not known ahead of time or when they need to be computed on the fly. It also allows for more concise and readable code, avoiding the need for additional steps when assigning properties to objects.

Check out how `selectedFruit` is used as a dynamic key in this code:

```javascript
const fruitInventory = {
  apples: 2,
  oranges: 4,
};

const selectedFruit = 'apples';
// Using the `selectedFruit` variable as a dynamic key:
const selectedFruitCount = fruitInventory[selectedFruit];

console.log(selectedFruitCount);
// Prints: 2
```

This technique can be extended to the creation of objects, where property names are determined dynamically:

```javascript
const fruitType = 'bananas';

// Using the `fruitType` variable as a dynamic key:
const fruitInventory = {
  [fruitType]: 5,
};

console.log(fruitInventory); 
// Prints: { bananas: 5 }
```

Using square brackets (`[]`) around `fruitType` in the object declaration tells JavaScript to use the variable's value as the property name. Without the brackets, the string `'fruitType'` would be used as the key rather than its value (`'bananas'`).

### Exercise 6: Dynamic keys in objects

```javascript
// ! Exercise 6:
// a. Define a variable named `propertyName` and assign a string (like 
//    'username', 'age', or 'email') to it.
// 
// b. Create an object named `userProfile`. 
// 
// c. Use `propertyName` as a dynamic key in `userProfile`. Assign it a 
//    relevant value.
//
// d. Console log the `userProfile` object to see the result.
//
// Your code here:

```

## Review: `import` and `export`

The `import` and `export` syntax allows us to share code between different files in JavaScript. This is a more modern and native approach compared to the `require` and `module.exports` syntax used in CommonJS.

With `export`, you can make functions, objects, or primitives available for use in other files.

There are two main types of exports:

1. **Named exports**: For exporting multiple items from a file:

   ```javascript
   export const myNumber = 123;
   export const myString = 'Hello';
   ```

2. **Default exports**: For exporting a single item from a file:

   ```javascript
   export default function superCoolFunction() {
     /* ... */
   }
   ```

> 🏆 It's possible to mix default and named exports in a single module, but it's a best practice to stick to one style for consistency and clarity. Named exports are often preferred over default exports.

Using `import`, you can bring those exported items into another file.

1. **Importing named exports**:

   ```javascript
   import { myNumber, myString } from './myData.js';
   ```

2. **Importing a default export**:

   ```javascript
   import superCoolFunction from './superCoolFunction.js';
   ```

You can also import all named exports as a single object, which is useful when dealing with modules that export several items:

```javascript
import * as MyData from './myData.js';
console.log(MyData.myNumber);
console.log(MyData.myString);
```

This allows for more organized code by separating concerns into modules.

### Exercise 7: Import and Export

Follow the steps below for some practice with `import` and `export`. Update the values for `default`, `age`, and `job` accordingly:

1. Initialize a node project:

   ```bash
   npm init -y
   ```

2. Add the following property as a new line in the `package.json` file:

   ```json
   "type": "module",
   ```

3. Create two files: `exportingFile.js` and `importingFile.js`:

   ```bash
   touch exportingFile.js
   touch importingFile.js
   ```

4. In `exportingFile.js`, add the following:

   ```javascript
   export default 'Matt';
   ```

5. In `importingFile.js`, add the following:

   ```javascript
   import name from './exportingFile.js';

   console.log(name);
   // Prints: Matt
   ```

6. Run `importingFile.js` like so:

   ```bash
   node importingFile.js
   ```

7. To export additional values, update `exportingFile.js` like so:

   ```javascript
   export default 'Matt';
   export const computer = 'MacBook Pro'

   const age = 43;
   const job = 'programmer';

   export {age, job}
   ```

   These additions can be imported by updating `importingFile.js` like so:

   ```javascript
   import name, { computer, age, job } from './exportingFile.js';

   console.log(name, computer, age, job);
   // Prints: 'Matt', 'MacBook Pro', 43, 'programmer'
   ```

## Review: Default parameters

Default parameters are just that - default values for parameters. These defaults are applied when no value is passed for those parameters during a function call.

Take this example:

```javascript
function addTwoNumbers(numA, numB) {
  return numA + numB;
}

addTwoNumbers(2);
```

This will return `NaN` because the value of `numB` is `undefined`.

Let's apply some defaults to the `numB` parameter:

```javascript
function addTwoNumbers(numA, numB = 2) {
  return numA + numB;
}

addTwoNumbers(2);
```

Now, this function will return the number `4`. What if we also give a default to `numA`?

```javascript
function addTwoNumbers(numA = 1, numB = 2) {
  return numA + numB;
}

addTwoNumbers(2);
```

This function is still going to return the number `4`. The default value of `1` on `numA` will be overridden by the value of `2` that we passed in.

### Exercise 8: Default parameters

```javascript
// ! Exercise 8:
// a. Create a function with two parameters, `noun` and `adjective`.
// 
// b. Give `noun` a default value of "cat" and `adjective` a default value of 
//    "orange".
//
// c. The function should log a sentence 'The cat is orange.' by default, but 
//    should substitute the appropriate parameters when it is supplied with 
//    arguments.
//
// Your code here:

```

## Review: The ternary operator

The ternary operator gives us a way to handle conditional logic in a single line of code. Ternaries can be viewed as a more concise version of an `if...else` statement. It can also simplify assigning a value to a variable based on a condition.

A ternary consists of three parts:

1. **Condition**: A boolean expression evaluated for truthiness, placed before the `?`.
2. **True Expression**: The value assigned to the variable if the condition is `true`, located immediately after the `?`.
3. **False Expression**: The value assigned to the variable if the condition is `false`, following the `:`.

Consider the following example using an `if...else` statement:

```javascript
const age = 22;
let access;

if (age > 21) {
  access = 'Yes';
} else {
  access = 'No';
}

console.log(access); // 'Yes'
```

This logic can be streamlined using a ternary:

```javascript
const age = 22;
let access = age > 21 ? 'Yes' : 'No';

console.log(access); // 'Yes'
```

> 💡 The ternary operator is a powerful tool for simplifying conditional expressions, making it ideal for straightforward assignments based on a single condition.

### Exercise 9: Ternary operator

```javascript
// ! Exercise 9:
// a. Convert the following `if...else` statement into a ternary:
//
//    if (pizza === 'tasty') {
//      console.log('yum');
//    } else {
//      console.log('yuck');
//    }
//
// Starting code (don't modify this):

const pizza = 'tasty';

// Your code here:

```

## Review: Boolean gates

Logical operators such as `&&` (AND) and `||` (OR) play an interesting role when used outside of `if...else` statements. In this context, they can be used to evaluate and return values directly based on the truthiness or falsyness of the values involved.

1. **The `&&` operator**

   The `&&` operator evaluates expressions from left to right and returns the **first falsy value** it encounters. If all values are truthy, it returns the last value.

   Let's take a look at a few examples of the `&&` operator at work:

   - When the first expression (`false`) being evaluated is falsy, `result` will be assigned that value (`false`).

     ```javascript
     const result = false && 'foo';
     console.log(result);
     // Prints: false
     ```

   - When the first value is truthy (`'hello'`) and the second value is falsy (`''`), `result` is assigned the empty string (`''`), as it is the first falsy value encountered.

     ```javascript
     const result = 'hello' && '';
     console.log(result);
     // Prints: ''
     ```

   - When both values are truthy, the result is the value of the last expression (`'bar'`).

     ```javascript
     const result = 'foo' && 'bar';
     console.log(result); 
     // Prints: 'bar'
     ```

   > 💡 Remember, in JavaScript, falsy values include `''` (empty strings), `0`, `null`, `undefined`, `NaN`, and `false`. Everything else is considered truthy.

2. **The `||` operator**

   The `||` operator evaluates expressions from left to right and returns the **first truthy value** it encounters. If all values are falsy, it returns the last value.

   Let's take a look at a few examples of the `||` operator at work:

   - When the first expression (`''`) is falsy, `result` is assigned `'foo'` as it's the first truthy value.

     ```javascript
     const result = '' || 'foo';
     console.log(result);
     // Prints: 'foo'
     ```

   - If the first value (`2`) is truthy, the evaluation stops, and `result` is assigned the first value (`2`).

     ```javascript
     const result = 2 || 0;
     console.log(result);
     // Prints: 2
     ```

   - When all values being evaluated are falsy (`''` and `0`), `result` is assigned the last value (`0`), as no truthy value is found.

     ```javascript
     const result = '' || 0;
     console.log(result);
     // Prints: 0
     ```

   > 💡 The `||` operator can be helpful for setting fallback or default values.

Keeping what you've learned so far in mind, can you guess what the values of the variables will be?

```javascript
const result1 = 'bar' && 'foo';
const result2 = false || 243;
const result3 = 42 && false;
const result4 = myVar || 3000;

console.log('result1:', result1);
console.log('result2:', result2);
console.log('result3:', result3);
console.log('result4:', result4);
```

### Exercise 10: Boolean gates

In modern JavaScript, a common pattern is to assign a default value to variables if no specific value is provided. This technique is instrumental in settings where configurations might be optional.

For example, users might not set their language or theme preferences on a website, and you'd want to fall back to some default settings.

Now that you've seen how to assign default values using the logical OR operator let's try it out with a direct application:

- Let's assume we have a variable called `localLangConfig` that might contain a language code (like `'es'` for Spanish, `'fr'` for French) or might be `null` if no language is selected.
- Your task is to create a variable `lang` that should use the value from `localLangConfig` if it's not null. If `localLangConfig` is null, set `lang` to a default value, `'en'` (representing English).

```javascript
// ! Exercise 10:
// ! 10.1: Set language
// a. Construct a single line of code that assigns a default value using the 
//    logical OR operator. This line should match the logic of the following 
//    statement:
//
//    "lang is equal to localLangConfig or the default value of English."
//
// b. Create a variable called `lang`.
//
// c. Assign `lang` the value of localLangConfig or 'en' as a default if 
//    `localLangConfig is falsy.
//
// d. Log the value of `lang` to the console.
//
// Your code here (localLangConfig is provided to get you started):

// Simulated language configuration (change this variable to test)
const localLangConfig = null; // Change to 'es', 'fr', etc., or leave it `null`.

```

Now, let's try this same pattern to set a user's preferred theme on a website:

```javascript
// ! 10.2: Set website theme
// Intro: In this exercise, you'll construct a single line of code that assigns 
//        a default value to a variable named `theme` using the logical OR 
//        operator. This line should match the logic of the following statement:
//
//        "theme is equal to savedUserTheme or the default value of light."
//
// a. Create a variable called `theme`.
//
// b. Assign `theme` the value of `savedUserTheme` or 'light' as a default.
//
// c. Log the value of `theme` to the console.
//
// Your code here (`savedUserTheme` is provided to get you started):

// Simulated user theme preference (change this variable to test)
const savedUserTheme = null; // Change to 'dark', etc., or leave it `null`.

```

### Review: Optional chaining

Optional chaining is a way to access deeply nested properties in an object safely. This approach helps us avoid errors when we attempt to access `undefined` or `null` properties.

Consider a scenario where we attempt to access a property that doesn't exist, which normally results in an error:

```javascript
const adventurer = {
  name: 'Alice',
};

console.log(adventurer.dog.name); 
// TypeError: Cannot read properties of undefined (reading 'name')
```

In this application, it's probable that the `dog` property might be added in later. This is where some optional chaining might prove helpful.

Using `console.log(adventurer.dog?.name)` will allow our code to run without an error:

```javascript
const adventurer = {
  name: 'Alice',
};

let dog = adventurer.dog?.name;

console.log(dog); // undefined
```

Instead of the non-existent property causing an error, our code now logs `undefined`.

### Exercise 11: Optional chaining

```javascript
// ! Exercise 11:
// a. Use optional chaining in a console.log so that a console log of
//    `adventurer.cat.age` returns `undefined` instead of an error.
//
// Starting code (don't modify this):

const adventurer = {
  name: 'Alice',
};

// Your code here:

```
