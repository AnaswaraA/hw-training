# for csv output

import requests
import lxml.html

import csv

base_url = 'https://www.carbon38.com/'
search_url ='https://www.carbon38.com/shop-all-activewear/tops'

field =['product_url','bread_crumbs','product_name','description','brand','prize','reviews','color','size','image_url']
pro =[]
def carbon_crawler(start_url):
    ht = requests.get(start_url)
    doc = lxml.html.fromstring(ht.content)
    m = doc.xpath('//a[@class="isp_product_image_href"]/@href')
    a_string = "https://carbon38.com"
    my_new_url = [a_string + x for x in m]
    new_list=set(my_new_url)

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
    data ={ }
    # data['c'] += 1
    data["product_url"] = url
    data["bread_crumbs"] =link.xpath('//div[@class="breadcrumbs-list"] /text()')
    product_name = link.xpath("//h1/text()")
    name = ' '.join([str(elem) for elem in product_name])
    data['product_name'] = name
    description =link.xpath('//div[@class="Faq__ItemWrapper"]/div/div/text() | //div[@class="Faq__ItemWrapper"]/div/div/span/text() |//div[@class="Faq__ItemWrapper"]/div/div/p/text()')
    desc = ' '.join([str(elem) for elem in description])
    data['description'] = desc.strip()
    brand = link.xpath('//h2[contains(@class,"ProductMeta__Vendor")]/a/text()')
    brands = ' '.join([str(elem) for elem in brand])
    data['brand']=brands
    prize = link.xpath('//div[@class="ProductMeta "]/div/span/ text()')
    price = ' '.join([str(elem) for elem in prize])
    data['prize'] = price
    reviews = link.xpath('//div[@class="okeReviews-reviewsSummary-ratingCount"]/text()')
    review = ' '.join([str(elem) for elem in reviews])
    data['reviews'] = review
    color= link.xpath('//li[@class="HorizontalList__Item"]/label/span/text()')
    colour =' '.join([str(elem) for elem in color])
    data['color'] =colour
    data['size'] = link.xpath('//ul[contains(@class,"SizeSwatchList")]/li/label/text()')
    image_url = link.xpath('//div[@class="AspectRatio AspectRatio--withFallback"]/img/@data-src')[0]
    data["image_url"] = "https:"+ image_url


    print(data)
    pro.append(data)
    with open('csv_file.csv','w',encoding = 'utf-8',newline='') as f:
        writer= csv.DictWriter(f,fieldnames=field)
        writer.writeheader()
        writer.writerows(pro)

carbon_crawler('https://www.carbon38.com/shop-all-activewear/tops')
