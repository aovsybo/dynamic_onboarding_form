from django.db import models


class EstablishmentType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип заведения'
        verbose_name_plural = 'Типы заведения'


class EstablishmentQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    establishment_type = models.ForeignKey(to=EstablishmentType, on_delete=models.PROTECT)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Establishment(models.Model):
    title = models.CharField('Название заведения', max_length=255)
    city = models.CharField('Страна и город', max_length=255)
    address = models.CharField('Адрес', max_length=400)
    establishment_type = models.ForeignKey(EstablishmentType, verbose_name='Тип заведения', on_delete=models.PROTECT)
    is_new = models.BooleanField('Зто новое заведение')

    def __str__(self):
        return self.title

    def get_responses(self):
        return ClientResponse.objects.filter(establishment=self)

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'


class ClientResponse(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    question = models.ForeignKey(EstablishmentQuestion, on_delete=models.CASCADE)
    response_text = models.TextField()

    def __str__(self):
        return f"{self.establishment} -> {self.question}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'