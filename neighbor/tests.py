from django.test import TestCase
from .models import Neighborhood,Business,News,UserProfile
from django.contrib.auth.models import User
# Create your tests here.

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        '''
        creating a foreign key instance
        '''

        self.newhood=Neighborhood(hoodpic='pic.jpg',hoodname='Kpop',numberofpeople='134',hoodlocation='13thstreet')

    def test_instance(self):
        '''
        Testing the self instance
        '''
        self.assertTrue(isinstance(self.newhood,Neighborhood))

    def test_save_hood(self):
        '''
        Testing save neighborhood function
        '''
        self.newhood.savehood()
        hoods=Neighborhood.objects.all()
        self.assertTrue(len(hoods)>0)

    def test_delete_hood(self):
        '''
        Testing delete neighborhood function
        '''
        self.newhood.savehood()
        self.newhood.deletehood()
        hoods=Neighborhood.objects.all()
        self.assertTrue(len(hoods)==0)

    def test_get_hood(self):
        '''
        Testing neighborhood retrieval
        '''
        self.newhood.savehood()
        firsthood=Neighborhood.get_hood()
        self.assertTrue(firsthood is not None)

class BusinessTestClass(TestCase):

    def setUp(self):
        '''
        creating a user foreign key instance
        '''
        self.newuser=User(username='pinto') 
        '''
        saving the foreign key instance
        '''
        self.newuser.save()

        '''
        creating a neighborhood foreign key instance
        '''

        self.hood=Neighborhood(hoodpic='pic.jpg',hoodname='Kpop',numberofpeople='134',hoodlocation='13thstreet')
        '''
        saving the foreign key instance
        '''
        self.hood.save()

        '''
        creating the Business class instance and including foreign key references
        '''

        self.biz=Business(businessname='spaceship',businesspic='img.jpg',businessemail='what@gmail',editor=self.newuser,area=self.hood)

    def test_instance(self):
        '''
        Testing the Business instance
        '''
        self.assertTrue(isinstance(self.biz,Business))

    def test_save_business(self):
        '''
        Testing the save business function
        '''
        self.biz.savebusiness()
        allbiz=Business.objects.all()
        self.assertTrue(len(allbiz)>0)

    def test_delete_business(self):
        '''
        Testing the delete business function
        '''
        self.biz.savebusiness()
        self.biz.deletebusiness()
        allbiz=Business.objects.all()
        self.assertTrue(len(allbiz)==0)

    def test_get_businesses(self):
        '''
        Testing business retrieval
        '''
        self.biz.savebusiness()
        firstbiz=Business.get_businesses()
        self.assertTrue(firstbiz is not None)



class NewsTestClass(TestCase):

    def setUp(self):
        '''
        creating a user foreign key instance
        '''
        self.newuser=User(username='pinto') 
        '''
        saving the foreign key instance
        '''
        self.newuser.save()

        '''
        creating the News class instance and including foreign key references
        '''

        self.news=News(title='study',newspic='img.jpg',description='scholarships',editor=self.newuser,newslocation='nairobi')

    def test_instance(self):
        '''
        Testing the news instance
        '''
        self.assertTrue(isinstance(self.news,News))

    def test_save_news(self):
        '''
        Testing the save news function
        '''
        self.news.savenews()
        allnews=News.objects.all()
        self.assertTrue(len(allnews)>0)

    def test_delete_news(self):
        '''
        Testing the delete news function
        '''
        self.news.savenews()
        self.news.deletenews()
        allnews=News.objects.all()
        self.assertTrue(len(allnews)==0)

    def test_get_news(self):
        '''
        Testing news retrieval
        '''
        self.news.savenews()
        firstnews=News.get_news()
        self.assertTrue(firstnews is not None)