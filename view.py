# i am created this file - vishwa
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    t_text = request.POST.get('text', 'default')
    # check the checkbox for what you want
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    purpose = ""

    # check that check box is on
    if removepunc == "on":
        punctuations = '''!@#$%^&*()_+|}{:"?></.,;'[]'''
        analyzed = ""
        # analyzed for remove punctutations
        for char in t_text:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'remove punctuations', 'analyze_text': analyzed}
        t_text = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in t_text:
            analyzed += char.upper()
        params = {'purpose': 'capitalization', 'analyze_text': analyzed}
        purpose += "|capitalization"
        t_text = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in t_text:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'remove newline', 'analyze_text': analyzed}
        purpose += "|remove newline"
        t_text = analyzed
        # return render(request, 'analyze.html', params)

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(t_text):
            if not (t_text[index] == " " and t_text[index + 1] == " "):
                analyzed += char
        params = {'purpose': 'remove space', 'analyze_text': analyzed}
        purpose += "|remove space|"
        return render(request, 'analyze.html', params)

    if not ( removepunc == "on" or fullcaps == "on" or newlineremover == "on"
            or spaceremover == "on"):
        return HttpResponse("please select at least one checkbox")
    else:
        return render(request, 'analyze.html', params)


