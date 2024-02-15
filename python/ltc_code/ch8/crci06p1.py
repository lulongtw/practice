n = int(input())

# List starts with dummy index 0 that we don't use
# (because villagers are numbered from 1)
villager_songs = [set()] #一開始就有一個set 是要當index0 方便之後村民計算

for i in range(n):
    villager_songs.append(set())  #總村民的個人歌單

num_evenings = int(input())

song_number = 0

for i in range(num_evenings):
    lst = input().split()
    lst.pop(0)
    for j in range(len(lst)):
        lst[j] = int(lst[j])

    today = set(lst)  #今日出席人員

    if 1 in today:  # Bard is there; villagers learn new song
        for villager in today:
            villager_songs[villager].add(song_number) #給當天有出席的村民 在總村民的該人歌單上加上當天歌名
        song_number = song_number + 1                 #歌名更新
    else:  # Bard isn't there; villagers learn union of songs
        songs_known = set()
        for villager in today:                        #bard不在時 給所有村民交流所有歌
            songs_known.update(villager_songs[villager])
        for villager in today:
            villager_songs[villager].update(songs_known)

for i in range(1, n + 1):
    if len(villager_songs[i]) == song_number:
        print(i)
