from scrapy.item import Item, Field


class Website(Item):

    feature = Field()
    description = Field()
    tripID = Field()
    #url = Field()

    #trip_stats = Field()
    #trip_meta_data = Field()
    #elec_stats = Field()
    #def keys(self):
    #    return ['feature', 'description']
