# Limits

## TL;DR

The **limit** of a function describes the value that $f(x)$ approaches as $x$ approaches a particular value.

$$
\boxed{
\lim_{x\to a}f(x)=L
}
$$

The value $f(a)$ does not necessarily have to exist.

---

## Direct Substitution

For many continuous functions, the limit can be calculated by simply substituting $x=a$.

For example:

$$
\lim_{x\to2}(x^2+3x)
=
10
$$

If direct substitution produces an indeterminate form, further calculation is required.

---

## Limit Rules

If

$$
\lim_{x\to a}f(x)=L
$$

and

$$
\lim_{x\to a}g(x)=M
$$

then:

**Sum:**

$$
\lim_{x\to a}(f(x)+g(x))=L+M
$$

**Product:**

$$
\lim_{x\to a}f(x)g(x)=LM
$$

**Quotient:**

$$
\lim_{x\to a}\frac{f(x)}{g(x)}
=

\frac{L}{M}
$$

for $M\neq0$.

---

## Indeterminate Forms

Expressions such as

$$
\frac{0}{0}
$$

or

$$
\frac{\infty}{\infty}
$$

are **indeterminate forms**. They do not directly determine the value of the limit.

For example:

$$
\lim_{x\to1}\frac{x^2-1}{x-1}
$$

Direct substitution gives:

$$
\frac{0}{0}
$$

Factoring gives:

$$
\frac{(x-1)(x+1)}{x-1}=x+1
$$

Therefore:

$$
\lim_{x\to1}(x+1)=2
$$

Common techniques for resolving indeterminate forms include:

* Factoring and cancelling
* Finding a common denominator
* Rationalizing
* Applying L'Hôpital's rule

---

## Left and Right Limits

The **left-hand limit** is:

$$
\lim_{x\to a^-}f(x)
$$

and the **right-hand limit** is:

$$
\lim_{x\to a^+}f(x)
$$

A two-sided limit exists only if both are equal:

$$
\boxed{
\lim_{x\to a^-}f(x)
=

\lim_{x\to a^+}f(x)
}
$$

This is particularly important for piecewise functions and discontinuities.

---

## Limits at Infinity

Limits can also describe the behavior of a function for very large values of $x$:

$$
\lim_{x\to\infty}f(x)
$$

For example:

$$
\lim_{x\to\infty}\frac{1}{x}=0
$$

For rational functions, the highest powers of $x$ often determine the limit.

For example:

$$
\lim_{x\to\infty}
\frac{3x^2+1}{2x^2-5}
=

\frac{3}{2}
$$

---

## L'Hôpital's Rule

For certain indeterminate forms, **L'Hôpital's rule** allows the numerator and denominator to be differentiated:

$$
\boxed{
\lim_{x\to a}\frac{f(x)}{g(x)}
=

\lim_{x\to a}\frac{f'(x)}{g'(x)}
}
$$

provided the necessary conditions are satisfied.

For example:

$$
\lim_{x\to0}\frac{\sin x}{x}
$$

can be evaluated as:

$$
\lim_{x\to0}\frac{\cos x}{1}=1
$$

---

## Important Standard Limits

Some important limits are:

$$
\boxed{
\lim_{x\to0}\frac{\sin x}{x}=1
}
$$

$$
\boxed{
\lim_{x\to0}\frac{e^x-1}{x}=1
}
$$

and

$$
\boxed{
\lim_{x\to\infty}
\left(1+\frac{1}{x}\right)^x=e
}
$$

