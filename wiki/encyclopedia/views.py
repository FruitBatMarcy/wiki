from django.shortcuts import render
import html
import markdown2

from . import util


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
            #TODO sends html in plaintext and ignores markups
            "entry": htmlEntry
        })
    return render(request, "encyclopedia/notfound.html", {
        "title": title
    })