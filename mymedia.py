import requests
import urllib3


urllib3.disable_warnings()


class MyMedia:
    """
    An object representing a MyMedia video.
    """

    PLAYLIST = "https://stream.library.utoronto.ca:1935/MyMedia/play/mp4:1/" \
               "{ID}.mp4/playlist.m3u8"
    CHUNKLIST = "https://stream.library.utoronto.ca:1935/MyMedia/play/mp4:1/" \
                "{ID}.mp4/{NAME}"

    def __init__(self, link: str) -> None:
        """
        Initialize this object.
        :param link:
        """
        self.link = link
        self.video_id = ""
        self.video_title = ""
        self.playlist = ""
        self.chunklist = ""
        self.chunks = []

        self._fetch_information()

    def _fetch_information(self) -> None:
        """
        Fetch information about this video.
        :return:
        """
        self.video_id = self.link[self.link.rfind("/") + 1:]
        self.playlist = self.PLAYLIST.format(ID=self.video_id)

        r = requests.get(self.playlist, verify=False)
        content = r.text.splitlines()
        self.chunklist = self.CHUNKLIST.format(ID=self.video_id,
                                               NAME=content[-1])

        r = requests.get(self.chunklist, verify=False)
        for chunk in r.text.splitlines():
            if chunk.rstrip().endswith('.ts'):
                self.chunks.append(self.CHUNKLIST.format(ID=self.video_id,
                                                         NAME=chunk))

    def get_link(self) -> str:
        """
        Return the link to this video.
        :return:
        """
        return self.link

    def get_id(self) -> str:
        """
        Return the ID of this video.
        :return:
        """
        return self.video_id

    def get_title(self) -> str:
        """
        Return the title of this video.
        :return:
        """
        return self.video_title

    def get_playlist(self) -> str:
        """
        Return the playlist of this video.
        :return:
        """
        return self.playlist

    def get_chunklist(self) -> str:
        """
        Return the chunklist of this video.
        :return:
        """
        return self.chunklist

    def get_chunks(self) -> list:
        """
        Return the chunks of this video.
        :return:
        """
        return self.chunks
