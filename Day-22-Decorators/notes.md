# Day 22: Decorators


## 01 - Introduction to Decorators
Explains what decorators are in Python: functions that can modify or enhance other functions. Introduces the `@decorator_name` syntax used to apply a decorator to a function.

## 02 - Writing a Simple Decorator
Shows how to create a basic decorator. Demonstrates defining a decorator function, using an inner wrapper function, and applying the decorator to another function with the `@` syntax.

## 03 - Decorators with Arguments
Describes how to write decorators that can handle functions with any number of positional and keyword arguments by using `*args` and `**kwargs` in the wrapper.

## 04 - Chaining Multiple Decorators
Explains how to apply more than one decorator to a single function by stacking multiple `@decorator` lines above the function definition.

## 05 - Practical Use Cases
Lists common scenarios where decorators are useful, such as logging, access control, timing function execution, and memoization.

## 06 - Using `functools.wraps`
Introduces the `functools.wraps` decorator, which helps preserve the original function’s metadata (like its name and docstring) when it is wrapped by a decorator.
