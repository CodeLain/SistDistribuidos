import hashlib
from django.db import models

# Create your models here.
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

class Voter(models.Model):
    full_name = models.CharField(max_length=80)
    voted = models.BooleanField(default=False)
    circuit = models.ForeignKey(to='Circuit', on_delete=models.SET_NULL, null=True)
    time_stamp = models.DateField(auto_now=True)

    def create_vote(self, candidate):
        self.voted = True
        Vote.objects.create(candidate)
        self.save()


class Vote(models.Model):
    candidate = models.ForeignKey(to='Candidate', on_delete=models.CASCADE)


class Circuit(models.Model):
    vote_center = models.ForeignKey(to='VoteCenter', on_delete=models.CASCADE)


class VoteCenter(models.Model):
    name = models.CharField(max_length=80)
    address = models.TextField()


class ElectoralCort(models.Model):
    private_key = models.TextField(max_length=255) #primera en ecriptar



    #ContarVotos
    #desencriptarVotos
    #ValidarVoto


class Witness(models.Model):
    full_name = models.CharField(max_length=80)
    private_key = models.TextField(max_length=255)
    #rol

    #PermitirVoto
    #Encriptaran/firman para saber que estuvo presente


class Candidate(models.Model):
    political_party = models.ForeignKey(to='PoliticalParty', on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=80)


class PoliticalParty(models.Model):
    public_key = models.TextField(max_length=255)
    name = models.CharField(max_length=80)

    #Encriptar
