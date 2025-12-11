from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
import markdown2


from . import util

class SearchForm(forms.Form):
    task = forms.CharField(label="Search")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if request.method == "POST":
        title = request.POST

    entry = util.get_entry(title)
    if entry != None:
        htmlEntry = markdown2.markdown(entry)
        
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            #TODO sends html in plaintext and ignores markups
            "entry": htmlEntry
        })
    return render(request, "encyclopedia/notfound.html", {
        "title": title
    })

def search(request):
    search = request.GET.__getitem__("q")
    entries = util.list_entries()
    sItems = []
    for entry in entries:
        if entry == search:
            return HttpResponseRedirect("../" + search)
        if entry.lower().__contains__(search.lower()):
            sItems.append(entry)
    return render(request, "encyclopedia/results.html", {
        "entries": sItems
    })
    

