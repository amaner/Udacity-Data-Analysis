Given:
P(disease) = 1/10000 = 0.0001
P(+|disease) = 0.99 and P(-|no disease) = 0.99

This means:
P(-|disease) = 1-0.99 = 0.01
P(+|no disease) = 1-0.99 = 0.01

AND probabilities (via multiplication):
P(disease AND +) = 0.0001 * 0.99 = 0.000099
P(disease AND -) = 0.0001 * 0.01 = 0.000001
P(no disease AND +) = 0.9999 * 0.01 = 0.009999
P(no disease AND -) = 0.9999 * 0.99 = 0.989901

Asked:
P(disease|+)

Bayes:
P(disease|+) = P(disease AND +) / (P(disease AND +) + P(no disease AND +))
= 0.000099 / (0.000099 + 0.009999) = 1%

