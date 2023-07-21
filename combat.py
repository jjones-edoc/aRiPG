from entity import Entity, Effect, Spell
import random

class Combat:
    def __init__(self, entities):
        self.entities = entities

    def user_turn(self):
        for entity in self.entities:
            if entity.is_alive() and entity.friendly:
                print(f"{entity.name}'s turn:")
                self.show_actions(entity)

    def enemy_turn(self):
        for entity in self.entities:
            if entity.is_alive() and not entity.friendly:
                # Choose a random spell from the entity's available spells
                spell = random.choice(entity.available_spells())
                entity.cast_spell(spell.name, self.entities)

    def show_actions(self, entity):
        available_spells = entity.available_spells()
        print("Choose an action:")
        for i, spell in enumerate(available_spells, 1):
            print(f"{i}. Cast {spell.name}")

        action = int(input()) - 1

        if action >= 0 and action < len(available_spells):
            spell = available_spells[action]
            entity.cast_spell(spell.name, self.entities)
            

    def turn(self):
        # see if all enemies or any ally is alive
        stop = True
        for entity in self.entities:
            entity.start_turn()
            if entity.friendly and not entity.is_alive():
                print("You lost!")
                break
            elif not entity.friendly and entity.is_alive():
                stop = False
        if stop:
            print("You won!")
            return False        

        self.user_turn()
        self.enemy_turn()            

        return True

    def start(self):
        print("Starting battle!")
        while self.turn():
            pass
        print("Battle ended!")

