from django.shortcuts import render
from django.http import HttpResponse
#def index(request):
    #name = request.GET.get("name") or "world!" #تاسك ٢
    #return HttpResponse("Hello," + name)

#def index2(request, val1 = 0):   # تاسك ٣
    #return HttpResponse("value1 = " + str(val1))


#def index(request):
    #name = request.GET.get("name") or "world!"
    #return render(request, "bookmodule/index.html")
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})    

def index2(request, val1 = 0):
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)
# لاب اربعه
def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

# Task 1: Links
def html5_links(request):
    return render(request, 'bookmodule/html5_links.html')

# Task 2: Text Formatting
def html5_formatting(request):
    return render(request, 'bookmodule/html5_formatting.html')

# Task 3: Listing
def html5_listing(request):
    return render(request, 'bookmodule/html5_listing.html')

# Task 4: Tables
def html5_tables(request):
    return render(request, 'bookmodule/html5_tables.html')