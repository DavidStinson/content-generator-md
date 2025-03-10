package org.example.codealong.factory;

public class TruckFactory implements CarFactory {
    @Override
    public Car createCar() {
        return new Truck();
    }
}
