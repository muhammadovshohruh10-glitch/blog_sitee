from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_list(request):
    html = """
    <h1>BLOG</h1>
      """
    return HttpResponse(html)
