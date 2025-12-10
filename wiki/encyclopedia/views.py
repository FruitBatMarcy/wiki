from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    entry = util.get_entry(title)
    if entry != None:
        return 1
    return render(request, "encyclopedia/notfound.html", {
        "title": title
    })