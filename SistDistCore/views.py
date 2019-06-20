from django.http import HttpResponse
from django.shortcuts import render
from SistDistCore.models import Candidate

# Create your views here.
from django.views import View


class DisplayVotes(View):
    def get(self, request):
        candidates = Candidate.objects.all()
        context = {
            'candidates': candidates,
            'user': 1,
        }
        return render(request, 'vote.html', context)

    def post(self, request):
        user_id = request.POST.get('userID')
        candidate_id = request.POST.get('candidateID')

        print(user_id)
        print(candidate_id)

        return HttpResponse('<h1>VOTO VOTADO</h1>')
