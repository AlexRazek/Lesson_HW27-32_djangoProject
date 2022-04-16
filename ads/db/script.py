import pandas as pandas

# from ads.models import Ad

data_ads = pandas.read_csv('ads.csv', sep=",").to_dict()

i = 0

while max(data_ads['Id'].keys()) > i:
    print(data_ads['name'][i])
    '''ad = Ad.objects.create(
        name=data_ads["name"][i],
        author=data_ads["author"][i],
        price=data_ads["price"][i],
        description=data_ads["description"][i],
        address=data_ads["address"][i],
        is_published=data_ads["is_published"][i],
    )'''
    print(data_ads['Id'][i])
    i +=1