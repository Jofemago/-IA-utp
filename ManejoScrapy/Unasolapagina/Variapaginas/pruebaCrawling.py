

from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


class AirbnbITem(Item):

    tipo = Field()
    capacidad = Field()



#defino el spiders
class AirbnbCrawler(CrawlSpider):
    #para poder hacer crawling vertical y horizontal
    name = 'MiPrimerCrawler'
    start_urls = ['https://www.airbnb.com/s/Londres--Reino-Unido/']

    allowed_domains = ['airbnb.com']#donde se puede desplazar el bot
    #diferencia entre spider y este
    #me sirven para el crawlomg vertical y horizontal
    rules =(
        #reglas para visitar la pagina de la paginacion
        #LinkExtractor me permite extraer todas las paginas que exitan con la condicion allow
        #parametro follow = True para que lo siga
        Rule(LinkExtractor(allow = r'section_offset=')), #Horizontal,sel puede acceder a las paginas que tienen esa expresion regular en su URL
        Rule(LinkExtractor(allow = r'/rooms/(.)*'), callback = 'parse_items') #verticalmente va entrar a paginas que contienen esta expresion regular
    )

    def parse_items(self, response):

        item = ItemLoader(AirbnbITem(), response)
        item.add_xpath('tipo', '//*[@id="summary"]/div/div[1]/a/div/span/span/span/text()')
        item.add_xpath('capacidad','//*[@id="room"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/span/text()',MapCompose(lambda i : i[0]))
        #el map compose me sirve para organizar los datos que se ingresan y cuales me sirven
        yield item.load_item()


#ahora llenar los items, solo se llenan en crawling vertical



#para ejecutar
#scrapy runspider pruebaCrawling.oy -o bnb.csv -t csv --set CLOSESPIDER_ITENCOUNT=30
