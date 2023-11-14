## 0x13-javascript_objects_scopes_closures 

# How to create an object in JavaScript
In JavaScript, you can create objects using either the object literal notation or the Object constructor. Here are examples of both:

1. Object Literal Notation:

```js

// Creating an object using object literal notation
const person = {
  firstName: 'John',
  lastName: 'Doe',
  age: 30,
  email: 'john.doe@example.com',
};
// Accessing properties
console.log(person.firstName); // Outputs: John
console.log(person.age);       // Outputs: 30
```

In this example, person is an object with properties like firstName, lastName, age, and email. You can access these properties using dot notation.

# What this means

Method Context:

When a function is a method of an object, this refers to the object on which the method is called.

```js 

const person = {
  name: 'John',
  sayHello: function() {
    console.log(`Hello, my name is ${this.name}`);
  }
};

person.sayHello(); // Outputs: Hello, my name is John
```

# What undefined means

Object Properties:

If you try to access the value of an object property that does not exist, the result will be undefined.
javascript
Copy code
const person = { name: 'John' };
console.log(person.age); // Outputs: undefined

# What is a closure

A closure is a fundamental concept in JavaScript, and it refers to the ability of a function to retain access to variables from its outer (enclosing) scope even after the outer function has finished execution. In simpler terms, a closure allows a function to "close over" or "capture" variables from its surrounding lexical scope.

Here's a basic example to illustrate the concept:

```js 
function outerFunction() {
  let outerVariable = 'I am from the outer function';

  function innerFunction() {
    console.log(outerVariable); // Accessing outerVariable from the outer scope
  }

  return innerFunction; // Returning the inner function
}

const closureExample = outerFunction();

// Even though outerFunction has finished executing, innerFunction still has access to outerVariable
closureExample(); // Outputs: I am from the outer function
```
In this example:

outerFunction defines a variable outerVariable and declares an innerFunction inside it.
innerFunction is returned from outerFunction, and it forms a closure, capturing the outerVariable from its lexical scope.
When outerFunction is invoked and assigned to closureExample, it returns innerFunction.
Later, when closureExample is invoked, it still has access to outerVariable even though outerFunction has finished executing.
Closures are powerful because they provide a way to create private variables, maintain state between function calls, and implement various design patterns in JavaScript. Here are some common use cases for closures:

1. Private Variables:
Closures allow you to create private variables that are not directly accessible from outside the function.
go

```js

function createCounter() {
  let count = 0;

  return function() {
    count++;
    console.log(count);
  };
}

const counter = createCounter();
counter(); // Outputs: 1
counter(); // Outputs: 2
```

## What is a prototype

In JavaScript, a prototype is an internal, hidden property of objects that allows objects to inherit properties and methods from other objects. Every JavaScript object has an associated prototype, which acts as a template or blueprint for that object. Understanding prototypes is fundamental to understanding JavaScript's object-oriented nature.

Here are key concepts related to prototypes:

Prototype Chain:

Each object in JavaScript has a prototype, which is another object. When you access a property or method on an object, and if the object itself doesn't have that property or method, JavaScript looks for it in the object's prototype. This process continues up the prototype chain until the property or method is found or until the end of the chain is reached.
prototype Property:

Functions in JavaScript have a special property called prototype. When you create an object using a constructor function, the newly created object's prototype is set to the constructor function's prototype.

```js
function Person(name) {
  this.name = name;
}

const john = new Person('John');

// The prototype of 'john' is the same as the prototype of 'Person'
console.log(Object.getPrototypeOf(john) === Person.prototype); // Outputs: true
```

__proto__ Property:

The __proto__ property is a non-standard, but widely supported, way to access the prototype of an object. It is not recommended for direct use due to standardization concerns. Instead, you can use Object.getPrototypeOf().

```js
console.log(john.__proto__ === Person.prototype); // Outputs: true
Object.create() Method:

The Object.create() method allows you to create a new object with a specified prototype.
javascript
Copy code
const personPrototype = {
  sayHello: function() {
    console.log(`Hello, my name is ${this.name}`);
  }
};

const john = Object.create(personPrototype);
john.name = 'John';

john.sayHello(); // Outputs: Hello, my name is John
```

Constructor Functions:

When you create objects using constructor functions, the prototype property of the constructor function is automatically set as the prototype of the created objects.
```js
function Person(name) {
  this.name = name;
}

const john = new Person('John');
console.log(Object.getPrototypeOf(john) === Person.prototype); // Outputs: true
Prototypal Inheritance:

Prototypal inheritance allows objects to inherit properties and methods from other objects. It's a key feature of JavaScript's object-oriented programming model.
javascript
Copy code
function Animal(name) {
  this.name = name;
}

Animal.prototype.sayHello = function() {
  console.log(`Hello, I'm ${this.name}`);
};

function Dog(name, breed) {
  Animal.call(this, name);
  this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

const myDog = new Dog('Buddy', 'Golden Retriever');
myDog.sayHello(); // Outputs: Hello, I'm Buddy
Understanding prototypes is crucial for working with objects, especially when creating constructor functions, defining methods on object prototypes, and dealing with prototypal inheritance. It's a core concept in JavaScript's object-oriented design.