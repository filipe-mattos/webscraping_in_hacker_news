import requests

#url_new = 'http://hn.algolia.com/api/v1/search_by_date?tags=story'
#url_popular = 'https://hn.algolia.com/api/v1/search?tags=story'
#url_id = 'http://hn.algolia.com/api/v1/items/{id}'
#url_comment = 'https://hn.algolia.com/api/v1/search?tags=comment,story_{id}'

def get_new_news():
  req = requests.get('http://hn.algolia.com/api/v1/search_by_date?tags=story').json()
  aux = req['hits']
  list_news = []
  for data in aux:
    dictionary = {
      'title': data['title'],
      'objectID': data['objectID'],
      'author': data['author'],
      'points': data['points'],
      'url': data['url'],
      'num_comments': data['num_comments']
    }
    list_news.append(dictionary)
  return list_news

def get_popu_news():
  req = requests.get('https://hn.algolia.com/api/v1/search?tags=story').json()
  aux = req['hits']
  list_news = []
  for data in aux:
    dictionary = {
      'title': data['title'],
      'objectID': data['objectID'],
      'author': data['author'],
      'points': data['points'],
      'url': data['url'],
      'num_comments': data['num_comments']
    }
    list_news.append(dictionary)
  return list_news

def get_id_news(idobj):
  req = requests.get(f'http://hn.algolia.com/api/v1/items/{idobj}').json()
  list_news = []
  dictionary = {
      'title': req['title'],
      'objectID': req['id'],
      'author': req['author'],
      'points': req['points'],
      'url': req['url']
    }
  list_news.append(dictionary)
  return list_news

def get_comments_by_id(idobj):
  req = requests.get(f'https://hn.algolia.com/api/v1/search?tags=comment,story_{idobj}&hitsPerPage=100').json()
  comments = req['hits']
  list_comments = []
  for comment in comments:
    dictionary = {
      'author': comment['author'],
      'comment_text': comment['comment_text'],
      'created_at': comment['created_at']
    }
    list_comments.append(dictionary)
  return(list_comments)