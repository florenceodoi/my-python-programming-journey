# Python Programming Journey - Module 3

## Overview

In Module 3, I learned how Python makes decisions, repeats tasks, and works with multiple values using lists.

This module introduced me to conditional statements, loops, logical operators, bitwise operators, lists, sorting, slicing, and nested lists.

## What I Learned

### Comparison Operators

I learned how to compare values using:

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

I also learned that `=` is used to assign a value, while `==` is used to compare values.

### Conditional Statements

I learned how Python makes decisions using:

```python
if
elif
else
```

Example:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Indentation is important because it determines which instructions belong to each condition.

### Loops

I learned how to repeat instructions using `while` and `for` loops.

Example:

```python
for i in range(1, 6):
    print(i)
```

I also learned how to use:

- `break` to stop a loop
- `continue` to skip the current iteration

### Logical Operators

I learned how to combine conditions using:

- `and`
- `or`
- `not`

Example:

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Access granted")
```

### Lists

I learned that lists allow multiple values to be stored in one variable.

Example:

```python
numbers = [10, 5, 7, 2, 1]
```

I practised:

- Accessing list items
- Adding items using `append()`
- Adding items using `insert()`
- Removing items using `del`
- Checking list length using `len()`
- Sorting lists using `sort()`
- Reversing lists using `reverse()`

### List Slicing

I learned how to select part of a list using slicing.

Example:

```python
numbers = [10, 8, 6, 4, 2]

new_list = numbers[1:3]
```

### Nested Lists

I also learned that lists can contain other lists.

Example:

```python
board = [
    [1, 2],
    [3, 4]
]
```

Nested lists can be used to represent tables and matrices.

## Hands-on Practice

During this module, I practised:

- Comparing values
- Writing `if`, `elif`, and `else` statements
- Using `for` and `while` loops
- Using `break` and `continue`
- Working with logical operators
- Creating and modifying lists
- Sorting and slicing lists

## Commands Used

| Command | What it does |
|---|---|
| `python comparisons.py` | Runs the comparison operators program |
| `python conditionals.py` | Runs the conditional statements program |
| `python loops.py` | Runs the loops program |
| `python logical_operators.py` | Runs the logical operators program |
| `python lists.py` | Runs the lists program |
| `git status` | Shows changes in the repository |
| `git add .` | Adds files to the staging area |
| `git commit -m "message"` | Saves changes with a description |
| `git push` | Uploads the committed work to GitHub |

## Challenge

One challenge in this module was understanding how indentation affects conditional statements and loops.

Practising the code and checking the output helped me understand how Python follows the flow of instructions.

## Key Takeaways

My main takeaway from Module 3 is that Python can now do more than just perform calculations.

I can now write programs that:

- Make decisions
- Repeat tasks
- Compare values
- Work with multiple conditions
- Store multiple values in lists
- Sort and process data

This module helped me understand how Python programs become more interactive and structured.

## Module Status

Module 3 Completed.