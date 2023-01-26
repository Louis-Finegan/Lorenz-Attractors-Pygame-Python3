# Lorenz Attractors

## Lorenz Attractors

System of Ordinary Differential Equations:

$$\frac{dx}{dt}=\sigma(y-x)$$

$$\frac{dy}{dt}=x(\rho-z)-y$$

$$\frac{dz}{dt}=xy-\beta z$$

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

The System of Ordinary Differential Equation were solved by using: `solve_ivp` function, Then the `plot.game` method is called which generates the interactive pygame display with the 3 solutions: white red and blue, appearing point by point at *30 fps*.

## How to use

Run the python file `main.py`. The pygame display will appear. Press `s` to start generating the solution, press `q` to quit or close the display and press `r` to reset the display.
