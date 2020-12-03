import pandas as pd

from item.common import *

def get_lb5_stats(html_source):
  all_stats = get_all_stats(html_source)

  try:
    lb5_idx = all_stats.index('[Required Limit Break 5]')
  except:
    return None

  try:
    sub_idx = all_stats.index('[Sub-Options] ')
    lb5_stats = all_stats[lb5_idx+1:sub_idx]
  except:
    lb5_stats = all_stats[lb5_idx+1:]

  return ' '.join(lb5_stats)

def build_lb5_stats(item_type, names, htmls):
  print('Building {} - {}...'.format(item_type, 'LB5 Stats'), end= ' ')
  all_lb5_stats = pd.DataFrame()
  stats_label = get_stats_label()

  all_lb5_stats['Name'] = names
  
  lb5 = []
  for name in names:
    html = htmls[name]
    lb5_stats = get_lb5_stats(html)
    lb5.append(lb5_stats)

  all_lb5_stats['Required Limit Break 5'] = lb5
  print('Done.')
  return all_lb5_stats

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://heavenhold.com/items/elphabas-smile-shield/'
  html_source = html.parse(ur.urlopen(url))
  print(str(get_lb5_stats(html_source)))

