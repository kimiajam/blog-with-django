from django.shortcuts import render

def post_list(request):
    return render(request,'blog/blog.html')

def post_detail(request):
    return render(request,'blog/post-details.html')

