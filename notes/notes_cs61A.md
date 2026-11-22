1. iterator:
An iterable is any value that can be iterated through, 
or gone through one item at a time. One construct that we've used to iterate through an iterable is a for statement

In general, an iterable is an object on which calling the built-in iter function returns an iterator. 
An iterator is an object on which calling the built-in next function returns the next value.

2. generator:
We can create our own custom iterators by writing a generator function, which returns a special type of iterator called a generator. 
Generator functions have yield statements within the body of the function instead of return statements. 
Calling a generator function will return a generator object and will not execute the body of the function.

Since generators are iterators, we call next on them to get the next item. The first time next is called, execution begins at the first line of the function body and continues until the yield statement is reached. 
The result of evaluating the expression in the yield statement is returned.

On any consecutive calls to next, execution picks up from the line after the yield statement that was previously executed and continues until the next yield statement is reached


3. Class attributes are "shared" across all instances of a class because they are attributes of the class, not the instance.
If the object is a class, then assignment sets an class attribute
If the object is an instance, then assignment sets an instance attribute

4. Inheritance and Composition
Inheritance is best for representing is-a relationships
Composition is best for representing has-a relationships
