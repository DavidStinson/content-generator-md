package org.example.codealong.singleton;

public class TestSingleton {
    public static void main(String[] args) {
        DatabaseConnectionManager manager1 = DatabaseConnectionManager.getInstance();
        DatabaseConnectionManager manager2 = DatabaseConnectionManager.getInstance();

        System.out.println(manager1);
        System.out.println(manager2);
    }
}
