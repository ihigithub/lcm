# calculates least common multiple
from gcd.gcd import users_gcd


def users_lcm(a, b):
    gcd = users_gcd(a, b)
    return a * b / gcd


def lcm_of_three(a, b, c):
    lcm_of_first_two = users_lcm(a, b)
    lcm_of_last_two = users_lcm(b, c)
    return users_lcm(lcm_of_first_two, lcm_of_last_two)


def lcm_of_n(_list_of_numbers_for_lcm):

    if len(_list_of_numbers_for_lcm) == 2:

        return users_lcm(_list_of_numbers_for_lcm[0], _list_of_numbers_for_lcm[1])

    else:
        new_list = []
        for i in range(len(_list_of_numbers_for_lcm)-1):
            a = _list_of_numbers_for_lcm[i]
            b = _list_of_numbers_for_lcm[i+1]
            new_list.append(users_lcm(a, b))
        # print new_list
        return lcm_of_n(new_list)


# test users_lcm
# print users_lcm(10,5)

# test lcm_of_three
# print lcm_of_three(2,5,70)

# test of arbitrary numbers
list_of_numbers_for_lcm = [2, 3, 5, 40]
print lcm_of_n(list_of_numbers_for_lcm)

