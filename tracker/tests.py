from django.test import TestCase
from tracker.models import Homicide, Article 

# models test
class HomicideTest(TestCase):

    def create_article(self, url='http://foo.com', headline='this is the headline', content='this is the content'):
        return Article.objects.create(url=url, headline=headline, content=content)

    def test_article_creation(self):
        w = self.create_article()
        self.assertTrue(isinstance(w, Article))

    def test_homicide_creation(self):
        w = self.create_article()
        self.assertTrue(isinstance(w, Article))
