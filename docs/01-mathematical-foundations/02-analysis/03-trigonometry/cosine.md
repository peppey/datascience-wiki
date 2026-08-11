# Cosine

## TL;DR

The **cosine function** is a fundamental trigonometric function that relates an angle to the ratio of the adjacent side to the hypotenuse in a right triangle.

$$
\cos(\theta)=\frac{\text{adjacent}}{\text{hypotenuse}}
$$

On the **unit circle**, cosine gives the $x$-coordinate of a point.

## Definition

For an angle $\theta$,

$$
\cos(\theta)
$$

is the horizontal coordinate of the corresponding point on the unit circle.

The cosine function maps real numbers to the interval:

$$
\cos:\mathbb{R}\rightarrow[-1,1]
$$

## Important Properties

### Range

$$
-1\leq\cos(x)\leq1
$$

### Periodicity

Cosine has period $2\pi$:

$$
\cos(x+2\pi)=\cos(x)
$$

### Even Function

Cosine is an even function:

$$
\cos(-x)=\cos(x)
$$

### Derivative

$$
\frac{d}{dx}\cos(x)=-\sin(x)
$$

### Integral

$$
\int\cos(x),dx=\sin(x)+C
$$

## Important Values

| $x$              |            $\cos(x)$ |
| ---------------- | -------------------: |
| $0$              |                  $1$ |
| $\frac{\pi}{6}$  | $\frac{\sqrt{3}}{2}$ |
| $\frac{\pi}{4}$  | $\frac{\sqrt{2}}{2}$ |
| $\frac{\pi}{3}$  |        $\frac{1}{2}$ |
| $\frac{\pi}{2}$  |                  $0$ |
| $\pi$            |                 $-1$ |
| $\frac{3\pi}{2}$ |                  $0$ |
| $2\pi$           |                  $1$ |

## Relation to Sine

Sine and cosine are closely related:

$$
\cos(x)=\sin\left(x+\frac{\pi}{2}\right)
$$

They also satisfy the Pythagorean identity:

$$
\sin^2(x)+\cos^2(x)=1
$$

## Applications

Cosine is widely used in:

* Geometry and trigonometry
* Physics and engineering
* Signal processing
* Fourier analysis
* Computer graphics
* Machine learning and similarity measures

For example, **cosine similarity** measures the angle between two vectors and is commonly used for comparing embeddings.
