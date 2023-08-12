from django.shortcuts import render,redirect
from .models import Plan

def plan_list(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'plan_list.html', context)

def ADD(request):
    if request.method == "POST":
        activity = request.POST.get('activity')
        duration = request.POST.get('duration')
        day = request.POST.get('day')
        time_spent = request.POST.get('time')
        
        plans = Plan(
            activity = activity,
            duration = duration,
            day = day,
            time_spent = time_spent
        )
        
        plans.save()
        return redirect('plan_list')
        
    return render(request,'plan_list.html')

def EDIT(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return redirect(request, 'plan_list.html', context)

def UPDATE(request,id):
    if request.method == "POST":
        activity = request.POST.get('activity')
        duration = request.POST.get('duration')
        day = request.POST.get('day')
        time_spent = request.POST.get('time')
        
        plans = Plan(
            id = id,
            activity = activity,
            duration = duration,
            day = day,
            time_spent = time_spent
        )
        
        plans.save()
        return redirect('plan_list')    
        
    return redirect(request, 'plan_list.html')

def DELETE(request,id):
    plans = Plan.objects.filter(id=id)
    plans.delete()
    context = {'plans': plans}
    return redirect('plan_list')