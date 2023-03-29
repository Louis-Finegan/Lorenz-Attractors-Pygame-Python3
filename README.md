# Lorenz Attractors

## Lorenz Attractors

The Lorenz Attractors are governed by the following System of Ordinary Differential Equations:

$$\frac{dx}{dt}=\sigma(y-x)$$

$$\frac{dy}{dt}=x(\rho-z)-y$$

$$\frac{dz}{dt}=xy-\beta z$$

For more information Click [here](https://en.wikipedia.org/wiki/Lorenz_system).

## Purpose

Demonstrate the chaotic nature of the Lorenz Attractors with slight variation in the initial conditions.

## Libaries Used:

1. `numpy`

2. `scipy` using the `integrate` module

3. `pygame`

## Approach

3 instances of the `lorenz` class were created with slight variation in their initial conditions. these conditions were random using numpy's uniform random number generator:
        
        `[np.random.uniform(0.99, 1.01),np.random.uniform(0.99, 1.01),np.random.uniform(0.99, 1.01)]`

The initial condition was centered around `[1, 1, 1]`. This is to stop the points in the solution from displaying off the pygame display.

NOTE: Initial conditions will be printed in the terminal.

The System of Ordinary Differential Equation were solved by using, `solve_ivp` function, Then the `plot.game` method is called which generates the interactive pygame display with the 3 solutions: white red and/or blue, appearing point by point at *30 fps*.

## How to use

Run the python file `main.py`.

1. Press `s` to start then select one of the following options:

* press `a` to generate all 3 solution on the display at the same time.

* press `w` to generate the white solution.

* press `g` to generate the green solution.

* press `b` to generate the green solution.

2. Press `q` or close the window to quit.

3. Press `r` to reset the display.

4. follow on from step 1 to generate a new plot.

## Conclusion

It is clear, by observing all 3 solutions after a sufficent amount of time, there nature is hugely different. Then it can be said with a slight change in the Lorenz Attractors initial conditions, these models will have different solutions after a long period of time. 
