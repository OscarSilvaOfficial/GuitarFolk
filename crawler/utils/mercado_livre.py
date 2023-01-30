import requests, re

ML_PRODUCTS_LIST_URL = 'https://lista.mercadolivre.com.br' 

def get_ml_urls_pattern(text, product_domain):
  regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(regex, text)
  all_urls = [x[0] for x in url]
  
  product_urls = []
  for url in all_urls:
    if product_domain in url:
      product_urls.append(url)
      
  return product_urls

def get_ml_next_page_path(next): 
  return f'/instrumentos-musicais/instrumentos-corda/guitarras/eletricas/usado/guitarras-usadas_Desde_{next}_NoIndex_True'

def get_ml_site_info():  
  pages_to_find_urls = []
  for next in [0, 49, 97, 145]:
    pages_to_find_urls.append(ML_PRODUCTS_LIST_URL + get_ml_next_page_path(next))
  
  data = ''
  for page in pages_to_find_urls:
    document = requests.get(page)
    data += document.text
    
  return data