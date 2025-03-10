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
