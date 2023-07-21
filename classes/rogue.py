rogue = {
    "HP": {
        "BASE": 80,
        "GROWTH": 1.4,
    },
    "MP": {
        "BASE": 60,
        "GROWTH": 1.0,
    },
    "DEF": {
        "BASE": 12,
        "GROWTH": 1.3,
    },
    "ATK": {
        "BASE": 12,
        "GROWTH": 1.6,
    },
    "SKILLS": {
        "Backstab": {
            "LEVEL": 1,
            "MP": 0,
            "DMG": 30,
            "CD": 0,
            "DESC": "A swift and precise strike that deals %d damage.",
            "GROWTH": 1.4,
            "target": 1
        },
        "Stealth": {
            "LEVEL": 5,
            "MP": 10,
            "DMG": 0,
            "CD": 1,
            "DESC": "Enters stealth mode, gaining increased evasion for the next turn.",
        },
        "Poison Dagger": {
            "LEVEL": 10,
            "MP": 20,
            "DMG": 20,
            "CD": 2,
            "DESC": "Coats the dagger with a poisonous substance, dealing %d damage to the target over time.",
            "GROWTH": 1.3,
            "target": 1
        },
        "Eviscerate": {
            "LEVEL": 15,
            "MP": 30,
            "DMG": 45,
            "CD": 2,
            "DESC": "Unleashes a powerful strike that deals %d damage.",
            "GROWTH": 1.5,
            "target": 1
        },
        "Shadow Dance": {
            "LEVEL": 20,
            "MP": 40,
            "DMG": 0,
            "CD": 3,
            "DESC": "Performs a dance of shadows, increasing evasion and critical hit chance for the next turn.",
        },
    } 
}
