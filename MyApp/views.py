from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import student 
import json 

def student_data(request):
    return render(request, 'create.html')

def getdata(request):
    res = {'status' : "Not-save",'msg' : "Data not fetched..."}
    if request.method == 'POST':
        name=request.POST.get('Name')
        Age=request.POST.get('Age')
        Contact=request.POST.get('Contact')
        print("\n\n\n")
        print('Name ',name, 'Age', Age, 'Contact', Contact)
        print("\n\n\n")
        student.objects.create(
        name = name,
        age =  Age,
        contact = Contact,)
        stu_data=student.objects.all()
        res = {'status' : 'Save','data' : "stu_data"}
        return HttpResponse(json.dumps(res), content_type='application/json')
    return HttpResponse(json.dumps(res), content_type='application/json')

def update_data(request, id):
    id=student.objects.filter(pk=id)
    print("user id",id)    
    return render(request, 'update.html', {'Data':id})





def get_update_data(request):
    res = {'status' : False,'msg' : "Not_Updated"}
    if request.method == 'POST':
        # stu_data=student.objects.filter(id=id)

        Name=request.POST.get('fullname')
        Age=request.POST.get('Age')
        Contact=request.POST.get('Contact')
        ids =request.POST.get('ids')

        print("\n\nUSER ID IS ",ids)
        
        print("\n\n\n")
        print('Name ',Name, 'Age', Age, 'Contact', Contact,)
        print("\n\n\n")

        student.objects.filter(pk=ids).update(name=Name, age=Age, contact=Contact)

        # stu_data.objects.create(
        # name = name,
        # age =  Age,
        # contact = Contact,)
        res = {'status' : True,'msg' : "data Updated" }
    
    
    return HttpResponse(json.dumps(res), content_type='application/json')




def show_data(request):
    stu_data=student.objects.all()
    return render(request, 'show.html', {'data' : stu_data})



def ThankYou(request):
    value='Thank-You, Data Submitted'
    return render(request, 'thanks.html', {'data':value})

def updated(request):
    value='Thank-You, Data Updatted'
    return render(request, 'thanks.html', {'data':value})


def Delete(request):
    # Name=request.POST.get('fullname')
    id=request.POST.get('ID')
    print("user id",id)
    data=student.objects.get(pk=id)
    data.delete()
    return render(request, 'redirect.html', {'data':"Data Deleted"})