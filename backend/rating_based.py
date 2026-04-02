import pandas as pd


def rating_based_recommendation(data, top_n=5):

    # Sort by Rating and Review Count
    sorted_data = data.sort_values(
        by=["Rating", "Review Count"],
        ascending=False
    )

    # Remove duplicate products
    unique_products = sorted_data.drop_duplicates(subset="ProdID")

    return unique_products[
        ["Name", "Brand", "Rating", "Review Count"]
    ].head(top_n)


# testing
if __name__ == "__main__":

    data = pd.read_csv("clean_data.csv")

    recommendations = rating_based_recommendation(data)

    print("Top Rated Products:")
    print(recommendations)