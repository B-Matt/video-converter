from media_info import MediaInfo
from ffmpeg import FFmpeg
from pathlib import Path

media_info = MediaInfo()


ffmpeg_path = ""
converter = FFmpeg(ffmpeg_path)

print(converter.get_media_info("F:/Python/ffmpeg/promo_insta.mp4"))
