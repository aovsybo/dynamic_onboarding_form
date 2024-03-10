from django.db import models


class EstablishmentType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class EstablishmentQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    establishment_type = models.ForeignKey(to=EstablishmentType, on_delete=models.PROTECT)

    def __str__(self):
        return self.question_text


class Establishment(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=400)
    establishment_type = models.ForeignKey(EstablishmentType, on_delete=models.PROTECT)
    is_new = models.BooleanField()

    def __str__(self):
        return self.title


class ClientResponse(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    question = models.ForeignKey(EstablishmentQuestion, on_delete=models.CASCADE)
    response_text = models.TextField()

    def __str__(self):
        return f"{self.establishment} -> {self.question}"
