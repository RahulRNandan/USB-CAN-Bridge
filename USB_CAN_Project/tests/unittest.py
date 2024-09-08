import unittest
from unittest.mock import patch
import io

class TestUSBEmulation(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_usb_data_output(self, mock_stdout):
        # Run the USB simulator and check if it prints the expected data
        with patch('usb_simulator.simulate_usb_data', return_value=None):
            usb_simulator.simulate_usb_data()
        output = mock_stdout.getvalue()
        self.assertIn('USB Data:', output)

if __name__ == '__main__':
    unittest.main()
