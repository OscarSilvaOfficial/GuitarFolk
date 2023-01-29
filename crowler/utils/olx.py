import requests, time, re

OLX_PRODUCTS_LIST_URL = 'https://www.olx.com.br' 

def get_olx_urls_pattern(text, product_domain):
  regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(regex, text)
  all_urls = [x[0] for x in url]
  
  product_urls = []
  for url in all_urls:
    domain_name = url.split('//')[1] if '//' in url else url
    is_product_url = len(domain_name.split('.')[0]) == 2 or len(domain_name.split('.')[1]) == 2
    if product_domain in url and is_product_url:
      product_urls.append(url)
      
  return product_urls

def get_olx_next_page_path(next): 
  return f'/brasil?o={next}&q=guitarra%20usada'

def get_olx_site_info():  
  pages_to_find_urls = []
  for next in [1, 2, 3, 4]:
    pages_to_find_urls.append(OLX_PRODUCTS_LIST_URL + get_olx_next_page_path(next))
  
  data = ''
  for page in pages_to_find_urls:
    document = requests.get(page, time.sleep(5), headers={'User-agent': 'Mozilla/5.0'})
    data += document.text
    
  return data