# BACKPROPAGATION

## Introduction

Backpropagation is an algorithm used to efficiently calculate the gradients of a loss function with respect to the parameters of a neural network. It is the fundamental mechanism that enables neural networks to learn from data.

The central idea is to propagate the error of a network backwards, from the output layer towards the input layer, using the chain rule of calculus. This allows us to determine how much each individual weight and bias contributes to the overall prediction error.

Backpropagation is closely related to gradient-based optimization methods such as Gradient Descent and Stochastic Gradient Descent (SGD). While backpropagation computes the gradients, an optimization algorithm uses these gradients to update the network parameters.

The algorithm consists of two main phases:

- **Forward Pass:** The input is propagated through the network to calculate the output and evaluate the loss function.
- **Backward Pass:** The gradients of the loss function with respect to all network parameters are calculated by propagating derivatives backwards through the network.

## Mathematical Foundations

### The Chain Rule

The mathematical foundation of backpropagation is the chain rule of differential calculus.

Suppose a function is defined as a composition of two functions:

$$
y=f(g(x))
$$

The derivative of $y$ with respect to $x$ is given by:

$$
\frac{dy}{dx}
=
\frac{df}{dg}
\cdot
\frac{dg}{dx}
$$

More generally, for a composition of multiple functions,

$$
y=f_n(f_{n-1}(\dots f_1(x)))
$$

the derivative is obtained by multiplying the individual derivatives:

$$
\frac{dy}{dx}
=
\prod_{i=1}^{n}
\frac{df_i}{df_{i-1}}
$$

where $f_0=x$.

This property is particularly useful for neural networks because their computations consist of multiple nested functions.

By applying the chain rule repeatedly, we can calculate the derivative of the loss function with respect to parameters located at any depth in the network.

### Computational Graphs

A computational graph represents a mathematical function as a directed graph in which nodes represent operations or variables and edges represent dependencies between them.

Neural networks can be represented as computational graphs. During the forward pass, information flows from the input nodes towards the output nodes. During the backward pass, derivatives flow in the opposite direction.

Consider a simple composition:

$$
z=f(y), \qquad y=g(x)
$$

The computational graph can be represented as:

$$
x \longrightarrow g \longrightarrow y
\longrightarrow f \longrightarrow z
$$

The forward pass evaluates the intermediate variables, whereas the backward pass calculates the derivatives:

$$
\frac{\partial z}{\partial y}
=
f'(y)
$$

$$
\frac{\partial z}{\partial x}
=
\frac{\partial z}{\partial y}
\frac{\partial y}{\partial x}
=
f'(y)g'(x)
$$

The intermediate values calculated during the forward pass are usually stored because they are required to evaluate the derivatives during the backward pass.

## Neural Network Representation

Consider a feedforward neural network consisting of $L$ layers.

Each layer applies an affine transformation followed by a nonlinear activation function.

The output of layer $l$ is defined as:

$$
z^{(l)}
=
W^{(l)}a^{(l-1)}+b^{(l)}
$$

$$
a^{(l)}
=
\sigma^{(l)}(z^{(l)})
$$

where:

- $W^{(l)}$ denotes the weight matrix of layer $l$.
- $b^{(l)}$ denotes the bias vector of layer $l$.
- $z^{(l)}$ denotes the pre-activation values.
- $a^{(l)}$ denotes the activation values.
- $\sigma^{(l)}$ denotes the activation function.
- $a^{(0)}=x$ denotes the input vector.

The network output is therefore:

$$
\hat{y}=a^{(L)}
$$

A loss function measures the difference between the predicted output and the actual target:

$$
\mathcal{L}(\hat{y},y)
$$

The objective of training is to minimize the loss with respect to all weights and biases:

$$
\min_{\{W^{(l)},b^{(l)}\}_{l=1}^{L}}
\mathcal{L}(\hat{y},y)
$$

Backpropagation provides the gradients required to solve this optimization problem.

## Forward Pass

The forward pass evaluates the neural network by propagating the input through its layers.

Starting with the input vector,

$$
a^{(0)}=x
$$

each layer calculates its pre-activation and activation values:

$$
z^{(l)}
=
W^{(l)}a^{(l-1)}+b^{(l)}
$$

$$
a^{(l)}
=
\sigma^{(l)}(z^{(l)})
$$

This process continues until the output layer is reached:

$$
\hat{y}=a^{(L)}
$$

The loss function is then evaluated:

$$
\mathcal{L}
=
\mathcal{L}(a^{(L)},y)
$$

The forward pass is necessary not only to calculate the prediction error but also to obtain the intermediate activations required for the backward pass.

## Backward Pass

The backward pass calculates the partial derivatives of the loss function with respect to the network parameters.

The key idea is to calculate the derivatives layer by layer, starting at the output layer and moving backwards towards the input layer.

### Error Signal

We define the error signal of layer $l$ as the derivative of the loss function with respect to the pre-activation values:

$$
\delta^{(l)}
=
\frac{\partial \mathcal{L}}
{\partial z^{(l)}}
$$

This quantity describes how sensitive the loss function is to changes in the pre-activation values of a particular layer.

Using the chain rule, the error signal of the output layer is:

$$
\delta^{(L)}
=
\frac{\partial \mathcal{L}}
{\partial a^{(L)}}
\odot
\sigma'^{(L)}(z^{(L)})
$$

where $\odot$ denotes element-wise multiplication.

For all preceding layers, the error signal can be calculated recursively:

$$
\boxed{
\delta^{(l)}
=
\left(W^{(l+1)}\right)^T
\delta^{(l+1)}
\odot
\sigma'^{(l)}(z^{(l)})
}
$$

This is the central recurrence relation of backpropagation.

It consists of two operations:

- The error signal is propagated backwards through the weight matrix of the next layer.
- The result is multiplied element-wise by the derivative of the activation function.

Consequently, each layer receives information about how its activations contribute to the error of all subsequent layers.

### Gradients with Respect to Weights

The gradient of the loss function with respect to the weight matrix of layer $l$ is obtained using the chain rule:

$$
\frac{\partial \mathcal{L}}
{\partial W^{(l)}}
=
\frac{\partial \mathcal{L}}
{\partial z^{(l)}}
\frac{\partial z^{(l)}}
{\partial W^{(l)}}
$$

Since

$$
z^{(l)}
=
W^{(l)}a^{(l-1)}+b^{(l)}
$$

we obtain:

$$
\boxed{
\frac{\partial \mathcal{L}}
{\partial W^{(l)}}
=
\delta^{(l)}
\left(a^{(l-1)}\right)^T
}
$$

The gradient is therefore given by the outer product of the error signal and the activations of the preceding layer.

### Gradients with Respect to Biases

The gradient with respect to the bias vector is:

$$
\frac{\partial \mathcal{L}}
{\partial b^{(l)}}
=
\frac{\partial \mathcal{L}}
{\partial z^{(l)}}
\frac{\partial z^{(l)}}
{\partial b^{(l)}}
$$

Because the derivative of the pre-activation values with respect to the biases is the identity matrix, we obtain:

$$
\boxed{
\frac{\partial \mathcal{L}}
{\partial b^{(l)}}
=
\delta^{(l)}
}
$$

Thus, the error signal directly represents the gradient with respect to the bias vector.

## Backpropagation Algorithm

The complete algorithm can be summarized as follows:

**Initialization**

Initialize all weights and biases, usually with an appropriate random initialization scheme.

**Forward Pass**

Given an input $x$, calculate the activations of all layers:

$$
a^{(0)}=x
$$

$$
z^{(l)}=W^{(l)}a^{(l-1)}+b^{(l)}
$$

$$
a^{(l)}=\sigma^{(l)}(z^{(l)})
$$

Evaluate the loss:

$$
\mathcal{L}=\mathcal{L}(a^{(L)},y)
$$

**Backward Pass**

Calculate the error signal of the output layer:

$$
\delta^{(L)}
=
\nabla_{a^{(L)}}\mathcal{L}
\odot
\sigma'^{(L)}(z^{(L)})
$$

Propagate the error backwards through all hidden layers:

$$
\delta^{(l)}
=
\left(W^{(l+1)}\right)^T
\delta^{(l+1)}
\odot
\sigma'^{(l)}(z^{(l)})
$$

Calculate the gradients:

$$
\frac{\partial \mathcal{L}}{\partial W^{(l)}}
=
\delta^{(l)}(a^{(l-1)})^T
$$

$$
\frac{\partial \mathcal{L}}{\partial b^{(l)}}
=
\delta^{(l)}
$$

**Parameter Update**

The gradients can now be used by an optimization algorithm to update the parameters.

For standard Gradient Descent:

$$
W^{(l)}
\leftarrow
W^{(l)}
-
\eta
\frac{\partial \mathcal{L}}{\partial W^{(l)}}
$$

$$
b^{(l)}
\leftarrow
b^{(l)}
-
\eta
\frac{\partial \mathcal{L}}{\partial b^{(l)}}
$$

where $\eta$ denotes the learning rate.

These steps are repeated over multiple training iterations until a stopping criterion is reached.

## Special Case: Softmax and Cross-Entropy

A particularly important combination in classification problems is the Softmax activation function together with the categorical cross-entropy loss.

The Softmax function transforms the output logits $z$ into a probability distribution:

$$
\hat{y}_i
=
\frac{e^{z_i}}
{\sum_{j=1}^{K}e^{z_j}}
$$

The categorical cross-entropy loss is defined as:

$$
\mathcal{L}
=
-\sum_{i=1}^{K}
y_i\log(\hat{y}_i)
$$

where $y_i$ represents the target distribution.

Combining the derivative of Softmax with the derivative of cross-entropy leads to a particularly simple error signal:

$$
\boxed{
\delta^{(L)}
=
\hat{y}-y
}
$$

This simplification is one reason why Softmax and cross-entropy are commonly used together in multiclass classification.

## Computational Complexity

Backpropagation is computationally efficient because it reuses intermediate results and derivatives rather than independently differentiating the loss with respect to every parameter.

For a fully connected neural network, the dominant computational cost is typically associated with the matrix multiplications in the forward and backward passes.

The backward pass has a computational complexity of the same order as the forward pass.

Consequently, the total computational cost of calculating the gradients is approximately a small constant multiple of the cost of evaluating the network.

This makes backpropagation practical even for neural networks containing millions or billions of parameters.

## Limitations and Challenges

### Vanishing Gradients

The vanishing gradient problem occurs when gradients become increasingly small as they are propagated backwards through many layers.

This can happen when activation functions have derivatives significantly smaller than one, such as the sigmoid function in saturated regions.

As a result, parameters in earlier layers receive very small updates, making learning slow or preventing effective learning altogether.

Common approaches to mitigating this problem include:

- Using ReLU or related activation functions.
- Applying appropriate weight initialization methods.
- Using residual connections.
- Employing normalization techniques.

### Exploding Gradients

The exploding gradient problem occurs when gradients grow exponentially during backward propagation.

This can lead to excessively large parameter updates and unstable training.

Possible solutions include:

- Gradient clipping.
- Appropriate weight initialization.
- Normalization techniques.
- Carefully selecting the learning rate.

### Numerical Stability

The repeated multiplication of derivatives can introduce numerical instability, particularly in very deep networks.

Floating-point precision, overflow and underflow can affect gradient calculations.

Modern deep learning frameworks therefore implement numerically stable operations and specialized gradient computation routines.

## Relationship to Automatic Differentiation

Backpropagation is closely related to reverse-mode automatic differentiation.

Automatic differentiation is a general technique for evaluating derivatives of computational programs by applying the chain rule to their individual operations.

Reverse-mode automatic differentiation evaluates derivatives by propagating sensitivities backwards through a computational graph.

Since neural networks typically have many parameters but comparatively few output values, reverse-mode automatic differentiation is particularly suitable for calculating their gradients.

Modern frameworks such as PyTorch and TensorFlow use automatic differentiation to calculate gradients without requiring the user to implement the backpropagation equations manually.

## Summary

Backpropagation is the fundamental algorithm used to calculate gradients in neural networks.

Its mathematical foundation is the chain rule, which allows derivatives to be propagated backwards through a sequence of differentiable operations.

The algorithm consists of a forward pass to evaluate the network and a backward pass to calculate the gradients of the loss function with respect to all trainable parameters.

These gradients are subsequently used by optimization algorithms such as Gradient Descent, SGD or Adam to update the network parameters.

Backpropagation itself does not perform the optimization. Instead, it provides the gradient information that makes gradient-based learning possible.