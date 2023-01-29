from fast_nosql_manager import MongoRepository

from utils.env import MONGO_URL

mongo = MongoRepository(
  db_name='guitar_folk', 
  db_str_connection=MONGO_URL,
)

def add_product_urls(products):
  collection_name = 'products'
  mongo.create_document(collection_name, products)
  