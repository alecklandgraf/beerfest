from django.db import models
from autoslug import AutoSlugField


STATE_CHOICES = [(u'AK', u'AK'), (u'AL', u'AL'), (u'AR', u'AR'), (u'AZ', u'AZ'), (u'CA', u'CA'), (u'CO', u'CO'), (u'CT', u'CT'), ("DC", "Washington, D.C."), (u'DE', u'DE'), (u'FL', u'FL'), (u'GA', u'GA'), (u'HI', u'HI'), (u'IA', u'IA'), (u'ID', u'ID'), (u'IL', u'IL'), (u'IN', u'IN'), (u'KS', u'KS'), (u'KY', u'KY'), (u'LA', u'LA'), (u'MA', u'MA'), (u'MD', u'MD'), (u'ME', u'ME'), (u'MI', u'MI'), (u'MN', u'MN'), (u'MO', u'MO'), (u'MS', u'MS'), (u'MT', u'MT'), (u'NC', u'NC'), (u'ND', u'ND'), (u'NE', u'NE'), (u'NH', u'NH'), (u'NJ', u'NJ'), (u'NM', u'NM'), (u'NV', u'NV'), (u'NY', u'NY'), (u'OH', u'OH'), (u'OK', u'OK'), (u'OR', u'OR'), (u'PA', u'PA'), (u'RIL', u'RIL'), (u'SC', u'SC'), (u'SD', u'SD'), (u'TN', u'TN'), (u'TX', u'TX'), (u'UT', u'UT'), (u'VA', u'VA'), (u'VT', u'VT'), (u'WA', u'WA'), (u'WI', u'WI'), (u'WV', u'WV'), (u'WY', u'WY')]
REGION_CHOICES = [('West Coast', 'West Coast'), ('East Coast', 'East Coast'), ('Central', 'Central'), ]
# BEER_STYLE_CHOICES = [
#     ('American Pale Ale', 'American Pale Ale'),
#     ('American Pale Wheat Ale', 'American Pale Wheat Ale'),
#     ('American Style Hefeweizen', 'American Style Hefeweizen'),
#     ('American Style IPA', 'American Style IPA'),
#     ('American Wheat', 'American Wheat'),
#     ('American-Style IPA', 'American-Style IPA'),
#     ('Bamberg Style Helles Rauchbier Lager', 'Bamberg Style Helles Rauchbier Lager'),
#     ('Beermosa', 'Beermosa'),
#     ('Belgian IPA', 'Belgian IPA'),
#     ('Belgian Inspired Saison', 'Belgian Inspired Saison'),
#     ('Belgian Style Golden Ale', 'Belgian Style Golden Ale'),
#     ('Belgian Wit with Fruit', 'Belgian Wit with Fruit'),
#     ('Belgian-Style Blonde Ale', 'Belgian-Style Blonde Ale'),
#     ('Berliner Weiss', 'Berliner Weiss'),
#     ('Biere de Garde', 'Biere de Garde'),
#     ('Blonde Ale', 'Blonde Ale'),
#     ('Bohemian Pilsner', 'Bohemian Pilsner'),
#     ('Bohemian Style Pilsner', 'Bohemian Style Pilsner'),
#     ('Cascadian Dark Ale', 'Cascadian Dark Ale'),
#     ('Copper Ale', 'Copper Ale'),
#     ('Craft Malt Liquor', 'Craft Malt Liquor'),
#     ('Cream Ale', 'Cream Ale'),
#     ('Czech', 'Czech'),
#     ('Dortmunder', 'Dortmunder'),
#     ('Double Pale Ale', 'Double Pale Ale'),
#     ('English Style Brown', 'English Style Brown'),
#     ('Extra Pale Ale', 'Extra Pale Ale'),
#     ('Farmhouse Style Saison', 'Farmhouse Style Saison'),
#     ('Fruit Beer', 'Fruit Beer'),
#     ('Fruit Wheat Beer', 'Fruit Wheat Beer'),
#     ('German Radler', 'German Radler'),
#     ('German Style Wheat Beer', 'German Style Wheat Beer'),
#     ('Gluten Free IPA', 'Gluten Free IPA'),
#     ('Gluten Free NW Pale Ale', 'Gluten Free NW Pale Ale'),
#     ('Golden Ale', 'Golden Ale'),
#     ('Hefeweizen', 'Hefeweizen'),
#     ('IPA', 'IPA'),
#     ('Imperial Pacific Ale', 'Imperial Pacific Ale'),
#     ('Imperial Pilsner Lager', 'Imperial Pilsner Lager'),
#     ('Imperial Red Ale', 'Imperial Red Ale'),
#     ('Imperial Red IPA', 'Imperial Red IPA'),
#     ('India Pale Lager', 'India Pale Lager'),
#     ('Kolsch', 'Kolsch'),
#     ('Mixed Berry Belgian Lambic', 'Mixed Berry Belgian Lambic'),
#     ('NW Pale Ale', 'NW Pale Ale'),
#     ('Orange Infused Pale Ale', 'Orange Infused Pale Ale'),
#     ('Organic Belgian Pear Ale', 'Organic Belgian Pear Ale'),
#     ('Organic Herb/Spice Blonde Ale', 'Organic Herb/Spice Blonde Ale'),
#     ('Pale Ale', 'Pale Ale'),
#     ('Pale Lager', 'Pale Lager'),
#     ('Saison', 'Saison'),
#     ('Scottish Heather Ale', 'Scottish Heather Ale'),
#     ('Strawberry & Ginger Hefeweizen', 'Strawberry & Ginger Hefeweizen'),
#     ('Summer Cream Ale', 'Summer Cream Ale'),
#     ('Summer Lager', 'Summer Lager'),
#     ('Thai Lager', 'Thai Lager'),
#     ('Unfiltered Black Rye IPA', 'Unfiltered Black Rye IPA'),
#     ('West Coast IPA', 'West Coast IPA'),
#     ('Witbier', 'Witbier'),
# ]


class Brewery(models.Model):
    # required fields
    name = models.CharField(max_length=100)
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
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Beer(models.Model):
    # required fields
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    brewery = models.ForeignKey(Brewery)

    # non-required fields
    description = models.TextField(blank=True, null=True)
    style = models.ForeignKey(BeerStyle)
    ibu = models.IntegerField(blank=True, null=True, help_text='International Bitterness Units: from 0 to 100, some beer are higher')
    abv = models.FloatField(blank=True, null=True, help_text='Alchol by Volume, percentage from 0 to 100')
    vintage = models.DateTimeField(blank=True, null=True)
    og = models.FloatField(blank=True, null=True, help_text='Original Gravity')
    fg = models.FloatField(blank=True, null=True, help_text='Final Gravity')
    plato = models.FloatField(blank=True, null=True, help_text='Strength')
    degrees_lovibond = models.FloatField(blank=True, null=True, help_text='Color Scale')
    color = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        if self.abv and self.ibu:
            return u'%s - %s - %s - %s - %s' % (self.name, self.brewery, self.style, self.abv, self.ibu, )
        return u'%s - %s - %s' % (self.name, self.brewery, self.style, )
