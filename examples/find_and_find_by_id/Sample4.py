"""Following example works with Python Client"""
from mapr.ojai.ojai_query.QueryOp import QueryOp
from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

"""Create a connection, get store, insert new document into store"""
# create a connection
connection = ConnectionFactory.get_connection(url="localhost:5678")

# Get a store and assign it as a DocumentStore object
if connection.is_store_exists(store_path='/find_sample_store1'):
    document_store = connection.get_store(store_path='/find_sample_store1')
else:
    document_store = connection.create_store(store_path='/find_sample_store1')

query_condition = connection.new_condition()\
    .or_()\
    .is_('address.street', QueryOp.EQUAL, '351 Hoger Way')\
    .is_('address.street', QueryOp.EQUAL, '39 De Mattei Court')\
    .is_('address.zipCode', QueryOp.EQUAL, 99999).close().close().build()

query = connection.new_query().select(['address']).where(query_condition).build()

query_result = document_store.find(query, results_as_document=True, include_query_plan=True)

for doc in query_result:
    print(doc.as_dictionary())