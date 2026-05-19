from solution import Track, Album

track1 = Track("Bohemian Rhapsody", 355, "Queen", 1975)
track2 = Track("Don't Stop Me Now", 210, "Queen", 1978)
track3 = Track("We Are the Champions", 179, "Queen", 1977)

album = Album("A Night at the Opera", "Queen", 1975)

album.add_track(track1)
album.add_track(track2)
album.add_track(track3)

album.show_tracks()

album.play_track(0)
album.pause()

album.stop()


album.remove_track("Don't Stop Me Now")
