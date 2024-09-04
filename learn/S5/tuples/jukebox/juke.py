from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:

    print("Choose your album: Invalid choice exists")
    # for i in range(len(albums)):
    #     # selected albums 
    #     album = albums[i][0]
    #     print(f"{i+1}. {album}")

    # each album is a tuple - rerpresents (title<string>, artist<string>, year<int>, songs<list>)
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}. {title}")
    
    album_choice = int(input())

    if 0 < album_choice < len(albums) + 1:
        print("Choose your song:")

        # songs list for that album
        songs = albums[album_choice-1][SONGS_LIST_INDEX]

        # each song represents a tuple of (number, title)
        for (song_id) in songs:
            number, title = (song_id)
            print(f"{number}. {title}")
        song_choice = int(input())
        """"
        for i in range(len(songs)):
            print(f"{i+1}. {songs[i][1]}")
        song_choice = int(input())
        """
        
        if 0 < song_choice < len(songs) + 1:
            print(f"Playing \"{songs[song_choice-1][SONG_TITLE_INDEX]}\"")
            print("="*40)
        else:
            print("No track detected")
    else:
        print("No album detected")

    