import unittest
from six import text_type, u, b, PY2, PY3
from nose.tools import raises
from expects import *

from opentok import OpenTok, __version__


class GetterSetterTest(unittest.TestCase):
    def setUp(self):
        self.api_key = u("123456")
        self.api_secret = u("1234567890abcdef1234567890abcdef1234567890")
        self.session_id = u(
            "1_MX4xMjM0NTZ-flNhdCBNYXIgMTUgMTQ6NDI6MjMgUERUIDIwMTR-MC40OTAxMzAyNX4"
        )
        self.opentok = OpenTok(self.api_key, self.api_secret)

    def test_getset_appname_appversion(self):
        self.opentok.app_name = "Vonage-Video-App"
        self.opentok.app_version = "1.0.0"
        expect(self.opentok.headers()["User-Agent"]).to(
            contain(u("Vonage-Video-App/1.0.0"))
        )