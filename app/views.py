from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':1232,'b':143}
    return render(request,'operations.html',context=d)
