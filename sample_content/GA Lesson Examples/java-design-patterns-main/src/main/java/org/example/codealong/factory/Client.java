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
