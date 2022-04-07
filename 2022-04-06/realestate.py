import datetime
import requests
import lxml.html
import csv


data ={"count":0}
field=['count','datatime','firstname','middlename','lastname','office_name','title','description','languages','image_url','agent_phone_numbers','office_phone_numbers','email','website','address','city','state','zipcode','profile_url']
start_url="https://www.harrynorman.com/agents"
headers ={"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "accept-encoding":"gzip, deflate, br",
          "accept-language":"en-GB,en-US;q=0.9,en;q=0.8",
          "upgrade-insecure-requests":"1",
         "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTM L, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
with open('realestate.csv', 'a') as f:
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()

def realestate(url):
    ht = requests.get(url, headers=headers)
    doc = lxml.html.fromstring(ht.content)
    m = doc.xpath('//a[@class="agent-link"]/@href')
    a_string = "https://www.harrynorman.com/"
    my_new_url = [a_string + x for x in m]



    for url in my_new_url:
        agents(url=url)

def agents(url):
    r = requests.get(url, headers=headers)
    doc = lxml.html.fromstring(r.content)
    now=datetime.datetime.now()
    data["datatime"]= now.strftime("%d/%m/%Y %H:%M:%S")
    data["count"]+=1
    fname = doc.xpath('//div[@class="col-sm-10 text-center agent-information"]/h1[@class="body-title"]/text()')
    name = ' '.join([str(elem) for elem in fname])
    parts = name.split()
    if len(parts) == 3:
        first, middle, last = parts
        le = ([first, middle, last])
    else:
        first = parts[0]
        middle = ""
        last = parts[-1]
        le = ([first, middle, last])
    data["firstname"] =le[0]
    data["middlename"] = le[1]
    data["lastname"] =le[-1]
    office_name = doc.xpath('//div[@class="col-sm-10 text-center agent-information"]/span/text()')
    ostring = ' '.join([str(elem) for elem in office_name])
    osplit = ostring.split()
    if len(osplit)>1:
        d = osplit[0] + " " + osplit[1]
        data["office_name"] = d
    else:

        data["office_name"]=' '.join([str(elem) for elem in osplit])
    title = doc.xpath('//div[@class="col-sm-10 text-center agent-information"]/div/h3/text()')
    if title==[]:
        data["title"] =" "
    else:
        s_title = ' '.join([str(elem) for elem in title])
        cl_title=(s_title.translate({ord(i): None for i in '\xae'}))
        data["title"]=cl_title
    des = doc.xpath('//div[@class="col-sm-24"]/p/span/text()')
    if des == []:
        data["description"]=""
    else:
        data["description"]=des
    languages = doc.xpath('//div[@class="language-list col-sm-6"]/ul/li/text()')
    if languages ==[]:
        data["languages"]=[]
    else:
        data["languages"] =languages

    image_url = doc.xpath('//img[@class="agent-photo"]/@src')
    image= ' '.join([str(elem) for elem in image_url])
    data["image_url"]=image
    phnumber=doc.xpath('//a[@class="non-link agent-phone"]/text()')
    if phnumber==[]:
        data["agent_phone_numbers"] =" "
        data["office_phone_numbers"] =" "
    else:
        agent=[]
        agent_p=phnumber[0]
        agent.append(agent_p)
        data["agent_phone_numbers"]=agent
        office=[]
        office_p=phnumber[1]
        office.append(office_p)
        data["office_phone_numbers"]=office
    email = doc.xpath('//a[@class="agent_email"]/text()')
    email_s = ' '.join([str(elem) for elem in email])
    data["email"] = email_s
    website = doc.xpath('//a[@class="button white-alt"]/@href')
    website_s = ' '.join([str(elem) for elem in website])
    data["website"] = website_s
    address = doc.xpath('//div[@class="line-height-reset"]/text()')
    data["address"]=address[0]
    b=' '.join([str(elem) for elem in address])
    a=b.split()
    data["city"]=a[-3]
    data["state"]=a[-2]
    data["zipcode"]=a[-1]
    data["profile_url"]=url
    temp_data=[data]
    if data['count']<11:
        with open('realestate.csv','a') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writerows(temp_data)
        print(data)


realestate("https://www.harrynorman.com/agents")
