import tkinter as tk
import tkinter.messagebox as  tkMessageBox
from django.shortcuts import render
from .models import *
from django.contrib.auth import get_user_model
user = get_user_model()

# Create your views here.

def index(request):
    trains=Train.objects.all()
    context={"trains":trains}

    return render(request,"railways/index.html",context)

def view_tickets(request,pk):
    tickets=Ticket.objects.all().filter(ticket_name=pk)
    context={"tickets":tickets}
    return render(request,"railways/view_tickets.html",context)


def details(request,pk):
    trains=Train.objects.get(id=pk)
    context={"trains":trains}
    return render(request,"railways/details.html",context)

def book_ticket(request,pk):
    trains=Train.objects.get(id=pk)
    context={"trains":trains}
    if request.method=="POST":
        if trains.number>0:
            cost1=trains.cost
            trains.number=trains.number-1
            gend=request.POST["gender"]
            print(gend)
            p=Ticket(ticket_name=request.user.username,train=trains,number=trains.number,cost=cost1,gender=gend,time=trains.time,date=trains.date)
            p.save()
            trains.save()
            root = tk.Tk()
            root.withdraw()
            MsgBox=tkMessageBox.showwarning('alert title', 'Booked')
            print(MsgBox)
            if MsgBox == 'ok':
                root.destroy()


        else:
            root = tk.Tk()
            root.withdraw()
            MsgBox=tkMessageBox.showwarning('alert title', 'No more tickets')
            print(MsgBox)
            if MsgBox == 'ok':
                root.destroy()

    return render(request,"railways/tickets.html",context)

