from django.urls import path
from .views import *

urlpatterns = [
    path('vote/', DisplayVotes.as_view(), name='display_votes'),
    path('enable/', EnableVote.as_view(), name='enable'),
    path('blocked_vote/', BlockedVote.as_view(), name='blocked_vote'),
    path('check_vote/', PermisionToVote.as_view()),
    path('electoral_court/', ElectoralCourt.as_view()),
    path('stop_voting/', StopVoting.as_view()),
    path('count_voutes/', CountVotes.as_view(), name='count_votes'),
]