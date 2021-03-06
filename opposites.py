# ----------------------------------------------------------------------------- 
# FILE: opposites.py                                                            
#                                                                               
# DESC: These are opposite word pairs taken from source:                        
# http://englishgrammarhere.com/opposite-words/alphabetical-opposite-word-list-a
# These pairs are used to generate 2 word passwords by genpass.py               
# ----------------------------------------------------------------------------- 

OPPOSITE_WORD_PAIRS = (

    #   | a - c                     | c - f                     | f - p                     | p - z                  
        ("about", "exactly"),       ("children", "parents"),    ("form", "destroy"),        ("peace", "war"),           
        ("above", "below"),         ("clean", "dirty"),         ("fortune", "bad luck"),    ("pending", "already"),     
        ("absence", "presence"),    ("clear", "cloudy"),        ("freeze", "melt"),         ("permit", "forbid"),       
        ("abundance", "lack"),      ("clever", "stupid"),       ("frequently", "occasionally"),("pleasant", "awful"),      
        ("accept", "refuse"),       ("close", "open"),          ("fresh", "stale"),         ("plenty", "lack"),         
        ("accidental", "intentional"),("closed", "open"),       ("front", "rear"),          ("polite", "rude"),         
        ("active", "lazy"),         ("cold", "heat"),           ("funny", "serious"),       ("poor", "rich"),           
        ("add", "subtract"),        ("come", "go"),             ("future", "past"),         ("poverty", "wealth"),      
        ("admit", "deny"),          ("comedy", "drama"),        ("general", "particular"),  ("present", "past"),        
        ("adult", "child"),         ("complicated", "simple"),  ("generous", "mean"),       ("pretty", "ugly"),         
        ("advanced", "elementary"), ("compliment", "insult"),   ("gentle", "violent"),      ("private", "public"),      
        ("affirmative", "negative"), ("compulsory", "voluntary"),("gentleman", "lady"),     ("protect", "attack"),      
        ("afraid", "brave"),        ("connect", "separate"),    ("giant", "tiny"),          ("protection", "attack"),   
        ("after", "before"),        ("consonant", "vowel"),     ("give", "take"),           ("pull", "push"),           
        ("against", "for"),         ("construction", "destruction"),("guest", "host"),      ("pupil", "teacher"),       
        ("agree", "refuse"),        ("continue", "interrupt"),  ("guilty", "innocent"),     ("rainy", "sunny"),         
        ("alike", "different"),     ("cool", "warm"),           ("handsome", "ugly"),       ("receive", "send"),        
        ("alive", "dead"),          ("correct", "wrong"),       ("happiness", "sadness"),   ("regret", "satisfaction"), 
        ("all", "none"),            ("courage", "fear"),        ("happy", "sad"),           ("reply", "ask"),           
        ("allow", "forbid"),        ("courageous", "cowardly"), ("hard", "easy"),           ("rest", "work"),           
        ("already", "not yet"),     ("create", "destroy"),      ("harvest", "plant"),       ("rise", "sink"),           
        ("always", "never"),        ("cruel", "human"),         ("healthy", "ill"),         ("rough", "smooth"),        
        ("amateur", "professional"),("cry", "laugh"),           ("heaven", "hell"),         ("rural", "urban"),         
        ("amuse", "bore"),          ("damage", "repair"),       ("heavy", "light"),         ("safety", "danger"),       
        ("ancestor", "descendant"), ("danger", "security"),     ("here", "there"),          ("salt", "sugar"),          
        ("ancient", "modern"),      ("dangerous", "safe"),      ("high", "low"),            ("save", "spend"),          
        ("angel", "devil"),         ("dark", "light"),          ("hit", "miss"),            ("scream", "whisper"),      
        ("animal", "human"),        ("daughter", "son"),        ("hopeless", "hopeful"),    ("senior", "junior"),       
        ("annoy", "satisfy"),       ("dawn", "dusk"),           ("horizontal", "vertical"), ("servant", "master"),      
        ("answer", "question"),     ("day", "night"),           ("huge", "tiny"),           ("set free", "arrest"),     
        ("antonym", "synonym"),     ("deep", "shallow"),        ("humane", "cruel"),        ("shout", "whisper"),       
        ("apart", "together"),      ("defeat", "victory"),      ("hungry", "thirsty"),      ("shut", "open"),           
        ("approximately", "exactly"),("delicious", "awful"),    ("husband", "wife"),        ("sick", "healthy"),        
        ("argue", "agree"),         ("desperate", "hopeful"),   ("ignore", "notice"),       ("silent", "noisy"),        
        ("arrest", "free"),         ("dictatorship", "republic"),("ill", "healthy"),         ("single", "married"),      
        ("arrival", "departure"),   ("die", "live"),            ("in", "out"),              ("sit", "stand"),           
        ("arrive", "depart"),       ("difficult", "easy"),      ("increase", "reduce"),     ("soft", "hard"),           
        ("artificial", "natural"),  ("disease", "health"),      ("inside", "outside"),      ("some", "many"),           
        ("ascent", "descent"),      ("distant", "near"),        ("intelligent", "silly"),   ("sometimes", "often"),     
        ("asleep", "awake"),        ("divide", "unite"),        ("land", "take off"),       ("sour", "sweet"),          
        ("attack", "defence"),      ("division", "unity"),      ("large", "small"),         ("start", "stop"),          
        ("attic", "cellar"),        ("divorce", "marriage"),    ("last", "first"),          ("stranger", "native"),     
        ("autumn", "spring"),       ("divorced", "married"),    ("learn", "teach"),         ("strict", "gentle"),       
        ("awful", "nice"),          ("domestic", "foreign"),    ("left", "right"),          ("strong", "weak"),         
        ("back", "front"),          ("down", "up"),             ("less", "more"),           ("student", "teacher"),     
        ("background", "foreground"),("downstairs", "upstairs"),("let", "forbid"),          ("suburb", "centre"),       
        ("backward", "forward"),    ("dry", "humid"),           ("lie", "stand"),           ("summer", "winter"),       
        ("bad", "good"),            ("dull", "interesting"),    ("life", "death"),          ("sun", "moon"),            
        ("beautiful", "ugly"),      ("early", "late"),          ("like", "hate"),           ("suspect", "trust"),       
        ("beauty", "ugliness"),     ("east", "west"),           ("liquid", "solid"),        ("tall", "small"),          
        ("begin", "end"),           ("emigrate", "immigrate"),  ("little", "much"),         ("thick", "thin"),          
        ("beginning", "end"),       ("emigration", "immigration"),("long", "short"),        ("throw", "catch"),         
        ("behind", "front"),        ("empty", "full"),          ("lose", "win"),            ("tight", "loose"),         
        ("best", "worst"),          ("ending", "beginning"),    ("loser", "winner"),        ("tomorrow", "yesterday"),  
        ("better", "worse"),        ("enemy", "friend"),        ("loud", "quiet"),          ("town", "village"),        
        ("big", "small"),           ("enjoy", "hate"),          ("love", "hate"),           ("tragedy", "comedy"),      
        ("birth", "death"),         ("enter", "leave"),         ("lovely", "terrible"),     ("useful", "useless"),      
        ("bitter", "sweet"),        ("entrance", "exit"),       ("lower", "raise"),         ("valley", "mountain"),     
        ("black", "white"),         ("even", "odd"),            ("misfortune", "fortune"),  ("visitor", "host"),        
        ("blunt", "sharp"),         ("everybody", "nobody"),    ("nasty", "nice"),          ("waste", "save"),          
        ("body", "soul"),           ("everything", "nothing"),  ("nephew", "niece"),        ("weak", "powerful"),       
        ("boring", "exciting"),     ("exclude", "include"),     ("new", "ancient"),         ("wealthy", "poor"),        
        ("borrow", "lend"),         ("export", "import"),       ("no", "yes"),              ("wedding", "divorce"),     
        ("bottom", "top"),          ("exposure", "shelter"),    ("noisy", "quiet"),         ("well", "ill"),            
        ("boy", "girl"),            ("extreme", "moderate"),    ("noon", "midnight"),       ("wet", "dry"),             
        ("brave", "cowardly"),      ("fail", "succeed"),        ("normal", "strange"),      ("wide", "narrow"),         
        ("break", "fix"),           ("failure", "success"),     ("north", "south"),         ("woman", "man"),           
        ("broad", "narrow"),        ("false", "true"),          ("now", "then"),            ("women", "men"),           
        ("brother", "sister"),      ("far", "near"),            ("occupied", "vacant"),     ("young", "old"),           
        ("build", "destroy"),       ("fast", "slow"),           ("off", "on"),              
        ("busy", "lazy"),           ("fat", "slim"),            ("often", "seldom"),        
        ("buy", "sell"),            ("female", "male"),         ("old", "modern"),          
        ("calm", "excited"),        ("few", "many"),            ("opponent", "supporter"),  
        ("careful", "careless"),    ("final", "first"),         ("order", "mess"),          
        ("catch", "miss"),          ("find", "lose"),           ("ordinary", "special"),    
        ("ceiling", "floor"),       ("finish", "start"),        ("other", "same"),          
        ("centre", "outskirts"),    ("flat", "hilly"),          ("over", "under"),          
        ("certainly", "probably"),  ("follow", "lead"),         ("part", "whole"),          
        ("changeable", "constant"), ("foreigner", "native"),    ("partial", "total"),       
        ("cheap", "expensive"),     ("forget", "remember"),     ("pass", "fail"),
    )

