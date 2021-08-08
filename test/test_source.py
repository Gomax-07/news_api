import unittest 
from app.models import NewsSource

class SourceTest(unittest.TestCase):
    """test class test the behaviourof the source class
    """
    def setUp(self):
        """setUP method that will run before every test
        """
        self.news_source = NewsSource('cnn','CNN.','View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN','https://www.nytimes.com/2018/08/31/sports/tennis/us-open-results.html')

    def test_instance(self):
        """test to check creation of new article source instance
        """
        self.assertTrue(isinstance(self.news_source, NewsSource))   