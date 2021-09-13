# Fun with Functions - Instructions

The learning objectives of this lab are as follows:
1. Importing the contents of one Python script into another script.
2. Practicing creating functions with what you have learned so far in the course.
3. Testing your functions via the `assert` operator.
4. Reading doc strings

The more meta objectives are to:
1. Give you more insight into how `assert` works.
2. Give you a chance to learn how to test your code.
3. Use the above two points to more efficiently do homework and perform better on tests.


## Assignment Files
For this assignment you have given the following files:
1. functions.py: This file contains various function headers and docstrings indicating what task the function is to perform once you have completed it.
2. main.py: This is the file in which you will:
    * Call functions with certain parameters.
    * Check to see if the function ran correctly using assert

## Steps

### Importing a Python script
For this assignment we will be defining our functions in `functions.py` and calling them in the `main.py` file. In order to do this we must first `import` the `functions.py` file into `main.py` using the same syntax we would use for `import math`. As such, add the following line of code to the top of `main.py`:
```python
import functions
```
Just as `import math` allows us to use the functions included in the math module, `import functions` will allow us to use the functions in that file by use of the `.` notation (e.g., `functions.concat("hi", "everyone")`).

### Running main.py

Now that we have imported functions open the `main.py` file next to the
`functions.py` file next to each other so you can see them side by side. You
should notice that in the `functions.py` file the concat function has already
been filled in. Take a minute to read the docstring underneath it. A docstring
is a multi-line string that comes immediately after the function header that
gives a description of things like the argument of a function, what it returns
(if anything), as well as some general notes on it's functionality.

Now, direct your attention to the included `assert` statements in `main.py`.
The `assert` operator "asserts" that two things are true and produces an 
error if they are not. For instance, `assert 1 == 1` will not produce and error where
as `assert "hi" == "hello"` will. Assert statements, when what they are asserting is 
true, do not print anything to the screen. Therefore, the print statement underneath
the two included assert statements indicating the `functions.concat` function 
performed as expected will only run if both asserts pass successfully. As such,
these assert statements offer a straightforward way to test our code.

In order to test this, run the main.py file on your command line.


### Completing the functions 

For each of the functions you will be expected to do the following:
1. Complete the function body according to the specifications in their respective docstrings
2. Create two tests for the function you created under the function's comment block in `main.py` using `assert`. Use a print statement after the two asserts to indicate if both of the test cases pass.

## Git Command Reminders
* git add <filename>: To add a file's changes to the staging area.
* git commit -m "a message here": To create a commit with the contents of the staging area.
* git push: To push the local commits to remote (GitHub repo).
