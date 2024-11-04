from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'index.html')

def result(request):
    context = {
        'name' : request.POST['name'],
        'location' : request.POST['location'],
        'language' : request.POST['language'],
        'comment' : request.POST['comment'],
        'gender' : request.POST['gender'],
        'program' : request.POST['program']
    }
    print("checkbox",request.POST['program'])
    return render(request, "result.html", context)
