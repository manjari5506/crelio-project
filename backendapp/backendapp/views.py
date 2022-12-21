from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("homepage requested")
    alphabet= [
        "abc","def","xyz"
    ]
    return JsonResponse(alphabet, safe=False)