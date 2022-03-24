import lxml.html
import lxml
import requests

def CarbonCrawler(url):
# html= requests.get("https://carbon38.com/products/crop-tank-2-0?variant=40293599805629")
#     html = requests.get("https://www.carbon38.com/shop-all-activewear/tops")
    ht = requests.get(url)
    doc = lxml.html.fromstring(ht.content)
    m= doc.xpath('//a[@class="isp_product_image_href"]/@href')

    for links in m:
        link = requests.get('https://www.carbon38.com/' + links)
        link_datas = lxml.html.fromstring(link.content)
        brand_name = link_datas.xpath("//h1/text()")
        prize = link_datas.xpath('//div[@class="ProductMeta__PriceList Heading"]/span[@ class ="ProductMeta__Price Price Price--highlight Text--subdued"] / text()')
        brand= link_datas.xpath('//h2[@class="ProductMeta__Vendor Heading u-h1"]/a/text()')
        reviews = link_datas.xpath('//div[@class="okeReviews-reviewsSummary-ratingCount"]/text()')
        color = doc.xpath('//ul[@class="ColorSwatchList HorizontalList HorizontalList--spacingTight"]/li[@class="HorizontalList__Item"]/label/span/text()')
        size = doc.xpath('//div[@class="ProductForm__Option ProductForm__Option--labelled"]/fieldset[@class="ProductForm__Fieldset"]/ul[@class="SizeSwatchList HorizontalList HorizontalList--spacingTight"]/li/label/text()')
        print(brand,brand_name,prize,reviews,color,size)
#
carbon=CarbonCrawler("https://www.carbon38.com/shop-all-activewear/tops")
print(carbon)
