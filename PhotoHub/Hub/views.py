from django.http import HttpResponse
from django.shortcuts import render, redirect

#Importing User model for creating a User instance or authenticating and login , logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout

#Importing Customer and Photographer module
from Hub.models import Customer, Photographer, Appointment, Blog

#For message displaying
from django.contrib import messages

import math
from django.utils import timezone

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Photographer':
            ph = Photographer.objects.get(photographer_id=request.user.id)
            context= {'id':ph.photographer_id, 'role':'Photographer','image': ph.image}
            return render(request, 'landing.html', context)

        else : 
            cst = Customer.objects.get(customer_id=request.user.id)
            context= {'role':'Customer','image':cst.image}
            return render(request, 'landing.html', context)

    return render(request, 'landing.html')
    

def role(request):
    user = User.objects.get(id=request.user.id)
    if len(user.groups.all()) == 0:
       return render(request, 'role.html')
    else:
        return redirect('/')
         
  
def googleLogin(request):
    if request.method == 'POST':
       role = request.POST.get('role')

       #Update Google logged in user with it's role
       new_group, created = Group.objects.get_or_create(name = role)
       user = User.objects.get(id=request.user.id)
       user.groups.add(new_group)

       #Add to customer/photographer module depending upon role
       if new_group.name == 'Customer':
            customer = Customer(customer_id=user.id, email=user.email)
            customer.save()
       else :
            photographer = Photographer(photographer_id=user.id, email=user.email)
            photographer.save()
      
       context = {'role':new_group.name, 'id':user.id} 
       messages.info(request, 'Your initial registration is successfull !')
       return render(request, 'signup2.html', context)



def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
           # A backend authenticated the credentials
           login(request, user)
           messages.info(request, 'Successfully logged in as ' + str(request.user) + ' !')
        #  print(request.user.email)
        #  print(user.groups.all()[0])
           return redirect('/')
        else:
           # No backend authenticated the credentials
           messages.warning(request, 'Invalid credentials! Please try again.')
           return redirect('/')

    return HttpResponse('<h1>Error 404</h1><br> <h3>Page not found!</h3>')


def logoutUser(request):
    logout(request)
    messages.info(request, 'Your have logged out successfully !')
    return redirect('/')


def profile(request, af):
    alert=""
    if int(af) > 0:
        alert='true'
    else :
        alert='false'

    if request.user.groups.all()[0].name == 'Photographer':
        ph = Photographer.objects.get(photographer_id=request.user.id)
        appointments = Appointment.objects.filter(photographer=ph)
        length = len(appointments)
        
        #For comparing datetime field of django models.
        for appointment in appointments:
            appointment.appointment_status = update_appointment_status(appointment)
            appointment.save()

        context={
                 'fname': ph.fname, 'lname':ph.lname, 'gender':ph.gender, 'phone':ph.phone, 'city':ph.city, 'pin':ph.pincode,
                 'email':ph.email[:21], 'category':ph.category, 'role':'Photographer', 'image':ph.image, 'status':ph.status,
                 'state':ph.state, 'appointments': appointments, 'length': length, 'alert': alert, 'id':ph.photographer_id
        }
        
        return render(request, 'profile.html',  context)
    else :
        cst = Customer.objects.get(customer_id=request.user.id)
        appointments = Appointment.objects.filter(customer=cst)
        length = len(appointments)

        for appointment in appointments:
            appointment.appointment_status = update_appointment_status(appointment)
            appointment.save()

        context={
                'fname': cst.fname, 'lname':cst.lname, 'phone':cst.phone, 'city':cst.city, 'state':cst.state, 'pin':cst.pincode,
                'email':cst.email[:21], 'role':'Customer', 'image':cst.image, 'appointments': appointments, 'length': length,
                'alert': alert
             }
        return render(request, 'profile.html', context)


def update_appointment_status(appointment):
    #For comparing datetime field of django models.
    now = timezone.now()
    apt_status = 'Incoming'
    if now >= appointment.start_date and now <= appointment.end_date:
      apt_status = 'Ongoing' 
    elif now > appointment.end_date:
      apt_status = 'Closed'

    return apt_status   

def register_step1(request):
    if request.method=='POST':
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
       
        user = User.objects.create_user(username, email, password)
        user.save()

        #returns a tuple
        new_group, created = Group.objects.get_or_create(name = role)
        user.groups.add(new_group)

        #Add to customer/photographer module depending upon role
        if new_group.name == 'Customer':
            customer = Customer(customer_id=user.id, email=user.email)
            customer.save()
        else :
            photographer = Photographer(photographer_id=user.id, email=user.email)
            photographer.save()
      
        print(user.id, new_group.name)
        context = {'role':new_group.name, 'id':user.id} 
        messages.success(request, 'Your initial registration is successfull !')
        return render(request, 'signup2.html', context)

    return HttpResponse('<h1>Error 404</h1><br> <h3>Page not found!</h3>')   
        
def register_step2(request):
    if request.method=='POST': 
        id = request.POST.get('id')
        role = request.POST.get('role')
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        area = request.POST.get('area')
        pin = request.POST.get('pin')
        image= request.FILES['dp']

        if role=='Photographer':
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            category = request.POST.get('category')
            photographer = Photographer.objects.get(photographer_id=id)
            photographer.fname = fname
            photographer.lname = lname
            photographer.phone = phone
            photographer.state = state
            photographer.city = city
            photographer.area = area
            photographer.pincode = pin
            photographer.age = age
            photographer.gender = gender
            photographer.category = category
            photographer.image = image
            photographer.save()

        else :
            customer = Customer.objects.get(customer_id=id)
            customer.fname = fname
            customer.lname = lname
            customer.phone = phone
            customer.state = state
            customer.city = city
            customer.area = area
            customer.pincode = pin
            customer.image = image
            customer.save()

        messages.info(request, "Your registration is completed successfuly !")
        return redirect('/')


def editProfile(request):
   if request.method == 'POST':
      fname = request.POST.get('fname')
      lname = request.POST.get('lname')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      state = request.POST.get('state')
      city = request.POST.get('city')
      area = request.POST.get('area')
      pin = request.POST.get('pin')
      image= request.FILES['dp'] 

      if request.user.groups.all()[0].name == 'Photographer':
          age = request.POST.get('age')
          category = request.POST.get('category')  
          photographer = Photographer.objects.get(photographer_id=request.user.id)
          photographer.fname = fname
          photographer.lname = lname
          photographer.phone = phone
          photographer.state = state
          photographer.city = city
          photographer.area = area
          photographer.pincode = pin
          photographer.age = age
          photographer.email = email
          photographer.category = category
          photographer.image = image
          photographer.save()

      else :
            customer = Customer.objects.get(customer_id=request.user.id)
            customer.fname = fname
            customer.lname = lname
            customer.email = email
            customer.phone = phone
            customer.state = state
            customer.city = city
            customer.area = area
            customer.pincode = pin
            customer.image = image
            customer.save()

      return redirect('/profile1')


   if request.user.groups.all()[0].name == 'Photographer':
        ph = Photographer.objects.get(photographer_id=request.user.id)

        context={
                 'fname': ph.fname, 'lname':ph.lname, 'phone':ph.phone, 'city':ph.city, 'pin':ph.pincode,
                 'email':ph.email, 'category':ph.category, 'image':ph.image, 'state':ph.state, 'age':ph.age,
                 'area': ph.area, 'id':ph.photographer_id
        }
        
        return render(request, 'editProfile.html',  context)

   else :
        cst = Customer.objects.get(customer_id=request.user.id)
        context={
                'fname': cst.fname, 'lname':cst.lname, 'phone':cst.phone, 'city':cst.city, 'state':cst.state, 'pin':cst.pincode,
                'email':cst.email, 'image':cst.image, 'area': cst.area
             }
        return render(request, 'editProfile.html', context)
   


def category(request):
    context = {}

    cst = Customer.objects.get(customer_id=request.user.id)
    context['image'] = cst.image
    
    #creates dictionary for each object
    catphs = Photographer.objects.values('category', 'photographer_id')
    cats = {item['category'] for item in catphs}
    #print(cats)
    
    allcatph = []
    for cat in cats:
        catph = Photographer.objects.filter(category=cat)
        tuple = (cat, catph)
        allcatph.append(tuple)

   # print(allcatph)    
    context['allcatph'] = allcatph
    return render(request, 'category.html', context)



def allfromCat(request, cat):
    context = {}
    
    cst = Customer.objects.get(customer_id=request.user.id)
    context['image'] = cst.image

    catph = Photographer.objects.filter(category=cat)
    context['catph'] = catph
    context['category'] = cat
    return render(request, 'allfromCat.html', context)


def appointment(request, pid):
    cst = Customer.objects.get(customer_id=request.user.id)
    context = {'image': cst.image, 'pid': pid}
    return render(request, 'appointment.html', context)


def createAppointment(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        state = request.POST.get('state')
        city = request.POST.get('city')
        area = request.POST.get('area')
        zip = request.POST.get('zip')
        
        ph = Photographer.objects.get(photographer_id=pid)
        cst = Customer.objects.get(customer_id=request.user.id)
        appointment = Appointment(
                                  customer=cst, 
                                  photographer=ph, 
                                  start_date=sdate, 
                                  end_date=edate, 
                                  state=state,
                                  city=city,
                                  area=area,
                                  zip=zip,
                                  appointment_status='incoming'                        
                                  )
        appointment.save()
        ph.status="Busy"
        ph.save()
        context = {'ph': ph, 'cst': cst, 'appointment' : appointment ,'image': cst.image}
        return render(request, 'successAppointment.html', context)


def pagination(request, bnum):
    pnum, first, last = bnum.split('_')
    
    #Range of buttons to show for controlling pagination
    first = int(first)
    last = int(last)

    #Appointments to show for current pnum
    pnum = int(pnum)-1
    start=pnum*2
    end=start+2

    if request.user.groups.all()[0].name == 'Photographer':
        ph = Photographer.objects.get(photographer_id=request.user.id)
        appointments = Appointment.objects.filter(photographer=ph)

        # for setting up pagination
        pages = [int(i) for i in range(1, math.ceil(len(appointments)/2)+1)]
        length = len(pages)
        if last == 0:
            last = min(3, length)

        if request.method=='POST':
            f = int(request.POST.get('first'))
            l = int(request.POST.get('last'))
            funct = request.POST.get('funct') 

            first, last = updateMarkers(f, l, funct)
            
            start = int(request.POST.get('start'))
            end = int(request.POST.get('end'))

        apt_list = appointments[start:end]
        context={
            'role':'Customer', 
            'apt_list':apt_list, 
            'pages':pages, 
            'first':first, 
            'last':last, 
            'length':length,
            'start':start,
            'end':end,
            'pnum':pnum+1,
            'image': ph.image
            }    
        return render(request, 'pagination.html', context)

    else :
        cst = Customer.objects.get(customer_id=request.user.id)
        appointments = Appointment.objects.filter(customer=cst)

        # for setting up pagination
        pages = [int(i) for i in range(1, math.ceil(len(appointments)/2)+1)]
        length = len(pages)
        if last == 0:
           last = min(3, length)

        if request.method=='POST':
            f = int(request.POST.get('first'))
            l = int(request.POST.get('last'))
            funct = request.POST.get('funct') 

            first, last = updateMarkers(f, l, funct)

            start = int(request.POST.get('start'))
            end = int(request.POST.get('end'))

        apt_list = appointments[start:end]
        context={
            'role':'Customer', 
            'apt_list':apt_list, 
            'pages':pages, 
            'first':first, 
            'last':last, 
            'length':length,
            'start':start,
            'end':end,
            'pnum':pnum+1,
            'image': cst.image
            }    
        return render(request, 'pagination.html', context)


def updateMarkers(first, last, funct):
    if funct=='prev':
        first=first-1
        last = last-1

    else :
        first=first+1
        last = last+1

    return [first, last]


# For Blog of photographer
def blog(request, pid):
    ph = Photographer.objects.get(photographer_id=pid)
    post = Blog.objects.filter(photographer = ph)
    context={}
    context['ph'] = ph
    context['post'] = post
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Customer':
            usr = Customer.objects.get(customer_id=request.user.id)
            context['role'] = 'Customer'
            context['image'] = usr.image
            context['id'] = usr.customer_id
        else : 
            usr = Photographer.objects.get(photographer_id=request.user.id)
            context['role'] = 'Photographer'
            context['image'] = usr.image
            context['id'] = usr.photographer_id

    return render(request, 'blog.html', context)


def deletePost(request, pid):
    post = Blog.objects.get(id=pid)
    post.delete()
    return redirect('/blog/'+str(post.photographer.photographer_id))


def editPost(request, pid):
    post = Blog.objects.get(id=pid)
    if request.method == 'POST':
        img = request.FILES['img']
        head = request.POST.get('head')
        date = request.POST.get('date')
        desc = request.POST.get('desc')
        post.img = img
        post.head = head
        post.date = date
        post.desc = desc
        post.save()
        return redirect('/blog/'+str(post.photographer.photographer_id))
    else : 
        context = {}
        context['post'] = post
        context['id'] = post.photographer.photographer_id
        context['image'] = post.photographer.image
        return render(request, 'editPost.html', context)

    
def addPost(request, pid):
    if request.method == 'POST':
        photographer = Photographer.objects.get(photographer_id = pid)
        img = request.FILES['img']
        head = request.POST.get('head')
        date = request.POST.get('date')
        desc = request.POST.get('desc')
        post = Blog(
                    photographer = photographer,
                    img = img,
                    head = head,
                    date = date,
                    desc = desc
                    )
        post.save()
        return redirect('/blog/'+str(pid))
    ph = Photographer.objects.get(photographer_id = pid)
    context = {}
    context['id'] = ph.photographer_id
    context['image'] = ph.image
    return render(request, 'addPost.html', context)



def changeStatus(request):
    if request.method == 'POST':
        ph = Photographer.objects.get(photographer_id=request.user.id)
        ph.status = request.POST.get('status')
        ph.save()

        return redirect('/profile0')    
    