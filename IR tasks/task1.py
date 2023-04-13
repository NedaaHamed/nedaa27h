Doc1= 'new home sales top forecasts.'
Doc2= 'home sales rise in July'
Doc3= 'increase in home sales in July.'
Doc4= 'July new home sales rise'

text =[Doc1,Doc2,Doc3,Doc4]

distinct_items= set()
for doc in text:
    for item in doc.split():
        distinct_items.add(item)
print (distinct_items)

inverted_index = {}
for i, doc in enumerate(text):
    for term in doc.split():
        if term in inverted_index:
            inverted_index[term].add(i)
        else: 
            inverted_index[term] = {i}
print (inverted_index)

posting_list = inverted_index['home']
print(posting_list)



