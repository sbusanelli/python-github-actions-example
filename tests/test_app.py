
import sys
import unittest
from common import us_state_mapping
import requests

class TestAppMethods(unittest.TestCase):
  def test_index(self):
    self.assertEqual('foo'.upper(), 'FOO')
  def test_us_location(self):
    r = requests.get('https://ipinfo.io')
    rd = r.json()
    state = rd.get('region')
    tlc = us_state_mapping.us_state_to_tlc[state]
    self.assertEqual(state , us_state_mapping.tlc_to_us_state[tlc])
  
if __name__ == '__main__':
    unittest.main()
