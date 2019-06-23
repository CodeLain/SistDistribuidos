import json

from cryptography.hazmat.primitives.asymmetric import padding
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from SDCore.models import Candidate, Vote, Voter, EncriptedVotes, ElectoralCort
from SDCore.keys import public_key, private_key
import jwt
import base64

# Create your views here.
from django.views import View


class DisplayVotes(View):
    def get(self, request):
        candidates = Candidate.objects.all()
        encrypted_candidates = []
        for candidate in candidates:
            candidate_dict = {}
            candidate_dict['full_name'] = candidate.full_name
            candidate_dict['political_party'] = candidate.political_party.name
            candidate_dict['encrypted_id'] = jwt.encode({'candidate_id': candidate.id}, public_key, algorithm='RS256')
            encrypted_candidates.append(candidate_dict)
            print(candidate_dict['encrypted_id'])
            # print(jwt.decode(candidate_dict['encrypted_id'], private_key, algorithms='RS256'))

        context = {
            'encrypted_candidates': encrypted_candidates,
            'user': 1,
        }
        return render(request, 'vote.html', context)

    def post(self, request):
        # try:
        user = request.POST.get('userID')
        candidate_id = request.POST.get('candidateID')
        candidate_id = candidate_id.replace('b&#39;', '').replace('&#39;', '')
        EncriptedVotes.objects.create(encripted_vote=candidate_id)
        user = Voter.objects.get(pk=user)
        user.enable_vote = False
        user.voted = True
        user.save()
        return JsonResponse({'opperation': True})


class EnableVote(View):
    def get(self, request):
        context = {

        }
        return render(request, 'vote-income.html', context)

    def post(self, request):
        credential_value = request.POST.get('credential_value')
        ci_value = request.POST.get('ci_value')
        electoral_court = ElectoralCort.objects.first()

        if electoral_court.closed_votes:
            return JsonResponse({'opperation': False, 'message': 'El tiempo de votacion ha terminado'})

        if credential_value != "" and ci_value == "":
            try:
                voter = Voter.objects.get(credential=credential_value)
                if voter.voted:
                    return JsonResponse({'opperation': False, 'message': 'Esta persona ya voto previamente'})
                voter.enable_vote = True
                voter.save()
                return JsonResponse({'opperation': True, 'message': 'Persona habilitada a votar'})
            except Voter.DoesNotExist:
                return JsonResponse({'opperation': False, 'message': 'No existe un votante con esta credencial civica'})
        elif credential_value == "" and ci_value != "":
            try:
                voter = Voter.objects.get(ci=ci_value)
                if voter.voted:
                    return JsonResponse({'opperation': False, 'message': 'Esta persona ya voto previamente'})
                voter.enable_vote = True
                voter.save()
                return JsonResponse({'opperation': True, 'message': 'Persona habilitada a votar'})
            except Voter.DoesNotExist:
                return JsonResponse(
                    {'opperation': False, 'message': 'No existe un votante con esta cedula de identidad'})
        # seguir aca!
        return HttpResponse('TEST')


class BlockedVote(View):
    def get(self, request):
        return render(request, 'blocked_vote.html')


class PermisionToVote(View):
    def get(self, request):
        try:
            voters = Voter.objects.get(enable_vote=True)
            return JsonResponse({'opperation': True})
        except Voter.DoesNotExist:
            return JsonResponse({'opperation': False})


class ElectoralCourt(View):
    def get(self, request):
        return render(request, 'vote-count.html')


class StopVoting(View):
    def post(self, request):
        electoral_court = ElectoralCort.objects.first()
        electoral_court.closed_votes = True
        electoral_court.save()
        return JsonResponse({'opperation': True})

class CountVotes(View):
    def get(self, request):
        encripted_votes = EncriptedVotes.objects.all()
        candidates = Candidate.objects.all()
        candidate_votes = {}
        for candidate in candidates:
            candidate_dict = candidate.__dict__
            candidate_dict['votes'] = 0
            candidate_dict['political_party'] = candidate.political_party.name
            del candidate_dict['_state']
            candidate_votes[candidate_dict['id']] = candidate_dict

        for encripted_vote in encripted_votes:
            decrypted_vote = jwt.decode(encripted_vote.encripted_vote, private_key, algorithms='RS256')
            candidate_votes[decrypted_vote['candidate_id']]['votes'] += 1

        return JsonResponse(status=200, data=candidate_votes)
