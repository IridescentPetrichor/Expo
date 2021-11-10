class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

All_Star = Song(["Some Body Once Told Me"
                 "The World was gonna roll me"
                 "I ain't the sharpest tool in the shed"])

Like_You_Do = Song(["Lately, I can't help but think"
                    "that our roads might take us down"
                    "different phases"])

All_Star.sing_me_a_song()
Like_You_Do.sing_me_a_song()
