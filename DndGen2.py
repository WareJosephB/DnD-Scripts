from random import randint
from math import floor, ceil


def d(N):
    return randint(1, N) - 1  # Makes dice work with 0-indexed arrays

Level = 1  # This should be the only thing you change.

Lev = 2 #d(Level)+1  # d(Level) + 1  # Level = Any level up to 'max level' defined above

Proficiency = ceil(Lev/4.0)+1

if Lev > 15:
    Drag = 5
elif Lev > 10:
    Drag = 4
elif Lev > 5:
    Drag = 3
else:
    Drag = 2

Stat = []
Skills = []
Features = []

N = 0
while N < 6:  # Generates 4d6d1 in order
    Stats = []
    Stats.append(d(6) + 1)
    Stats.append(d(6) + 1)
    Stats.append(d(6) + 1)
    Stats.append(d(6) + 1)
    Min = min(Stats)
    Max = Stats[0] + Stats[1] + Stats[2] + Stats[3]
    Stat.append(Max - Min)
    N = N + 1

Races = ["Aasimar", "Aarakocra", "Bugbear", "Dragonborn", "Dwarf", "Elf",
         "Firbolg", "Genasi", "Gnome", "Goblin", "Goliath", "Half-Elf",
         "Halfling", "Half-Orc", "Hobgoblin", "Human", "Kenku", "Kobold",
         "Lizardfolk", "Orc", "Tabaxi", "Tiefling", "Tortle", "Triton",
         "Yuan-Ti"]

Raceskills = [[], [], ["Stealth"], [], [], ["Perception"], [], [], [], [],
              ["Athletics"],[], [], ["Intimidation"],[], []]

Skillians = [0,0,0,0,0,0,0,0,0,0,0,1]
             

#Racetools = []
'''
LangRaces = [["Common", "Celestial"], ["Common", "Aaracokra", "Auran"],
             ["Common", "Goblin"], ["Common", "Draconic"],
             ["Common", "Dwarvish"], ["Common", "Elvish"],
             ["Common", "Elvish", "Giant"], ["Common"],
             ["Common", "Gnomish"], ["Common", "Goblin"], ["Common", "Giant"],
             ["Common", "Elvish"], ["Common", "Halfling"],
             ["Common", "Orcish"], ["Common", "Goblin"], ["Common"],
             ["Common", "Auran"], ["Common", "Draconic"],
             ["Common", "Draconic"], ["Common", "Orcish"], ["Common"],
             ["Common"], ["Common", "Aquan"], ["Common", "Aquan"],
             ["Common", "Abyssal", "Draconic"]]
Longs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0,
         0, 0]

 f '''

Langs = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin",
         "Halfling", "Orcish", "Abyssal", "Celestial", "Deep Speech",
         "Draconic", "Infernal", "Aquan", "Auran", "Ignan",
         "Terran", "Sylvan", "Undercommon", "Druidic", "Thieves' Cant",
         "Aaracokra", "Blink Dog", "Bullywug", "Giant Eagle", "Giant Elk",
         "Giant Owl", "Gith", "Gnoll", "Grell", "Grung", "Hook Horror",
         "Modron", "Otyugh", "Sahuagin", "Slaad", "Sphinx", "Thri-kreen",
         "Tlincalli", "Troglodyte", "Umber Hulk", "Vegepygmy", "Winter Wolf",
         "Worg", "Yeti"]

Subraces = [["DMG", "Protector", "Scourge", "Fallen"], [], [],
            ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green",
             "Red", "Silver", "White"], ["Duergar", "Hill", "Mountain"],
            ["Drow", "Eladrin", "High", "Wood"], [],
            ["Air", "Earth", "Fire", "Water"], ["Deep", "Forest", "Rock"],
            [], [], ["PHB", "Wood", "Moon", "Drow", "Aquatic"],
            ["Ghostwise", "Lightfoot", "Stout"], [], [],
            ["Regular", "Variant"], [], [], [], [], [], ["PHB", "SCAG"], [],
            [], []]

# Sub-sub races
Wood = ["(Elf Weapon Training) Wood", "(Fleet of Foot) Wood",
        "(Mask of the Wild) Wood"]
Moon = ["(Elf Weapon Training) High", "(Cantrip) High"]
SCAG = ["(Devil's Tongue)", "(Hellfire)", "(Winged)"]

Backgrounds = ["Acolyte", "Anthropologist", "Archeologist", "Bounty Hunter",
               "Charlatan", "City Watch", "Clan Crafter", "Cloistered Scholar",
               "Courtier", "Criminal", "Entertainer", "Faction Agent",
               "Far Traveller", "Folk Hero", "Guild Artisan", "Haunted One",
               "Hermit", "Inheritor", "Knight of the Order",
               "Mercenary Veteran", "Noble", "Outlander", "Sage", "Sailor",
               "Soldier", "Urchin", "Urthgart Tribe Member",
               "Waterdhavian Noble"]

Langgrounds = [2,2,1,0,0,2,1,2,2,0,0,2,1,0,1,1,1,0,1,0,1,1,2,0,0,0,1,1]


Classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
           "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]

Subclasses = [["Ancestral Guardian", "Battlerager", "Beserker", "Storm Herald",
               "Totem Warrior", "Zealot"],
              ["Glamour", "Lore", "Swords", "Valour", "Whispers"],
              ["Arcana", "Death", "Forge", "Grave", "Knowledge", "Life",
               "Light", "Nature", "Tempest", "Trickery", "War"],
              ["Dreams", "Land", "Moon", "Shepherd"],
              ["Arcane Archer", "Battle Master", "Cavalier", "Champion",
               "Eldritch Knight", "Purple Dragon Knight", "Samurai"],
              ["Drunken Master", "Four Elements", "Kensei", "Long Death",
               "Open Hand", "Shadow", "Sun Soul"],
              ["Ancients", "Crown", "Conquest", "Devotion", "Oathbreaker",
               "Redemption", "Vegeance"],
              ["Beast Master", "Gloom Stalker", "Horizon Walker", "Hunter",
               "Monster Slayer"],
              ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind",
               "Scout", "Swashbuckler", "Thief"],
              ["Divine Soul", "Draconic", "Shadow", "Storm", "Wild Magic"],
              ["Archfey", "Celestial", "Fiend", "Great Old One", "Hexblade",
               "Undying"],
              ["Abjuration", "Bladesinger", "Conjuration", "Divination",
               "Enchantment", "Evocation", "Illusion", "Necromancy",
               "Transmutation", "War Magic"]]

# Sub-sub classes
Storm = ["Desert", "Sea", "Tundra"]
Totem = ["Bear", "Elk", "Hawk", "Tiger", "Wolf"]

SwordFS = ["Dueling", "Two Weapon Fighting"]

FS = ["Archery", "Defence", "Dueling", "Great Weapon Fighting",
      "Protection", "Two-Weapon Fighting"]
Man = ["Commander's Strike", "Disarming Attack", "Distracting Strike",
       "Evasive Footwork", "Feinting Attack", "Goading Attack",
       "Lunging Attack", "Manuevering Attack", "Menacing Attack", "Parry",
       "Precision Attack", "Pushing Attack", "Rally", "Riposte",
       "Sweeping Attack", "Trip Attack"]
AA = ["Banishing", "Beguiling", "Bursting", "Enfeebling", "Grasping",
      "Piercing", "Seeking", "Shadow"]

KWm = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer",
       "Mace", "Quarterstaff", "Sickle", "Spear", "Battleaxe", "Flail",
       "Longsword", "Morningstar", "Rapier", "Scimitar", "Shortsword",
       "Trident", "Warpick", "Warhammer", "Whip"]
KWr = ["Crossbow (light)", "Dart", "Shortbow", "Sling", "Blowgun",
       "Crossbow (hand)", "Longbow"]
KW = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer",
      "Mace", "Quarterstaff", "Sickle", "Spear", "Battleaxe", "Flail",
      "Longsword", "Morningstar", "Rapier", "Scimitar", "Shortsword",
      "Trident", "Warpick", "Warhammer", "Whip", "Crossbow (light)", "Dart",
      "Shortbow", "Sling", "Blowgun", "Crossbow (hand)", "Longbow"]

FE3 = ["Fire Snake, ", "Four Thunders, ", "Unbroken Air, ", "Gale Spirits, ",
       "Flowing River, ", "Cinder Strike, ", "Water Whip, "]
FE6 = ["Fire Snake, ", "Four Thunders, ", "Unbroken Air, ", "Gale Spirits, ",
       "Flowing River, ", "Cinder Strike, ", "Water Whip, ", "North Wind, ",
       "Summit, "]
FE11 = ["Fire Snake, ", "Four Thunders, ", "Unbroken Air, ", "Gale Spirits, ",
        "Flowing River, ", "Cinder Strike, ", "Water Whip, ", "North Wind, ",
        "Summit, ", "Phoenix, ", "Mist, ", "Wind, "]
FE17 = ["Fire Snake, ", "Four Thunders, ", "Unbroken Air, ", "Gale Spirits, ",
        "Flowing River, ", "Cinder Strike, ", "Water Whip, ", "North Wind, ",
        "Summit, ", "Phoenix, ", "Mist, ", "Wind, ", "Winter, ", "Defence, ",
        "Hungry Flame, ", "Rolling Earth, "]

PFS = ["Defence", "Dueling", "Great Weapon Fighting", "Protection"]

FT = ["Arctic", "Coast", "Desert", "Forest", "Grassland", "Mountain", "Swamp",
      "Underdark"]
RFS = ["Archery", "Defence", "Dueling", "Two Weapon Fighting"]

MM = ["Careful", "Distant", "Empowered", "Extended", "Heightened", "Quickened",
      "Subtle", "Twinned"]
DA = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red",
      "Silver", "White"]

PW = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer",
      "Mace", "Quarterstaff", "Sickle", "Spear", "Battleaxe", "Flail",
      "Longsword", "Morningstar", "Rapier", "Scimitar", "Shortsword",
      "Trident", "Warpick", "Warhammer", "Whip", "Glaive", "Greataxe",
      "Greatsword", "Halberd", "Lance", "Maul", "Pike"]

Fam = ["Bat", "Cat", "Crab", "Frog", "Hawk", "Lizard", "Octopus", "Owl",
       "Poisonous Snake", "Quipper", "Rat", "Raven", "Seahorse", "Spider",
       "Weasel", "Imp", "Quasit", "Sprite", "Psuedodragon"]

Align = ["Good", "Neutral", "Evil"]
Blign = ["Lawful", "Neutral", "Chaotic"]
F = d(3)
G = d(2)
if F == G == 1:
    Ment = "True Neutral"
else:
    Ment = Blign[G]+" "+Align[F]

A = 18 #d(25)
'''Lang = LangRaces[A]
Long = Longs[A]
Skill = Raceskills[A]
Skig = Skillians[A]
if Races[A] == "Tiefling":
    Lang.append(["Abyssal", "Infernal"][d(2)])'''
if Subraces[A] != []:
    B = d(len(Subraces[A]))
    Subrace = Subraces[A][B] + "-"
    Race = Races[A]
    '''lang = LangRaces[A]
    if Subrace == "Deep-" or Subrace == "Duergar":
        Lang.append("Undercommon")
if Races[A] == "Genasi":
    Lang.append(["Auran", "Terran", "Ignan", "Aquan"][B])'''
else:
    B = 0
    Subrace = '' 
    Race = Races[A]
    
'''if Races[A] == "Human" and Subraces[B] == "Variant":
    Skig = Skig + 1'''
if Subrace == "SCAG-":
    Subrace = SCAG[d(3)]+" Feral-"
if Subrace == "Wood-" and Race == "Half-Elf":
    Subrace = Wood[d(3)]
if Subrace == "Moon-":
    Subrace = Moon[d(2)]

C = d(28)
Background = Backgrounds[C]

D = 7 #d(12)
Class = Classes[D]
'''if Class == "Druid":
    Lang.append("Druidic")
elif Class == "Rogue":
    Lang.append("Thieves' Cant")'''


if D == 0:
    HDice = 12
elif D == 4 or D == 6 or D == 7:
    HDice = 10
elif D == 11 or D == 9:
    HDice = 6
else:
    HDice = 8

if D == 7:
    Q = d(2)
    Class = ["PHB Ranger", "Revised Ranger"][Q]

E = d(len(Subclasses[D]))

if Lev > 2:
    Subclass = Subclasses[D][E]
elif Lev > 1 and (D == 3 or D == 11):
    Subclass = Subclasses[D][E]
elif D == 2 or D == 9 or D == 10:
    Subclass = Subclasses[D][E]
else:
    Subclass = ''

if D == 0 and E == 3 and Lev > 2:
    Subclass = Subclass + ": " + Storm[d(3)]  # Storm Barb
elif D == 0 and E == 4 and Lev > 2:
    Subclass = Subclass + ": " + Totem[d(5)]  # Totem Barb
    if Lev > 5:
        Subclass = Subclass + ", " + Totem[d(5)]
    if Lev > 13:
        Subclass = Subclass + ", " + Totem[d(5)]
elif D == 1 and E == 2 and Lev > 2:
    Subclass = Subclass + "; Fighting Style: " + SwordFS[d(2)]
elif D == 3:
    Subclass = Subclass + "; Home Terrain: " + [
     "Arctic", "Desert", "Forest", "Grassland", "Hill", "Mountain", "Swamp",
     "Underdark", "Underwater"][d(9)]
    if Lev > 1 and E == 1:
        Subclass = Subclass + "; Circle: " + [
         "Arctic", "Desert", "Forest", "Grassland", "Mountain", "Swamp",
         "Underdark", "Coastal"][d(8)]
elif D == 4:
    if E == 3 and Lev > 9:
        One = d(6)
        Two = d(6)
        while One == Two:
            Two = d(6)
        Subclass = Subclass + "; Fighting Styles: " + FS[One] + ", " + FS[Two]
    else:
        Subclass = Subclass + "; Fighting Style: " + FS[d(6)]
    if E == 1:
        if Lev > 14:
            Num = 9
        elif Lev > 9:
            Num = 7
        elif Lev > 6:
            Num = 5
        elif Lev > 2:
            Num = 3
        else:
            Num = 0
        N = 0
        M = []
        QUE = "; Manuevers: "
        while N < Num:
            Yurt = d(16)
            while Yurt in M:
                Yurt = d(16)
            M.append(Yurt)
            QUE = QUE + Man[Yurt]
            N += 1
            if N != Num:
                QUE = QUE + ", "
        Subclass = Subclass + QUE
    if E == 0:
        if Lev > 17:
            Num = 6
        elif Lev > 14:
            Num = 5
        elif Lev > 9:
            Num = 4
        elif Lev > 6:
            Num = 3
        elif Lev > 2:
            Num = 2
        else:
            Num = 0
        N = 0
        M = []
        QUE = "; Arcane Shots: "
        while N < Num:
            Yurt = d(8)
            while Yurt in M:
                Yurt = d(8)
            M.append(Yurt)
            QUE = QUE + AA[Yurt]
            N += 1
            if N != Num:
                QUE = QUE + ", "
        Subclass = Subclass + QUE
elif D == 5:
    if E == 1:
        Th = Si = El = Se = 0
        M = []
        QUE = "; Elemental Disciplines known: Elemental Attunement, "
        if Lev > 16:
            Three = 0
            Six = 0
            Eleven = 2
            Seventeen = 2
        elif Lev > 10:
            Three = Seventeen = 0
            Eleven = 2
            Six = 1
        elif Lev > 5:
            Three = Seventeen = Eleven = 0
            Six = 2
        elif Lev > 3:
            Three = 0
            Six = Eleven = Seventeen = 0
        else:
            Three = Six = Eleven = Seventeen = 0
            QUE = ", "
        while Th < Three:
            Yurt = d(7)
            while Yurt in M:
                Yurt = d(7)
            M.append(Yurt)
            QUE = QUE + FE3[Yurt]
            Th = Th+1
        while Si < Six:
            Yurt = d(9)
            while Yurt in M:
                Yurt = d(9)
            M.append(Yurt)
            QUE = QUE + FE6[Yurt]
            Si = Si + 1
        while El < Eleven:
            Yurt = d(12)
            while Yurt in M:
                Yurt = d(12)
            M.append(Yurt)
            QUE = QUE + FE11[Yurt]
            El = El + 1
        while Se < Seventeen:
            Yurt = d(16)
            while Yurt in M:
                Yurt = d(12)
            M.append(Yurt)
            QUE = QUE + FE17[Yurt]
            Se = Se + 1
        QUE = QUE[:-2]
        Subclass = Subclass + QUE
    if E == 2:
        QUE = "; Weapons: "
        M = []
        N = 0
        if Lev > 16:
            Num = 3
        elif Lev > 10:
            Num = 2
        elif Lev > 5:
            Num = 1
        if Lev > 2:
            NumR = d(7)
            NumM = d(21)
            QUE = QUE + KWr[NumR]+", "
            QUE = QUE + KWm[NumM]+", "
            M.append(NumM)
            M.append(NumR+21)
            N = 0
            while N < Num:
                Yurt = d(28)
                while Yurt in M:
                    Yurt = d(28)
                QUE = QUE + KW[Yurt] + ", "
                M.append(Yurt)
                N = N + 1
            QUE = QUE[:-2]
            Subclass = Subclass + QUE
elif D == 6 and Lev > 1:
    Subclass = Subclass + "; Fighting Style: " + PFS[d(4)]
elif D == 7:
    if Q == 0:
        Subclass = Subclass + "; Favoured terrain: "+FT[d(8)]
        if Lev < 3:
            Subclass = Subclass[2:]
        M = []
        FE = ['Aberations', 'Beasts', 'Celestials', 'Constructs', 'Dragons',
              'Fey', 'Fiends', 'Giants', 'Monstrosities', 'Oozes', 'Plants',
              'Undead', 'Humanoids']
        FEH = ['Dwarf', 'Elf', 'Gnoll', 'Gnome', 'Goblinoid', 'Grimlock',
               'Human', 'Kobold', 'Lizardfolk', 'Merfolk', 'Orc', 'Sahuagin',
               'Xvart', 'Aarakocra', 'Bullywug', 'Grung', 'Kenku', 'Kuo-Toa',
               'Troglodyte', 'Firenewt', 'Thri-Kreen', 'Gith', 'Quaggoth',
               'Yuan-Ti']
        One = d(13)
        if One == 12:
            One_one = d(24)
            M.append(One_one)
            One_two = d(24)
            while One_one == One_two:
                One_two = d(24)
            M.append(One_two)
            Subclass = Subclass + "; Favoured enemies: "+FEH[One_one]+", "+FEH[
                    One_two]
        else:
            Subclass = Subclass + "; Favoured enemies: "+FE[One]
        if Lev > 5:
            Two = d(13)
            while Two == One and Two != 12:
                Two = d(13)
            if Two == 12:
                Two_one = d(24)
                while Two_one in M:
                    Two_one = d(24)
                Two_two = d(24)
                while Two_two in M:
                    Two_two = d(24)
                Subclass = Subclass + ", " + FEH[Two_one] + ", " + FEH[Two_two]
            else:
                Subclass = Subclass + ", " + FE[Two]
        if Lev > 13:
            Three = d(13)
            while (Three == One or Three == Two) and Three != 12:
                Three = d(13)
            if Three == 12:
                Three_one = d(24)
                while Three_one in M:
                    Three_one = d(24)
                M.append(Three_one)
                Three_two = d(24)
                while Three_two in M:
                    Three_two = d(24)
                M.append(Three_two)
                Subclass = Subclass + ", " + FEH[Three_one] + ", " + FEH[
                        Three_two]
            else:
                Subclass = Subclass + ", " + FE[Three]
    else:
        FE = ["Beasts", "Fey", "Humanoids", "Monstrosities", "Undead"]
        GFE = ["Aberrations", "Celestials", "Constructs", "Dragons",
               "Elementals", "Fiends", "Giants"]
        Subclass = Subclass + "; Favoured enemies: " + FE[d(5)]
        if Lev < 3:
            Subclass = Subclass[2:]
        if Lev > 5:
            Subclass = Subclass + ", " + GFE[d(7)]
    if Lev > 1:
        Subclass = Subclass + "; Fighting Style: " + RFS[d(4)]
    if E == 3:
        if Lev > 2:
            Subclass = Subclass + "; " + ["Colossus Slayer", "Giant Killer",
                                          "Horde Breaker"][d(3)]
        if Lev > 6:
            Subclass = Subclass + ", " + ["Escape the Horse",
                                          "Multiattack Defence",
                                          "Steel Will"][d(3)]
        if Lev > 10:
            Subclass = Subclass + ", " + ["Volley", "Whirlwind Attack"][d(2)]
        if Lev > 14:
            Subclass = Subclass + ", " + ["Evasion", "Stand against the Tide",
                                          "Uncanny Dodge"][d(3)]
elif D == 9:
    if E == 1:
        Subclass = Subclass + " (" + DA[d(10)]+")"
    if Lev > 16:
        Num = 4
    elif Lev > 9:
        Num = 3
    elif Lev > 2:
        Num = 2
    else:
        Num = 0
    N = 0
    M = []
    if Lev > 2:
        Subclass = Subclass + "; Metamagic options: "
    while N < Num:
        Yurt = d(8)
        while Yurt in M:
            Yurt = d(8)
        M.append(Yurt)
        Subclass = Subclass + MM[Yurt]
        N += 1
        if N < Num:
            Subclass = Subclass + ", "
elif D == 10 and Lev > 2:
    P = d(3)
    Subclass = Subclass + ["; Blade Pact", "; Chain Pact", "; Tome Pact"][P]
    if P == 0:
        Subclass = Subclass + ": " + PW[d(28)]
    elif P == 1:
        Subclass = Subclass + ": " + Fam[d(19)]

'''

def ASI(K):
    K = str(input("'Feat' or 'ASI' at level " + str(K) + "?"))
    if K == 'ASI':
        One = d(6)
        Two = d(6)
        if min(Stat) == 20:
            print "You are already flawless. Rolling a feat."
            print "Haven't got this far yet"
        else:
            while Stat[One] == 20:
                One = d(6)
            Stat[One] += 1
            while Stat[Two] == 20:
                Two = d(6)
            Stat[Two] += 1
    else:
        print "Haven't got this far yet"
'''


def ASI(K):
    One = d(6)
    Two = d(6)
    if min(Stat) == 20:
        print "You are already flawless. Rolling a feat."
        print "Haven't got this far yet"
    else:
        while Stat[One] == 20:
            One = d(6)
        Stat[One] += 1
        if min(Stat) == 20:
            print "You are already flawless."
        else:
            while Stat[Two] == 20:
                Two = d(6)
            Stat[Two] += 1

if Lev > 3:
    ASI(4)
if Lev > 5 and Class == 'Fighter':
    ASI(6)
if Lev > 7:
    ASI(8)
if Lev > 9 and Class == 'Rogue':
    ASI(10)
if Lev > 11:
    ASI(12)
if Lev > 13 and Class == 'Fighter':
    ASI(14)
if Lev > 15:
    ASI(16)
if Lev > 18:
    ASI(19)

StrMod = floor((Stat[0]-10)/2.0)
DexMod = floor((Stat[1]-10)/2.0)
ConMod = floor((Stat[2]-10)/2.0)
IntMod = floor((Stat[3]-10)/2.0)
WisMod = floor((Stat[4]-10)/2.0)
ChaMod = floor((Stat[5]-10)/2.0)

StrAtt = Proficiency + StrMod
DexAtt = Proficiency + DexMod
ConAtt = Proficiency + ConMod
IntAtt = Proficiency + IntMod
WisAtt = Proficiency + WisMod
ChaAtt = Proficiency + ChaMod

StrSav = 8 + StrAtt
DexSav = 8 + DexAtt
ConSav = 8 + ConAtt
IntSav = 8 + IntAtt
WisSav = 8 + WisAtt
ChaSav = 8 + ChaAtt

HP = HDice + floor((Stat[2]-10)/2.0)
N = 1
while N < Lev:
    HP += d(HDice) + 1 + floor((Stat[2]-10)/2.0)
    N += 1

if Subclass != "":
    Subclass = " (" + Subclass + ")"

PO = d(2)
Sexes = ["Male", "Female"]
Sex = Sexes[PO]
'''
Long = Long + Langgrounds[C]
Lon = 0
while Lon < Long:
    Qubert = Langs[d(len(Langs))]
    while Qubert in Lang:
        Qubert = Langs[d(len(Langs))]
    Lang.append(Qubert)
    Lon = Lon + 1

Languages = Lang[0]
Tick = 1
while Tick < len(Lang)-1:
    Languages = Languages + ", " + Lang[Tick]
    Tick = Tick + 1
Languages = Languages + " and " + Lang[-1]'''
malenames = ["James","John","Robert","Michael","William","David","Richard","Charles","Joseph","Thomas","Christopher","Daniel","Paul","Mark","Donald","George","Kenneth","Steven","Edward","Brian","Ronald","Anthony","Kevin","Jason","Matthew","Gary","Timothy","Jose","Larry","Jeffrey","Frank","Scott","Eric","Stephen","Andrew","Raymond","Gregory","Joshua","Jerry","Dennis","Walter","Patrick","Peter","Harold","Douglas","Henry","Carl","Arthur","Ryan","Roger","Joe","Juan","Jack","Albert","Jonathan","Justin","Terry","Gerald","Keith","Samuel","Willie","Ralph","Lawrence","Nicholas","Roy","Benjamin","Bruce","Brandon","Adam","Harry","Fred","Wayne","Billy","Steve","Louis","Jeremy","Aaron","Randy","Howard","Eugene","Carlos","Russell","Bobby","Victor","Martin","Ernest","Phillip","Todd","Jesse","Craig","Alan","Shawn","Clarence","Sean","Philip","Chris","Johnny","Earl","Jimmy","Antonio","Danny","Bryan","Tony","Luis","Mike","Stanley","Leonard","Nathan","Dale","Manuel","Rodney","Curtis","Norman","Allen","Marvin","Vincent","Glenn","Jeffery","Travis","Jeff","Chad","Jacob","Lee","Melvin","Alfred","Kyle","Francis","Bradley","Jesus","Herbert","Frederick","Ray","Joel","Edwin","Don","Eddie","Ricky","Troy","Randall","Barry","Alexander","Bernard","Mario","Leroy","Francisco","Marcus","Micheal","Theodore","Clifford","Miguel","Oscar","Jay","Jim","Tom","Calvin","Alex","Jon","Ronnie","Bill","Lloyd","Tommy","Leon","Derek","Warren","Darrell","Jerome","Floyd","Leo","Alvin","Tim","Wesley","Gordon","Dean","Greg","Jorge","Dustin","Pedro","Derrick","Dan","Lewis","Zachary","Corey","Herman","Maurice","Vernon","Roberto","Clyde","Glen","Hector","Shane","Ricardo","Sam","Rick","Lester","Brent","Ramon","Charlie","Tyler","Gilbert","Gene","Marc","Reginald","Ruben","Brett","Angel","Nathaniel","Rafael","Leslie","Edgar","Milton","Raul","Ben","Chester","Cecil","Duane","Franklin","Andre","Elmer","Brad","Gabriel","Ron","Mitchell","Roland","Arnold","Harvey","Jared","Adrian","Karl","Cory","Claude","Erik","Darryl","Jamie","Neil","Jessie","Christian","Javier","Fernando","Clinton","Ted","Mathew","Tyrone","Darren","Lonnie","Lance","Cody","Julio","Kelly","Kurt","Allan","Nelson","Guy","Clayton","Hugh","Max","Dwayne","Dwight","Armando","Felix","Jimmie","Everett","Jordan","Ian","Wallace","Ken","Bob","Jaime","Casey","Alfredo","Alberto","Dave","Ivan","Johnnie","Sidney","Byron","Julian","Isaac","Morris","Clifton","Willard","Daryl","Ross","Virgil","Andy","Marshall","Salvador","Perry","Kirk","Sergio","Marion","Tracy","Seth","Kent","Terrance","Rene","Eduardo","Terrence","Enrique","Freddie","Wade","Austin","Stuart","Fredrick","Arturo","Alejandro","Jackie","Joey","Nick","Luther","Wendell","Jeremiah","Evan","Julius","Dana","Donnie","Otis","Shannon","Trevor","Oliver","Luke","Homer","Gerard","Doug","Kenny","Hubert","Angelo","Shaun","Lyle","Matt","Lynn","Alfonso","Orlando","Rex","Carlton","Ernesto","Cameron","Neal","Pablo","Lorenzo","Omar","Wilbur","Blake","Grant","Horace","Roderick","Kerry","Abraham","Willis","Rickey","Jean","Ira","Andres","Cesar","Johnathan","Malcolm","Rudolph","Damon","Kelvin","Rudy","Preston","Alton","Archie","Marco","Wm","Pete","Randolph","Garry","Geoffrey","Jonathon","Felipe","Bennie","Gerardo","Ed","Dominic","Robin","Loren","Delbert","Colin","Guillermo","Earnest","Lucas","Benny","Noel","Spencer","Rodolfo","Myron","Edmund","Garrett","Salvatore","Cedric","Lowell","Gregg","Sherman","Wilson","Devin","Sylvester","Kim","Roosevelt","Israel","Jermaine","Forrest","Wilbert","Leland","Simon","Guadalupe","Clark","Irving","Carroll","Bryant","Owen","Rufus","Woodrow","Sammy","Kristopher","Mack","Levi","Marcos","Gustavo","Jake","Lionel","Marty","Taylor","Ellis","Dallas","Gilberto","Clint","Nicolas","Laurence","Ismael","Orville","Drew","Jody","Ervin","Dewey","Al","Wilfred","Josh","Hugo","Ignacio","Caleb","Tomas","Sheldon","Erick","Frankie","Stewart","Doyle","Darrel","Rogelio","Terence","Santiago","Alonzo","Elias","Bert","Elbert","Ramiro","Conrad","Pat","Noah","Grady","Phil","Cornelius","Lamar","Rolando","Clay","Percy","Dexter","Bradford","Merle","Darin","Amos","Terrell","Moses","Irvin","Saul","Roman","Darnell","Randal","Tommie","Timmy","Darrin","Winston","Brendan","Toby","Van","Abel","Dominick","Boyd","Courtney","Jan","Emilio","Elijah","Cary","Domingo","Santos","Aubrey","Emmett","Marlon","Emanuel","Jerald","Edmond","Emil","Dewayne","Will","Otto","Teddy","Reynaldo","Bret","Morgan","Jess","Trent","Humberto","Emmanuel","Stephan","Louie","Vicente","Lamont","Stacy","Garland","Miles","Micah","Efrain","Billie","Logan","Heath","Rodger","Harley","Demetrius","Ethan","Eldon","Rocky","Pierre","Junior","Freddy","Eli","Bryce","Antoine","Robbie","Kendall","Royce","Sterling","Mickey","Chase","Grover","Elton","Cleveland","Dylan","Chuck","Damian","Reuben","Stan","August","Leonardo","Jasper","Russel","Erwin","Benito","Hans","Monte","Blaine","Ernie","Curt","Quentin","Agustin","Murray","Jamal","Devon","Adolfo","Harrison","Tyson","Burton","Brady","Elliott","Wilfredo","Bart","Jarrod","Vance","Denis","Damien","Joaquin","Harlan","Desmond","Elliot","Darwin","Ashley","Gregorio","Buddy","Xavier","Kermit","Roscoe","Esteban","Anton","Solomon","Scotty","Norbert","Elvin","Williams","Nolan","Carey","Rod","Quinton","Hal","Brain","Rob","Elwood","Kendrick","Darius","Moises","Son","Marlin","Fidel","Thaddeus","Cliff","Marcel","Ali","Jackson","Raphael","Bryon","Armand","Alvaro","Jeffry","Dane","Joesph","Thurman","Ned","Sammie","Rusty","Michel","Monty","Rory","Fabian","Reggie","Mason","Graham","Kris","Isaiah","Vaughn","Gus","Avery","Loyd","Diego","Alexis","Adolph","Norris","Millard","Rocco","Gonzalo","Derick","Rodrigo","Gerry","Stacey","Carmen","Wiley","Rigoberto","Alphonso","Ty","Shelby","Rickie","Noe","Vern","Bobbie","Reed","Jefferson","Elvis","Bernardo","Mauricio","Hiram","Donovan","Basil","Riley","Ollie","Nickolas","Maynard","Scot","Vince","Quincy","Eddy","Sebastian","Federico","Ulysses","Heriberto","Donnell","Cole","Denny","Davis","Gavin","Emery","Ward","Romeo","Jayson","Dion","Dante","Clement","Coy","Odell","Maxwell","Jarvis","Bruno","Issac","Mary","Dudley","Brock","Sanford","Colby","Carmelo","Barney","Nestor","Hollis","Stefan","Donny","Art","Linwood","Beau","Weldon","Galen","Isidro","Truman","Delmar","Johnathon","Silas","Frederic","Dick","Kirby","Irwin","Cruz","Merlin","Merrill","Charley","Marcelino","Lane","Harris","Cleo","Carlo","Trenton","Kurtis","Hunter","Aurelio","Winfred","Vito","Collin","Denver","Carter","Leonel","Emory","Pasquale","Mohammad","Mariano","Danial","Blair","Landon","Dirk","Branden","Adan","Numbers","Clair","Buford","German","Bernie","Wilmer","Joan","Emerson","Zachery","Fletcher","Jacques","Errol","Dalton","Monroe","Josue","Dominique","Edwardo","Booker","Wilford","Sonny","Shelton","Carson","Theron","Raymundo","Daren","Tristan","Houston","Robby","Lincoln","Jame","Genaro","Gale","Bennett","Octavio","Cornell","Laverne","Hung","Arron","Antony","Herschel","Alva","Giovanni","Garth","Cyrus","Cyril","Ronny","Stevie","Lon","Freeman","Erin","Duncan","Kennith","Carmine","Augustine","Young","Erich","Chadwick","Wilburn","Russ","Reid","Myles","Anderson","Morton","Jonas","Forest","Mitchel","Mervin","Zane","Rich","Jamel","Lazaro","Alphonse","Randell","Major","Johnie","Jarrett","Brooks","Ariel","Abdul","Dusty","Luciano","Lindsey","Tracey","Seymour","Scottie","Eugenio","Mohammed","Sandy","Valentin","Chance","Arnulfo","Lucien","Ferdinand","Thad","Ezra","Sydney","Aldo","Rubin","Royal","Mitch","Earle","Abe","Wyatt","Marquis","Lanny","Kareem","Jamar","Boris","Isiah","Emile","Elmo","Aron","Leopoldo","Everette","Josef","Gail","Eloy","Dorian","Rodrick","Reinaldo","Lucio","Jerrod","Weston","Hershel","Barton","Parker","Lemuel","Lavern","Burt","Jules","Gil","Eliseo","Ahmad","Nigel","Efren","Antwan","Alden","Margarito","Coleman","Refugio","Dino","Osvaldo","Les","Deandre","Normand","Kieth","Ivory","Andrea","Trey","Norberto","Napoleon","Jerold","Fritz","Rosendo","Milford","Sang","Deon","Christoper","Alfonzo","Lyman","Josiah","Brant","Wilton","Rico","Jamaal","Dewitt","Carol","Brenton","Yong","Olin","Foster","Faustino","Claudio","Judson","Gino","Edgardo","Berry","Alec","Tanner","Jarred","Donn","Trinidad","Tad","Shirley","Prince","Porfirio","Odis","Maria","Lenard","Chauncey","Chang","Tod","Mel","Marcelo","Kory","Augustus","Keven","Hilario","Bud","Sal","Rosario","Orval","Mauro","Dannie","Zachariah","Olen","Anibal","Milo","Jed","Frances","Thanh","Dillon","Amado","Newton","Connie","Lenny","Tory","Richie","Lupe","Horacio","Brice","Mohamed","Delmer","Dario","Reyes","Dee","Mac","Jonah","Jerrold","Robt","Hank","Sung","Rupert","Rolland","Kenton","Damion","Chi","Antone","Waldo","Fredric","Bradly","Quinn","Kip","Burl","Walker","Tyree","Jefferey","Ahmed"]
femalenames = ["Mary","Patricia","Linda","Barbara","Elizabeth","Jennifer","Maria","Susan","Margaret","Dorothy","Lisa","Nancy","Karen","Betty","Helen","Sandra","Donna","Carol","Ruth","Sharon","Michelle","Laura","Sarah","Kimberly","Deborah","Jessica","Shirley","Cynthia","Angela","Melissa","Brenda","Amy","Anna","Rebecca","Virginia","Kathleen","Pamela","Martha","Debra","Amanda","Stephanie","Carolyn","Christine","Marie","Janet","Catherine","Frances","Ann","Joyce","Diane","Alice","Julie","Heather","Teresa","Doris","Gloria","Evelyn","Jean","Cheryl","Mildred","Katherine","Joan","Ashley","Judith","Rose","Janice","Kelly","Nicole","Judy","Christina","Kathy","Theresa","Beverly","Denise","Tammy","Irene","Jane","Lori","Rachel","Marilyn","Andrea","Kathryn","Louise","Sara","Anne","Jacqueline","Wanda","Bonnie","Julia","Ruby","Lois","Tina","Phyllis","Norma","Paula","Diana","Annie","Lillian","Emily","Robin","Peggy","Crystal","Gladys","Rita","Dawn","Connie","Florence","Tracy","Edna","Tiffany","Carmen","Rosa","Cindy","Grace","Wendy","Victoria","Edith","Kim","Sherry","Sylvia","Josephine","Thelma","Shannon","Sheila","Ethel","Ellen","Elaine","Marjorie","Carrie","Charlotte","Monica","Esther","Pauline","Emma","Juanita","Anita","Rhonda","Hazel","Amber","Eva","Debbie","April","Leslie","Clara","Lucille","Jamie","Joanne","Eleanor","Valerie","Danielle","Megan","Alicia","Suzanne","Michele","Gail","Bertha","Darlene","Veronica","Jill","Erin","Geraldine","Lauren","Cathy","Joann","Lorraine","Lynn","Sally","Regina","Erica","Beatrice","Dolores","Bernice","Audrey","Yvonne","Annette","June","Samantha","Marion","Dana","Stacy","Ana","Renee","Ida","Vivian","Roberta","Holly","Brittany","Melanie","Loretta","Yolanda","Jeanette","Laurie","Katie","Kristen","Vanessa","Alma","Sue","Elsie","Beth","Jeanne","Vicki","Carla","Tara","Rosemary","Eileen","Terri","Gertrude","Lucy","Tonya","Ella","Stacey","Wilma","Gina","Kristin","Jessie","Natalie","Agnes","Vera","Willie","Charlene","Bessie","Delores","Melinda","Pearl","Arlene","Maureen","Colleen","Allison","Tamara","Joy","Georgia","Constance","Lillie","Claudia","Jackie","Marcia","Tanya","Nellie","Minnie","Marlene","Heidi","Glenda","Lydia","Viola","Courtney","Marian","Stella","Caroline","Dora","Jo","Vickie","Mattie","Terry","Maxine","Irma","Mabel","Marsha","Myrtle","Lena","Christy","Deanna","Patsy","Hilda","Gwendolyn","Jennie","Nora","Margie","Nina","Cassandra","Leah","Penny","Kay","Priscilla","Naomi","Carole","Brandy","Olga","Billie","Dianne","Tracey","Leona","Jenny","Felicia","Sonia","Miriam","Velma","Becky","Bobbie","Violet","Kristina","Toni","Misty","Mae","Shelly","Daisy","Ramona","Sherri","Erika","Katrina","Claire","Lindsey","Lindsay","Geneva","Guadalupe","Belinda","Margarita","Sheryl","Cora","Faye","Ada","Natasha","Sabrina","Isabel","Marguerite","Hattie","Harriet","Molly","Cecilia","Kristi","Brandi","Blanche","Sandy","Rosie","Joanna","Iris","Eunice","Angie","Inez","Lynda","Madeline","Amelia","Alberta","Genevieve","Monique","Jodi","Janie","Maggie","Kayla","Sonya","Jan","Lee","Kristine","Candace","Fannie","Maryann","Opal","Alison","Yvette","Melody","Luz","Susie","Olivia","Flora","Shelley","Kristy","Mamie","Lula","Lola","Verna","Beulah","Antoinette","Candice","Juana","Jeannette","Pam","Kelli","Hannah","Whitney","Bridget","Karla","Celia","Latoya","Patty","Shelia","Gayle","Della","Vicky","Lynne","Sheri","Marianne","Kara","Jacquelyn","Erma","Blanca","Myra","Leticia","Pat","Krista","Roxanne","Angelica","Johnnie","Robyn","Francis","Adrienne","Rosalie","Alexandra","Brooke","Bethany","Sadie","Bernadette","Traci","Jody","Kendra","Jasmine","Nichole","Rachael","Chelsea","Mable","Ernestine","Muriel","Marcella","Elena","Krystal","Angelina","Nadine","Kari","Estelle","Dianna","Paulette","Lora","Mona","Doreen","Rosemarie","Angel","Desiree","Antonia","Hope","Ginger","Janis","Betsy","Christie","Freda","Mercedes","Meredith","Lynette","Teri","Cristina","Eula","Leigh","Meghan","Sophia","Eloise","Rochelle","Gretchen","Cecelia","Raquel","Henrietta","Alyssa","Jana","Kelley","Gwen","Kerry","Jenna","Tricia","Laverne","Olive","Alexis","Tasha","Silvia","Elvira","Casey","Delia","Sophie","Kate","Patti","Lorena","Kellie","Sonja","Lila","Lana","Darla","May","Mindy","Essie","Mandy","Lorene","Elsa","Josefina","Jeannie","Miranda","Dixie","Lucia","Marta","Faith","Lela","Johanna","Shari","Camille","Tami","Shawna","Elisa","Ebony","Melba","Ora","Nettie","Tabitha","Ollie","Jaime","Winifred","Kristie","Marina","Alisha","Aimee","Rena","Myrna","Marla","Tammie","Latasha","Bonita","Patrice","Ronda","Sherrie","Addie","Francine","Deloris","Stacie","Adriana","Cheri","Shelby","Abigail","Celeste","Jewel","Cara","Adele","Rebekah","Lucinda","Dorthy","Chris","Effie","Trina","Reba","Shawn","Sallie","Aurora","Lenora","Etta","Lottie","Kerri","Trisha","Nikki","Estella","Francisca","Josie","Tracie","Marissa","Karin","Brittney","Janelle","Lourdes","Laurel","Helene","Fern","Elva","Corinne","Kelsey","Ina","Bettie","Elisabeth","Aida","Caitlin","Ingrid","Iva","Eugenia","Christa","Goldie","Cassie","Maude","Jenifer","Therese","Frankie","Dena","Lorna","Janette","Latonya","Candy","Morgan","Consuelo","Tamika","Rosetta","Debora","Cherie","Polly","Dina","Jewell","Fay","Jillian","Dorothea","Nell","Trudy","Esperanza","Patrica","Kimberley","Shanna","Helena","Carolina","Cleo","Stefanie","Rosario","Ola","Janine","Mollie","Lupe","Alisa","Lou","Maribel","Susanne","Bette","Susana","Elise","Cecile","Isabelle","Lesley","Jocelyn","Paige","Joni","Rachelle","Leola","Daphne","Alta","Ester","Petra","Graciela","Imogene","Jolene","Keisha","Lacey","Glenna","Gabriela","Keri","Ursula","Lizzie","Kirsten","Shana","Adeline","Mayra","Jayne","Jaclyn","Gracie","Sondra","Carmela","Marisa","Rosalind","Charity","Tonia","Beatriz","Marisol","Clarice","Jeanine","Sheena","Angeline","Frieda","Lily","Robbie","Shauna","Millie","Claudette","Cathleen","Angelia","Gabrielle","Autumn","Katharine","Summer","Jodie","Staci","Lea","Christi","Jimmie","Justine","Elma","Luella","Margret","Dominique","Socorro","Rene","Martina","Margo","Mavis","Callie","Bobbi","Maritza","Lucile","Leanne","Jeannine","Deana","Aileen","Lorie","Ladonna","Willa","Manuela","Gale","Selma","Dolly","Sybil","Abby","Lara","Dale","Ivy","Dee","Winnie","Marcy","Luisa","Jeri","Magdalena","Ofelia","Meagan","Audra","Matilda","Leila","Cornelia","Bianca","Simone","Bettye","Randi","Virgie","Latisha","Barbra","Georgina","Eliza","Leann","Bridgette","Rhoda","Haley","Adela","Nola","Bernadine","Flossie","Ila","Greta","Ruthie","Nelda","Minerva","Lilly","Terrie","Letha","Hilary","Estela","Valarie","Brianna","Rosalyn","Earline","Catalina","Ava","Mia","Clarissa","Lidia","Corrine","Alexandria","Concepcion","Tia","Sharron","Rae","Dona","Ericka","Jami","Elnora","Chandra","Lenore","Neva","Marylou","Melisa","Tabatha","Serena","Avis","Allie","Sofia","Jeanie","Odessa","Nannie","Harriett","Loraine","Penelope","Milagros","Emilia","Benita","Allyson","Ashlee","Tania","Tommie","Esmeralda","Karina","Eve","Pearlie","Zelma","Malinda","Noreen","Tameka","Saundra","Hillary","Amie","Althea","Rosalinda","Jordan","Lilia","Alana","Gay","Clare","Alejandra","Elinor","Michael","Lorrie","Jerri","Darcy","Earnestine","Carmella","Taylor","Noemi","Marcie","Liza","Annabelle","Louisa","Earlene","Mallory","Carlene","Nita","Selena","Tanisha","Katy","Julianne","John","Lakisha","Edwina","Maricela","Margery","Kenya","Dollie","Roxie","Roslyn","Kathrine","Nanette","Charmaine","Lavonne","Ilene","Kris","Tammi","Suzette","Corine","Kaye","Jerry","Merle","Chrystal","Lina","Deanne","Lilian","Juliana","Aline","Luann","Kasey","Maryanne","Evangeline","Colette","Melva","Lawanda","Yesenia","Nadia","Madge","Kathie","Eddie","Ophelia","Valeria","Nona","Mitzi","Mari","Georgette","Claudine","Fran","Alissa","Roseann","Lakeisha","Susanna","Reva","Deidre","Chasity","Sheree","Carly","James","Elvia","Alyce","Deirdre","Gena","Briana","Araceli","Katelyn","Rosanne","Wendi","Tessa","Berta","Marva","Imelda","Marietta","Marci","Leonor","Arline","Sasha","Madelyn","Janna","Juliette","Deena","Aurelia","Josefa","Augusta","Liliana","Young","Christian","Lessie","Amalia","Savannah","Anastasia","Vilma","Natalia","Rosella","Lynnette","Corina","Alfreda","Leanna","Carey","Amparo","Coleen","Tamra","Aisha","Wilda","Karyn","Cherry","Queen","Maura","Mai","Evangelina","Rosanna","Hallie","Erna","Enid","Mariana","Lacy","Juliet","Jacklyn","Freida","Madeleine","Mara","Hester","Cathryn","Lelia","Casandra","Bridgett","Angelita","Jannie","Dionne","Annmarie","Katina","Beryl","Phoebe","Millicent","Katheryn","Diann","Carissa","Maryellen","Liz","Lauri","Helga","Gilda","Adrian","Rhea","Marquita","Hollie","Tisha","Tamera","Angelique","Francesca","Britney","Kaitlin","Lolita","Florine","Rowena","Reyna","Twila","Fanny","Janell","Ines","Concetta","Bertie","Alba","Brigitte","Alyson","Vonda","Pansy","Elba","Noelle","Letitia","Kitty","Deann","Brandie","Louella","Leta","Felecia","Sharlene","Lesa","Beverley","Robert","Isabella","Herminia","Terra","Celina"]
surnames = ["Smith","Johnson","Williams","Jones","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson","Thomas","Jackson","White","Harris","Martin","Thompson","Garcia","Martinez","Robinson","Clark","Rodriguez","Lewis","Lee","Walker","Hall","Allen","Young","Hernandez","King","Wright","Lopez","Hill","Scott","Green","Adams","Baker","Gonzalez","Nelson","Carter","Mitchell","Perez","Roberts","Turner","Phillips","Campbell","Parker","Evans","Edwards","Collins","Stewart","Sanchez","Morris","Rogers","Reed","Cook","Morgan","Bell","Murphy","Bailey","Rivera","Cooper","Richardson","Cox","Howard","Ward","Torres","Peterson","Gray","Ramirez","James","Watson","Brooks","Kelly","Sanders","Price","Bennett","Wood","Barnes","Ross","Henderson","Coleman","Jenkins","Perry","Powell","Long","Patterson","Hughes","Flores","Washington","Butler","Simmons","Foster","Gonzales","Bryant","Alexander","Russell","Griffin","Diaz","Hayes","Myers","Ford","Hamilton","Graham","Sullivan","Wallace","Woods","Cole","West","Jordan","Owens","Reynolds","Fisher","Ellis","Harrison","Gibson","Mcdonald","Cruz","Marshall","Ortiz","Gomez","Murray","Freeman","Wells","Webb","Simpson","Stevens","Tucker","Porter","Hunter","Hicks","Crawford","Henry","Boyd","Mason","Morales","Kennedy","Warren","Dixon","Ramos","Reyes","Burns","Gordon","Shaw","Holmes","Rice","Robertson","Hunt","Black","Daniels","Palmer","Mills","Nichols","Grant","Knight","Ferguson","Rose","Stone","Hawkins","Dunn","Perkins","Hudson","Spencer","Gardner","Stephens","Payne","Pierce","Berry","Matthews","Arnold","Wagner","Willis","Ray","Watkins","Olson","Carroll","Duncan","Snyder","Hart","Cunningham","Bradley","Lane","Andrews","Ruiz","Harper","Fox","Riley","Armstrong","Carpenter","Weaver","Greene","Lawrence","Elliott","Chavez","Sims","Austin","Peters","Kelley","Franklin","Lawson","Fields","Gutierrez","Ryan","Schmidt","Carr","Vasquez","Castillo","Wheeler","Chapman","Oliver","Montgomery","Richards","Williamson","Johnston","Banks","Meyer","Bishop","Mccoy","Howell","Alvarez","Morrison","Hansen","Fernandez","Garza","Harvey","Little","Burton","Stanley","Nguyen","George","Jacobs","Reid","Kim","Fuller","Lynch","Dean","Gilbert","Garrett","Romero","Welch","Larson","Frazier","Burke","Hanson","Day","Mendoza","Moreno","Bowman","Medina","Fowler","Brewer","Hoffman","Carlson","Silva","Pearson","Holland","Douglas","Fleming","Jensen","Vargas","Byrd","Davidson","Hopkins","May","Terry","Herrera","Wade","Soto","Walters","Curtis","Neal","Caldwell","Lowe","Jennings","Barnett","Graves","Jimenez","Horton","Shelton","Barrett","Obrien","Castro","Sutton","Gregory","Mckinney","Lucas","Miles","Craig","Rodriquez","Chambers","Holt","Lambert","Fletcher","Watts","Bates","Hale","Rhodes","Pena","Beck","Newman","Haynes","Mcdaniel","Mendez","Bush","Vaughn","Parks","Dawson","Santiago","Norris","Hardy","Love","Steele","Curry","Powers","Schultz","Barker","Guzman","Page","Munoz","Ball","Keller","Chandler","Weber","Leonard","Walsh","Lyons","Ramsey","Wolfe","Schneider","Mullins","Benson","Sharp","Bowen","Daniel","Barber","Cummings","Hines","Baldwin","Griffith","Valdez","Hubbard","Salazar","Reeves","Warner","Stevenson","Burgess","Santos","Tate","Cross","Garner","Mann","Mack","Moss","Thornton","Dennis","Mcgee","Farmer","Delgado","Aguilar","Vega","Glover","Manning","Cohen","Harmon","Rodgers","Robbins","Newton","Todd","Blair","Higgins","Ingram","Reese","Cannon","Strickland","Townsend","Potter","Goodwin","Walton","Rowe","Hampton","Ortega","Patton","Swanson","Joseph","Francis","Goodman","Maldonado","Yates","Becker","Erickson","Hodges","Rios","Conner","Adkins","Webster","Norman","Malone","Hammond","Flowers","Cobb","Moody","Quinn","Blake","Maxwell","Pope","Floyd","Osborne","Paul","Mccarthy","Guerrero","Lindsey","Estrada","Sandoval","Gibbs","Tyler","Gross","Fitzgerald","Stokes","Doyle","Sherman","Saunders","Wise","Colon","Gill","Alvarado","Greer","Padilla","Simon","Waters","Nunez","Ballard","Schwartz","Mcbride","Houston","Christensen","Klein","Pratt","Briggs","Parsons","Mclaughlin","Zimmerman","French","Buchanan","Moran","Copeland","Roy","Pittman","Brady","Mccormik","Holloway","Brock","Poole","Frank","Logan","Owen","Bass","Marsh","Drake","Wong","Jefferson","Park","Morton","Abbott","Sparks","Patrick","Norton","Huff","Clayton","Massey","Lloyd","Figueroa","Carson","Bowers","Roberson","Barton","Tran","Lamb","Harrington","Casey","Boone","Cortez","Clarke","Mathis","Singleton","Wilkins","Cain","Bryan","Underwood","Hogan","Mckenzie","Collier","Luna","Phelps","Mcguire","Allison","Bridges","Wilkerson","Nash","Summers","Atkins","Wilcox","Pitts","Conley","Marquez","Burnett","Richard","Cochran","Chase","Davenport","Hood","Gates","Clay","Ayala","Sawyer","Roman","Vazquez","Dickerson","Hodge","Acosta","Flynn","Espinoza","Nicholson","Monroe","Wolf","Morrow","Kirk","Randall","Anthony","Whitaker","Oconnor","Skinner","Ware","Molina","Kirby","Huffman","Bradford","Charles","Gilmore","Dominguez","Oneal","Bruce","Lang","Combs","Kramer","Heath","Hancock","Gallagher","Gaines","Shaffer","Short","Wiggins","Mathews","Mcclain","Fischer","Wall","Small","Melton","Hensley","Bond","Dyer","Cameron","Grimes","Contreras","Christian","Wyatt","Baxter","Snow","Mosley","Shepherd","Larsen","Hoover","Beasley","Glenn","Petersen","Whitehead","Meyers","Keith","Garrison","Vincent","Shields","Horn","Savage","Olsen","Schroeder","Hartman","Woodard","Mueller","Kemp","Deleon","Booth","Patel","Calhoun","Wiley","Eaton","Cline","Navarro","Harrell","Lester","Humphrey","Parrish","Duran","Hutchinson","Hess","Dorsey","Bullock","Robles","Beard","Dalton","Avila","Vance","Rich","Blackwell","York","Johns","Blankenship","Trevino","Salinas","Campos","Pruitt","Moses","Callahan","Golden","Montoya","Hardin","Guerra","Mcdowell","Carey","Stafford","Gallegos","Henson","Wilkinson","Booker","Merritt","Miranda","Atkinson","Orr","Decker","Hobbs","Preston","Tanner","Knox","Pacheco","Stephenson","Glass","Rojas","Serrano","Marks","Hickman","English","Sweeney","Strong","Prince","Mcclure","Conway","Walter","Roth","Maynard","Farrell","Lowery","Hurst","Nixon","Weiss","Trujillo","Ellison","Sloan","Juarez","Winters","Mclean","Randolph","Leon","Boyer","Villarreal","Mccall","Gentry","Carrillo","Kent","Ayers","Lara","Shannon","Sexton","Pace","Hull","Leblanc","Browning","Velasquez","Leach","Chang","House","Sellers","Herring","Noble","Foley","Bartlett","Mercado","Landry","Durham","Walls","Barr","Mckee","Bauer","Rivers","Everett","Bradshaw","Pugh","Velez","Rush","Estes","Dodson","Morse","Sheppard","Weeks","Camacho","Bean","Barron","Livingston","Middleton","Spears","Branch","Blevins","Chen","Kerr","Mcconnell","Hatfield","Harding","Ashley","Solis","Herman","Frost","Giles","Blackburn","William","Pennington","Woodward","Finley","Mcintosh","Koch","Best","Solomon","Mccullough","Dudley","Nolan","Blanchard","Rivas","Brennan","Mejia","Kane","Benton","Joyce","Buckley","Haley","Valentine","Maddox","Russo","Mcknight","Buck","Moon","Mcmillan","Crosby","Berg","Dotson","Mays","Roach","Church","Chan","Richmond","Meadows","Faulkner","Oneill","Knapp","Kline","Barry","Ochoa","Jacobson","Gay","Avery","Hendricks","Horne","Shepard","Hebert","Cherry","Cardenas","Mcintyre","Whitney","Waller","Holman","Donaldson","Cantu","Terrell","Morin","Gillespie","Fuentes","Tillman","Sanford","Bentley","Peck","Key","Salas","Rollins","Gamble","Dickson","Battle","Santana","Cabrera","Cervantes","Howe","Hinton","Hurley","Spence","Zamora","Yang","Mcneil","Suarez","Case","Petty","Gould","Mcfarland","Sampson","Carver","Bray","Rosario","Macdonald","Stout","Hester","Melendez","Dillon","Farley","Hopper","Galloway","Potts","Bernard","Joyner","Stein","Aguirre","Osborn","Mercer","Bender","Franco","Rowland","Sykes","Benjamin","Travis","Pickett","Crane","Sears","Mayo","Dunlap","Hayden","Wilder","Mckay","Coffey","Mccarty","Ewing","Cooley","Vaughan","Bonner","Cotton","Holder","Stark","Ferrell","Cantrell","Fulton","Lynn","Lott","Calderon","Rosa","Pollard","Hooper","Burch","Mullen","Fry","Riddle","Levy","David","Duke","Odonnell","Guy","Michael","Britt","Frederick","Daugherty","Berger","Dillard","Alston","Jarvis","Frye","Riggs","Chaney","Odom","Duffy","Fitzpatrick","Valenzuela","Merrill","Mayer","Alford","Mcpherson","Acevedo","Donovan","Barrera","Albert","Cote","Reilly","Compton","Raymond","Mooney","Mcgowan","Craft","Cleveland","Clemons","Wynn","Nielsen","Baird","Stanton","Snider","Rosales","Bright","Witt","Stuart","Hays","Holden","Rutledge","Kinney","Clements","Castaneda","Slater","Hahn","Emerson","Conrad","Burks","Delaney","Pate","Lancaster","Sweet","Justice","Tyson","Sharpe","Whitfield","Talley","Macias","Irwin","Burris","Ratliff","Mccray","Madden","Kaufman","Beach","Goff","Cash","Bolton","Mcfadden","Levine","Good","Byers","Kirkland","Kidd","Workman","Carney","Dale","Mcleod","Holcomb","England","Finch","Head","Burt","Hendrix","Sosa","Haney","Franks","Sargent","Nieves","Downs","Rasmussen","Bird","Hewitt","Lindsay","Le","Foreman","Valencia","Oneil","Delacruz","Vinson","Dejesus","Hyde","Forbes","Gilliam","Guthrie","Wooten","Huber","Barlow","Boyle","Mcmahon","Buckner","Rocha","Puckett","Langley","Knowles","Cooke","Velazquez","Whitley","Noel","Vang","Shea","Rouse","Hartley","Mayfield","Elder","Rankin","Hanna","Cowan","Lucero","Arroyo","Slaughter","Haas","Oconnell","Minor","Kendrick","Shirley","Kendall","Boucher","Archer","Boggs","Odell","Dougherty","Andersen","Newell","Crowe","Wang","Friedman","Bland","Swain","Holley","Felix","Pearce","Childs","Yarbrough","Galvan","Proctor","Meeks","Lozano","Mora","Rangel","Bacon","Villanueva","Schaefer","Rosado","Helms","Boyce","Goss","Stinson","Smart","Lake","Ibarra","Hutchins","Covington","Reyna","Gregg","Werner","Crowley","Hatcher","Mackey","Bunch","Womack","Polk","Jamison","Dodd","Childress","Childers","Camp","Villa","Dye","Springer","Mahoney","Dailey","Belcher","Lockhart","Griggs","Costa","Connor","Brandt","Winter","Walden","Moser","Tracy","Tatum","Mccann","Akers","Lutz","Pryor","Law","Orozco","Mcallister","Lugo","Davies","Shoemaker","Madison","Rutherford","Newsome","Magee","Chamberlain","Blanton","Simms","Godfrey","Flanagan","Crum","Cordova","Escobar","Downing","Sinclair","Donahue","Krueger","Mcginnis","Gore","Farris","Webber","Corbett","Andrade","Starr","Lyon","Yoder","Hastings","Mcgrath","Spivey","Krause","Harden","Crabtree","Kirkpatrick","Hollis","Brandon","Arrington","Ervin","Clifton","Ritter","Mcghee","Bolden","Maloney","Gagnon","Dunbar","Ponce","Pike","Mayes","Heard","Beatty","Mobley","Kimball","Butts","Montes","Herbert","Grady","Eldridge","Braun","Hamm","Gibbons","Seymour","Moyer","Manley","Herron","Plummer","Elmore","Cramer","Gary","Rucker","Hilton","Blue","Pierson","Fontenot","Field","Rubio","Grace","Goldstein","Elkins","Wills","Novak","John","Hickey","Worley","Gorman","Katz","Dickinson","Broussard","Fritz","Woodruff","Crow","Christopher","Britton","Forrest","Nance","Lehman","Bingham","Zuniga","Whaley","Shafer","Coffman","Steward","Delarosa","Nix","Neely","Numbers","Mata","Manuel","Davila","Mccabe","Kessler","Emery","Bowling","Hinkle","Welsh","Pagan","Goldberg","Goins","Crouch","Cuevas","Quinones","Mcdermott","Hendrickson","Samuels","Denton","Bergeron","Lam","Ivey","Locke","Haines","Thurman","Snell","Hoskins","Byrne","Milton","Winston","Arthur","Arias","Stanford","Roe","Corbin","Beltran","Chappell","Hurt","Downey","Dooley","Tuttle","Couch","Payton","Mcelroy","Crockett","Groves","Clement","Leslie","Cartwright","Dickey","Mcgill","Dubois","Muniz","Erwin","Self","Tolbert","Dempsey","Cisneros","Sewell","Latham","Garland","Vigil","Tapia","Sterling","Rainey","Norwood","Lacy","Stroud","Meade","Amos","Tipton","Lord","Kuhn","Hilliard","Bonilla","Teague","Courtney","Gunn","Ho","Greenwood","Correa","Reece","Weston","Poe","Trent","Pineda","Phipps","Frey","Kaiser","Ames","Paige","Gunter","Schmitt","Milligan","Espinosa","Carlton","Bowden","Vickers","Lowry","Pritchard","Costello","Piper","Mcclellan","Lovell","Drew","Sheehan","Quick","Hatch","Dobson","Singh","Jeffries","Hollingsworth","Sorensen","Meza","Fink","Donnelly","Burrell","Bruno","Tomlinson","Colbert","Billings","Ritchie","Helton","Sutherland","Peoples","Mcqueen","Gaston","Thomason","Mckinley","Givens","Crocker","Vogel","Robison","Dunham","Coker","Swartz","Keys","Lilly","Ladner","Hannah","Willard","Richter","Hargrove","Edmonds","Brantley","Albright","Murdock","Boswell","Muller","Quintero","Padgett","Kenney","Daly","Connolly","Pierre","Inman","Quintana","Lund","Barnard","Villegas","Simons","Land","Huggins","Tidwell","Sanderson","Bullard","Mcclendon","Duarte","Draper","Meredith","Marrero","Dwyer","Abrams","Stover","Goode","Fraser","Crews","Bernal","Smiley","Godwin","Fish","Conklin","Mcneal","Baca","Esparza","Crowder","Bower","Nicholas","Chung","Brewster","Mcneill","Dick","Rodrigues","Leal","Coates","Raines","Mccain","Mccord","Miner","Holbrook","Swift","Dukes","Carlisle","Aldridge","Ackerman","Starks","Ricks","Holliday","Ferris","Hairston","Sheffield","Lange","Fountain","Marino","Doss","Betts","Kaplan","Carmichael","Bloom","Ruffin","Penn","Kern","Bowles","Sizemore","Larkin","Dupree","Jewell","Silver","Seals","Metcalf","Hutchison","Henley","Farr","Castle","Mccauley","Hankins","Gustafson","Deal","Curran","Ash","Waddell","Ramey","Cates","Pollock","Major","Irvin","Cummins","Messer","Heller","Dewitt","Lin","Funk","Cornett","Palacios","Galindo","Cano","Hathaway","Singer","Pham","Enriquez","Aaron","Salgado","Pelletier","Painter","Wiseman","Blount","Hand","Feliciano","Temple","Houser","Doherty","Mead","Mcgraw","Toney","Swan","Melvin","Capps","Blanco","Blackmon","Wesley","Thomson","Mcmanus","Fair","Burkett","Post","Gleason","Rudolph","Ott","Dickens","Cormier","Voss","Rushing","Rosenberg","Hurd","Dumas","Benitez","Arellano","Story","Marin","Caudill","Bragg","Jaramillo","Huerta","Gipson","Colvin","Biggs","Vela","Platt","Cassidy","Tompkins","Mccollum","Kay","Gabriel","Dolan","Daley","Crump","Street","Sneed","Kilgore","Grove","Grimm","Davison","Brunson","Prater","Marcum","Devine","Kyle","Dodge","Stratton","Rosas","Choi","Tripp","Ledbetter","Lay","Hightower","Haywood","Feldman","Epps","Yeager","Posey","Sylvester","Scruggs","Cope","Stubbs","Richey","Overton","Trotter","Sprague","Cordero","Butcher","Burger","Stiles","Burgos","Woodson","Horner","Bassett","Purcell","Haskins","Gee","Akins","Abraham","Hoyt","Ziegler","Spaulding","Hadley","Grubbs","Sumner","Murillo","Zavala","Shook","Lockwood","Jarrett","Driscoll","Dahl","Thorpe","Sheridan","Redmond","Putnam","Mcwilliams","Mcrae","Cornell","Felton","Romano","Joiner","Sadler","Hedrick","Hager","Hagen","Fitch","Coulter","Thacker","Mansfield","Langston","Guidry","Ferreira","Corley","Conn","Rossi","Lackey","Cody","Baez","Saenz","Mcnamara","Darnell","Michel","Mcmullen","Mckenna","Mcdonough","Link","Engel","Browne","Roper","Peacock","Eubanks","Drummond","Stringer","Pritchett","Parham","Mims","Landers","Ham","Grayson","Stacy","Schafer","Egan","Timmons","Ohara","Keen","Hamlin","Finn","Cortes","Mcnair","Louis","Clifford","Nadeau","Moseley","Michaud","Rosen","Oakes","Kurtz","Jeffers","Calloway","Beal","Bautista","Winn","Suggs","Stern","Stapleton","Lyles","Laird","Montano","Diamond","Dawkins","Roland","Hagan","Goldman","Bryson","Barajas","Lovett","Segura","Metz","Lockett","Langford","Hinson","Eastman","Rock","Hooks","Woody","Smallwood","Shapiro","Crowell","Whalen","Triplett","Hooker","Chatman","Aldrich","Cahill","Youngblood","Ybarra","Stallings","Sheets","Samuel","Reeder","Person","Pack","Lacey","Connelly","Bateman","Abernathy","Winkler","Wilkes","Masters","Hackett","Granger","Gillis","Schmitz","Sapp","Napier","Souza","Lanier","Gomes","Weir","Otero","Ledford","Burroughs","Babcock","Ventura","Siegel","Dugan","Clinton","Christie","Bledsoe","Atwood","Wray","Varner","Spangler","Otto","Anaya","Staley","Kraft","Fournier","Eddy","Belanger","Wolff","Thorne","Bynum","Burnette","Boykin","Swenson","Purvis","Pina","Khan","Duvall","Darby","Xiong","Kauffman","Ali","Yu","Healy","Engle","Corona","Benoit","Valle","Steiner","Spicer","Shaver","Randle","Lundy","Dow","Chin","Calvert","Staton","Neff","Kearney","Darden","Oakley","Medeiros","Mccracken","Crenshaw","Block","Beaver","Perdue","Dill","Whittaker","Tobin","Cornelius","Washburn","Hogue","Goodrich","Easley","Bravo","Dennison","Vera","Shipley","Kerns","Jorgensen","Crain","Abel","Villalobos","Maurer","Longoria","Keene","Coon","Sierra","Witherspoon","Staples","Pettit","Kincaid","Eason","Madrid","Echols","Lusk","Wu","Stahl","Currie","Thayer","Shultz","Sherwood","Mcnally","Seay","North","Maher","Kenny","Hope","Gagne","Barrow","Nava","Myles","Moreland","Honeycutt","Hearn","Diggs","Caron","Whitten","Westbrook","Stovall","Ragland","Queen","Munson","Meier","Looney","Kimble","Jolly","Hobson","London","Goddard","Culver","Burr","Presley","Negron","Connell","Tovar","Marcus","Huddleston","Hammer","Ashby","Salter","Root","Pendleton","Oleary","Nickerson","Myrick","Judd","Jacobsen","Elliot","Bain","Adair","Starnes","Sheldon","Matos","Light","Busby","Herndon","Hanley","Bellamy","Jack","Doty","Bartley","Yazzie","Rowell","Parson","Gifford","Cullen","Christiansen","Benavides","Barnhart","Talbot","Mock","Crandall","Connors","Bonds","Whitt","Gage","Bergman","Arredondo","Addison","Marion","Lujan","Dowdy","Jernigan","Huynh","Bouchard","Dutton","Rhoades","Ouellette","Kiser","Rubin","Herrington","Hare","Denny","Blackman","Babb","Allred","Rudd","Paulson","Ogden","Koenig","Jacob","Irving","Geiger","Begay","Parra","Champion","Lassiter","Hawk","Esposito","Cho","Waldron","Vernon","Ransom","Prather","Keenan","Jean","Grover","Chacon","Vick","Sands","Roark","Parr","Mayberry","Greenberg","Coley","Bruner","Whitman","Skaggs","Shipman","Means","Leary","Hutton","Romo","Medrano","Ladd","Kruse","Friend","Darling","Askew","Valentin","Schulz","Alfaro","Tabor","Mohr","Gallo","Bermudez","Pereira","Isaac","Bliss","Reaves","Flint","Comer","Boston","Woodall","Naquin","Guevara","Earl","Delong","Carrier","Pickens","Brand","Tilley","Schaffer","Read","Lim","Knutson","Fenton","Doran","Chu","Vogt","Vann","Prescott","Mclain","Landis","Corcoran","Ambrose","Zapata","Hyatt","Hemphill","Faulk","Call","Dove","Boudreaux","Aragon","Whitlock","Trejo","Ackett","Shearer","Saldana","Hanks","Gold","Driver","Mckinnon","Koehler","Champagne","Bourgeois","Pool","Keyes","Goodson","Foote","Early","Lunsford","Goldsmith","Flood","Winslow","Sams","Reagan"]

Names = [malenames, femalenames, surnames]

Name = Names[PO][d(1000)]+" "+Names[2][d(2000)]

print "You are " + Name + ", the " + Sex + " " + Subrace + Race + "."
print "You're a " +Background + " " + Class + Subclass + "."
print "You're level " + str(Lev) + ", " + Ment + ", your HP is " + str(int(HP)) + "."
print Stat