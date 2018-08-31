from unittest import TestCase

from . import BackendTestMixin
from embed_video.backends import YoutubeBackend, UnknownIdException


class YoutubeBackendTestCase(BackendTestMixin, TestCase):
    urls = (
        ('https://youtu.be/jsrRJyHBvzw', 'jsrRJyHBvzw'),
        ('https://youtu.be/n17B_uFF4cA', 'n17B_uFF4cA'),
        ('https://youtu.be/t-ZRX8984sc', 't-ZRX8984sc'),
        ('https://youtube.com/watch?v=jsrRJyHBvzw', 'jsrRJyHBvzw'),
        ('https://www.youtube.com/v/0zM3nApSvMg?rel=0', '0zM3nApSvMg'),
        ('https://www.youtube.com/embed/0zM3nApSvMg?rel=0', '0zM3nApSvMg'),
        ('https://www.youtube.com/watch?v=jsrRJyHBvzw', 'jsrRJyHBvzw'),
        ('https://www.youtube.com/watch?v=t-ZRX8984sc', 't-ZRX8984sc'),
        ('https://www.youtube.com/watch?v=iwGFalTRHDA&feature=related', 'iwGFalTRHDA'),
        ('https://www.youtube.com/watch?feature=player_embedded&v=2NpZbaAIXag', '2NpZbaAIXag'),
        ('https://www.youtube.com/watch?v=XPk521voaOE&feature=youtube_gdata_player', 'XPk521voaOE'),
        ('https://www.youtube.com/watch?v=6xu00J3-g2s&list=PLb5n6wzDlPakFKvJ69rJ9AJW24Aaaki2z', '6xu00J3-g2s'),
        ('https://m.youtube.com/#/watch?v=IAooXLAPoBQ', 'IAooXLAPoBQ'),
        ('https://m.youtube.com/watch?v=IAooXLAPoBQ', 'IAooXLAPoBQ'),
        ('https://www.youtube.com/edit?video_id=eBea01qmnOE', 'eBea01qmnOE')
    )

    instance = YoutubeBackend

    def test_youtube_keyerror(self):
        """ Test for issue #7 """
        backend = self.instance('http://youtube.com/watch?id=5')
        self.assertRaises(UnknownIdException, backend.get_code)

    def test_thumbnail(self):
        for url in self.urls:
            backend = self.instance(url[0])
            self.assertIn(url[1], backend.thumbnail)

    def test_get_better_resolution_youtube(self):
        backend = self.instance('https://www.youtube.com/watch?v=1Zo0-sWD7xE')
        self.assertIn(
            'img.youtube.com/vi/1Zo0-sWD7xE/maxresdefault.jpg',
            backend.thumbnail)
