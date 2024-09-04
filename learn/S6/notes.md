# Python Parameters and Arguments

## Parameters

Parameters are variables that are listed inside the parentheses in the function definition. They define what inputs the function expects.

### Types of Parameters

1. **Positional Parameters:**
   - Parameters that are defined in a straightforward manner and are expected to be provided in the exact order they are defined.

2. **Default Parameters:**
   - Parameters that have default values. If no argument is passed for such a parameter, the default value is used.

3. **Keyword-Only Parameters:**
   - Parameters that must be specified using their names in function calls. These parameters follow a `*` in the function definition.

4. **Variable-Length Parameters:**
   - Parameters that can accept an arbitrary number of arguments.
     - **`*args`:** Accepts any number of positional arguments, which are accessible as a tuple.
     - **`**kwargs`:** Accepts any number of keyword arguments, which are accessible as a dictionary.

## Arguments

Arguments are the actual values or data you pass to the function's parameters when calling it.

### Types of Arguments

1. **Positional Arguments:**
   - Arguments that are passed to the function in the correct positional order.

2. **Keyword Arguments:**
   - Arguments that are passed to the function by explicitly naming each parameter and providing a value.

3. **Default Arguments:**
   - When a function call omits arguments for parameters with default values, those default values are used.

4. **Variable-Length Arguments:**
   - **`*args`:** When you pass a variable number of positional arguments.
   - **`**kwargs`:** When you pass a variable number of keyword arguments.
