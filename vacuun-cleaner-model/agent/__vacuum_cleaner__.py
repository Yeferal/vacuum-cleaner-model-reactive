
# estados: limpio, sucio, derecha, izquierda
# percepciones: limpio, sucio, derecha, izquierda
class VacuumCleaner:
    def __init__(self):
        self.rules = {
            'limpio': "nada",
            'sucio': "limpiar",
            'derecha': "mover-derecha",
            'izquierda': "mover-izquierda"
        }
        self.actions = {
            'nada': 'cuadro-limpio',
            'limpiar': 'limpiar-cuadro',
            'mover-derecha': 'mover-derecha-esperar',
            'mover-izquierda': 'mover-izquierda-esperar'
        }
        self.model = {
            ("limpio", "nada", "derecha"): "derecha",
            ("limpio", "nada", "izquierda"): "izquierda",
            ("limpio", "nada", "sucio"): "sucio",
            ("limpio", "nada", "limpio"): "limpio",
            ("sucio", "limpiar", "sucio"): "limpio",
            ("sucio", "limpiar", "sucio"): "limpio",
            ("derecha", "mover-izquierda", "izquierda"): "izquierda",
            ("derecha", "mover-derecha", "izquierda"): "izquierda",
            ("derecha", "mover-derecha", "sucio"): "sucio",
            ("izquierda", "mover-izquierda", "derecha"): "derecha",
            ("izquierda", "mover-izquierda", "sucio"): "sucio",
            ("izquierda", "mover-derecha", "derecha"): "derecha"
        }


    def update_state(self, state, action, perception):
        print("========================")
        print(F"({state}, {action}, {perception}) : {self.model.get((state, action, perception), None)}")
        print("========================")
        if self.model.get((state, action, perception), None):
            return self.model.get((state, action, perception), None)
        else:
            return "limpio"

    def getRule(self, state):
        return self.rules[state]

    def rule_action(self, perception, state):
        if perception in self.rules:
            return self.rules[perception]
        else:
            return self.rules["limpio"]

