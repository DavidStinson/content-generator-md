package org.example.codealong.factory;

public class SUVFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new SUV();
    }
}
