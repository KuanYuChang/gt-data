import pandas as pd

from item.common import *

def get_sub_stats(html_source):
  all_stats = get_all_stats(html_source)

  try:
    sub_idx = all_stats.index('[Sub-Options] ')
    return all_stats[sub_idx+1:]
  except:
    return []

def get_num_max_sub(html_source):
  sub_stats = get_sub_stats(html_source)

  try:
    return sub_stats[0][len('(Max '):-1]
  except:
    return None

def get_all_sub(html_source):
  sub_stats = get_sub_stats(html_source)

  try:
    all_sub = []
    num_sub = len(sub_stats[1:]) // 2
    for i in range(num_sub):
      idx1 = i * 2 + 1
      idx2 = idx1 + 1
      sub = sub_stats[idx1] + sub_stats[idx2]
      all_sub.append(sub)
    return '\n'.join(all_sub)
  except:
    return None

def build_sub_stats(item_type, names, htmls):
  print('Building {} - {}...'.format(item_type, 'Sub Stats'), end= ' ')
  all_sub_stats = pd.DataFrame()
  stats_label = get_stats_label()

  all_sub_stats['Name'] = names

  num_max_subs = []
  all_subs = []
  for name in names:
    html = htmls[name]
    num_max_sub = get_num_max_sub(html)
    all_sub = get_all_sub(html)

    num_max_subs.append(num_max_sub)
    all_subs.append(all_sub)

  all_sub_stats['Max'] = num_max_subs
  all_sub_stats['Sub-Options'] = all_subs
  print('Done.')
  return all_sub_stats

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://heavenhold.com/items/elphabas-smile-shield/'
  html_source = html.parse(ur.urlopen(url))
  sub_stats = get_sub_stats(html_source)
  print(sub_stats)
  print('Max: {}'.format(sub_stats[0][len('(Max '):-1]))
  num_sub = len(sub_stats) // 2
  subs = []
  for i in range(num_sub):
    sub = sub_stats[(i*2)+1] + sub_stats[(i*2)+2]
    subs.append(sub)
  print('Sub options: {}'.format('\n'.join(subs)))

