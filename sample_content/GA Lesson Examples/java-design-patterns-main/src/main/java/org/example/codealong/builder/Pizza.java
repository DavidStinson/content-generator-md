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
