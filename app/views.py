from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':240,'b':2409,'c':76}
    return render(request,'conditions.html',d)

def loops(request):
    d={'name':'SHAILESH RAJ'}
    return render(request,'loops.html',d)