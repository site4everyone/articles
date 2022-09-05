from django.shortcuts import render
from .models import Article
# views of search app
def home(request):
  query=request.GET.get('keyword', None)
  
  if query is not None:
    lst = Article.objects.filter(title__icontains=query)
  else:
    lst = Article.objects.all()
  
  
  return render(request, 'index.html', {'articles':lst})
