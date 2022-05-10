if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_sorted_arr = sorted(list(set(arr)))
    print(unique_sorted_arr[-2])