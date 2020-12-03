import pandas as pd

from item.common import *

def get_base_stats(html_source):
  all_stats = get_all_stats(html_source)

  try:
    lb5_idx = all_stats.index('[Required Limit Break 5]')
    return all_stats[:lb5_idx]
  except:
    try:
      sub_idx = all_stats.index('[Sub-Options] ')
      return all_stats[:sub_idx]
    except:
      return all_stats

def build_base_stats(item_type, names, htmls):
  print('Building {} - {}...'.format(item_type, 'Base Stats'), end= ' ')
  all_base_stats = pd.DataFrame()
  stats_label = get_stats_label()

  all_base_stats['Name'] = names
  for label in stats_label:
    attribute = []

    for name in names:
      html = htmls[name]
      base_stats = get_base_stats(html)

      try:
        idx = base_stats.index(label)
        if label[0] == ' ':
          attribute.append(base_stats[idx-1])
        else:
          attribute.append(base_stats[idx+1])
      except:
        attribute.append(None)
  
    all_base_stats[label] = attribute

  print('Done.')
  return all_base_stats

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://heavenhold.com/items/elphabas-smile-shield/'
  html_source = html.parse(ur.urlopen(url))
  print(str(get_base_stats(html_source)))

