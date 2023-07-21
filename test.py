from entity import Entity, Effect, Spell
from combat import Combat

# create a mage and warrior
mage = Entity(100, 200, 10, 5, "Mage", "mage", "A mage", friendly=True)
warrior = Entity(200, 0, 10, 10, "Warrior", "warrior", "A warrior", friendly=True)
# give them a couple spells each
mage.learn_spell(Spell("Fireball", "A fireball", 3, effects=[Effect("Fireball", "A fireball", hp_modifier=-30), Effect("Mana Cost", "Mana cost", mp_modifier=-5, spell_target="self")]))
mage.learn_spell(Spell("Frost Nova", "A frost nova", 3, effects=[Effect("Frost Nova", "A frost nova", hp_modifier=-20, def_modifier=-2, spell_target="enemies"), Effect("Mana Cost", "Mana cost", mp_modifier=-5, spell_target="self")]))
warrior.learn_spell(Spell("Slash", "A slash", 3, effects=[Effect("Slash", "A slash", hp_modifier=-30)]))
warrior.learn_spell(Spell("Roar", "A roar", 3, effects=[Effect("Roar", "A roar", atk_modifier=20, duration=3, spell_target="allies")]))

#create a couple enemies
warlock = Entity(100, 200, 10, 5, "Warlock", "warlock", "A warlock")
skeleton = Entity(200, 0, 10, 10, "Skeleton", "skeleton", "A skeleton")
warlock.learn_spell(Spell("Dark Bolt", "A dark bolt", 3, effects=[Effect("Dark Bolt", "A dark bolt", hp_modifier=-30)]))
skeleton.learn_spell(Spell("Slash", "A slash", 3, effects=[Effect("Slash", "A slash", hp_modifier=-30)]))

# Start the combat
combat = Combat([mage, warrior, warlock, skeleton])
combat.start()
