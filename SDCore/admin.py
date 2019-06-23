from django.contrib import admin
from SDCore.models import Voter, Vote, Circuit, VoteCenter, ElectoralCort, Candidate, PoliticalParty, EncriptedVotes

# Register your models here.

admin.site.register(Voter)
admin.site.register(Vote)
admin.site.register(Circuit)
admin.site.register(VoteCenter)
admin.site.register(ElectoralCort)
admin.site.register(Candidate)
admin.site.register(PoliticalParty)
admin.site.register(EncriptedVotes)
