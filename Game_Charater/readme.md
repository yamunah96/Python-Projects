# Game Character System

A simple Python project to demonstrate **Object-Oriented Programming (OOP)** and **Inheritance**.

## Features

- Parent class: `GameCharacter`
- Child classes:
  - `Wizard`
  - `Warrior`
  - `Archer`
- Each character has:
  - Name
  - Health
  - Level
- Each child has its own resource:
  - Wizard → Daggers
  - Warrior → Swords
  - Archer → Arrows
- Characters attack each other.
- Health and weapon resources change after each attack.
- The game runs for multiple rounds.

## OOP Concepts Used

- Classes and Objects
- Constructors
- Inheritance
- Parent and Child Classes
- Instance Attributes
- Methods
- Loops
- Conditional Statements

## Class Structure

```text
GameCharater
│
├── Wizard
│   └── magic_attack()
│
├── Warrior
│   └── warrior_attack()
│
└── Archer
    └── archer_attack()
