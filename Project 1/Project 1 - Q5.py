# DO NOT DELETE/EDIT THIS LINE OF CODE, AS IT IS USED TO PROVIDE ACCESS TO
# THE FUNCTIONS FROM Q2 AND Q3
from hidden import friend_besties, friend_second_besties

def friendly_prediction(unknown_user, features, bestie_dict, feat_dict):
    # find the users best friend('s)
    users_best_friends = friend_besties(unknown_user, bestie_dict)
    second_best_friends = friend_second_besties(unknown_user, bestie_dict)

    new_dict = {}
    # add features to new dict first:
    for feature in features:
        if feature not in new_dict:
            new_dict[feature] = []

    # find their interests that coincide with user's features
    for feature in features:
        for friend in users_best_friends:
            if friend in feat_dict and feature in feat_dict[friend]:
                new_dict[feature].append(feat_dict[friend][feature])

    # if their best friend doesn't fit all the features, use the 2nd degree
    # friendship
    for feature in features:
        for close_friend in users_best_friends:
            for friend in second_best_friends:
                if friend in feat_dict and feature in feat_dict[friend]:
                    for key, value in feat_dict[friend].items():
                        if key is feature:
                            new_dict[feature].append(value)
    for feature in new_dict:
        new_dict[feature] = sorted(new_dict[feature])
    return new_dict


