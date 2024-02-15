for j in range(10):
    x = input().split()
    c = int(x[0])
    n = int(x[1])

    play = 0
    for i in range(n):
        x = input()
        if x == "B":
            play+=c
        play-=1
        if play < 0 :
            play = 0

    print(play)