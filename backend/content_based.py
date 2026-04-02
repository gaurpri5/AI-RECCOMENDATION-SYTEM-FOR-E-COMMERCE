import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def content_based_recommendation(cleaned_data, product_name, top_n=5):

    # Fix NaN in Tags column
    cleaned_data["Tags"] = cleaned_data["Tags"].fillna("")

    # Step 1: Check if product exists
    if product_name not in cleaned_data["Name"].values:
        print("Product not found.")
        return pd.DataFrame()

    # Step 2: Convert Tags column into TF-IDF vectors
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(cleaned_data["Tags"])

    # Step 3: Calculate cosine similarity
    similarity = cosine_similarity(tfidf_matrix)

    # Step 4: Get index of selected product
    index = cleaned_data[cleaned_data["Name"] == product_name].index[0]

    # Step 5: Get similarity scores
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Step 6: Take top similar products (excluding itself)
    top_products = scores[1:top_n+1]
    product_indices = [i[0] for i in top_products]

    # Step 7: Return recommended products
    return cleaned_data.iloc[product_indices][
        ["Name", "Brand", "Review Count"]
    ]
if __name__ == "__main__":

    import pandas as pd

    # Load cleaned dataset
    data = pd.read_csv("clean_data.csv")

    # Select first product automatically
    product = data["Name"].iloc[0]

    # Get recommendations
    recommendations = content_based_recommendation(
        cleaned_data=data,
        product_name=product,
        top_n=5
    )

    print("Selected Product:", product)
    print("\nRecommended Products:")
    print(recommendations)





