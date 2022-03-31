import requests
import lxml.html
import json
#
# base_url = 'https://www.carbon38.com/'
# search_url = 'https://www.carbon38.com/shop-all-activewear/tops'
# data = {
#     'brand_name': [],
#     'brand': [],
#     'prize': [],
#     'reviews': [],
#     'color': [],
#     'size': [],
#
# }
#
#
# def Carbon_url(data):
#     ht = requests.get(search_url)
#     doc = lxml.html.fromstring(ht.content)
#     m = doc.xpath('//a[@class="isp_product_image_href"]/@href')
#
#
#
#     for url in m:
#         Carbon(url=url)
#         with open("carbon1.json", "a") as f:
#             f.write(json.dumps(data, indent=2))
#
#
# def Carbon(url):
#     link_datas = requests.get(search_url)
#     link = lxml.html.fromstring(link_datas.content)
#     linkk = requests.get(url)
#     linkkk = lxml.html.fromstring(linkk.content)
#     # brand_name = link.xpath("//h1/text()")
#     # prize = link.xpath(
#     #     '//div[@class="ProductMeta__PriceList Heading"]/span[@ class ="ProductMeta__Price Price Price--highlight Text--subdued"] / text()')
#     # brand = link.xpath('//h2[@class="ProductMeta__Vendor Heading u-h1"]/a/text()')
#     # reviews = link.xpath('//div[@class="okeReviews-reviewsSummary-ratingCount"]/text()')
#     # color = link.xpath('//ul[@class="ColorSwatchList HorizontalList HorizontalList--spacingTight"]/li[@class="HorizontalList__Item"]/label/span/text()')
#     # size = link.xpath('//div[@class="ProductForm__Option ProductForm__Option--labelled"]/fieldset[@class="ProductForm__Fieldset"]/ul[@class="SizeSwatchList HorizontalList HorizontalList--spacingTight"]/li/label/text()')
#     data['brand_name'] = linkkk.xpath("//h1/text()")
#     # data['brand'] = link.xpath('//h2[@class="ProductMeta__Vendor Heading u-h1"]/a/text()')
#     # data['prize'] = link.xpath(
#     #     '//div[@class="ProductMeta__PriceList Heading"]/span[@ class ="ProductMeta__Price Price Price--highlight Text--subdued"] / text()')
#     # data['reviews'] = link.xpath('//div[@class="okeReviews-reviewsSummary-ratingCount"]/text()')
#     # data['color'] = link.xpath(
#     #     '//ul[@class="ColorSwatchList HorizontalList HorizontalList--spacingTight"]/li[@class="HorizontalList__Item"]/label/span/text()')
#     # data['size'] = link.xpath('//div[@class="ProductForm__Option ProductForm__Option--labelled"]/fieldset[@class="ProductForm__Fieldset"]/ul[@class="SizeSwatchList HorizontalList HorizontalList--spacingTight"]/li/label/text()')
#     print("brand_name", data['brand_name'])
#     # print("brand", data['brand'])
#     # print("prize", data['prize'])
#     # print("reviews", data['reviews'])
#     # print("color", data['color'])
#     # print("size", data['size'])
#
#
# def Carbon_next(search_url):
#     ht = requests.get(search_url)
#     doc = lxml.html.fromstring(ht.content)
#     m = doc.xpath('//a[@class="isp_product_image_href"]/@href')
#     if ht.status_code == requests.codes.ok:
#         ht = requests.get(search_url)
#         doc = lxml.html.fromstring(ht.content)
#         m = doc.xpath('//a[@class="isp_product_image_href"]/@href')
#
#
#         # links = requests.get(search_url)
#         # link_datas = lxml.html.fromstring(links.content)
#
#         for links in m:
#             link = requests.get('https://www.carbon38.com/' + links)
#             Carbon(link)
#
#
# Carbon_url(data)
#
# Carbon_next(search_url)





import requests
import lxml.html
import json
import csv
import pandas as pd
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


    # with open("datac.json", "a") as f:
    #     f.write(json.dumps(data )+",\n")
    #
    #

    print(data)
    pro.append(data)
    with open('csv_file.csv','w',encoding = 'utf-8',newline='') as f:
        writer= csv.DictWriter(f,fieldnames=field)
        writer.writeheader()
        writer.writerows(pro)

carbon_crawler('https://www.carbon38.com/shop-all-activewear/tops')
