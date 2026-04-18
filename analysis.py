def analyze_options(df):
    counts = df["Option"].value_counts()
    percentages = df["Option"].value_counts(normalize=True) * 100

    summary = {
        "counts": counts,
        "percentages": percentages
    }
    return summary


def region_analysis(df):
    return df.groupby(["Region", "Option"]).size().unstack()