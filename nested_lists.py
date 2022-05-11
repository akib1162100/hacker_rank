if __name__ == '__main__':
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)
    unique_score_list = list(set(score_list))
    unique_score_list.sort()
    second_lowest_score = unique_score_list[1]
    zipped = list(zip(name_list, score_list))
    # zipped =sorted(zipped,key=lambda x: x[1])
    scond_list = [x for x in zipped if x[1] == second_lowest_score]
    scond_list.sort()
    for x in scond_list:
        print(x[0])
    # print(score_list)