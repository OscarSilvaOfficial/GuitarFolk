import datetime

from utils.mercado_livre import get_ml_site_info, get_ml_urls_pattern
from utils.olx import get_olx_site_info, get_olx_urls_pattern
from utils.mongo import add_product_urls

now = datetime.datetime.now()

ml_site_text = get_ml_site_info()
olx_site_text = get_olx_site_info()

ml_urls_finded = get_ml_urls_pattern(ml_site_text, 'produto.mercadolivre.com.br')
olx_urls_finded = get_olx_urls_pattern(olx_site_text, '.olx.com.br')

document = { 
  str(now.timestamp()): { 
    'mercado_livre': ml_urls_finded,
    'olx': olx_urls_finded
  } 
}

add_product_urls(document)