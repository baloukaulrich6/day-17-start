""" Nous devons avoir un attribut text(pour les questions) et un attribut answer(pour les reponses) les deux attributs doivent toujour etre initialiser avec une valeur """
class Question:
    def __init__(self, text, answer):
        self.question = text
        self.reponse = answer


""" Dans cette seconde partie on va crée une banque de question"""