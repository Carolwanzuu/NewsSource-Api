import unittest
from flask import current_app
from app import create_app

class SourceTest(unittest.TestCase):
    '''
    test class to test the behavior of the source class
    '''
    def setUp(self):
        self.new_source = Source('reuters','U.S. Republicans vow to oppose Yellen G7 tax deal, casting doubt on its future - Reuters', 'Desperation should drive funding for Alzheimer research, it should not drive the interpretation of scientific evidence, Karlawish said.','https://www.reuters.com/world/us/us-republicans-vow-oppose-yellens-g7-tax-deal-casting-doubt-its-future-2021-06-08/', 'business', 'US' )
  
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_initialization(self):
        self.assertEqual(self.new_source.id, 'reuters')
        self.assertEqual(self.new_source.title, 'U.S. Republicans vow to oppose Yellen G7 tax deal, casting doubt on its future - Reuters')
        self.assertEqual(self.new_source.description, 'Desperation should drive funding for Alzheimer research, it should not drive the interpretation of scientific evidence, Karlawish said.')
        self.assertEqual(self.new_source.category, 'business')
        self.assertEqual(self.new_source.url, 'https://www.reuters.com/world/us/us-republicans-vow-oppose-yellens-g7-tax-deal-casting-doubt-its-future-2021-06-08/')

class ArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Article('http://www.abc.net.au/news/2021-06-07/vic-covid-lockdown-optimism-next-steps/100194304', 'ABC News' ,'Victorian health officials running "neck-and-neck" with COVID-19 outbreak',"As the end of Victoria's extended lockdown looms, health officials are assessing the next steps in the state's COVID-19 outbreak, which has grown to 70 active cases.", 'https://live-production.wcms.abc-cdn.net.au/11b9c49c382e18ffce7d88caa1cf805f?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=13&width=862&height=485', '2021-06-06T14:27:59Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


    def test_initialization(self):
        self.assertEqual(self.new_article.url, 'http://www.abc.net.au/news/2021-06-07/vic-covid-lockdown-optimism-next-steps/100194304')
        self.assertEqual(self.new_article.author, 'ABC News')
        self.assertEqual(self.new_article.title, 'Victorian health officials running "neck-and-neck" with COVID-19 outbreak')
        self.assertEqual(self.new_article.description, "As the end of Victoria's extended lockdown looms, health officials are assessing the next steps in the state's COVID-19 outbreak, which has grown to 70 active cases.")
        self.assertEqual(self.new_article.urlimg, 'https://live-production.wcms.abc-cdn.net.au/11b9c49c382e18ffce7d88caa1cf805f?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=13&width=862&height=485')
        self.assertEqual(self.new_article.published, '2021-06-06T14:27:59Z')


if __name__ == '__main__':
  unittest.main()