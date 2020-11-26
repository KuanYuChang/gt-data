from datetime import date

def save_csv (csv_dir, category, data_frame):
  today = date.today()
  csv_path = '{}/{}/{}.csv'
  data_frame.to_csv (csv_path.format(csv_dir, category, today), index = False)
  data_frame.to_csv (csv_path.format(csv_dir, category, 'current'), index = False)

