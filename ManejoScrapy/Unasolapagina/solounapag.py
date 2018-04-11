#lo que se busca con esto es sacar informacion de una sola pagina 


from scrapy.item import Field #es un campo de los que guarda el elemento
from scrapy.item  import Item # es el elemento donde voy a guardar lo que quiero de la pagina
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


#problema de extraer informacion de StackOverflow: preguntas

#definir estructura de los item, que informacion vamos a alamancer
#definimos una clase que va ser un item que buscanmos en el el html


class Pregunta(Item):

    pregunta = Field()
    id = Field()


#implementacion del spiders

#para traer info de solo una pagina
class SpiderStackOverFlow(Spider):

    name = 'MiPrimerSpider'
    start_urls = ['https://stackoverflow.com/']

    #response es lo que recibimos en formato XML
    #
    def parse(self,response):

        #esta la invoca el framework, automaticamente
        #creamos selector
        sel = Selector(response)
        #preguntas = sel.xpath('//div[@class="question-summary narrow"]')
        preguntas = sel.xpath('//div[@id="question-mini-list"]/div/div')

        #iterar sobre todas las preguntas c
        for i, elem in enumerate(preguntas):
            item = ItemLoader(Pregunta(), elem)
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_value('id', i)
            yield item.load_item()

#scrapy runspider video2.py -o stakoverflow2.csv -t csv para ejecutar
