# ffprobe -print_format json -show_format -show_streams promo_insta.mp4

import json as json
from utils import Utils


class FormatInfo(object):
    """
        Describes video format container.
        Atributes are:
          * format_name - format short name
          * format_name_long - format full name
          * bit_rate - video bitrate
          * duration - video duration in seconds
          * size - file size
    """

    def __init__(self):
        self.format_name = None
        self.format_name_long = None
        self.bit_rate = None
        self.duration = None
        self.size = None

    def parse_format_data(self, key, val):
        """
        Parses format part of ffprobe output (key=value).
        """
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
    """
        Describes video stream container.
        Atributes are:
          * type - stream type (audio or video)
          * codec_name - codec name
          * duration - stream duration (in seconds)
          * bit_rate - stream bitrate (in bytes/second)
        Video attributes:
          * width - video width
          * height - video height
          * fps - stream FPS
        Audio attributes:
          * channels - number of channels in the stream
          * sample_rate - sample rate (Hz)
        Meta-data:
          * create_time - time when stream is created
          * language - stream language
    """

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
        """
        Parses stream part of ffprobe output (key=value).
        """
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
        """
        Calculates FPS from given value.
        Returns 0 if is not possible to divide two numbers.
        """
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
        Attributes are:
          * format_info - FormatInfo object
          * streams_info - List of StreamInfo objects
    """

    def __init__(self):
        self.format_info = FormatInfo()
        self.streams_info = []

    def parse_raw_data(self, data):
        """
            Parses JSON output into media objects.
        """
        decoded_data = json.loads(data)

        self.parse_format(decoded_data["format"])
        self.parse_streams(decoded_data["streams"])

    def parse_format(self, data):
        """
            Parses format part of ffprobe output into objects variables.
        """
        for key, value in data.items():
            self.format_info.parse_format_data(key, value)

    def parse_streams(self, raw):
        """
            Parses streams part of ffprobe output into objects variables.
        """
        for data in raw:
            stream = StreamInfo()
            self.streams_info.append(stream)
            for key, value in data.items():
                stream.parse_stream_data(key, value)
