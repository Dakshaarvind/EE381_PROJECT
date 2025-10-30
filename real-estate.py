import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('Sales_01_20.csv')


# Print column names to verify (comment out after checking)
print("Column names in CSV:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())


df['Year'] = pd.to_datetime(df['List Year']).dt.year

# Group by year and calculate statistics
yearly_stats = df.groupby('Year')['Sale Amount'].agg(['mean', 'std', 'count'])

# Calculate probability of sales in $200,000 to $300,000 range
yearly_prob = []
years = []

for year in range(2001, 2021):
    year_data = df[df['Year'] == year]['Sale Amount']
    total_sales = len(year_data)
    
    if total_sales > 0:
        # Count sales in the $200k-$300k range (inclusive)
        in_range = len(year_data[(year_data >= 200000) & (year_data <= 300000)])
        probability = in_range / total_sales
    else:
        probability = 0
    
    yearly_prob.append(probability)
    years.append(year)

# Print results
print("\n" + "="*70)
print("YEARLY STATISTICS (2001-2020)")
print("="*70)
print(f"{'Year':<8} {'Mean':<15} {'Std Dev':<15} {'Probability ($200k-$300k)':<25}")
print("-"*70)

for year in range(2001, 2021):
    if year in yearly_stats.index:
        mean_val = yearly_stats.loc[year, 'mean']
        std_val = yearly_stats.loc[year, 'std']
        prob_val = yearly_prob[year - 2001]
        print(f"{year:<8} ${mean_val:<14,.2f} ${std_val:<14,.2f} {prob_val:<25.4f}")
    else:
        print(f"{year:<8} No data available")

print("="*70)

# Create bar graphs
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Yearly Mean Sale Prices
years_with_data = yearly_stats.index.tolist()
means = yearly_stats['mean'].tolist()

ax1.bar(years_with_data, means, color='skyblue', edgecolor='black')
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Mean Sale Price ($)', fontsize=12, fontweight='bold')
ax1.set_title('Yearly Mean Sale Prices (2001-2020)', fontsize=14, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)
ax1.set_xticks(range(2001, 2021))
ax1.set_xticklabels(range(2001, 2021), rotation=45)

# Format y-axis to show currency
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# Plot 2: Yearly Standard Deviation of Sale Prices
stds = yearly_stats['std'].tolist()

ax2.bar(years_with_data, stds, color='lightcoral', edgecolor='black')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Standard Deviation ($)', fontsize=12, fontweight='bold')
ax2.set_title('Yearly Standard Deviation of Sale Prices (2001-2020)', fontsize=14, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
ax2.set_xticks(range(2001, 2021))
ax2.set_xticklabels(range(2001, 2021), rotation=45)

# Format y-axis to show currency
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

plt.tight_layout()
plt.savefig('yearly_statistics.png', dpi=300, bbox_inches='tight')
plt.show()

# Create probability bar graph
fig, ax3 = plt.subplots(figsize=(12, 6))

ax3.bar(years, yearly_prob, color='lightgreen', edgecolor='black')
ax3.set_xlabel('Year', fontsize=12, fontweight='bold')
ax3.set_ylabel('Probability', fontsize=12, fontweight='bold')
ax3.set_title('Yearly Probability of Sale Price $200,000 - $300,000 (2001-2020)', 
              fontsize=14, fontweight='bold')
ax3.grid(axis='y', alpha=0.3)
ax3.set_xticks(range(2001, 2021))
ax3.set_xticklabels(range(2001, 2021), rotation=45)
ax3.set_ylim([0, max(yearly_prob) * 1.1])

# Format y-axis as percentage
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.2%}'))

plt.tight_layout()
plt.savefig('yearly_probability.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nGraphs saved as 'yearly_statistics.png' and 'yearly_probability.png'")
print("Analysis complete!")