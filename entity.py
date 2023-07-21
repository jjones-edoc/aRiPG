from dataclasses import dataclass, field
import random

@dataclass
class Effect:
    name: str
    description: str
    hp_modifier: int = 0
    mp_modifier: int = 0
    atk_modifier: int = 0
    def_modifier: int = 0
    duration: int = 0
    shield_value: int = 0
    can_attack: bool = True
    spell_target: str = "enemy"  # "self", "ally", "enemy", "enemies", "allies", "all"

@dataclass
class Equipment:
    name: str
    description: str
    hp_modifier: int = 0
    mp_modifier: int = 0
    atk_modifier: int = 0
    def_modifier: int = 0
    effects: list = field(default_factory=list)

@dataclass
class Spell:
    name: str
    description: str
    max_cooldown: int = 0
    current_cooldown: int = 0    
    effects: list = field(default_factory=list) # if a spell cost mana add an effect that reduces mana with target of self

@dataclass
class Entity:
    max_hp: int
    max_mp: int
    base_atk: int
    base_def: int
    name: str
    role: str
    description: str
    friendly: bool = False
    current_hp: int = field(init=False)
    current_mp: int = field(init=False)
    current_atk: int = field(init=False)
    current_def: int = field(init=False)
    current_exp: int = field(init=False)
    can_attack: bool = True
    shield_value: int = 0
    equipment: list = field(default_factory=list)
    effects: list = field(default_factory=list)
    level: int = 1
    experience_until_next_level: int = 100
    spells: list = field(default_factory=list)

    def __post_init__(self):
        self.current_hp = self.max_hp
        self.current_mp = self.max_mp
        self.current_atk = self.base_atk
        self.current_def = self.base_def
        self.learn_spell(Spell("Basic Attack", "A basic attack", effects=[Effect("Basic Attack", "A basic attack", hp_modifier=-self.current_atk, spell_target="enemy")]))
        
    def print_stats(self):
        print(f"{self.name} ({self.role})")
        print(f"Level: {self.level}")
        print(f"HP: {self.current_hp}/{self.max_hp}")
        print(f"MP: {self.current_mp}/{self.max_mp}")
        print(f"ATK: {self.current_atk}")
        print(f"DEF: {self.current_def}")
        print(f"Spells: {self.spells}")
        print("")

    def add_equipment(self, equipment):
        self.equipment.append(equipment)
        self.apply_equipment_stats(equipment)
        self.effects.extend(equipment.effects)

    def remove_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)
            self.remove_equipment_stats(equipment)
            self.remove_equipment_effects(equipment)

    def apply_equipment_stats(self, equipment):
        self.max_hp += equipment.hp_modifier
        self.max_mp += equipment.mp_modifier
        self.base_atk += equipment.atk_modifier
        self.base_def += equipment.def_modifier
        self.current_hp = min(self.current_hp + equipment.hp_modifier, self.max_hp)
        self.current_mp = min(self.current_mp + equipment.mp_modifier, self.max_mp)

    def remove_equipment_stats(self, equipment):
        self.max_hp -= equipment.hp_modifier
        self.max_mp -= equipment.mp_modifier
        self.base_atk -= equipment.atk_modifier
        self.base_def -= equipment.def_modifier
        self.current_hp = min(self.current_hp, self.max_hp)
        self.current_mp = min(self.current_mp, self.max_mp)

    def remove_equipment_effects(self, equipment):
        self.effects = [effect for effect in self.effects if effect not in equipment.effects]

    def apply_effect(self, effect):
        print(f"{self.name} is affected by {effect.name}")
        if effect.shield_value > self.shield_value:
            self.shield_value = effect.shield_value
        
        # if the effect is a negative hp_modifier, then absorb the damage with the shield and defence
        if effect.hp_modifier < 0:
            damage = abs(effect.hp_modifier) - self.shield_value - self.current_def
            if damage > 0:
                self.current_hp -= damage
                self.shield_value = 0
            else:
                self.shield_value -= abs(effect.hp_modifier)
            
        self.current_mp = max(min(self.current_mp + effect.mp_modifier, self.max_mp), 0)
        self.current_atk += effect.atk_modifier
        self.current_def += effect.def_modifier
        if effect.duration != 99:
            effect.duration -= 1

    def is_alive(self):
        return self.current_hp > 0
    
    def cast_spell(self, spell_name, targets):
        enemies = []
        allies = []
        for target in targets:
            if target.friendly == self.friendly:
                if target.name != self.name:
                    allies.append(target)
            else:
                enemies.append(target)   
        print(f"{self.name} casts {spell_name}")
        
        for spell in self.spells:
            if spell.name == spell_name:
                for effect in spell.effects:
                    if effect.spell_target == "all":
                        for target in targets:
                            target.apply_effect(effect)    
                    elif effect.spell_target == "enemies":
                        for enemy in enemies:
                            enemy.apply_effect(effect)
                    elif effect.spell_target == "ally":
                        random.choice(allies).apply_effect(effect)
                    elif effect.spell_target == "allies":
                        for ally in allies:
                            ally.apply_effect(effect)
                    elif effect.spell_target == "self":
                        self.apply_effect(effect)
                    else:
                        random.choice(enemies).apply_effect(effect)    
                spell.current_cooldown = spell.max_cooldown
                break                           
    
    def available_spells(self):
        available_spells = []
        if not self.can_attack:
            return available_spells
        for spell in self.spells:
            can_cast = True
            if spell.current_cooldown == 0:
                for effect in spell.effects:
                    if effect.spell_target == "self":
                        if effect.mp_modifier < 0:
                            if self.current_mp <= abs(effect.mp_modifier):
                                can_cast = False
            else:
                can_cast = False
            if can_cast:
                available_spells.append(spell)
        return available_spells           
    
    def add_exp(self, exp): 
        self.current_exp += exp
        if self.current_exp >= self.experience_until_next_level:
            self.current_exp -= self.experience_until_next_level
            self.experience_until_next_level = int(self.experience_until_next_level * 1.5)
            return True
        return False    

    def start_turn(self):
        effects_to_remove = []
        # handle spell cooldowns
        for spell in self.spells:
            if spell.current_cooldown > 0:
                spell.current_cooldown -= 1

        can_attack_this_turn = True

        self.shield_value = 0
        self.current_atk = self.base_atk
        self.current_def = self.base_def

        for effect in self.effects:
            if not effect.can_attack:
                can_attack_this_turn = False

            self.apply_effect(effect)

            if effect.duration <= 0:
                effects_to_remove.append(effect)

        for effect in effects_to_remove:
            self.effects.remove(effect)

        self.can_attack = can_attack_this_turn
        self.print_stats()

    def level_up(self, HP = 0, MP = 0, ATK = 0, DEF = 0):
        self.level += 1
        self.max_hp += HP
        self.max_mp += MP
        self.base_atk += ATK
        self.base_def += DEF

    def learn_spell(self, spell):
        self.spells.append(spell)

