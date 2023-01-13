from django.shortcuts import render, HttpResponseRedirect
from .models import AllShayari, Contact
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'landing.html')


def home(request):
    mix = AllShayari.objects.filter(category='Mix')
    context = {'mix': mix}
    return render(request, 'TextSyri/home.html', context)


def love(request):
    love = AllShayari.objects.filter(category='Love')
    context = {'love': love}
    return render(request, 'TextSyri/love.html', context)


def dosti(request):
    dosti = AllShayari.objects.filter(category='Dosti')
    context = {'dosti': dosti}
    return render(request, 'TextSyri/dosti.html', context)


def wish(request):
    wish = AllShayari.objects.filter(category='Wish')
    context = {'wish': wish}
    return render(request, 'TextSyri/wish.html', context)


def sad(request):
    sad = AllShayari.objects.filter(category='Sad')
    context = {'sad': sad}
    return render(request, 'TextSyri/sad.html', context)


def dhokha(request):
    dhokha = AllShayari.objects.filter(category='Dhokha')
    context = {'dhokha': dhokha}
    return render(request, 'TextSyri/dhokha.html', context)


def alone(request):
    alone = AllShayari.objects.filter(category='Alone')
    context = {'alone': alone}
    return render(request, 'TextSyri/alone.html', context)

def break_up(request):
    break_up = AllShayari.objects.filter(category='BreakUp')
    context = {'break_up': break_up}
    return render(request, 'TextSyri/breakup.html', context)

def bhakti(request):
    bhakti = AllShayari.objects.filter(category='Bhakti')
    context = {'bhakti': bhakti}
    return render(request, 'TextSyri/bhakti.html', context)


def deshbhakti(request):
    deshbhakti = AllShayari.objects.filter(category='Deshbhakti')
    context = {'deshbhakti': deshbhakti}
    return render(request, 'TextSyri/deshbhakti.html', context)


def thought(request):
    thought = AllShayari.objects.filter(category='Thought')
    context = {'thought': thought}
    return render(request, 'TextSyri/thought.html', context)

def contact(request):
    try:
        if request.method == 'POST':
            Fname = request.POST['fname']
            Lname = request.POST['lname']
            Email = request.POST['email']
            Msg = request.POST['message']

            obj = Contact(first_name = Fname, last_name=Lname, email=Email, message=Msg)
            obj.save()
            messages.success(request, 'Your message has been sent. Thanks !')
    except Exception as e:
        return HttpResponseRedirect('/')

    return render(request, 'TextSyri/contact.html')
