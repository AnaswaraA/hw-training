
# for json output

import re
import requests
import lxml.html
import json

base_url = 'https://www.carbon38.com/'
search_url ='https://www.carbon38.com/shop-all-activewear/tops'
data = {
    'count': 0
}


def carbon_crawler(start_url):
    ht = requests.get(start_url)
    doc = lxml.html.fromstring(ht.content)
    m = doc.xpath('//a[@class="isp_product_image_href"]/@href')
    a_string = "https://carbon38.com"
    my_new_url = [a_string + x for x in m]
    new_list = set(my_new_url)

    for url in new_list:
        carbon(url=url)

    for i in range(2, 5):
        next_page = 'https://carbon38.com/collections/tops?page=' + str(i)
        a = str(next_page)
        next_page_url = requests.get(a)
        doc = lxml.html.fromstring(next_page_url.content)

        m = doc.xpath('//a[@class="isp_product_image_href"]/@href')
        a_string = "https://carbon38.com"
        my_new_url = [a_string + x for x in m]

        n = set(my_new_url)
        for url in n:
            carbon(url=url)


def carbon(url):
    link_datas = requests.get(url)
    link = lxml.html.fromstring(link_datas.content)
    # data ={ }
    data['count'] += 1
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
    data['price'] = prices
    reviews = link.xpath('//div[@class="okeReviews-reviewsSummary-ratingCount"]/text()')
    review_string = ' '.join([str(elem) for elem in reviews])
    review_no = re.findall("\d+", review_string)
    data['reviews'] = ' '.join([str(elem) for elem in review_no])
    color = link.xpath('//li[@class="HorizontalList__Item"]/label/span/text()')
    colour = ' '.join([str(elem) for elem in color])
    data['color'] = colour
    data['size'] = link.xpath('//ul[contains(@class,"SizeSwatchList")]/li/label/text()')
    image_url = link.xpath('//div[@class="AspectRatio AspectRatio--withFallback"]/img/@data-src')[0]
    data["image_url"] = "https:" + image_url

    with open("dataj.json", "a") as f:
        f.write(json.dumps(data) + ",\n")
    print(data)


carbon_crawler('https://www.carbon38.com/shop-all-activewear/tops')