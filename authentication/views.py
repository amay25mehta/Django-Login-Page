from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout







# Create your views here.

def home(request):  
    return render(request,"authentication/index.html")  #renders the home page ,stored in index.html



'''
Used python manage.py makemigrations and python manage.py migrate to make all tables in the database
'''    

def signup(request): #Defining signup to add functionality to signin.html
    if request.method == "POST":   #if someone submited form then this if block will open
        username = request.POST['username']  #using request to get the username
        fname = request.POST['fname'] #using request to get the firstname and store it in fname
        lname = request.POST['lname']#same to get lastname
        email = request.POST['email']#same to get email
        pass1 = request.POST['pass1']#same to get password
        
       

        myuser = User.objects.create_user(username, email, pass1)  #creating myuser object using the User inbuild model which will include username,email and pass1
        myuser.first_name = fname  #to access the firstname from the database
        myuser.last_name = lname  #to access the lastname from the databsase
        
        myuser.save()  #will save the user to the  database

        messages.success(request, "Your Account has been created succesfully!! ")  #using messages(inbuild library of django) to display the message

        return redirect('signin')  #will redirect to signin itself with the message on top.
    
    return render(request, "authentication/signup.html") #will render signup.html page

def teachersignup(request):  #same function but just for staff/teachers only

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
        

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
      
        
        myuser.save()

        messages.success(request, "Your Account has been created succesfully!! ")

        return redirect('signin')
    return render(request,"authentication/teachersignup.html")    

def signin(request):   #Defining signin to add functionality to signin.html

    if request.method == 'POST':
        username = request.POST['username']  #requesting username 
        pass1 = request.POST['pass1']  #requesting password
        
        user = authenticate(username=username, password=pass1)  #using django inbuild authenticate function to check if the username and password matches or not, it will report None if author is not authenticated.
        
        if user is not None:  #if user is authenticated which is not None
            login(request, user)  #using login inbuild function to login the user
            fname = user.first_name  #getting firstname as fname stored as first_name in database table
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/profile.html",{"fname":fname}) #will render the profile.html page  with firstname 
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    

    return render(request,"authentication/signin.html")  

def teachersignin(request):  #same function but for teachersignin page.

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/teacherprofile.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    

    return render(request,"authentication/teachersignin.html")     

def signout(request):  #signout functionality
    logout(request)  #using inbuild logout function tp logout from the profile
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')   #will redirect to home page


def profile(request):
    return render(request,"authentication/profile.html")               