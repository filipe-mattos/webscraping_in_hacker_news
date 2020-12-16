from flask import Flask, render_template, request
from request import get_new_news, get_popu_news, get_id_news, get_comments_by_id

app = Flask('Hn scraping')

@app.route('/')
def call_index():
  print(request.args)
  order_by = request.args.get('order_by')
  print(order_by)
  if order_by == 'new':
    news = get_new_news()
  elif order_by == 'popular':
    news = get_popu_news()
  else:
    news = get_popu_news()
  return render_template('index.html', result = news)

@app.route('/<idobj>')
def call_id(idobj):
  news = get_id_news(idobj)
  list_comments = get_comments_by_id(idobj)
  return render_template('id.html', result = news[0], comments = list_comments)

app.run(host="127.0.0.1")