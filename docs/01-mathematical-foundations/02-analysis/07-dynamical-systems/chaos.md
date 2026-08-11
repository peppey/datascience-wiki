# Chaos

## TL;DR

**Chaos theory** studies deterministic systems whose behavior can be highly complex and unpredictable.

A key property of chaotic systems is **sensitive dependence on initial conditions**: tiny differences in the starting state can lead to dramatically different outcomes.

This is often called the **butterfly effect**.

---

## Deterministic but Unpredictable

A chaotic system follows deterministic rules:

$$
x_{n+1}=f(x_n).
$$

There is no randomness in the rule itself.

However, small differences in the initial condition can grow rapidly, making long-term prediction difficult.

For two nearby initial states:

$$
|x_0-y_0|\ll1,
$$

their trajectories may eventually become very different.

---

## Example: Logistic Map

A simple example is the **logistic map**:

$$
x_{n+1}=r x_n(1-x_n).
$$

For certain values of $r$, the system exhibits chaotic behavior.

For example, when:

$$
r=4,
$$

the system is chaotic for many initial conditions in $(0,1)$.

Despite its simple equation, its trajectories can be highly complex.

---

## Lyapunov Exponent

The **Lyapunov exponent** measures how quickly nearby trajectories diverge.

A positive Lyapunov exponent indicates exponential sensitivity to initial conditions:

$$
|\delta x(t)|
\approx
|\delta x(0)|e^{\lambda t}.
$$

Here, $\lambda$ is the Lyapunov exponent.

If:

$$
\lambda>0,
$$

nearby trajectories tend to diverge exponentially.

---

## Chaos and Fractals

Chaotic dynamical systems can produce **fractals**.

For example, the Mandelbrot set is closely connected to the dynamics of iterated complex functions.

Chaotic attractors can also have fractal structure.

---

## Examples of Chaotic Systems

Chaotic behavior can occur in:

* weather and climate models
* the double pendulum
* fluid dynamics
* population models
* electrical circuits
* celestial dynamics

A famous continuous-time example is the **Lorenz system**:

$$
\frac{dx}{dt}=\sigma(y-x)
$$

$$
\frac{dy}{dt}=x(\rho-z)-y
$$

$$
\frac{dz}{dt}=xy-\beta z.
$$

For certain parameter values, it produces the **Lorenz attractor**.

---

## Key Properties

Chaotic systems often exhibit:

* deterministic dynamics
* sensitivity to initial conditions
* aperiodic behavior
* bounded trajectories
* complex attractors

Not every complex or unpredictable system is chaotic. Chaos specifically refers to complex behavior arising from deterministic dynamics.

---

## Key Idea

**Chaos is deterministic behavior that becomes effectively unpredictable because small differences in initial conditions can grow rapidly.**

$$
\boxed{
\text{Deterministic rules}
+
\text{Sensitive dependence}
\rightarrow
\text{Chaotic behavior}
}
$$
