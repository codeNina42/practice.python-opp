import time

def type_lyrics(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.05)
    print()

class Song:
    @staticmethod
    def print_lyrics():
        lyrics = [
            "Haathon ko sambhalo mere haathon main",
            "kaise haaton ko sambhalo mere haathon main",
            "jab tak neend na aaye in lakeeron main",
            "baatein hon..",
            "Haan...."
        ]

        delays = [2.0, 1.8, 2.1, 2.4, 1.7]

        print("Arz kiya hai Lyrics")
        time.sleep(1.5)

        for i, line in enumerate(lyrics):
            type_lyrics(line)
            time.sleep(delays[i])


Song.print_lyrics()
     
