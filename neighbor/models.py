from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.


class Neighborhood(models.Model):
    '''
    Class that has details of the neighborhood name, number of occupants and location
    '''
    hoodpic=models.ImageField(upload_to='images',blank=True)
    hoodname=models.CharField(max_length=30)
    numberofpeople=models.IntegerField(blank=True,default=0)
    hoodlocation=models.CharField(max_length=30)


    def __str__(self):
        return self.hoodname

    def savehood(self):
        '''
        Saving a neighborhood
        '''
        self.save()

    def deletehood(self):
        '''
        Deleting a neighborhood
        '''
        self.delete()

    @classmethod
    def get_hood(cls):
        '''
        Getting all neighborhoods
        '''
        hood=cls.objects.all()
        return hood

    @classmethod
    def hoodbyid(cls,hoodid):
        '''
        Getting a neighborhood by id
        '''
        hood=cls.objects.get(id=hoodid)
        return hood

    @classmethod
    def search_by_name(cls,name):
        '''
        Searching a neighborhood by name
        '''
        hood=cls.objects.filter(hoodname=name)
        return hood

class UserProfile(models.Model):
    '''
    Class for details of an individual occupant in a neighborhood
    '''
    profile_pic=models.ImageField(upload_to='images/',blank=True)
    editor=models.OneToOneField(User,on_delete=models.CASCADE)
    hood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    email=models.CharField(max_length=60)

    def __str__ (self):
        return self.email
    
    @classmethod
    def single_profile(cls,userid):
        '''
        Getting a single profile
        '''
        singleprof=cls.objects.filter(editor=userid)
        return singleprof


class Business(models.Model):
    '''
    Class for details of businesses in the neighborhood
    '''
    businesspic=models.ImageField(upload_to='images/',blank=True)
    businessname=models.CharField(max_length=30)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    area=models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    businessemail=models.CharField(max_length=30)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.businessname

    def savebusiness(self):
        '''
        Saving a business
        '''
        self.save()
    def deletebusiness(self):
        '''
        Deleting a business
        '''
        self.delete()

    @classmethod
    def get_businesses(cls):
        '''
        Getting all businesses
        '''
        biz=cls.objects.all()
        return biz

    @classmethod
    def bizbyowner(cls,userid):
        '''
        Shows businesses posted by a single user
        '''
        biz=cls.objects.filter(editor=userid)
        return biz

    @classmethod
    def single_business(cls,businessid):
        '''
        Shows details of a single business posted by id
        '''
        biz=cls.objects.filter(id=businessid)
        return biz
    @classmethod
    def search_by_business(cls,name):
        '''
        Getting a business by name
        '''
        biz=cls.objects.filter(businessname=name)
        return biz

class News(models.Model):
    '''
    Class that news posted by members of the neighborhood such as meetings and alerts
    '''
    newspic=models.ImageField(upload_to='images/',blank=True)
    title=models.CharField(max_length=30)
    description=HTMLField()
    newslocation=models.CharField(max_length=30)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)

    
    def __str__ (self):

        return self.title

    def savenews(self):
        '''
        Saving news
        '''
        self.save()

    def deletenews(self):
        '''
        Deleting news
        '''
        self.delete()

    @classmethod
    def get_news(cls):
        '''
        Getting all news
        '''
        news=cls.objects.all()
        return news

    @classmethod
    def single_news(cls,newsid):
        '''
        Retrieves details of a single alert posted by the user
        '''
        news=cls.objects.filter(id=newsid)
        return news

    @classmethod
    def newsbyuser(cls,userid):
        '''
        Retrieves news posted by every single user
        '''
        news=cls.objects.filter(editor=userid)
        return news





