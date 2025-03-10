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
