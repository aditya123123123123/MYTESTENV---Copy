from django.shortcuts import render
from .forms import FormTeacher
from django.http import HttpResponse
from django.contrib import messages
from .models import Teacher
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


#all for the notion client thing
#client = NotionClient(token_v2="<e35ce8bafdd9239449a576d990e22ff508660c3d875560b442e1d6fc2e2410fcd6edddd14776d337a2b6545f258dcf5139d3ec9bfc6048aa8428a2a3f585fa928b1b9a396f0a4155a633fa74dfcd>")
#page = client.get_block("https://www.notion.so/Aditya-Jhalani-OS-2021-3c07f5fb90dc48f28e52d146807bc9f8")
# Create your views here.


# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
def main(request):
    return render(request,'myapp/main.html')
def viewTeacher(request, id):
    # add the dictionary during initialization
    tea=Teacher.objects.get(id=id)
    context={'teach':tea}
    return render(request,'myapp/viewTeacher.html', context)

def updateTeacher(request,id):
    obj = get_object_or_404(Teacher, id = id)
    form = FormTeacher(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        print("hello")
        return HttpResponseRedirect("/"+str(id))

    context={'form':form}

    return render(request,'myapp/updateTeacher.html',context)



def searchTeacher(request):
    form=FormTeacher(request.POST or None)
    email=''
    if form.is_valid():
        email=form.cleaned_data.get("email")
        print("hello")

    tea=Teacher.objects.filter(email=email)
    context={'teach':tea}

    return render(request,'myapp/searchTeacher.html',context)




def showteacher(request):
    form=FormTeacher(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Form submission Succesful')
    context={'form':form}

    return render(request, 'myapp/userdetails.html',context)


def showteacherdetails(request):
    #uncomment to show all values
    tea=Teacher.objects.all()
    #tea=Teacher.objects.filter(email='adityajhalani28@trinityschoolnyc.org')|Teacher.objects.filter(firstName='Aditya')
    context={'teach':tea}
    return render(request,'myapp/showTeacherDetails.html',context)


def YASH(request):
    return render(request,'myapp/FORYASH.html')