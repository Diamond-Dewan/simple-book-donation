from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .models import User, UserBooks, UserWishList
# from books.models import Book


# Create your views here.
# # Register user
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        address = request.POST['address']
        photo = request.FILES['photo']

        # Check if passwords matched
        if password == password2:
            # chech duplicat username
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username is not available')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email is being used!')
                    return redirect('register')
                else:
                    # create user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, phone=phone, address=address, photo=photo)
                    # Login after register
                    user.save()
                    # user.photo.save(photo, content)
                    messages.success(request, 'Registration Success!!')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

# User Login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Success!!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid User!!')
            return redirect('login')   
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully Logout')
        return redirect('index')

def dashboard(request):
    user_id = request.user
    try:
        userBooks = UserBooks.objects.get(userId=user_id.id)    # get UserBooks id Related to userid
        books = userBooks.bookId.all()      # get all book of that user id

        try:
            userWishedbooks = UserWishList.objects.get(userId=user_id.id)    # get UserWishList id Related to userid
            wishedBooks = userWishedbooks.bookId.all()      # get all book of that user id

        except:
            return render(request, 'accounts/dashboard.html')
            
        
        context = {
            'user_wished_books': wishedBooks,
            'user_books': books,
        }
        return render(request, 'accounts/dashboard.html', context)
    except:
        return render(request, 'accounts/dashboard.html')
        
    

def removeUserBook(request, book_id):
    user = UserBooks.objects.get(userId=request.user)
    user.bookId.filter(id=book_id).delete()

    return redirect('dashboard')

def removeUserWish(request, book_id):
    user = UserWishList.objects.get(userId=request.user)
    user.bookId.filter(id=book_id).delete()
    messages.success(request, 'Removed form Wishlist Success!!')
    
    return redirect('dashboard')
