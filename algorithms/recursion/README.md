- **Recursion** is a diff way of thinking about writing solutions. We can write solutions **iteratively**, and we can write them recursively.


Recursion is A process (a function in our case) that calls itself
When we write recursive functions, we keep pushing new functions onto the call stack! The same function over and over and it's waiting to be called

**How recursive functions work**

- Invoke the SAME function with a different input until you reach your base case
- **Two essential parts of any recursion:**
    - base case
    - different input, the recursive call the function same over and over but each time call it with a difference piece of data

**Base Case**

- The condition when the recursion ends
- This is an important concept to understand