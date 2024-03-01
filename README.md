
## Design-Pattern
- It represents a set of "good practices" by which the writing is guided
of code in OOP

### 1. Creational Design Pattern

- instantiation of classes or
object creation. 
- - class-creational & object-creational patterns.
- Ex: Factory Method, Abstract Factory, Builder, Singleton, Object Pool,
Prototype.

### 2. Structural Design Pattern

- the organization of classes and different objects to form a much larger structure and to bring a new functionality.
- Ex: Adapter, Bridge, Composite, Decorator, Facade, Flyweight,
Private Class Data si Proxy.

### 3. Behavioral Design Pattern

- identifying common patterns
of communication between objects and the realization of these patterns.
- Ex: Chain of responsability, Command, Interpreter, Iterator,
Mediator, Memento, Null Object, Observer, State, Strategy, Template method,
Visitor.

## Iterators, Generators, Context Managers and Decorators 

### 1. Iter & Iterator   (iterabil si iterator)
- iter has only __ iter__ method and iterator has 2 methods __ iter__ & __ next__

### 2. Generators 

- a simple way to create iterators.
- is a function
which returns an object (iterator) that we can iterate on
(one value at a time)
- if a function contains at least one yield statement, it becomes a generating function
- the yield function is similar to the return function, both will return a value, the difference is that return ends the iteration, 
and yield stops the function saving all the settings and continues from there when is called.

### 3. Context Managers

- objects that help us control access to
certain resources.
- interaction with external files, database,
external links.
- the most common way of iteration with context managers is
using the "with" block.
- The Context Management Protocol is form with 2 method:

> a. is invoked when entering the "with" block

> b. is invoked when exiting the "with" block


### 4 Decorators