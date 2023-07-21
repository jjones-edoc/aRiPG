mage = {
    "HP": {
        "BASE": 80,
        "GROWTH": 1.2,
    },
    "MP": {
        "BASE": 100,
        "GROWTH": 1.5,
    },
    "DEF": {
        "BASE": 10,
        "GROWTH": 1.2,
    },
    "ATK": {
        "BASE": 10,
        "GROWTH": 1.1,
    },
    "SPELLS": {
        "Fireball": {
            "LEVEL": 1,
            "MP": 10,
            "DMG": 20,
            "CD": 0,
            "DESC": "A fireball that deals %d damage.",
            "GROWTH": 1.5,
            "target": 1
        },
        "Cones of Cold": {
            "LEVEL": 5,
            "MP": 10,
            "DMG": 10,
            "CD": 1,
            "DESC": "A cone of cold that deals %d damage to all enemies.",
            "GROWTH": 1.5,
            "target": 5
        },
        "Invisibility": {
            "LEVEL": 10,
            "MP": 10,
            "DMG": 0,
            "CD": 3,
            "DESC": "Make target invisible next turn.",
        },
        "Lightning Bolt": {
            "LEVEL": 15,
            "MP": 20,
            "DMG": 50,
            "CD": 3,
            "DESC": "A lightning bolt that deals %d damage.",
            "GROWTH": 1.5,
            "target": 1
        },
        "Meteor": {
            "LEVEL": 20,
            "MP": 30,
            "DMG": 100,
            "CD": 5,
            "DESC": "A meteor that deals %d damage.",
            "GROWTH": 1.5,
            "target": 5
        },
    } 
}
