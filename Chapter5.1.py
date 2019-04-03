from __future__ import division
def main():
    # Exercise 5.1
    die_A = range(1,7)
    die_B = range(1,7)
    sums_to_eight = 0
    has_a_six = 0
    for dieA in die_A:
        for dieB in die_B:
            if dieA + dieB == 8:
                sums_to_eight += 1
                if dieA == 6 or dieB == 6:
                    has_a_six += 1

    print('There is a %d%% Chance' % (has_a_six/sums_to_eight*100))

    # Exercise 5.2
    print('Probability of 100 6s: %e' % (1/6)**100)
    print('Probability of 100 non6s: %e' % (5/6)**100)

    # Exercise 5.3
    # 1
    print((.5)^2)
    # 2
    print(.5)
    # 3
    print(.5)
    # 4
    print(.5)

if __name__ == '__main__':
    main()
