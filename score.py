def cal_score(score):
    summ = 0
    for i in range(len(score)):
        summ += int(score[i])
    
    avg = int(summ) / len(score)

    if 90 <= avg <=100:
        print("A")
    elif 80 <= avg <= 89:
        print("B")
    elif 70 <= avg <= 79:
        print("C")
    elif 60 <= avg <= 69:
        print("D")
    else:
        print("F")


def main():
    s = input("Scores: " ).split(", ")
    for i in range(len(s)):
        if 0 <= int(s[i]) <= 100:
            x = s
        else:
            print("값은 0에서 100 사이의 값이어야 합니다.")
            x = False
            break
            
    if x != False:
        cal_score(x)
    # print(s)


if __name__=="__main__":
    main()

#comment 2