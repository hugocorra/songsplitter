# -*- coding: utf-8 -*-

import os
from pydub import AudioSegment


def get_audio_time_tracks():
    return [
        ('1:20', 'Song with no name'),
        ('3:34', 'Koto'),
        ('4:52', 'How Did I Get Here'),
        ('7:06', 'Big Girls Cry (ODESZA Remix)'),
        ('10:28', 'White Lies'),
        ('12:00', 'All We Need'),
        ('14:25', 'Today'),
        ('18:10', 'Saola (ODESZA Remix)'),
        ('20:52', 'Above The Middle'),
        ('23:06', 'Sun Models'),
        ('26:53', 'If There\'s Time'),
        ('28:30', 'One Day They\'ll Know (ODESZA Remix)'),
        ('30:32', 'Open Wound (ODESZA Remix)'),
        ('33:45', 'Keep Her Close'),
        ('36:28', 'Bloom'),
        ('39:09', 'Waited 4 U (ODESZA Remix)'),
        ('43:20', 'Divinity (ODESZA Remix)'),
        ('46:10', 'My Friends Never Die'),
        ('48:42', 'Kusanagi'),
        ('50:57', 'Honestly no idea'),
        ('52:34', 'Memories That You Call'),
        ('56:27', 'Faded (ODESZA Remix)'),
        ('1:00:00', 'Something About You (ODESZA Remix)'),
        ('1:04:26', 'Say My Name'),
        ('1:08:43', 'IPlayYouListen'),
        ('1:11:52', 'A Heartbreak (ODESZA Remix)'),
        ('1:16:09', 'Make Me Feel Better'),
    ]


def time_to_milliseconds(lst_tracks):
    lreturn = []

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
    sound = AudioSegment.from_mp3("aaa.mp3")

    print 'converting time'
    tracks = get_audio_time_tracks()
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
                                  '{}_{}.mp3'.format(str(i), tracks[i][1]))

        track.export(outputfile, format="mp3")
