import requests
import time
import json
from pprint import pprint
import pandas as pd

class req_recipe:
  def __init__(self, application_id, interval_sec=3):
    self.interval_sec = interval_sec
    self.application_id = application_id
    self.category_list_url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json'
    self.category_ranking_url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json'
  
  def __call__(self, search_word):
    params = {
        "format" : "json",
        "applicationId" : self.application_id
    }
    res = requests.get(self.category_list_url, params=params)
    data = res.json()
    df = pd.DataFrame(data['result']['small'])
    category_list = df['categoryName'].to_list()

    try:
      df_keyword = df.query(f'categoryName.str.contains("{search_word}")', engine='python')
    except:
      return None
    
    result = []
    for search_idx, [index, row] in enumerate(df_keyword.iterrows()):
      time.sleep(self.interval_sec)
      params = {
          "format" : "json",
          "applicationId" : self.application_id,
          "categoryId" : row['categoryUrl'].split('/')[4] # f"{large}-{medium}-{small}" の形式
      }
      res = requests.get(self.category_ranking_url, params=params)

      for i in range(len(res.json()['result'])):
        result.append(dict(res.json()['result'][i]))
    return result

if __name__ == '__main__':
  r = req_recipe('1031564129861406174')
  pprint(r('バナナ'))