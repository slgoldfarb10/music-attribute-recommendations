## this program is for getting an array of the similarity scores (or euclidean distances really)
## between an artists's albums

import sys
import spotipy
import spotipy.util as util
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

##-----------------------------------------------------------------------------------------------##
    ## input your own client id and client secret here
token = util.prompt_for_user_token(username, scope, client_id='your-client-id',
                                   client_secret='your-client-secret',
                                   redirect_uri='http://localhost/')
##-----------------------------------------------------------------------------------------------##

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()

## input artist uri
    shakey_graves = "spotify:artist:1fZpYWNWdL5Z3wrDtISFUH"
    lady_lamb = "spotify:artist:2wunbYU5KWrpI7RCRBkwF0"
    kendrick_lamar = "spotify:artist:2YZyLoL8N0Wb9xBt1NhZWg"
    florence_the_machine = "spotify:artist:1moxjboGR7GNWYIMWsRjgG"
    young_thug = "spotify:artist:50co4Is1HCEo8bhOyUWKpn"
    lord_huron = "spotify:artist:6ltzsmQQbmdoHHbLZ4ZN25"
    alabama_shakes = "spotify:artist:16GcWuvvybAoaHr0NqT8Eh"
    anderson_paak = "spotify:artist:3jK9MiCrA42lLAdMGUZpwa"
    tnaf = "spotify:artist:0oeUpvxWsC8bWS6SnpU8b9"
    esatmz = "spotify:artist:7giUHu5pv6YTZgSkxxCcgh"
    rja = "spotify:artist:1SImpQO0GbjRgvlwCcCtFo"
    info_soc = "spotify:artist:6bJUzb3mLEYCkTAp7eNJgO"
    white_stripes = "spotify:artist:4F84IBURUo98rz4r61KF70"
    beatles = "spotify:artist:3WrFJ7ztbogyGnTHbHJFl2"
    bob_dylan = "spotify:artist:74ASZWbe4lXaubB36ztrGX"
    nas = "spotify:artist:20qISvAhX20dpIbOOzGK3q"

##---------------------------------##
    ## choose your artist here
    artist = nas
##---------------------------------##

## get all albums from artist
    albums = []

##---------------------------------##
    ## if the artist has deluxe/live/remix albums you'd rather not take, set this to false, else true
    ## if you set it to false, you have to manually get the ids for all the albums you want
    album_get_auto = False

    ## if you want singles/eps/nonstandard albums, set this to true
    album_get_alltypes = False
##---------------------------------##

    if album_get_auto:
        if album_get_alltypes :
            albums_data = sp.artist_albums(artist, limit=19)
        else :
            albums_data = sp.artist_albums(artist, album_type='album')

        for item in albums_data['items']:
            id = item['id']
            albums.append(id)

    else:
        if (artist == kendrick_lamar) :
            damn = "4eLPsYPBmXABThSJ821sqY"
            tpab = "7ycBtnsMtyVbbwTfJwRjSP"
            gkmc = "6PBZN8cbwkqm1ERj2BGXJ1"
            s80 = "13WjgUEEAQp0d9JqojlWp1"
            uu = "0kL3TYRsSXnu0iJvFO3rud"
            od = "7MoLQ8vckhwBbQqEYQTYQC"
            albums.extend((od,s80,gkmc,tpab,uu,damn))
        elif (artist == florence_the_machine) :
            hah = "0pKZJj9GzcKPCS8r4IaksA"
            hbhbhb = "2btszoya78vyT8fwelmVnz"
            ceremonials = "5DMgU1P55Su3EVXGvgID1p"
            lungs = "2KAK58PimXHF4lSoKO3RxA"
            albums.extend((hah,hbhbhb,ceremonials,lungs))
        elif (artist == young_thug) :
            ss = "187UNqZ7MX3neMYkkevmdm"
            btg = "51KZKzPd3OQT1r46a55VTt"
            jeffery = "7EpUpNUkkEGnaCvkcn1j4H"
            ss3 = "2z4c8M8aVzl7CTobIp36KF"
            imup = "4sAB9WulPpnAcig7alDGTg"
            albums.extend((ss,btg,jeffery,ss3,imup))
        elif (artist == alabama_shakes) :
            sac = "6TWqxofcKQaZ9gHI49G36P"
            bag = "6EoJL3ty0FyE7XmLpAX2sj"
            albums.extend((sac,bag))
        elif (artist == anderson_paak) :
            yl = "0K3FiXt6ekJTWaUku3LpHL"
            malibu = "4VFG1DOuTeDMBjBLZT7hCK"
            venice = "2DOiha5oI19Dmw5M9ryHD8"
            bubblin = "6N1y1a5qnqN8pBkizOdMvk"
            tio = "7z4UqvGprXWpQ0wo8ldLDA"
            albums.extend((bubblin,tio,yl,malibu,venice))
        elif (artist == esatmz) :
            pa = "5zTYki4rUrsOhT30gghHC6"
            st = "2N1YlyZ5VVI1vDR3VuYBMj"
            here = "7n5oHXSwnbGWrFTg9xLhhN"
            ufb = "39xrkt8RILtwa9DMyLkv32"
            albums.extend((pa,st,here,ufb))
        elif (artist == info_soc) :
            i_s = "3bv0NUg3BXwT5Uh4PW4zUD"
            hack = "1tyqJvplKI4UQtHLg6CFWo"
            pali = "0V7pbRhqkpsFzEGqEy0FIb"
            dba = "2Q4mhEwMdbw4aObEnzhzjZ"
            oom = "55La0eTpdynCKiUgWcqv7m"
            albums.extend((i_s,hack,pali,dba,oom))
        elif (artist == beatles) :
            ppm = "3KzAvEXcqJKBF97HrXwlgf"
            wtb = "1aYdiJk6XKeHWGO3FzHHTr"
            ahdn = "6wCttLq0ADzkPgtRnUihLV"
            bfs = "1vANZV20H5B4Fk6yf7Ot9a"
            _help = "0PT5m6hwPRrpBwIHVnvbFX"
            rs = "50o7kf2wLwVmOTVYJOTplm"
            revolver = "3PRoXYsngSwjEQWR5PsHWR"
            splhcb = "6QaVfG1pHYl1z15ZxkvVDW"
            mmt = "2BtE7qm1qzM80p9vLSiXkj"
            twa = "1klALx0u4AavZNEvC4LrTL"
            ys = "1gKZ5A1ndFqbcrWtW85cCy"
            ar = "0ETFjACtuP2ADo6LFhL6HN"
            lib = "0jTGHV5xqHPvEcwL8f6YU5"
            albums.extend((ppm,wtb,ahdn,bfs,_help,rs,revolver,splhcb,mmt,twa,ys,ar,lib))
        elif (artist == bob_dylan) :
            bd = "5k63xxy9YcKM0H9GS3vP1K"
            tfbd = "0o1uFxZ1VTviqvNaYkTJek"
            tac = "7DZeLXvr9eTVpyI1OlqtcS"
            asbd = "3q1W9iVdyuwVOGKn696Oh0"
            biabh = "1lPoRKSgZHQAYXxzBsOQ7v"
            h61r = "6YabPKtZAjxwyWbuO9p4ZD"
            bob = "4NP1rhnsPdYpnyJP0p0k0L"
            jwh = "2KzCDxKpgLqBffHu1IZ7Kn"
            ns = "5WBx64FIN04CvM2T1MGrUN"
            _sp = "3bXEPGWxOplvbLwyasRSW3"
            nm = "48efaobqOTbvnlxbETstey"
            pgbtk = "2Pj2kZM5XpyIeyFBTAVulL"
            pw = "3gYbjd76d8T5Ct5WxCxX5R"
            bott = "4WD4pslu83FF6oMa1e19mF"
            desire = "1T8usYsiGEMPMQOLFgJEbE"
            sl = "0bd6oCsp5JoJ5erpMzHu1U"
            stc = "5k4z33VjpVmkOB18IgOD8E"
            saved = "6ytk4mtIgQP7F67XL1nozV"
            sol = "14cScWsd0lPdSlNFfr9AmA"
            infidels = "66zadu7BtUnpbkT4iAkaHy"
            eb = "4cVK8CJSUabT0moSzPYYxl"
            kol = "0BoT4M1d5H6VJr3QUjsJma"
            ditg = "1jqNoER2ibSB8I0DMm54Ac"
            om = "18ue4s9PsV3WBw7kkzD689"
            utrs = "5aRiLRWxWoAT6rTUXbGUuI"
            gaibty = "4OIFBxR56S44aXiovovyK7"
            wgw = "6lfZX6OFJRxRcODaxwSRL5"
            toom = "185DHT5SvszXRrezx3lOjt"
            lat = "4BcfuxQ4EO07Y53yr6YhAJ"
            mt = "6y2WHyqRUCeHrjMXvjnRmD"
            ttl = "5mVEtOa0CmXH5nCivFoa4x"
            cith = "6Ylr6c6snKHzMBaZHXHEWm"
            tempest = "3LnS0XKSzd2TFoagESGUw3"
            sitn = "2mVpSZrllFAWhOgCoyz8ow"
            fa = "3wjymdW6uOqrgCLWBb6ph4"
            triplicate = "5coSubIBt21W8V40Po41pY"
            albums.extend((bd,tfbd,tac,asbd,biabh,h61r,bob,jwh,ns,_sp,nm,pgbtk,
                           pw,bott,desire,sl,stc,saved,sol,infidels,
                           eb,kol,ditg,om,utrs,gaibty,wgw,toom,lat,mt,ttl,
                           cith,tempest,sitn,fa,triplicate))
        elif (artist == nas) :
            ill = "3kEtdS2pH6hKcMU9Wioob1"
            iww = "78Fgb88MY0ECc4GVMejqTg"
            iam = "4UhEjfIRx4tE1XRY21vwNa"
            damus = "0yv3K62ndWgrZ0bbAEMzj5"
            still = "0cLzuJG2UDa0axMQkF7JR6"
            lt = "2mU2jRMwrsL1tG97xKoiav"
            gs = "3rV1aPkrWyMs6YTvTpSbIY"
            sd = "0jghcWTsQzux5T9sAfZO13"
            hhid = "6rEDApQnV2QGS0GSdE1hap"
            untitled = "41LyFl0XPrCqYeNml7obol"
            lig = "0ddTtajzPmxZ7UVW2VEAln"
            nasir = "66EwBbt2kPgugo8Wz0SKAw"
            albums.extend((ill,iww,iam,damus,still,lt,gs,sd,hhid,untitled,lig,nasir))


    print (albums)

# get tracks from albums
    tracks = []
    names = []
    for i, album in enumerate(albums):
        album_tracks = sp.album_tracks(album)
        tracks.append([])
        for item in album_tracks['items']:
            id = item['id']
            tracks[i].append(id)
            name = item['name']
            names.append(name)


# get features from tracks
    features = []
    df = []
    for i, group in enumerate(tracks) :
        features.append([])
        features[i] = sp.audio_features(tracks[i])
        df.append([])
        df[i] = pd.DataFrame(features[i])

    print(len(albums))

else:
    print ("Can't get token for", username)


D = []

## We store feature data from our dataframe `df`, in the `f1-12` arrays. We combine this into
## a feature matrix before entering it into the algorithm.
## Not all features are used in my program
for i,_df in enumerate(df) :
    f1 = _df['acousticness'].values
    f2 = _df['danceability'].values
    f3 = _df['energy'].values
    f4 = _df['instrumentalness'].values
    f5 = _df['key'].values
    f6 = _df['liveness'].values
    f7 = _df['loudness'].values / 60. #to normalize-ish
    f8 = _df['mode'].values
    f9 = _df['speechiness'].values
    f10 = _df['tempo'].values
    f11 = _df['time_signature'].values
    f12 = _df['valence'].values

    ## D is used for collecting distances for similarity checks

    D.append([])
    D[i] = np.matrix(np.dstack((f1,f2,f3,f4,f6,f9,f12)))


num_albums = len(albums)


#generates a n*n array with the average distances of all the albums from each other
album_dist = [[0 for j in range(num_albums)] for i in range(num_albums)]
for i,row in enumerate(album_dist) :
    for j,col in enumerate(album_dist) :
        album_dist[i][j] = np.mean(distance.cdist(D[i], D[j], 'euclidean'))

## use this output for a csv of the distances between all the albums
pd.DataFrame(album_dist).to_csv()

## use this output to get the list of songs and indices
#pd.DataFrame(names)
