from django.db import models
import datetime

class Entry(models.Model):
    """
    Receives data sent from wufoo.com and stores calculated scores
    """
    created = models.DateTimeField(default=datetime.datetime.now())
    grade = models.IntegerField()
    data = models.TextField()
    location = models.TextField()
    auditName = models.TextField()
    
    def get_absolute_url(self):
        return reverse('entry-view', kwargs={'pk': self.id})
        
    def __unicode__(self):
        return self.auditName
    
    class Meta:
        unique_together = ('created', 'location', 'auditName',)
    

class Item(models.Model):
""" 
    Represents the survey responses
"""	
    entry = models.ForeignKey('Entry', null=True)
    question = models.TextField()
    response = models.TextField()
    failed = models.IntegerField()
    
    def __unicode__(self):
        return '-'.join([
            self.id,
            self.question
        ])
        
        
    

    
    
	

	



