from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
    # 骗！
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return HttpResponse('<html><title>To-Do lists</title></html>')
