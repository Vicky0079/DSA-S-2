def recommend_friends(user, profiles):
    recommendations = []

    user_interests = set(profiles[user]["interests"])

    for other_user, data in profiles.items():

        if other_user != user:

            common = user_interests.intersection(
                set(data["interests"])
            )

            recommendations.append(
                (other_user, len(common))
            )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations