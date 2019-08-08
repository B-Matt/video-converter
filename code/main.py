from media_info import MediaInfo

media_info = MediaInfo()

with open('test_data/ffprobe_dump.json', 'r') as f:
    media_info.parse_raw_data(f.read())
    f.close()
