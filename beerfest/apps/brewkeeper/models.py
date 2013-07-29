from django.db import models
from autoslug import AutoSlugField


STATE_CHOICES = [(u'AK', u'AK'), (u'AL', u'AL'), (u'AR', u'AR'), (u'AZ', u'AZ'), (u'CA', u'CA'), (u'CO', u'CO'), (u'CT', u'CT'), ("DC", "Washington, D.C."), (u'DE', u'DE'), (u'FL', u'FL'), (u'GA', u'GA'), (u'HI', u'HI'), (u'IA', u'IA'), (u'ID', u'ID'), (u'IL', u'IL'), (u'IN', u'IN'), (u'KS', u'KS'), (u'KY', u'KY'), (u'LA', u'LA'), (u'MA', u'MA'), (u'MD', u'MD'), (u'ME', u'ME'), (u'MI', u'MI'), (u'MN', u'MN'), (u'MO', u'MO'), (u'MS', u'MS'), (u'MT', u'MT'), (u'NC', u'NC'), (u'ND', u'ND'), (u'NE', u'NE'), (u'NH', u'NH'), (u'NJ', u'NJ'), (u'NM', u'NM'), (u'NV', u'NV'), (u'NY', u'NY'), (u'OH', u'OH'), (u'OK', u'OK'), (u'OR', u'OR'), (u'PA', u'PA'), (u'RIL', u'RIL'), (u'SC', u'SC'), (u'SD', u'SD'), (u'TN', u'TN'), (u'TX', u'TX'), (u'UT', u'UT'), (u'VA', u'VA'), (u'VT', u'VT'), (u'WA', u'WA'), (u'WI', u'WI'), (u'WV', u'WV'), (u'WY', u'WY')]
REGION_CHOICES = [('West Coast', 'West Coast'), ('East Coast', 'East Coast'), ('Central', 'Central'), ]
BEER_RATING_CHOICES = [('A+', 'A+'), ('A', 'A'), ('A-', 'A'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('F', 'F'), ]


class Brewery(models.Model):
    # required fields
    name = models.CharField(db_index=True, max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    description = models.TextField(blank=True, null=True)

    # non-required fields
    country = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, choices=REGION_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True, null=True)
    zip_code = models.CharField(max_length=40, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class BeerStyle(models.Model):
    name = models.CharField(db_index=True, max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    genre = models.CharField(max_length=100, unique=True)
    ale = models.NullBooleanField(blank=True, null=True, default=False)
    lager = models.NullBooleanField(blank=True, null=True, default=False)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Beer(models.Model):
    # required fields
    name = models.CharField(db_index=True, max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    brewery = models.ForeignKey(Brewery)

    # non-required fields
    description = models.TextField(blank=True, null=True)
    style = models.ForeignKey(BeerStyle)
    ibu = models.IntegerField(db_index=True, blank=True, null=True, help_text='International Bitterness Units: from 0 to 100, some beer are higher')
    abv = models.FloatField(db_index=True, blank=True, null=True, help_text='Alchol by Volume, percentage from 0 to 100')
    vintage = models.DateTimeField(blank=True, null=True)
    og = models.FloatField(blank=True, null=True, help_text='Original Gravity')
    fg = models.FloatField(blank=True, null=True, help_text='Final Gravity')
    plato = models.FloatField(blank=True, null=True, help_text='Strength')
    degrees_lovibond = models.FloatField(blank=True, null=True, help_text='Color Scale')
    color = models.CharField(max_length=30, blank=True, null=True)
    rating = models.CharField(max_length=2, blank=True, null=True, help_text='F to A+', choices=BEER_RATING_CHOICES)

    # beer_advocate ratings: look, smell, taste, feel, overall

    @property
    def ale(self):
        return self.style.ale

    @property
    def lager(self):
        return self.style.lager

    @property
    def ale_or_lager(self):
        if self.ale:
            return 'ale'
        if self.lager:
            return 'lager'
        return 'unknown'

    def __unicode__(self):
        if self.abv and self.ibu:
            return u'%s - %s - %s - %s - %s' % (self.name, self.brewery, self.style, self.abv, self.ibu, )
        return u'%s - %s - %s' % (self.name, self.brewery, self.style, )
