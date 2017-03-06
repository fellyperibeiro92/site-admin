from django.shortcuts import render, get_object_or_404

from .models import Page
from .forms import ContactPages

def index(request):
  pages = Page.objects.all()
  template_name = 'paginas/about.html'
  context = {
    'pages': pages
  }
  return render(
    request
    , template_name
    , context
  )

def details(request, slug):
  context = {}

  page = get_object_or_404(Page, slug=slug)

  if request.method == 'POST':
    form = ContactPages(request.POST)
    if form.is_valid():
      context['is_valid'] = True
      # print(form.cleaned_data) //parse data to dictionary
      form.send_mail(page)
      form = ContactPages()
  else:
    form = ContactPages()

  template_name = 'paginas/details.html'

  context['form'] = form
  context['page'] = page

  return render(
    request
    , template_name
    , context
  )
