import requests
import lxml.html
import re
base_url = 'https://www.carbon38.com/'
search_url ='https://www.carbon38.com/shop-all-activewear/tops'
# url ="https://carbon38.com/collections/tops/products/cami-tank-in-cloud-compression"
data ={ }
count=2
class Carbon:
    def __init__(self,url):
        self.url =url
    def carbon_a(self):

        u = self.url
        ht = requests.get(u)
        doc = lxml.html.fromstring(ht.content)
        m = doc.xpath('//a[@class="isp_product_image_href"]/@href')
        a_string = "https://carbon38.com"
        my_new_url = [a_string + x for x in m]
        new_list = set(my_new_url)

        for url in new_list:
            data = {}
            # link_datas = requests.get("https://carbon38.com/collections/tops/products/cami-tank-in-cloud-compression")
            link_datas = requests.get(url)
            link = lxml.html.fromstring(link_datas.content)
            # data = {}
            # data['c'] += 1
            data["product_url"] = url
            data["bread_crumbs"] = link.xpath('//div[@class="breadcrumbs-list"] /text()')
            product_name = link.xpath("//h1/text()")
            name = ' '.join([str(elem) for elem in product_name])
            data['product_name'] = name
            description = link.xpath(
                '//div[@class="Faq__ItemWrapper"]/div/div/text() | //div[@class="Faq__ItemWrapper"]/div/div/span/text() |//div[@class="Faq__ItemWrapper"]/div/div/p/text()')
            desc = ' '.join([str(elem) for elem in description])
            data['description'] = desc.strip()
            brand = link.xpath('//h2[contains(@class,"ProductMeta__Vendor")]/a/text()')
            brands = ' '.join([str(elem) for elem in brand])
            data['brand'] = brands
            price = link.xpath('//div[@class="ProductMeta "]/div/span/ text()')[0]
            prize = re.findall("\d.+", price)
            prices = ' '.join([str(elem) for elem in prize])
            data['price'] = float(prices)
            reviews = link.xpath('//div[@class="okeReviews-reviewsSummary-ratingCount"]/text()')
            review_string = ' '.join([str(elem) for elem in reviews])
            review_no = re.findall("\d+", review_string)
            data['reviews'] = ' '.join([str(elem) for elem in review_no])
            color = link.xpath('//li[@class="HorizontalList__Item"]/label/span/text()')
            colour = ' '.join([str(elem) for elem in color])
            data['color'] = colour
            data['size'] = link.xpath('//ul[contains(@class,"SizeSwatchList")]/li/label/text()')
            image_url = link.xpath('//div[@class="AspectRatio AspectRatio--withFallback"]/noscript/img/@src')[0]
            data["image_url"] = "https:" + image_url
            print(data)
            # return data
            
obj3 =Carbon('https://www.carbon38.com/shop-all-activewear/tops')
kop3 = obj3.carbon_a()
print(kop3)
obj1 =Carbon('https://carbon38.com/collections/tops?page=1')
c1=obj1.carbon_a()
print(c1)
obj2 =Carbon('https://carbon38.com/collections/tops?page=2')
c2=obj2.carbon_a()
print(c2)
obj3 =Carbon('https://carbon38.com/collections/tops?page=3')
c3=obj3.carbon_a()
print(c3)

