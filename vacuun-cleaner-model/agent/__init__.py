import threading
import time
import random
from agent.__vacuum_cleaner__ import VacuumCleaner

# sqrRight = False;
# sqrLeft = True;
# sqrVacuum = random.choice(["Derecha","Izquierda"])



def main():
    # global perception
    state = 'limpio'
    action = 'nada'
    perception = None
    machine = VacuumCleaner()
    while True:
        try:
            print("Ingrese percepcion")
            perception = input()

            state = machine.update_state(state, action, perception)
            rule = machine.getRule(state)
            action = rule
            # Imprimer resultado
            txtAction = machine.actions.get(action)
            print(txtAction)
            print("")
            time.sleep(2)
        except KeyboardInterrupt:
            print("")


main()