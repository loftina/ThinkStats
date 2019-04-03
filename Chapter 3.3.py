
def percentile(scores, percentile_rank):
    scores.sort()
    index = (len(scores)-1) * percentile_rank / 100
    return scores[index]

def main():
    # Exercise 3.3
    scores = [55, 66, 77, 88, 99]
    result = percentile(scores, 50)
    print(result)


if __name__ == "__main__":
    main()