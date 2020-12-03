import pandas as pd
import urllib.request as ur
from lxml import html

from common import *
from item.base_stats import *
from item.lb5_stats import *
from item.sub_stats import *

# common variable
csv_dir = 'csv/item'
url_source = 'https://heavenhold.com/items/'
item_types = ['Shield', 'Accessory']

# build and save item name list
print('Requesting {}...'.format(url_source), end=' ')
html_source = html.parse(ur.urlopen(url_source))
print('Done.')

for item_type in item_types:
  print('Building {} name list...'.format(item_type), end=' ')
  item_names = html_source.xpath('//div[@id="{}"]//a[@class="item-name"]//text()'.format(item_type))
  item_urls = html_source.xpath('//div[@id="{}"]//a[@class="item-name"]//@href'.format(item_type))
  item_image_urls = []
  for style in html_source.xpath('//div[@id="{}"]//div[@class="item-image"]/@style'.format(item_type)):
    item_image_urls.append(style.split('image: ')[1][5:-2])
  print('Done.')

  print('Saving {} name list...'.format(item_type), end= ' ')
  items = pd.DataFrame()
  items['Name'] = item_names
  items['URL of image'] = item_image_urls
  items['URL'] = item_urls
  items.to_csv('{}/{}_source.csv'.format(csv_dir, item_type), index=False)
  print('Done.')

  print('Building {} register...'.format(item_type))
  item_pages = pd.Series(items['URL'].values, index=items['Name']).to_dict()
  item_names = list(item_pages.keys())
  htmls = {}
  for name in item_names:
    url = item_pages[name]
    print('  Requesting {}...'.format(name), end=' ')
    htmls[name] = html.parse(ur.urlopen(url))
    print('Done.')
  print('Done.')

  item_base_stats = build_base_stats(item_type, item_names, htmls)
  save_csv(csv_dir, '{}/base_stats'.format(item_type), item_base_stats)

  item_lb5_stats = build_lb5_stats(item_type, item_names, htmls)
  save_csv(csv_dir, '{}/lb5_stats'.format(item_type), item_lb5_stats)

  item_sub_stats = build_sub_stats(item_type, item_names, htmls)
  save_csv(csv_dir, '{}/sub_stats'.format(item_type), item_sub_stats)

