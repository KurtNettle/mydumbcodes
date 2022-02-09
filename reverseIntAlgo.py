import pstats
import cProfile

num = 299999999999299299999999999299999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687299999999999299999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687299999999999299299999999999299999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687299999999999299999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687299999999999299299999999999299999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687299999999999299999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999999999999992999999299999999999299999999999999992999999999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687999992999999999999999999966666768799299999999999999999996666676879999996666676872999999999992999999999999999999966666768799299999999999999999996666676879999996666676879996666676879929999999999999999999666667687999999666667687


def reverseIntAlgo(number, reversed_number):
    return number // 10, reversed_number * 10 + number % 10


def reverseInt(given_number):
    reversed_number = 0
    if given_number < 0:
        while (given_number < 0):
            given_number = given_number * -1
            given_number, reversed_number = reverseIntAlgo(given_number, reversed_number)
            given_number = given_number * -1
        return reversed_number * -1
    else:
        while (given_number > 0):
            given_number, reversed_number = reverseIntAlgo(given_number, reversed_number)
        return reversed_number


with cProfile.Profile() as pf:
    reverseInt(num)

stats = pstats.Stats(pf)
stats.sort_stats(pstats.SortKey.TIME)
stats.dump_stats(filename='reverseIntAlgo.prof')