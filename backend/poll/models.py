from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text} in {self.poll.name}"

class Voter(models.Model):
    poll = models.ForeignKey(Poll, related_name='voters', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.ip_address}) voted in {self.poll.name}"
