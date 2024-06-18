# MATEMATICAS

Matematicas - the Spanish word for Mathematics is an app that evaluates different mathematical expressions and solve different mathematical equations from simple to complex. The repository is available on [GitHub](https://github.com/OlaOluwalekan/matematicas)

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/OlaOluwalekan/matematicas
   ```
1. Navigate to the project directory
   ```bash
   cd /matematicas
   ```
1. Run the app
   ```bash
   python main.py
   ```

## Evaluation and Expression

Matematica evaluates express ranging from simple to complex. To evaluate an expression, select the option corresponding to evaluating expression. The prompt will ask that you enter the expression to be evaluated. Make sure you enter a correct mathematical expression.

### Rules for expression

- **Variables**: A variables can be any letter of the English alphabet in lower case [a-z] or upper case [A-Z] and variables are case sensitive, meaning `a` is different from `A`.

- **Operators**: Basic operators like addition, subtraction, multiplication and division uses the symbols `+`, `-`, `*`, and `/` respectively

- **Order**: The order of operation follows the conventional orders in maths. Expressions in parenthesis are evaluated first. followed by division and multiplication, then addition and subtraction.

- **special operations**: There are special operations that can ne performed with matematicas. Such operations include sine, cosine, and tangent of angles, logarithm to the base of 10, square roots, and exponential. The table below summarizes the characters or symbols used for these operations

  | Characters | Description               |
  | ---------- | ------------------------- |
  | sin(x)     | sine of x                 |
  | cos(x)     | cosine of x               |
  | tan(x)     | tangent of x              |
  | log(x)     | logarithm to base 10 of x |
  | sqrt(x)    | square root of x          |
  | x^y        | x to the power of y       |

  the sequence of characters above need to be as above to mean what is intended. For example the presence of cos(x) in an expression will be interpreted as the cosine of x and each character will not be treated as a separate variable. However, the presence soc(x) in an expression will mean `s`, `o`, `c`, and `x` are separate variables whose values are required to evaluate the expression. Also note that for readability and confusion, the above special operations (except for exponents) must be followed by parenthesis i.e. cos(x) and not cosx or cos x. The latter two will throw an error.

- **Results**: The result of an operation is given in floating point numbers. This is because some complex evaluation may involve imprecise division that results in larger decimal values.

## Quadratic Equations

To solve the roots of a quadratic equation, you can either enter the coefficients of quadratic equation (a, b, c) each separated by a comma `,` or enter the quadratic expression (without the `= 0`). Matematicas will determine the coefficient from the entry and thus solve for the roots of the quadratic equation. The solution can come in two forms.

1. The case where the roots are real. This scenario returns the roots `x1` and `x2` (or whatever variable you use) of the quadratic equation.

1. There is also the scenario where the quadratic roots are not real. in this instance, the roots of the equation is returned as a set strings in the form of complex numbers e.g `x1 = m + ni` where `ni` denotes the imaginary component.

## Numerical integrals

Matematicas make use of the Simpson rule, trapezoid rule or the mid-point rule to evaluate the integral of a given function within a specified limit `a` and `b` and a given sub-interval `n`
