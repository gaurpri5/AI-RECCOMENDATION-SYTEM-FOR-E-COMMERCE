import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def collaborative_filtering_recommendations(data, target_user_id, top_n=5):

    # Step 1: Create user-item matrix
    user_item_matrix = data.pivot_table(
        index="User's ID",
        columns="ProdID",
        values="Rating",
        aggfunc="mean"
    ).fillna(0)

    # Step 2: Compute cosine similarity between users
    user_similarity = cosine_similarity(user_item_matrix)

    # Step 3: Get index of target user
    target_user_index = user_item_matrix.index.get_loc(target_user_id)

    # Step 4: Get similarity scores
    user_similarities = user_similarity[target_user_index]

    # Step 5: Sort similar users
    similar_users_indices = user_similarities.argsort()[::-1][1:]

    recommended_items = []

    # Step 6: Find products rated by similar users
    for user_index in similar_users_indices:

        rated_by_similar_user = user_item_matrix.iloc[user_index]

        not_rated_by_target = (
            (rated_by_similar_user > 0) &
            (user_item_matrix.iloc[target_user_index] == 0)
        )

        items = user_item_matrix.columns[not_rated_by_target]

        recommended_items.extend(items)

        if len(recommended_items) >= top_n:
            break

    # Step 7: Get product details
    recommended_items = recommended_items[:top_n]

    recommended_products = data[
        data["ProdID"].isin(recommended_items)
    ][["Name", "Brand", "Rating", "Review Count"]]

    return recommended_products.drop_duplicates()


# testing block
if __name__ == "__main__":

    data = pd.read_csv("clean_data.csv")

    # Remove NaN user IDs
    data = data.dropna(subset=["User's ID"])

    # Convert to int
    data["User's ID"] = data["User's ID"].astype(int)

    print("Available users:")
    print(data["User's ID"].unique()[:10])

    target_user = int(input("Enter User ID: "))

    recommendations = collaborative_filtering_recommendations(
        data,
        target_user,
        top_n=5
    )

    print("\nRecommended Products:")
    print(recommendations)