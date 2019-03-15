from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose
from w3lib.html import  remove_tags


class CstcLoader(ItemLoader):
    default_output_processor = TakeFirst()


class CqkjjLoader(CstcLoader):
    content_out = MapCompose(remove_tags, lambda s: s.strip())
    source_out = MapCompose(Join(),lambda s: s.strip())
