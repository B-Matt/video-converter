from media_info import MediaInfo
from ffmpeg import FFmpeg

media_info = MediaInfo()
converter = FFmpeg('', '')

with open('test_data/ffprobe_dump.json', 'r') as f:
    media_info.parse_raw_data(f.read())
    f.close()
