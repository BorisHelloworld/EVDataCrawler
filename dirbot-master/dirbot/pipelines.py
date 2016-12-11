from scrapy.exceptions import DropItem
from collections import defaultdict

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""
    #pass
    
    # KEEP the items with the following key works; and filt out the others.
    words_to_filter = ['Temperature', 'Passenger','Cargo','Tire','Frontal']

    """
    This function has already been called every time an item is scraped...
    """
    def process_item(self, item, spider):
    # This function has already been called every time an item is scraped...
    # The following 3 lines could prove this...
    #    print "\n\n\n......\nThis is the feature list..."
    #    print item['feature']
    #    return item
    
        # print "Just Got Feature:        "
        # print item['feature']

        for word in self.words_to_filter:
            if word in unicode(item['feature']):
                print "Got One!!!!!!!!!!!!!!!!!!!!!!!"
                return item
            else:          
                continue    
        raise DropItem("Contains NO keywords...")
       

