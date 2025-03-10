---
title: Methods and Scope
type: Lesson
duration: "1:25"
creator:
  name: Kristen Tonga
  city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Methods and Scope

## Learning Objectives
At the end of this lesson, students will be able to:
- Describe how parameters relate to methods.
- Compare different types of variable scope.
- Identify the parts of a method.
- Use naming conventions for methods and variables.

## Lesson Guide

| Timing  | Type  | Topic  |
|:-:|---|---|
| 5 min | [Intial Setup](https://git.generalassemb.ly/ENT-JAVA-Accelerator/methods-and-scope/blob/main/README.md#initial-setup)  | Setting Up GHE |
| 5 min | [Opening](https://git.generalassemb.ly/ENT-JAVA-Accelerator/methods-and-scope/blob/main/README.md#opening-5-min)|Learning Objectives |
| 5 min | [Introduction](https://git.generalassemb.ly/ENT-JAVA-Accelerator/methods-and-scope/blob/main/README.md#introduction-writing-methods-5-min)|Writing Methods |
| 15 min| [Demo](https://git.generalassemb.ly/ENT-JAVA-Accelerator/methods-and-scope/blob/main/README.md#demo-lets-break-it-down-15-min)   | Let's Break It Down |
| 10 min | [Independent Practice](https://git.generalassemb.ly/ENT-JAVA-Accelerator/methods-and-scope/blob/main/README.md#independent-practice-discuss-10-min)  | Discuss |
| 10 min | [Demo](https://git.generalassemb.ly/ENT-JAVA-Accelerator/methods-and-scope/blob/main/README.md#demo-more-methods-10-min)  | More Methods |
| 15 min | [Independent Practice](https://git.generalassemb.ly/ENT-JAVA-Accelerator/methods-and-scope/blob/main/README.md#independent-practice-write-a-few-methods-15-min)  | Write a Few Methods |
| 5 min  | [Conclusion](https://git.generalassemb.ly/ENT-JAVA-Accelerator/methods-and-scope/blob/main/README.md#conclusion-5-min) | Review/Recap |

## Initial Setup

1. Open your terminal.
2. To access the `java-accelerator` directory, navigate to it from your home directory by entering the
   command `cd ~/java-accelerator`.
3. Go back to the browser window and click the **Fork** button located in the upper right corner of the repository page to create a copy of the repository under your own **GitHub Enterprise** account.
4. Once you have forked the repository, you will have your own copy under your GitHub Enterprise account.
    - Copy the URL of your forked repository, which will look like: `https://git.generalassemb.ly/username/repo-name`.
5. Click the **GREEN** Code button and then click the clipboard icon next to the **SSH URL** to copy the .git path.
6. Navigate back to the terminal and to the directory where you want to clone the repository. Enter the command `git clone`, followed by the `SSH URL` you just copied. This will clone the repository into your local machine.
7. Open this directory in JetBrains IntelliJ IDE by selecting Open from the IDE's welcome screen or using the menu
   option `File` > `Open`... and choosing the `methods-and-scope` folder.

## Opening (5 min)

We've previously covered variables and data types — two important building blocks for all programming languages. Today, we'll learn about two more topics: methods and scope. **Methods** are reusable chunks of code that complete some task, while **scope** defines where the variables actually have relevance in your program.

----

## Introduction: Writing Methods (5 min)

#### `main` Method

We've already met a method: the `main` method. Every Java program needs it. It's the entry point to the rest of the application, and it will invoke all of the other methods required by your program.

Let's briefly review it:

```java
public static void main(String[] args)
```

-----

## Demo: Let's Break It Down (15 min)

Let's look at what each part of this method does. We'll start with the basics, which we covered a bit in explaining the `main` method.

<!-- **Instructor Note**: Write the method on the board (or add `body` to the `main` method signature at the appropriate time) and underline and label each part as you go through the following sections.-->

```java
public                       void            interestingMethod(  String input  )     throws IOException
//<modifiers or visibility>  <return type>   <method name>    (  <parameters>  )     <exception list>
{
<opening brace>
    System.out.println("I am making " + input + " interesting.")
    <method body>
}
<closing brace>

```

#### Modifiers

Modifiers are used to modify how a method can be called.

Access modifiers include:
- **`private`**: Visible only to the class.
- **`protected`**: Visible to the package and all subclasses.
- **`public`**: Visible to the world.

When no access modifier is specified, the method is only visible to the class and package.

Non-access modifiers include:
- **`static`**: For creating class methods and variables.
- **`final`**: For making something permanent.
- **`abstract`**: For creating abstract classes and methods.
- **`synchronized`**: For threads.

We'll explain more of what all of these keywords mean in later lessons. For now, use `public`.

<!--**Instructor Note**: Refer back to `main` method and point out `static` modifier. Maybe eliminate `static` from a method and point out the error. -->

Any method called from within a `static` context must also be `static`. So for now, use `public static` for all methods. Again, we'll explain more on what this means later.

#### Return Type

A method can return a value, but the type of that returned value must be specified so the calling method knows what to do with it.

Let's see how that works. Create a new Java program using the given console template from Eclipse, or create a basic class with an inner `main` method. Then, code the two methods below. Use the commented `print` statements to explain local scope.

The problem:

```java
class Main {
    int mySum;
    
    public static void main(String[] args) {
        getSum();
        // System.out.println(sum); // not available
    }
    
    public static void getSum() {
        int sum = 2 + 2;
        System.out.println(sum);
    }
  }
```

The solution:

```java
class Main {
    int mySum;
    
    public static void main(String[] args) {
        int returned = returnSum();
        System.out.println(returned);
    }
    
    // public static void getSum() {
        // int sum = 2 + 2;
        // System.out.println(sum);
    // }
    
    public static int returnSum() {
        int sum = 2 + 2;
        System.out.println(sum);
        return sum;
    }
  }
```

A method executes until it reaches a `return` statement or a closing curly brace. If a data type has been specified, that data (or `null`) must be returned, or the code will not compile.

----

## Independent Practice: Discuss (10 min)

Take five minutes and discuss the following questions with the person next to you:

- What are some data types a method could return?
- Why might you want to return a value from a method?

Be ready to share your answers to the class.

-----

## Demo: More Methods (10 min)

#### Method Name

The method name is what the method is called. It's important to be explicit in naming your method so that, when a new developer comes in, they'll understand what the method does just by looking at its name.

By convention, a method name should be a **verb** in **camel case** — just like variable names. For example: `getName()`, not `GetName()` or `getname()` or `get_name()`.

#### Parameters (Enclosed Within Parentheses)

Parameters are arguments passed into a method when it's called. This makes the method more dynamic.

Let's look back at the `returnSum()` method.

> **Knowledge Check**: What would you need to do if you wanted to pass a number to this method?

```java
public static int returnSum(int num1) {
    int sum = num1 + num1;
    return sum;
}
```

> **Knowledge Check**: How about two numbers?

```java
public static int returnSum(int num1, int num2) {
    int sum = num1 + num2;
    return sum;
}
```

Note that the method can be called like so:

```java
public static void main(String[] args) {
    int returned = returnSum(2,4);
    System.out.println(returned);
    
    int returned = returnSum(10,52);
    System.out.println(returned);
}
```

<!--**Instructor Note**: Emphasize the ability to reuse code without rewriting it. Remind students of the DRY principle.-->

It's also possible to have a return type for an unknown number of arguments, which can be declared like this:

```java
public static void myMethod(String... vars) {}
```

Or like this:

```java
public static void myMethod(String[] vars) {}
```

These two signatures are the same thing under the hood.

> **Knowledge Check**: From where does the last one look familiar?

Like `main`, `myMethod()` will take an indefinite amount of parameters of the type `String`. For now, just know that it exists.

In Java, if a method declares a parameter, that **parameter** is required to be sent as an **argument** from the calling method.

#### Method Body (Enclosed Within Curly Braces)

This is where the main functionality of your method will be called.


## Independent Practice: Write a Few Methods (15 min)

Create a new Java project in Eclipse and work through as many of these exercises as you can within the next 15 minutes. Use the official [Oracle Java Docs](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html) to help you through these exercises and look up the different class methods available.

1. Write a method called `divide152By()`. It should accept a number as an argument and divide `152` by the given number. For example, the `divide152By` result of `2` — `152/2` — is `76`. Your method should return the result.

   Use your method to find the following:

    ```java
    divide152By(3);
    divide152By(43);
    divide152By(8);
    ```

2. Write a method called `transmogrifier()`. This method should accept three arguments, which you can assume will be numbers. Your method should return the "transmogrified" result, which is the product of the first two numbers raised to the power of the third number. For example, the transmogrified result of `5`, `3`, and `2` — `(5 times 3) to the power of 2` — is `225`.

   Use your method to find the following:

    ```java
    transmogrifier(5, 4, 3);
    transmogrifier(13, 12, 5);
    transmogrifier(42, 13, 7);
    ```


## Conclusion (5 min)

- Why do we use methods?
- When might you use a method?

## Resources

- [Oracle Java Docs: Defining Methods](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html)
- [Oracle Java Docs: A Closer Look at the "Hello World!" Application](https://docs.oracle.com/javase/tutorial/getStarted/application/)
- [Princeton: Java Programming Cheat Sheet](http://introcs.cs.princeton.edu/java/11cheatsheet/)
- [Java Modifier Types](http://www.tutorialspoint.com/java/java_modifier_types.htm)
- [Princeton: Recursion](http://introcs.cs.princeton.edu/java/23recursion/)
