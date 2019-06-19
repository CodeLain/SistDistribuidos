from django.contrib import admin
from SistDistCore.models import Voter, Vote, Circuit, VoteCenter, ElectoralCort, Candidate, PoliticalParty

# Register your models here.

admin.site.register(Voter)
admin.site.register(Vote)
admin.site.register(Circuit)
admin.site.register(VoteCenter)
admin.site.register(ElectoralCort)
admin.site.register(Candidate)
admin.site.register(PoliticalParty)
