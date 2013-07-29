from django.db import models
from autoslug import AutoSlugField


STATE_CHOICES = [(u'AK', u'AK'), (u'AL', u'AL'), (u'AR', u'AR'), (u'AZ', u'AZ'), (u'CA', u'CA'), (u'CO', u'CO'), (u'CT', u'CT'), ("DC", "Washington, D.C."), (u'DE', u'DE'), (u'FL', u'FL'), (u'GA', u'GA'), (u'HI', u'HI'), (u'IA', u'IA'), (u'ID', u'ID'), (u'IL', u'IL'), (u'IN', u'IN'), (u'KS', u'KS'), (u'KY', u'KY'), (u'LA', u'LA'), (u'MA', u'MA'), (u'MD', u'MD'), (u'ME', u'ME'), (u'MI', u'MI'), (u'MN', u'MN'), (u'MO', u'MO'), (u'MS', u'MS'), (u'MT', u'MT'), (u'NC', u'NC'), (u'ND', u'ND'), (u'NE', u'NE'), (u'NH', u'NH'), (u'NJ', u'NJ'), (u'NM', u'NM'), (u'NV', u'NV'), (u'NY', u'NY'), (u'OH', u'OH'), (u'OK', u'OK'), (u'OR', u'OR'), (u'PA', u'PA'), (u'RIL', u'RIL'), (u'SC', u'SC'), (u'SD', u'SD'), (u'TN', u'TN'), (u'TX', u'TX'), (u'UT', u'UT'), (u'VA', u'VA'), (u'VT', u'VT'), (u'WA', u'WA'), (u'WI', u'WI'), (u'WV', u'WV'), (u'WY', u'WY')]


class Brewery(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True, null=True)
    zip_code = models.CharField(max_length=40, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Beer(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    brewery = models.ForeignKey(Brewery)
    description = models.TextField(blank=True, null=True)
    ibu = models.IntegerField(blank=True, null=True, help_text='International Bitterness Units: from 0 to 100, some beer are higher')
    abv = models.FloatField(blank=True, null=True, help_text='Alchol by Volume, percentage from 0 to 100')
