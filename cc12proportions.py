# -*- coding: utf-8 -*-
"""CC12Proportions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r0RS7K00xKmKmYyc6Nk3CGYClxs7vSfH
"""

!pip install scipy statsmodels
!pip install matplotlib scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

"""*The department of code enforcement of a county government issues permits to general contractors to work on residential projects. For each permit issued, the department inspects the result of the project and gives a “pass” or “fail” rating. A failed project must be re-inspected until it receives a pass rating. The department had been frustrated by the high cost of re-inspection and decided to publish the inspection records of all contractors on the web. It was hoped that public access to the records would lower the re-inspection rate. A year after the web access was made public, two samples of records were randomly selected. One sample was selected from the pool of records before the web publication and one after. The proportion of projects that passed on the first inspection was noted for each sample. Out of 500 without public web access, 67% passed on the first inspection and out of 100 with public web access, 80% passed. Test whether there is sufficient evidence to conclude that public web access to the inspection records has increased the proportion of projects that passed on the first inspection by more than 5 percentage points. Use the critical value approach at the 10% level of significance.*"""

n1 = 500
p1 = 0.67
n2 = 100
p2 = 0.80
alpha = 0.10

SE = np.sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))

difference = p2 - p1 - 0.05
Z = difference / SE

critical_value = norm.ppf(1 - alpha)

x = np.linspace(-3, 3, 1000)
y = norm.pdf(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Normal Distribution', color='blue')
x_fill = np.linspace(critical_value, 3, 1000)
y_fill = norm.pdf(x_fill)
plt.fill_between(x_fill, y_fill, color='red', alpha=0.5, label='Rejection Region')
x_fill_non_reject = np.linspace(-3, critical_value, 1000)
y_fill_non_reject = norm.pdf(x_fill_non_reject)
plt.fill_between(x_fill_non_reject, y_fill_non_reject, color='blue', alpha=0.2, label='Non-Rejection Region')
plt.axvline(Z, color='green', linestyle='--', label=f'Test Statistic (Z={Z:.2f})')
plt.axvline(critical_value, color='red', linestyle='--', label=f'Critical Value (Z={critical_value:.2f})')
plt.xlabel('Z-Score')
plt.ylabel('Probability Density')
plt.title('Hypothesis Test for Difference in Proportions')
plt.legend()
plt.show()

"""*### Since the test statistic, 1.77 is greater than the critical value 1.28, we reject the null hypothesis.*
There is sufficient evidence at the 10% level of significance to conclude that public web access to the inspection records has increased the proportion of projects that passed on the first inspection by more than 5 percentage points.
"""