import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.interpolate import interp1d
'''
Utilized ChatGPT
'''

'Parameters for both distributions'
mu1, sigma1 = 0, 1
mu2, sigma2 = 175, 3

'Set wide range and calculate Probability Distribution and Cumulative Distribution for both parameters'
x_values = np.linspace(-10, 200, 1000)
pdf1 = norm.pdf(x_values, mu1, sigma1)
cdf1 = norm.cdf(x_values, mu1, sigma1)

pdf2 = norm.pdf(x_values, mu2, sigma2)
cdf2 = norm.cdf(x_values, mu2, sigma2)

'Calculate Area under PDF bell curves'
'FOR PDF 1 I USED THE STATED PARAMETERS OF x < 1, BUT THE PROVIDED GRAPHS FROM THE HW DOCUMENT HAS x < -0.5 AS A PARAMETER'
area_under_pdf1 = np.trapz(pdf1[x_values <= 1], x_values[x_values <= 1])
area_under_pdf2 = np.trapz(pdf2[x_values >= (mu2 + 2 * sigma2)], x_values[x_values >= (mu2 + 2 * sigma2)])

'Set index for CDF curves'
idx_x1_pdf1 = np.argmin(np.abs(x_values - 1))
idx_mu_2sigma_pdf2 = np.argmin(np.abs(x_values - (mu2 + 2 * sigma2)))

'Interpolate CDF values and calculate phi(x) values'
cdf_interp1 = interp1d(x_values, cdf1)
cdf_interp2 = interp1d(x_values, cdf2)

y_value_x1_pdf1 = cdf_interp1(x_values[idx_x1_pdf1])
y_value_mu_2sigma_pdf2 = cdf_interp2(x_values[idx_mu_2sigma_pdf2])

'Create one figure of 4 graphs stacked and grouped by parameters'
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

'Plot PDFs and CDFs for both parameters'
# PDF1
axs[0, 0].plot(x_values, pdf1, label='PDF: μ=0, σ=1')
axs[0, 0].set_title('Probability Distribution Function - N(0, 1)')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('Probability Density')
axs[0, 0].legend()
axs[0, 0].set_xlim(-5, 5)
axs[0, 0].fill_between(x_values, pdf1, where=(x_values <= 1), color='lightblue', alpha=0.5)
axs[0, 0].annotate(f'P(x<1, N(0, 1) = {area_under_pdf1:.3f}', xy=(0.0001, 0.2), xycoords='axes fraction', ha='left', fontsize=10, color='blue')

# CDF1
axs[1, 0].plot(x_values, cdf1, label='CDF: μ=0, σ=1')
axs[1, 0].set_title('Cumulative Distribution Function - N(0, 1)')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('Cumulative Probability')
axs[1, 0].legend()
axs[1, 0].set_xlim(-5, 5)
#In case this section looks strange, this line annotates the Cumulative Distribution graph to display the cumulative value, I had to play with
#the xytext position values to make it look decent. ChatGPT gave a character code for phi instead of the unicode designator
axs[1, 0].annotate(f'{chr(966)}(x) = {y_value_x1_pdf1:.3f}', xy=(1, y_value_x1_pdf1), xytext=((x_values[idx_x1_pdf1]-5), y_value_x1_pdf1 - 0.05),
                   arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# PDF2
axs[0, 1].plot(x_values, pdf2, label='PDF: μ=175, σ=3')
axs[0, 1].set_title('Probability Distribution Function - N(175, 3)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('Probability Density')
axs[0, 1].legend()
axs[0, 1].set_xlim(150, 200)
axs[0, 1].fill_between(x_values, pdf2, where=(x_values >= (mu2 + 2 * sigma2)), color='lightblue', alpha=0.5)
axs[0, 1].annotate(f'P(x>{mu2 + 2 * sigma2}, N(175, 3) = {area_under_pdf2:.3f}', xy=(1, 0.2), xycoords='axes fraction', ha='right', fontsize=10, color='blue')

# CDF2
axs[1, 1].plot(x_values, cdf2, label='CDF: μ=175, σ=3')
axs[1, 1].set_title('Cumulative Distribution Function - N(175, 3)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('Cumulative Probability')
axs[1, 1].legend()
axs[1, 1].set_xlim(150, 200)
#See note on lines 56 and 57
axs[1, 1].annotate(f'{chr(966)}(x) = {y_value_mu_2sigma_pdf2:.3f}', xy=(x_values[idx_mu_2sigma_pdf2], y_value_mu_2sigma_pdf2),
                   xytext=(x_values[idx_mu_2sigma_pdf2] - 20, 0.8),
                   arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

'Adjust layout and display Figure'
plt.tight_layout()
plt.show()
