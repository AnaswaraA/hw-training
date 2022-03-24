import requests
import lxml.html
import json

base_url = 'https://www.carbon38.com/'
search_url ='https://www.carbon38.com/shop-all-activewear/tops'
data = {
'brand_name': [],
    'brand': [],
    'prize': [],
    'reviews': [],
    'color': [],
    'size': [],
    'product_url':[],


}
def CarbonCrawler(start_url):
    ht = requests.get(start_url)
    doc = lxml.html.fromstring(ht.content)
    m = doc.xpath('//a[@class="isp_product_image_href"]/@href')
    a =[]
    for i in range(0,100):
        a.append("https://carbon38.com" + m[i])
    for url in a:
        Carbon(url=url)


def Carbon(url):
    link_datas = requests.get(url)
    link = lxml.html.fromstring(link_datas.content)
    data["product_url"] = url
    data['brand_name'] = link.xpath("//h1/text()")
    data['brand'] = link.xpath('//h2[@class="ProductMeta__Vendor Heading u-h1"]/a/text()')
    data['prize'] = link.xpath('//div[@class="ProductMeta "]/div/span/ text()')
    data['reviews'] = link.xpath('//div[@class="okeReviews-reviewsSummary-ratingCount"]/text()')
    data['color'] = link.xpath('//ul[@class="ColorSwatchList HorizontalList HorizontalList--spacingTight"]/li[@class="HorizontalList__Item"]/label/span/text()')
    data['size'] = link.xpath('//div[@class="ProductForm__Option ProductForm__Option--labelled"]/fieldset[@class="ProductForm__Fieldset"]/ul[@class="SizeSwatchList HorizontalList HorizontalList--spacingTight"]/li/label/text()')
    with open("carbon.json", "a") as f:
        f.write(json.dumps(data, indent=2))
    print(data)
CarbonCrawler('https://www.carbon38.com/shop-all-activewear/tops')