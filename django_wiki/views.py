from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
      return HttpResponse('<p> Welcome Home </p>')

def index(request):
# it is rendering a custom template from the django_wiki template
      # return render(request, 'django_wiki/wiki_index.html')
      if request.user.is_authenticated:
            return HttpResponse('<p> You ARE signed in. </p>')
      else:
            return HttpResponse('<p> You are NOT in. </p>')


