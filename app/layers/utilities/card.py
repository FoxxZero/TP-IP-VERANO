class Card:
    def __init__(self, name, gender, house, alternate_names, actor, image, user=None, id=None):
        self.name = name  # Nombre del personaje
        self.gender = gender  # Género
        self.house = house  # Casa
        self.alternate_names = alternate_names # nombres alternativos
        self.actor = actor  # Actor
        self.image = image  # URL de la imagen
        
        self.user = user  # Usuario asociado (si corresponde)
        self.id = id  # ID único (si corresponde)

    def __str__(self):
        return (f'name: {self.name}, gender: {self.gender}, house: {self.house}, '
                f'actor: {self.actor}, image: {self.image}, user: {self.user}, id: {self.id}')

    # Método equals.
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return (self.name, self.gender, self.house, self.actor) == \
               (other.name, other.gender, other.house, other.actor)

    # Método hashCode.
    def __hash__(self):
        return hash((self.name, self.gender, self.house, self.actor))
