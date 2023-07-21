warrior = {
    "HP": {
        "BASE": 100,
        "GROWTH": 1.8,
    },
    "MP": {
        "BASE": 20,
        "GROWTH": 0.5,
    },
    "DEF": {
        "BASE": 15,
        "GROWTH": 1.5,
    },
    "ATK": {
        "BASE": 15,
        "GROWTH": 1.8,
    },
    "SKILLS": {
        "Slash": {
            "LEVEL": 1,
            "MP": 0,
            "DMG": 20,
            "CD": 0,
            "DESC": "A basic slash that deals %d damage.",
            "GROWTH": 1.2,
            "target": 1
        },
        "Power Strike": {
            "LEVEL": 5,
            "MP": 10,
            "DMG": 40,
            "CD": 1,
            "DESC": "A powerful strike that deals %d damage.",
            "GROWTH": 1.3,
            "target": 1
        },
        "Rampage": {
            "LEVEL": 10,
            "MP": 20,
            "DMG": 30,
            "CD": 2,
            "DESC": "Unleashes a series of quick strikes that deal %d damage.",
            "GROWTH": 1.4,
            "target": 1
        },
        "Berserk": {
            "LEVEL": 15,
            "MP": 30,
            "DMG": 0,
            "CD": 3,
            "DESC": "Enters a berserk state, increasing attack damage for the next turn.",
        },
        "Whirlwind": {
            "LEVEL": 20,
            "MP": 40,
            "DMG": 60,
            "CD": 4,
            "DESC": "Performs a whirlwind attack that deals %d damage to all enemies.",
            "GROWTH": 1.5,
            "target": 5
        },
    } 
}
