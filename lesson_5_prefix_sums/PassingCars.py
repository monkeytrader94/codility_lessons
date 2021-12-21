def solution(A):

    east = 0
    passing_cars = 0

    for direction in A:
        if direction == 0:
            east += 1
        elif direction == 1:
            passing_cars += east

    if passing_cars > 1_000_000_000:
        return -1
    return passing_cars