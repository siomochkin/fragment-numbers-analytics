import unittest
from sold.main import *

class TestMain(unittest.TestCase):
    def test_get_data_between_markers(self):
        data = 'This is <start>important</start> data'
        self.assertEqual(get_data_between_markers(data, '<start>', '</start>'), "important")
        self.assertIsNone(get_data_between_markers(data, "<start>", "<end>"))
    
    def test_get_parsed_data(self):
        valid_html = "https://example.com"
        parsed_data = get_parsed_data(valid_html)
        self.assertIsInstance(parsed_data, BeautifulSoup)
        
    def test_get_phone_number(self):
        # If number exist
        html_with_phone = "<div class='tm-value'>123-456-7890</div>"
        soup = BeautifulSoup(html_with_phone, 'html.parser')
        phone_number = get_phone_number(soup)
        self.assertEqual(phone_number, "123-456-7890")
        
    def test_get_number_status(self):
        html_with_number_status = '<div class="tm-status">Status</div>'
        soup = BeautifulSoup(html_with_number_status, 'html.parser')
        status_number = get_number_status(soup)
        self.assertEqual(status_number, "Status")
        
    def test_get_price_in_ton(self):
        html = '<div class="icon-ton">243</div>'
        soup = BeautifulSoup(html, 'html.parser')
        ton = get_price_in_ton(soup)
        self.assertEqual(ton, '243')
        
    def test_get_sold_time(self):
        html = '<time datetime="2023-08-28T12:43:01+00:00">28 Aug 2023 at 12:43</time>'
        soup = BeautifulSoup(html, 'html.parser')
        data = get_sold_time(soup)
        self.assertEqual(data, '28 Aug 2023 12:43')
        
    def test_get_remaining_time(self):
        html = '<div class="tm-timer"><time datetime="2023-09-04T13:02:50+00:00" data-relative="text">3 days 0 hours 57 minutes</time> left</div>'
        soup = BeautifulSoup(html, 'html.parser')
        data = get_remaining_time(soup)
        self.assertEqual(data, "3:0:57")
        
    def test_convert_to_datetime_and_format(self):
        input_date = "01 Jan 2023 15:30"
        expected_output = "2023-01-01 15:30"
        self.assertEqual(convert_to_datetime_and_format(input_date), expected_output)
