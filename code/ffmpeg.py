import stat
import os.path
import os
import re
import signal
from subprocess import Popen, PIPE
from media_info import MediaInfo


class FFmpeg(object):
    """
        FFmpeg wrapper class used for calling FFmpeg commands and parsing files.
    """

    def __init__(self, path_ffmpeg):
        self.ffmpeg_path = path_ffmpeg

        if not os.path.exists(self.ffmpeg_path):
            raise Exception("FFmpeg binary not found: " +
                            str(self.ffmpeg_path))

    def call_command(self, cmds):
        """
            Calls commands in terminal.
        """
        os.chdir(self.ffmpeg_path)
        return Popen(cmds, shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)

    def get_media_info(self, file_name):
        """
            Gets media_info from given file.
            Returns MediaInfo object or None if specified file is not valid.
        """
        if not os.path.exists(file_name):
            return None

        info = MediaInfo()
        pipe = self.call_command(
            [self.ffmpeg_path, '-print_format json', '-show_format', '-show_streams', file_name])
        encoded_data, _ = pipe.communicate()
        output_data = encoded_data.decode('UTF-8')
        print("Raw:\n" + str(output_data))
        info.parse_raw_data(output_data)

        if info.format_info is None and len(info.streams_info) == 0:
            return None

        return info
