from django.shortcuts import render
from .models import Article
# views of search app
def home(request):
  query = ''
  try:
    query=request.GET['keyword']
  except:
    pass
  
  if query != '':
    lst = Article.objects.filter(title=query)
  else:
    lst = Article.objects.all()
  
  return render(request, 'index.html', {'articles':lst})
