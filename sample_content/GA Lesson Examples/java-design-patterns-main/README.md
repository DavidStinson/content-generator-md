# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Design Patterns

| Title           | Type   | Duration | Author               |
|-----------------|--------|----------|----------------------|
| Design Patterns | Lesson | 4:00     | Suresh Melvin Sigera |

## Learning objectives

- Understand the concept of design patterns and their importance in software engineering.
- Recognize the different categories of design patterns: creational, structural, and behavioral.
- Identify common design patterns used in Java development, such as Singleton, Factory Method, Abstract Factory, and
  Builder.
- Understand the intent, structure, and participants involved in each design pattern.
- Learn when and why to apply specific design patterns to solve recurring design problems in Java applications.
- Recognize the benefits and drawbacks of using design patterns, including considerations for performance, scalability,
  and maintainability.

### Initial Setup

1. Open your terminal.
2. To access the `java-accelerator` directory, navigate to it from your home directory by entering the
   command `cd ~/java-accelerator`.
3. Go back to the browser window and click the **Fork** button located in the upper right corner of the repository page to create a copy of the repository under your own **GitHub Enterprise** account.
4. Once you have forked the repository, you will have your own copy under your GitHub Enterprise account.
    - Copy the URL of your forked repository, which will look like: `https://git.generalassemb.ly/username/repo-name`.
5. Click the **GREEN** Code button and then click the clipboard icon next to the **SSH URL** to copy the .git path.
6. Navigate to the directory `java-design-patterns` by entering `cd java-design-patterns` in your terminal.
7. Open this directory in JetBrains IntelliJ IDE by selecting Open from the IDE's welcome screen or using the menu
   option `File` > `Open`... and choosing the `java-design-patterns` folder.

### What is a design pattern? (15 minutes)

A design pattern offers a standardized, reusable strategy to tackle frequent challenges encountered in software design.
These patterns are classified into various types, each aimed at addressing distinct issues or a combination thereof.

Notably, common design patterns are grouped into three main categories: creational patterns, which are concerned with
the mechanisms of object creation, ensuring flexibility and clarity in the instantiation process; structural patterns,
which pertain to how objects and classes are composed or structured to form larger structures, often focusing on
simplifying designs or enhancing the functionality of the system without altering its interface; and behavioral
patterns, which are centered around effective communication and the assignment of responsibilities between objects and
classes.

This structured approach to problem-solving not only enhances code efficiency and readability but also facilitates the
development process by providing tested, proven development paradigms.

### Singleton design pattern:

The Singleton design pattern is a sophisticated creational strategy aimed at solving a common issue in object-oriented
programming: ensuring a class generates a single instance, while also offering a universally accessible point to this
instance. It's particularly useful in scenarios where multiple objects need to coordinate actions across a system.

At the heart of the Singleton pattern is the principle of restricting object creation to one instance, thereby granting
controlled, global access to that instance. This singular control over resource instantiation is pivotal for a variety
of applications, including managing access to a shared resource, such as a file or a database connection, or when
implementing a centralized system for managing state or configurations across an application.

**Implementing the Singleton pattern involves several key steps**:

- **Private Constructor**: To prevent external instantiation, the class constructor is made `private`.
- **Private Static Instance**: The class maintains a `private`, `static` instance of itself.
- **Public Static Method**: This method, often named `getInstance()`, allows external access to the Singleton instance.
  On its first call, it creates the class instance and stores it in a static field. On subsequent calls, it returns the
  already created instance.

This design pattern ensures that the class is only instantiated once. The stored instance is returned on all future
calls to the `getInstance()` method, thus maintaining a single, global instance accessible throughout the application.

#### Advantages of Singleton Pattern:

- Controlled Access: It provides a controlled access point to a shared resource, ensuring that concurrent access does
  not create conflicting changes.
- Lazily Loaded, Memory Efficient: The instance is created only when it's needed for the first time, promoting efficient
  memory usage.
- Global State Management: Singleton offers a neat way to manage a global state or shared resources in an application.

#### Considerations and Criticisms (10 minutes):

While the Singleton pattern has its benefits, it's also subject to criticism, especially regarding its impact on
software testing, its promotion of global state (which is generally discouraged in software design principles), and
challenges in a multithreaded environment that requires careful handling to ensure the instance is created only once.

Moreover, the pattern's reliance on a global instance can introduce tight coupling between classes, making it harder to
test the classes that depend on the Singleton. This is because the pattern does not inherently provide a way to mock or
replace the Singleton instance during testing, although techniques such as dependency injection can mitigate this issue.

Despite these criticisms, the Singleton pattern remains a powerful tool in the software developer's toolkit,
particularly when its use is carefully weighed against the specific needs and constraints of the application being
designed.

### Code along : Singleton design pattern in action (20 minutes)

To illustrate the Singleton pattern in action, let's consider a classic example: a database connection manager. In many
applications, maintaining a single database connection pool is crucial for resource management and performance
optimization. Using the Singleton pattern, we can ensure that only one connection pool instance is created and it's
accessible globally across the application.

```java
package org.example.codealong.singleton;

import java.sql.Connection;

import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnectionManager {
    private static DatabaseConnectionManager instance;
    private Connection connection;

    private DatabaseConnectionManager() {
        try {
            // Load the H2 database driver
            Class.forName("org.h2.Driver");

            // Establish a connection to an H2 in-memory database
            String url = "jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1";
            String user = "sa"; // Default username is 'sa'
            String password = ""; // Default password is empty
            this.connection = DriverManager.getConnection(url, user, password);
        } catch (ClassNotFoundException | SQLException e) {
            // Handle potential exceptions
            System.out.println("Database connection creation failed.");
            e.printStackTrace();
        }
    }

    public static synchronized DatabaseConnectionManager getInstance() {
        if (instance == null) {
            instance = new DatabaseConnectionManager();
        }
        return instance;
    }

    public Connection getConnection() {
        return this.connection;
    }

    public static void main(String[] args) {
        // Request a connection multiple times
        Connection conn1 = DatabaseConnectionManager.getInstance().getConnection();
        Connection conn2 = DatabaseConnectionManager.getInstance().getConnection();
        Connection conn3 = DatabaseConnectionManager.getInstance().getConnection();

        // Compare and print out the connection references
        System.out.println("Database connection 1 established: " + conn1);
        System.out.println("Database connection 2 established: " + conn2);
        System.out.println("Database connection 3 established: " + conn3);

        // Demonstrating that the DatabaseConnectionManager instance is the same
        System.out.println("Is DatabaseConnectionManager instance the same for conn1 and conn2? " +
                (DatabaseConnectionManager.getInstance() == DatabaseConnectionManager.getInstance()));

        // Comparing connection object references directly
        System.out.println("Do conn1, conn2, and conn3 refer to the same object? " +
                (conn1 == conn2 && conn2 == conn3));
    }
}


```

This setup instantiates a `DatabaseConnectionManager` Singleton that establishes a connection to an H2 in-memory
database. The Singleton ensures that only one database connection is made, and it can be accessed globally throughout
the application.

### Factory design pattern (10 minutes)

The Factory Method pattern is a fundamental creational design pattern widely used in object-oriented software
development. It encapsulates the creation of objects within a class hierarchy, allowing clients to create instances of
objects without needing to know the exact class of the object being instantiated. This promotes loose coupling between
the client code and the classes being instantiated, enhancing flexibility and maintainability in the codebase.

At its core, the Factory Method pattern defines an interface for creating objects but allows subclasses to alter the
type of objects that will be created. This is achieved by defining a separate method, typically named something like "
factoryMethod," within an abstract base class. Subclasses then override this method to instantiate specific types of
objects that adhere to a common interface or are part of a related family of objects.

One of the key benefits of the Factory Method pattern is its ability to delegate the responsibility of object creation
to subclasses. This means that the decision-making process regarding which concrete class to instantiate is
decentralized, allowing each subclass to determine the appropriate type of object to create based on specific
requirements or conditions.

By using the Factory Method pattern, developers can introduce new types of objects into the system without modifying
existing client code. This promotes scalability and extensibility, as the addition of new subclasses enables the
creation of diverse sets of objects while maintaining compatibility with the existing codebase.

Furthermore, the Factory Method pattern is often used in conjunction with other design patterns, such as the Abstract
Factory pattern, to create families of related objects. In such cases, the Factory Method is responsible for creating
individual objects within a family, while the Abstract Factory coordinates the creation of entire families of related
objects.

In summary, the Factory Method pattern provides a flexible and scalable solution for object creation in object-oriented
systems. By encapsulating the instantiation process within subclasses, it promotes loose coupling, extensibility, and
maintainability in software development projects.

#### Advantages of Factory Pattern (10 minutes):

- **Encapsulation**: Factory pattern encapsulates the object creation logic, separating it from the client code. This
  promotes loose coupling between the client and the created objects.
- **Flexibility and Extensibility**: It allows for easy extension and modification of the object creation process. New
  types of objects can be added without altering existing client code, making the system more flexible and easily
  maintainable.
- **Abstraction**: Factory pattern provides an abstraction layer over object creation, allowing clients to work with
  interfaces or abstract classes rather than concrete implementations. This promotes code scalability and modifiability.
- **Centralized Control**: Object creation logic is centralized within the factory class, making it easier to manage and
  control the creation process. Any changes or updates to the creation logic can be applied uniformly across the system.
- **Decoupling**: Factory pattern decouples the client code from the specific types of objects being created, allowing
  clients to focus on their primary responsibilities without being concerned about object creation details.

#### Considerations and Criticisms (10 minutes):

- **Complexity**: In some cases, implementing a factory pattern may introduce additional complexity to the system,
  especially when dealing with a large number of object types or complex object creation logic.
- **Overhead**: Introducing a factory class may add some overhead to the application, particularly if the factory needs
  to be instantiated frequently or if the object creation process is resource-intensive.
- **Reduced Control**: While factory pattern promotes encapsulation and abstraction, it may also reduce the control that
  clients have over the creation process. Clients relying on a factory may have limited control over the specific
  attributes or configurations of the created objects.
- **Dependency Inversion Principle** (DIP): In some cases, the use of factory pattern may violate the Dependency
  Inversion Principle, especially if the factory class becomes a high-level module depending on low-level modules (the
  concrete classes being created).
- **Increased Complexity of Testing**: Testing code that relies heavily on factory pattern may become more complex, as
  it may involve mocking or stubbing factory objects to isolate the behavior being tested.

### Code along : Factory pattern in action (20 minutes)

Let's consider an example scenario where we have a software application for a car manufacturing company. The application
needs to create different types of cars, such as sedans, SUVs, and trucks. Instead of directly instantiating these types
of cars in the client code, we can use the Factory Method pattern to create them.

First, we define an interface or an abstract base class `Car` that represents the common behavior of all cars:

```java
package org.example.codealong.factory;

public interface Car {
    void drive();
}

```

Next, we create concrete implementations for each type of car, implementing the `Car` interface:

```java
package org.example.codealong.factory;

public class Sedan implements Car {
    @Override
    public void drive() {
        System.out.println("Driving a sedan");
    }
}

```

```java
package org.example.codealong.factory;

public class SUV implements Car {
    @Override
    public void drive() {
        System.out.println("Driving a SUV");
    }
}

```

```java
package org.example.codealong.factory;

public class Truck implements Car {
    @Override
    public void drive() {
        System.out.println("Driving a Truck");
    }
}

```

Now, we define the Factory Method interface or abstract class, which provides a method for creating cars:

```java
package org.example.codealong.factory;

public interface CarFactory {
    Car createCar();
}

```

We can then implement the Factory Method for each type of car:

```java
package org.example.codealong.factory;

public class SedanFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new Sedan();
    }
}

```

```java
package org.example.codealong.factory;

public class SUVFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new SUV();
    }
}

```

```java
package org.example.codealong.factory;

public class TruckFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new Truck();
    }
}

```

Finally, in the client code, we can use these factory classes to create cars without knowing the specific types:

```java
package org.example.codealong.factory;

public class Client {
    public static void main(String[] args) {
        CarFactory sedanFactory = new SedanFactory();
        Car sedan = sedanFactory.createCar();
        sedan.drive();

        CarFactory suvFactory = new SUVFactory();
        Car suv = suvFactory.createCar();
        suv.drive();

        CarFactory truckFactory = new TruckFactory();
        Car truck = truckFactory.createCar();
        truck.drive();
    }
}

```

In this example, the Factory Method pattern allows us to create different types of cars (sedans, SUVs, and trucks)
without explicitly specifying their concrete classes in the client code. Instead, the creation logic is encapsulated
within the respective factory classes, promoting loose coupling and maintainability in the software application.

### Abstract Factory design pattern (10 minutes)

The Abstract Factory pattern is a creational design pattern used to create families of related objects without
specifying their concrete classes. In other words, it provides an interface for creating a set of related objects
without the client code needing to know the specific implementations of those objects. This promotes loose coupling
between the client code and the concrete classes, making the code more flexible and maintainable.

This pattern becomes particularly useful when dealing with scenarios where your code needs to work with multiple
families of related objects, but you want to avoid directly depending on the specific types of those objects. This could
be because the types of objects may vary at runtime, or you want to allow for future extensibility by adding new types
of objects without modifying existing client code.

At its core, the Abstract Factory pattern defines an abstract factory interface or class that declares a set of methods
for creating each type of related object within a family. Concrete implementations of this abstract factory are then
responsible for instantiating specific types of objects that belong to the same family. This ensures that the created
objects are compatible and work seamlessly together.

By using the Abstract Factory pattern, developers can encapsulate the creation of related objects, allowing for easy
substitution of entire families of objects without impacting the client code. This promotes scalability and
maintainability by enabling the addition of new types of objects or families without requiring modifications to existing
code. Additionally, it helps in achieving a higher level of abstraction, as the client code only interacts with the
abstract factory and does not need to be concerned with the specific implementations of the objects being created.

In summary, the Abstract Factory pattern provides a flexible solution for creating families of related objects while
promoting loose coupling and extensibility in software design. It allows for the creation of interchangeable families of
objects, making it easier to adapt to changing requirements and maintain a modular and scalable codebase.

#### Advantages of Abstract Factory Pattern (10 minutes):

- **Provides Interface for Creating Families of Related Objects**: Abstract Factory pattern defines an interface for
  creating families of related or dependent objects without specifying their concrete classes. This allows for creating
  families of objects that are designed to work together seamlessly.
- **Encourages Consistency**: Abstract Factory pattern encourages consistency among products within the same family, as
  all products produced by a specific factory are expected to be compatible and follow the same conventions.
- **Promotes Loose Coupling**: Clients using the Abstract Factory pattern are decoupled from the concrete classes of the
  objects they create, as they rely on interfaces or abstract classes rather than concrete implementations. This
  promotes flexibility and facilitates changes to the concrete classes without affecting the client code.
- **Supports Dependency Injection**: Abstract Factory pattern can be used to implement dependency injection, allowing
  clients to receive a factory interface as a dependency and thus enabling runtime configuration of the concrete
  factories to be used.
- **Facilitates Product Variations**: Abstract Factory pattern allows for easy extension and modification of product
  families by introducing new concrete factories. This facilitates the creation of product variations or new product
  families without modifying existing client code.

#### Considerations and Criticisms (10 minutes):

- **Complexity**: Abstract Factory pattern can introduce additional complexity to the system, especially when dealing
  with a large number of product families or when the relationships between the products are intricate.
- **Increased Number of Classes**: Implementing Abstract Factory pattern typically involves creating multiple interfaces
  and concrete classes, which can lead to an increase in the number of classes in the system. This may make the codebase
  more difficult to manage and understand.
- **Static Structure**: The structure of the object creation process is static in Abstract Factory pattern, meaning that
  it cannot easily accommodate changes or additions to the product families at runtime. This may limit its flexibility
  in certain scenarios.
- **Tighter Coupling with Clients**: While Abstract Factory pattern promotes loose coupling between clients and concrete
  classes, it may result in tighter coupling between clients and the abstract factory interface, especially if clients
  need to work directly with the factory interface rather than through dependency injection.
- **Limited Extensibility**: Adding new product families or variations may require modifying the abstract factory
  interface and all of its concrete implementations, which can be cumbersome and may introduce maintenance challenges.

### Code along : Abstract Factory design pattern in action (20 minutes)

This program serves as a demonstration of the Abstract Factory design pattern applied in a fictional game development
scenario. The purpose of the program is to illustrate how the Abstract Factory pattern can be used to create families of
related objects, such as characters and weapons, without specifying their concrete classes directly. By employing this
design pattern, the program promotes flexibility and maintainability in game development by allowing for the creation of
interchangeable families of objects, facilitating easy adaptation to changing game requirements and the addition of new
types of characters and weapons in the future.

First, we define the abstract factory interface for creating characters and weapons:

```java
package org.example.codealong.abstractfactory;

// Abstract factory interface for creating characters
interface CharacterFactory {
    Character createCharacter();

    Weapon createWeapon();
}

// Abstract product interface for characters
interface Character {
    void display();
}

// Abstract product interface for weapons
interface Weapon {
    void attack();
}

```

Next, we create concrete implementations for different families of characters and weapons:

```java
// Concrete factory for creating elf characters and weapons
class ElfFactory implements CharacterFactory {
    @Override
    public Character createCharacter() {
        return new ElfCharacter();
    }

    @Override
    public Weapon createWeapon() {
        return new Bow();
    }
}

// Concrete factory for creating orc characters and weapons
class OrcFactory implements CharacterFactory {
    @Override
    public Character createCharacter() {
        return new OrcCharacter();
    }

    @Override
    public Weapon createWeapon() {
        return new Axe();
    }
}

// Concrete product for elf character
class ElfCharacter implements Character {
    @Override
    public void display() {
        System.out.println("Creating an Elf character.");
    }
}

// Concrete product for orc character
class OrcCharacter implements Character {
    @Override
    public void display() {
        System.out.println("Creating an Orc character.");
    }
}

// Concrete product for bow weapon
class Bow implements Weapon {
    @Override
    public void attack() {
        System.out.println("Attacking with a bow.");
    }
}

// Concrete product for axe weapon
class Axe implements Weapon {
    @Override
    public void attack() {
        System.out.println("Attacking with an axe.");
    }
}

```

Finally, we use the abstract factory to create characters and weapons without knowing their specific types:

```java
public class AbstractFactoryGameDemo {
    public static void main(String[] args) {
        // Create elf character and weapon
        CharacterFactory elfFactory = new ElfFactory();
        Character elfCharacter = elfFactory.createCharacter();
        Weapon elfWeapon = elfFactory.createWeapon();
        elfCharacter.display();
        elfWeapon.attack();

        // Create orc character and weapon
        CharacterFactory orcFactory = new OrcFactory();
        Character orcCharacter = orcFactory.createCharacter();
        Weapon orcWeapon = orcFactory.createWeapon();
        orcCharacter.display();
        orcWeapon.attack();
    }
}
```

In this example, the Abstract Factory pattern allows us to create families of related objects (characters and weapons)
without knowing their specific types. Instead, we use the abstract factory interface to create concrete instances of
characters and weapons, promoting loose coupling and flexibility in the game's design.

### Builder design pattern (10 minutes)

The Builder pattern is a creational design pattern that separates the construction of a complex object from its
representation, allowing the same construction process to create different representations. This pattern is particularly
useful when dealing with complex objects that require multiple steps to be constructed, or when there are different
variations of the same object.

Let's suppose we want to build a `Pizza` object which can have various `toppings`, `size`, and `crust` type. We'll
create a `PizzaBuilder` class to facilitate the construction of `Pizza` objects step by step.

#### Advantages of Builder Design Pattern: (10 minutes)

- **Separation of Concerns**: Builder pattern separates the construction of a complex object from its representation,
  allowing the same construction process to create different representations. This promotes cleaner and more modular
  code by separating the construction logic from the object's final structure.
- **Flexibility**: Builders allow for the construction of objects with complex configurations by providing a
  step-by-step approach. This flexibility enables the creation of different variations of objects without modifying
  their core implementation, making the codebase more adaptable to changing requirements.
- **Encapsulation**: Builder pattern encapsulates the construction process within the builder class, hiding the
  implementation details from the client code. This promotes information hiding and reduces the complexity of client
  code by providing a clear interface for object construction.
- **Immutability**: Builders can be designed to create immutable objects, ensuring that once constructed, the objects
  cannot be modified. Immutable objects are thread-safe and can help prevent unintended side effects in multi-threaded
  environments.
- **Complex Object Creation**: Builder pattern is particularly useful when dealing with complex objects that require
  multiple steps to be constructed or have optional parameters. By breaking down the construction process into smaller,
  manageable steps, builders simplify the creation of complex objects.

#### Considerations and Criticisms: (10 minutes)

- **Overhead**: Implementing the Builder pattern may introduce additional overhead compared to creating objects
  directly, especially for objects with simple construction requirements. This overhead comes from the additional
  builder class and the need to define multiple steps for object construction.
- **Increased Complexity**: Builder pattern adds complexity to the codebase, as it requires the definition of separate
  builder classes for each complex object. This complexity may make the code harder to understand, especially for
  developers unfamiliar with the pattern.
- **Potential for Inconsistency**: If the builder class is not properly implemented or used incorrectly, it may lead to
  inconsistencies in the constructed objects. For example, if mandatory parameters are not set before object
  construction, the resulting object may be incomplete or invalid.
- **Limited Usefulness for Simple Objects**: Builder pattern is most beneficial for constructing complex objects with
  many configurable parameters or optional features. For simple objects that can be created with a single constructor
  call, the overhead of using a builder may outweigh the benefits.
- **Dependency Injection Challenges**: When using dependency injection with builder pattern, injecting dependencies into
  the builder class and passing them to the constructed object may introduce additional complexity and boilerplate code.
  This can make the code harder to maintain and test.

### Code along : Builder design pattern in action (20 minutes)

```java
package org.example.codealong.builder;

class Pizza {
    private String size;
    private String crust;
    private String toppings;

    public Pizza(String size, String crust, String toppings) {
        this.size = size;
        this.crust = crust;
        this.toppings = toppings;
    }

    @Override
    public String toString() {
        return "Pizza{" +
                "size='" + size + '\'' +
                ", crust='" + crust + '\'' +
                ", toppings='" + toppings + '\'' +
                '}';
    }
}

```

```java
package org.example.codealong.builder;

public class PizzaBuilder {
    private String size;
    private String crust;
    private String toppings;

    public PizzaBuilder() {
        // Set default values
        this.size = "Medium";
        this.crust = "Thin";
        this.toppings = "Cheese";
    }

    public PizzaBuilder setSize(String size) {
        this.size = size;
        return this;
    }

    public PizzaBuilder setCrust(String crust) {
        this.crust = crust;
        return this;
    }

    public PizzaBuilder setToppings(String toppings) {
        this.toppings = toppings;
        return this;
    }

    public Pizza build() {
        return new Pizza(size, crust, toppings);
    }
}

```

```java
package org.example.codealong.builder;

public class Main {
    public static void main(String[] args) {
        // Create a Pizza using the builder
        Pizza pizza = new PizzaBuilder()
                .setSize("Large")
                .setCrust("Thick")
                .setToppings("Pepperoni, Mushrooms, Olives")
                .build();

        System.out.println(pizza); // Output: Pizza{size='Large', crust='Thick', toppings='Pepperoni, Mushrooms, Olives'}
    }
}

```

In this example, `Pizza` represents the complex object we want to build. The `PizzaBuilder` class provides a
step-by-step approach to constructing a `Pizza` object. Users can set the `size`, `crust`, and `toppings` of the pizza
using setter methods, and finally call the `build()` method to obtain the desired `Pizza` object.

This allows us to create different variations of `Pizza` objects without exposing its construction details, making the
code more maintainable and flexible.

### Class Discussion (10 minutes):

Consider the following software development scenarios and determine which design pattern would best fit each case.
Provide reasoning for your choices.

1. Use Case: Developing a text editor application where users can customize the appearance of the text (font, size,
   color) and save documents in different formats (e.g., plain text, rich text). Which design pattern would be most
   appropriate for managing the creation of customizable text documents?
2. Use Case: Developing a video streaming service that offers different subscription plans (e.g., basic, standard,
   premium), each with varying features (e.g., video quality, number of simultaneous streams). Which design pattern
   would be most appropriate for managing the creation of subscription plans and their associated features?
3. Use Case: Developing a system for generating reports in various formats (e.g., PDF, HTML, CSV) based on user-defined
   templates and data inputs. Which design pattern would be most appropriate for managing the generation of reports in
   different formats?

### Group Discussion Question (20 minutes):

**Your instructor will organize you into several groups to discuss the following scenario**:

Imagine you are tasked with designing a new system for managing inventory in a retail store. The system needs to handle
different types of products (e.g., electronics, clothing, groceries) and their respective attributes (e.g., price,
quantity, expiration date). Additionally, the system should support various operations such as adding new products,
updating inventory levels, and generating reports on sales and stock levels.

Within your group, discuss which design pattern(s) you believe would be most appropriate for implementing different
aspects of the inventory management system. Consider factors such as flexibility, scalability, and ease of maintenance.

After discussing within your group, be prepared to present your chosen design patterns and reasoning to the class.

### Summary (5 minutes):

During our lecture, we explored how various design patterns address common challenges in software development.
Specifically, we discussed the Builder pattern, which facilitates the creation of customizable objects, the Abstract
Factory pattern, which manages the creation of related objects without specifying their concrete classes, and the
Factory Method pattern, which generates objects based on specific requirements. These design patterns promote
flexibility, encapsulation, and maintainability in software systems.

### Further Reading (5 minutes):

- "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, John
  Vlissides
- "Head First Design Patterns" by Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra
- "Refactoring: Improving the Design of Existing Code" by Martin Fowler
- "Design Patterns in Java" by Steven John Metsker
- "Clean Code: A Handbook of Agile Software Craftsmanship" by Robert C. Martin
- "Effective Java" by Joshua Bloch
