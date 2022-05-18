import re
import requests
import lxml.html as lh

#def read_disct
wiki_lines = 'https://ru.wikipedia.org'
        
def read_wiki_subcats(page_link):
    '''Function for reading pages of type "Categoryes" on the site wikipedia'''
    # inputs:
    # page_link - apge url address (https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%83%D0%BD%D0%BA%D1%82%D1%8B_%D0%94%D0%BE%D0%BA%D1%88%D0%B8%D1%86%D0%BA%D0%BE%D0%B3%D0%BE_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD%D0%B0)
    # outputs:
    # dictionary {<ref text> : <ref url>}
    
    r = requests.get(page_link)
    doc = lh.fromstring(r.content)
    cat_divs = doc.xpath('//div[@class="CategoryTreeItem"]')
    
    result = {}
    
    for div in cat_divs:
        div_obj = div.xpath('a')[0]
        result[div_obj.text] = div_obj.get("href")
        
    return result


def read_wiki_cats(page_link):
    '''Function for reading a wiki categories'''
    # inputs:
    # page_link - apge url address (https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%83%D0%BD%D0%BA%D1%82%D1%8B_%D0%94%D0%BE%D0%BA%D1%88%D0%B8%D1%86%D0%BA%D0%BE%D0%B3%D0%BE_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD%D0%B0)
    # outputs:
    # dictionary {<ref text> : <ref url>}
    
    r = requests.get(page_link)
    doc = lh.fromstring(r.content)
    cat_divs = doc.xpath('//div[@id="mw-pages"]')[0].xpath('.//li')
    
    result = {}
    
    for div in cat_divs:
        div_obj = div.xpath('a')[0]
        result[div_obj.text] = div_obj.get('href')
    
    return result