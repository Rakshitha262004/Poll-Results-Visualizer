import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(counts):
    plt.figure()
    sns.barplot(x=counts.index, y=counts.values)
    plt.title("Vote Count by Option")
    plt.savefig("outputs/bar_chart.png")
    plt.close()


def plot_pie(counts):
    plt.figure()
    counts.plot.pie(autopct='%1.1f%%')
    plt.title("Vote Share")
    plt.savefig("outputs/pie_chart.png")
    plt.close()


def plot_region(region_data):
    region_data.plot(kind="bar", stacked=True)
    plt.title("Region-wise Preference")
    plt.savefig("outputs/region_chart.png")
    plt.close()