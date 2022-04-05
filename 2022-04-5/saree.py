import datetime
import requests
import lxml.html
import json
import csv
field =['count','product_code','product_name','image_url']
pro =[]
data ={'count':0}
with open('sareec.csv', 'a') as f:
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
def saree_page(start_url):
    ht = requests.get(start_url)
    doc = lxml.html.fromstring(ht.content)
    m = doc.xpath('//li[@class="item product product-item"]/div/div/a/@href')

    for url in m:
        saree(url=url)


def saree(url):
    ht = requests.get(url)
    doc = lxml.html.fromstring(ht.content)
    scraped_date = datetime.datetime.now()
    data['count'] +=1
    code=doc.xpath('//div[@class ="product attribute sku"]/div/text()')
    product_code= ' '.join([str(elem) for elem in code])
    data["product_code"]=product_code
    product_name= doc.xpath('//h1[@class ="page-title"]/span/text()')
    name = ' '.join([str(elem) for elem in product_name])
    data["product_name"] = name
    image=doc.xpath('//img[@class="no-sirv-lazy-load"]/@src')
    image_url= ' '.join([str(elem) for elem in image])
    data["image_url"]=image_url
    if data['count'] <11:
        with open("sareej.json", "a") as f:
            f.write(json.dumps(data) + ",\n")
        print(data)

        temp_data = [data]
        with open('sareec.csv','a') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writerows(temp_data)




saree_page('https://www.saree.com/saree')
