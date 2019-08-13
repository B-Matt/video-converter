from media_info import MediaInfo
from ffmpeg import FFmpeg

media_info = MediaInfo()
converter = FFmpeg('/usr/bin/ffmpeg', '/usr/bin/ffprobe')
media_info = converter.get_media_info("tests/promo.mp4")
print(media_info.format_info.duration)