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
