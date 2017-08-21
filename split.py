# -*- coding: utf-8 -*-

import os
import sys
from pydub import AudioSegment


def get_audio_time_tracks(songsfile):
    songs = []

    with open(songsfile) as f:
        for l in f:
            time, name = l.split(' ', 1)
            songs.append((time, name.rstrip()))

    return songs

def time_to_milliseconds(lst_tracks):
    lreturn = []

    print lst_tracks

    for track in lst_tracks:
        track_time = track[0].split(':')

        def seconds_to_milli(seconds):
            return seconds * 1000

        time_ms = 0

        # convert seconds, than minutes, than hours to milliseconds.
        for index, i in enumerate(track_time[::-1]):
            time_ms += seconds_to_milli(60**index * int(i))

        lreturn.append((time_ms, track[1]))

    return lreturn


if __name__ == '__main__':
    print 'loading...'

    if len(sys.argv) > 0:
        filename, file_extension = os.path.splitext(sys.argv[1])
    else:
        print 'file to be splitted must be provided.'
        exit(1)

    if len(sys.argv) > 0:
        songs_file = sys.argv[2]
    else:
        print 'songs file must be provided.'
        exit(1)

    sound = AudioSegment.from_file(filename + file_extension, file_extension[1:])

    print 'converting time'
    tracks = get_audio_time_tracks(songs_file)
    tracks_ms = time_to_milliseconds(tracks)

    for i in  xrange(0, len(tracks_ms)):
        init = tracks_ms[i][0]

        if i + 1 >= len(tracks_ms):
            end = len(sound)
        else:
            end = tracks_ms[i+1][0]

        print 'working on {}: {} - [{}:{}]'.format(tracks_ms[i][1], tracks[i][0], init, end)
        track = sound[init:end]

        outputs = 'outputs'

        if not os.path.exists(outputs):
            os.makedirs(outputs)

        output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), outputs)
        outputfile = os.path.join(output_path,
                                  '{}_{}{}'.format(str(i), tracks[i][1], file_extension))

        track.export(outputfile, format=file_extension[1:])
