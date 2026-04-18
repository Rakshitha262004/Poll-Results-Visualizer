from src.data_generator import generate_data
from src.data_loader import load_data
from src.preprocessing import clean_data
from src.analysis import analyze_options, region_analysis
from src.visualization import plot_bar, plot_pie, plot_region
from src.insights import generate_insights

# Step 1: Generate Data
generate_data()

# Step 2: Load Data
df = load_data("data/poll_data.csv")

# Step 3: Clean Data
df = clean_data(df)

# Step 4: Analyze
results = analyze_options(df)
region_data = region_analysis(df)

# Step 5: Visualize
plot_bar(results["counts"])
plot_pie(results["counts"])
plot_region(region_data)

# Step 6: Insights
insight = generate_insights(results["counts"])

print("\n📊 ANALYSIS COMPLETE")
print(insight)