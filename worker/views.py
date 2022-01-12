from django.shortcuts import render
from worker.models import Project,Blog,Review

# Create your views here.
def index(request):
	context={"Blogs":Blog.objects.values(),
				"Projects":Project.objects.values(),
				"Reviews":Review.objects.values()}
				
	return render(request,"index.html",context=context)