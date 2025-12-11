from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
import random
import markdown2


from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(label="content", widget=forms.Textarea)

class EditForm(forms.Form):
    content = forms.CharField(label="content", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry != None:
        htmlEntry = markdown2.markdown(entry)
        
        return render(request, "encyclopedia/entry.html", {
            "title": title,
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
        if entry.lower() == search.lower():
            return HttpResponseRedirect(search)
        if entry.lower().__contains__(search.lower()):
            sItems.append(entry)
    return render(request, "encyclopedia/results.html", {
        "entries": sItems
    })
    
def newentry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            entryTitle = form.cleaned_data["title"]
            entryContent = form.cleaned_data["content"]
            if util.list_entries().__contains__(entryTitle):
                form.add_error("title", "Entry Already Exists")
                return render(request, "encyclopedia/newentry.html",{
                   "form": form
                })
            util.save_entry(entryTitle,entryContent)
            return HttpResponseRedirect(entryTitle)

    return render(request, "encyclopedia/newentry.html",{
        "form": NewEntryForm()
    })

def randomEntry(request):
    entryList = util.list_entries()
    title = entryList[int((len(entryList)*random.random()))]
    entry = util.get_entry(title)
    htmlEntry = markdown2.markdown(entry)
    return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": htmlEntry
        })