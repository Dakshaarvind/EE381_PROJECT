import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
fname = 'Sales_01_20.csv'
data = np.loadtxt(fname, delimiter=',', skiprows=1)


years_col = data[:, 0].astype(int)  # First column: List Year
prices_col = data[:, 1]              # Second column: Sale Amount


print(f"Total number of sales: {len(data)}")
print(f"Year range: {int(np.min(years_col))} to {int(np.max(years_col))}")
print()

# Initialize arrays to store results
years = np.arange(2001, 2021)  # Years from 2001 to 2020
means = np.zeros(20)
stds = np.zeros(20)
probabilities = np.zeros(20)

# Calculate statistics for each year
print("="*70)
print("YEARLY STATISTICS (2001-2020)")
print("="*70)
print(f"{'Year':<8} {'Mean':<15} {'Std Dev':<15} {'Probability ($200k-$300k)':<25}")
print("-"*70)

for i, year in enumerate(years):
    # Get all prices for this year
    year_prices = prices_col[years_col == year]
    
    if len(year_prices) > 0:
        # Calculate mean and standard deviation
        means[i] = np.mean(year_prices)
        stds[i] = np.std(year_prices)
        
        # Calculate probability for $200k - $300k range
        in_range = np.sum((year_prices >= 200000) & (year_prices <= 300000))
        probabilities[i] = in_range / len(year_prices)
        
        print(f"{year:<8} ${means[i]:<14,.2f} ${stds[i]:<14,.2f} {probabilities[i]:<25.4f}")
    else:
        print(f"{year:<8} No data available")

print("="*70)
print()

# Create bar graphs for Mean and Standard Deviation
fig, ax = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Yearly Mean Sale Prices
ax[0].bar(years, means, color='skyblue', ec='black')
ax[0].set_xlabel('Year', fontsize=12, fontweight='bold')
ax[0].set_ylabel('Mean Sale Price ($)', fontsize=12, fontweight='bold')
ax[0].set_title('Yearly Mean Sale Prices (2001-2020)', fontsize=14, fontweight='bold')
ax[0].grid(axis='y', alpha=0.3)
ax[0].set_xticks(years)
ax[0].set_xticklabels(years, rotation=45)

# Plot 2: Yearly Standard Deviation of Sale Prices
ax[1].bar(years, stds, color='lightcoral', ec='black')
ax[1].set_xlabel('Year', fontsize=12, fontweight='bold')
ax[1].set_ylabel('Standard Deviation ($)', fontsize=12, fontweight='bold')
ax[1].set_title('Yearly Standard Deviation of Sale Prices (2001-2020)', fontsize=14, fontweight='bold')
ax[1].grid(axis='y', alpha=0.3)
ax[1].set_xticks(years)
ax[1].set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.savefig('yearly_statistics.png', dpi=300, bbox_inches='tight')
plt.show()

# Create probability bar graph
fig2, ax2 = plt.subplots(figsize=(12, 6))

ax2.bar(years, probabilities, color='lightgreen', ec='black')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Probability', fontsize=12, fontweight='bold')
ax2.set_title('Yearly Probability of Sale Price $200,000 - $300,000 (2001-2020)', 
              fontsize=14, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.savefig('yearly_probability.png', dpi=300, bbox_inches='tight')
plt.show()

print("Graphs saved as 'yearly_statistics.png' and 'yearly_probability.png'")
print("Analysis complete!")