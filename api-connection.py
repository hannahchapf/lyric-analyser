# Import lyrics genius package
import lyricsgenius as lg

# Connect to lyrics genius api
genius = lg.Genius('3m20IpD2q8iMn8ADNa1fe8PETnLVHm1TqsEWw1SPgyCVTpy86MU3wOtim-3a7N5L',
                   skip_non_songs=True, excluded_terms=None, remove_section_headers=True)

# Define file to write lyrics to
file = open("lyrics.txt", "w")

# Define function to search artists and return lyrics
def get_lyrics(arr, k):
    """ 
    This function takes in a list of artist names and a number as inputs and puts lyrics into a text file.
    arr is the artist array, and k is the number of lyrics per artist
    """
    # Set counter to 0
    c = 0
    # Loop through artist names
    for name in arr:
        try:
            # If artist exists in genius search and has at least k songs then write lyrics to the file
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))
            c += 1
            # Print what lyrics were written
            print(f"Songs grabbed:{len(s)}")
        except:
            # If artist cannot be found
            print(f"some exception at {name}: {c}")

# Define artists to search lyrics for
artists = ['Rihanna','Taylor Swift','girl in red']

# Run function for artists
get_lyrics(artists, 3)