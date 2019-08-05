# ffprobe -print_format json -show_format -show_streams promo_insta.mp4

from utils import Utils


class FormatInfo(object):
    def __init__(self):
        self.format_name = None
        self.format_name_long = None
        self.bit_rate = None
        self.duration = None
        self.size = None

    def parse_format_data(self, key, val):
        if key == "format_name":
            self.format_name = val
        elif key == "format_long_name":
            self.format_name_long = val
        elif key == "bit_rate":
            self.bit_rate = Utils.parse_int(val)
        elif key == "duration":
            self.duration = Utils.parse_float(val)
        elif key == "size":
            self.size = Utils.parse_int(val)


class StreamInfo(object):
    def __init__(self):
        self.type = None
        self.codec_name = None
        self.duration = None
        self.bit_rate = None

        # Video atributes
        self.width = None
        self.height = None
        self.fps = None

        # Audio atributes
        self.channels = None
        self.sample_rate = None

        # Meta-data atributes
        self.create_time = None
        self.language = None

    def parse_stream_data(self, key, val):
        if key == 'codec_type':
            self.type = val
        elif key == 'codec_name':
            self.codec_name = val
        elif key == 'duration':
            self.duration = Utils.parse_float(val)
        elif key == 'bit_rate':
            self.bit_rate = Utils.parse_int(val)
        elif key == 'width':
            self.width = Utils.parse_int(val)
        elif key == 'height':
            self.height = Utils.parse_int(val)
        elif key == 'avg_frame_rate':
            self.fps = self.calculate_fps(val)
        elif key == 'channels':
            self.channels = Utils.parse_int(val)
        elif key == 'sample_rate':
            self.sample_rate = Utils.parse_float(val)
        elif key == 'creation_time':  # print(y["streams"][0]["tags"])
            self.create_time = val
        elif key == 'language':
            self.language = val

    def calculate_fps(self, val):
        n, d = val.split('/')
        n = Utils.parse_float(n)
        d = Utils.parse_float(d)
        try:
            return (n / d)
        except:
            return 0


class MediaInfo(object):
    """
    JSON formater of ffprobe data!
    """
