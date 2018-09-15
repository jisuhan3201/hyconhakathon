from django.shortcuts import render
from . import models

def all_papers(request):

    all_papers = models.Paper.objects.all()
    print(all_papers)

    return render(request, 'papers/proposal.html', {'data': all_papers})
