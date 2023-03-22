# Morgan Gerdin
# Calculating Stats
# due 2/18/2022

def main():
    import statistics
    scores = [15, 78, 45, 69, 100, 97, 89, 32, 90, 89]          # make list of scores
    average = (statistics.mean(scores))
    minimum = str(min(scores))
    maximum = str(max(scores))
    print(f"The average test score is {average: .2f}")          # print results
    print(f"The lowest score is {minimum}")
    print(f"The highest score is {maximum}")


if __name__ == "__main__":  # call main
    main()
