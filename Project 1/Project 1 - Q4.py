# DO NOT DELETE/EDIT THIS LINE OF CODE, AS IT IS USED TO PROVIDE ACCESS TO
# THE FUNCTIONS FROM Q2 AND Q3
from hidden import friend_besties, friend_second_besties


def besties_coverage(individuals, bestie_dict, relationship_list):
    total_ppl = len(bestie_dict)
    indiv_friends = []
    if relationship_list == []:
        for individual in individuals:
            for friends in bestie_dict[individual]:
                indiv_friends.append(friends)
                ratio = len(indiv_friends) / total_ppl

    if relationship_list == [friend_besties]:
        for individual in individuals:
            ratio = (len(friend_besties(individual, bestie_dict)) + 1) / total_ppl

    if relationship_list == [friend_second_besties]:
        for individual in individuals:
            ratio = (len(friend_second_besties(individual, bestie_dict)) + 1) / total_ppl

    if relationship_list == [friend_besties, friend_second_besties] or relationship_list == [friend_second_besties,
                                                                                             friend_besties]:
        for individual in individuals:
            ratio = (len(friend_second_besties(individual, bestie_dict)) + 1) / total_ppl + len(
                friend_besties(individual, bestie_dict)) / total_ppl
    return ratio
