# Intro_to_the_Math_of_intelligence

---

This is the code for "Intro - The Math of Intelligence" by Siraj Raval on Youtube

## Coding Challenge -- Due Date, Thursday June 22nd, 2017
---

This week's coding challenge is to implement gradient descent to find the line of best fit that predicts the relationship between 2 variables of your choice from a [kaggle](https://www.kaggle.com/datasets) dataset. Bonus points for detailed documentation. Good luck! Post your github link in the youtube comments section

## Overview

---

This is the code for [this](https://youtu.be/xRJCOz3AfYY) video on Youtube by Siraj Raval. It is a code challenge to implement a gradient descent on any data.  The data I used was acquired from: [cengage](http://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/slr/frames/frame.html)


`List Price Vs. Best Price for a New GMC Pickup

In the following data
ListPrice (X) = List price (in $1000) for a GMC pickup truck
BestPrice(Y) = Best price (in $1000) for a GMC pickup truck
Reference: Consumer’s Digest
`
Here are some helpful links:

### Gradient descent visualization
---

![Alt image](https://raw.githubusercontent.com/mattnedrich/GradientDescentExample/master/gradient_descent_example.gif?raw="gdv")

### Sum of squared distances formula (to calculate our error)

![Alt image](https://spin.atomicobject.com/wp-content/uploads/linear_regression_error1.png?raw="sos")

### Partial derivative with respect to b and m (to perform gradient descent)

![Alt img](https://spin.atomicobject.com/wp-content/uploads/linear_regression_gradient1.png?raw="partial")

## Dependencies

- numpy

Python 2 and 3 both work for this. Use [pip](https://pip.pypa.io/en/stable/) to install any dependencies.

## Usage

Just run `python main.py` to see the results:

```
Python - main.py:63
Starting gradient descent at b = 0, m = 0, error = 238.13956769069583
Running...
After 1000 iterations b = 0.05045761733686893, m = 0.8727444438670023, error = 0.014459793723847128
[Finished in 1.337s]
```

## Credits

Credits for this code go to [mattnedrich](https://github.com/mattnedrich) and Siraj Ravel.
