# Double Descent

## TL;DR (30 seconds)

**Double Descent** describes a phenomenon in machine learning where the test error does not always follow the classical bias-variance trade-off.

Normally, we expect:

- small models → high bias → poor performance
- larger models → lower bias → better performance
- very large models → overfitting → worse generalization

With **Double Descent**, the test error can decrease again when the model becomes extremely large.

