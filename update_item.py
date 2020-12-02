import pandas as pd
import urllib.request as ur
from lxml import html

# common variable
csv_dir = 'csv/item'
url_source = 'https://heavenhold.com/items/'
item_types = ['Shield', 'Accessory']

# build and save item name list
print('Requesting {}...'.format(url_source), end=' ')
html_source = html.parse(ur.urlopen(url_source))
print('Done.')

for item_type in item_types:
  item_names = html_source.xpath('//div[@id="{}"]//a[@class="item-name"]//text()'.format(item_type))
  item_urls = html_source.xpath('//div[@id="{}"]//a[@class="item-name"]//@href'.format(item_type))
  item_image_urls = []
  for style in html_source.xpath('//div[@id="{}"]//div[@class="item-image"]/@style'.format(item_type)):
    item_image_urls.append(style.split('image: ')[1][5:-2])
  items = pd.DataFrame()
  items['Name'] = item_names
  items['URL of image'] = item_image_urls
  items['URL'] = item_urls
  items.to_csv('{}/{}_source.csv'.format(csv_dir, item_type), index=False)

