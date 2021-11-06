image bg starboard = "bg starboard.png"
image bg townsquare = "bg townsquare.png"
image laynormal = "Lay1.png"
image laytalk = "Lay2.png"
image layangry = "Lay3.png"
image layeyesclosed = "Lay4.png"
image laycry = "Lay5.png"
image laysmile = "Lay6.png"
image layblush = "Lay7.png"
image flower1 = "flower1.png"
image splashscreen = "splash.png"
image dicoangry = "Dico1.png"
image dicohappy = "Dico2.png"
image dicosalute = "Dico3.png"
image dicogun = "Dico5.png"
image diconormal = "Dico4.png"
image cloudnormal = "Cloud1.png"
image cloudeyesclosed = "Cloud2.png"
image cloudhappy = "Cloud4.png"
image cloudangry = "Cloud3 (2).png"
image cloudcry = "Cloud5.png"
image bg art = "bg art.png"
image crochappy = "Croc1.png"
image crocsad = "Croc2.png"
image crocmad = "Croc3.png"
image croctalk = "Croc4.png"
image crocnormal = "Croc5.png"
image bg gen2 = "bg gen2.png"
image dubangry = "Dub1.png"
image dubsmug = "Dub2.png"
image dubtalk1 = "Dub3.png"
image dubangry = "Dub5.png"
image dubsmile = "Dub6.png"
image dubmeh = "Dub7.png"
image bg pol = "bg pol.png"
image crinnorm = "Crin1.png"
image crintalk = "Crin2.png"
image crinhappy = "Crin3.png"
image crinmad = "Crin4.png"
image crincry = "Crin5.png"
image crinangry = "Crin6.png"
image crinhuh = "Crin7.png"
image bg gen1 = "bg gen1.png"
image dicosuitnerv = "dicosuit1.png"
image dicosuitsmile = "dicosuit2.png"
image dicosuithap = "dicosuit3.png"
image dicosuitbro = "dicosuit4.png"
image bg credit = "bg credits.png"
image avenorm = "Average6.png"
image avesus = "Average1.png"
image avesad = "Average2.png"
image avemad = "Average3.png"
image avehap = "Average4.png"
image avebored = "Average5.png"
image fbinorm = "Fbi1.png"
image fbihap = "Fbi2.png"
image fbimad = "Fbi3.png"
image fbismile = "Fbi4.png"
image fbisad = "Fbi5.png"
image fbidead = "Fbi6.png"
image fbitroll = "Fbi7.png"
image sourcry = "SourCry.png"
image sourhap = "SourHappy.png"
image sournorm = "SourNorm.png"
image soursad = "SourSad.png"
image soursmi = "SourSmile.png"
image swepnorm = "Swep1.png"
image swepeyesclosed = "Swep2.png"
image swephuh = "Swep3.png"
image swepflust = "Swep4.png"
image swepcry = "Swep5.png"
image swepangry = "Swep6.png"
image swepblush = "Swep7.png"
image sweptalk = "Swep8.png"
image swepsmile = "Swep9.png"
image swepblushtalk = "Swep10.png"
image over = "over.png"
image polo = "bg polo.png"
image polon = "bg polon.png"
image lads = "bg lads.png"
image movie = Movie(xpos=0, ypos=0, delay=11)
image chap2 = "chap2.png"
image fan = "wow.png"
image nexnorm = "Nex1.png"
image nexsmile = "Nex2.png"
image nexangry = "Nex3.png"
image nexmadtalk = "Nex4.png"
image caryblush = "Caryblush.png"
image carycry = "Carycry.png"
image caryhappy = "Caryhappy.png"
image carymad = "Carymad.png"
image carynorm = "Carynorm.png"
image carysans = "Carysans.png"
image carysmile = "Carysmile.png"
image carytalk = "Carytalk.png"
image carytroll = "Carytroll.png"
image crinfr = "crin_sprite.png"
image bg pilk = "bg pilk.png"

default gen1 = False
default dpoints = False
default lpoints = False
default trollars =True
default menuset = set()
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Lay = Character("Lay",
                     who_color="#99C7E5" , callback = callback)

define F = Character("Sun",
                    who_color="#F7DB97", callback = callback)

define Dubya = Character("Dubya",
                    who_color="#D83060", callback = callback)
define Cloud = Character("Cloud",
                    who_color="#75bbd9", callback = callback)

define Dico = Character("Dico",
                    who_color="#7D00FF", callback = callback)

define config.main_menu_music = "af5v.mp3"

define Crocidy = Character("Crocidy",
                    who_color="#900C3F", callback = callback)

define Crin = Character("Crin",
                    who_color="#ADDDF3", callback = callback)

define Sour = Character("Sour",
                    who_color="#99E09F", callback = callback)

define Swep = Character("Swep",
                    who_color="#EDC3FD", callback = callback)


define Average = Character("Average",
                    who_color="#ACE599", callback = callback)

define FBI = Character("FBI",
                    who_color="#99E09F", callback = callback)


define T = Character("T",
                    who_color="#581845", callback = callback)

define You = Character("You",
                    who_color="#ffffff", callback = callback)

define q = Character("???",
                    who_color="#ffffff", callback = callback)

define config.autosave_frequency = 10



label splashscreen:
 scene black
with Pause (1)

show splashscreen with dissolve
with Pause(2)
hide splashscreen with dissolve

return



label start:
    $ trollars = 0
    $ items = []
    play music "EIETqr1JNJdu.128.mp3" fadein 2.0
    "Long, Long ago. In a place far away. There was a place called Twitter..."
    "Twitter was a land full of an adventurous bunch, from all over the world."
    "It was a safe haven for fandoms alike."
    "Well it used to be..."
    "You see, an evil cult started to arise."
    "They turned the land from a joyous safe haven, into a miserable wasteland."
    "And it was all because of one man."
    " {color=#ACE599}Dream{/color}."
    " {color=#ACE599}Dream's{/color} malice spread throughout the kingdom, taking tyranny along with it"
    "He took his place as the unrightful owner of the throne."
    "Soon, {color=#ACE599}Dream's{/color} malice started to corrupt people's minds, mostly children, turning members of society into obsessed stans."
    "Although,"
    "there was some light at the end of the tunnel."
    "Uncorrupted children began to speak out against {color=#ACE599}Dream's{/color} manipulation, one child standing out from the rest...  "
    "{color=#ACE599}Average{/color}"
    "The children of light banded together as a desperate means for survival. Thus, {color=#ACE599}L'stanberg{/color} was born..."

stop music fadeout 2.0


### intro done basedddddd okkk time to work on the sprites or some shit

label background:

play music "A New Chapter.mp3" fadein 1.0 fadeout 1.0
scene bg starboard
with dissolve

"You take a good look at the sign in front of  you and wonder where you are..."

q "Hey?"
"You hear a strange voice from out of nowhere."
show laynormal
with dissolve

with zoomin
show laytalk
q "You seem new?"
q  "What's your name??"

python:

    name = renpy.input("What is your name?", length=32)
    name = name.strip()

    if not name:
        name = "Dumbass"

if name == "rnexus" or name == "Rnexus":
    Lay "Lol stupid!!111"

if name == "bleach" or name == "Bleach":
    Lay "Super mega gay"

if name == "MichealP" or name == "michealp":
   Lay "Every Micheal P Scream (As of 07_10_16: https://www.youtube.com/watch?v=sglcHw5OK88"

if name == "cary" or name == "Cary":
    Lay "wtf cary!?!?!?!?!???!!!!"
    Lay "Adobe Flash CS6 Cracked Free 2020 Google Drive.rar"


if name == "Crin" or name == "crin":
    Lay "Oh hi crin :)"

if name == "average" or name == "Average":
    show laysmile
    Lay "AWOOGA HUMANA HUMANA AVERAGE ME AMOR :HEART: :HEART:"

if name == "Gerno":
    Lay "Gerno stop playing KSP 24/7"

if name == "schloob":
    Lay "schloob"

if name == "Kosma":
    $ renpy.quit()

if name == "Texas":
    $ renpy.quit()


if name == "Dream" or name == "dream" or name == "Dreamwastaken" or name == "dreamwastaken":
     #python:
       # try: sys.modules['renpy.error'].report_exception("LOL, GET FUCKED! Man, I used to be such a big fan of you dream. Why are you so scared to call out your fans. Stop hiding behind 'Its only a small perrcentage of my community. Fuck off. Choose a new name.", False)
       #except: pass
      $ _skipping = False
      $ renpy.movie_cutscene("dream_fight_HD.ogv")
      $ renpy.quit()




if name == "Gogy" or name == "gogy":
    Lay "Disgusting"
    $ renpy.quit()


if name == "CD" or name == "cd":
    Lay "Cracker balls"
    $ renpy.quit()

if name == "Cloud" or name == "cloud":
    Lay "I hate women."

if name == "Sour" or name == "sour":
    Lay "sour here you cant take that name thats mine twat"


if name == "gaster" or name == "Gaster":
     Lay "=)"
     $ renpy.quit()

if name == "pilk" or name == "Pilk":
    jump pilk

else:

    show laysmile

    Lay "Nice to meet ya [name], my name is Lay!"
    # bro
    show laynormal
Lay "Wait a minute... How did you get here?"

menu:

    set menuset
    "How did you get here?"

    "You got lost.":
        show layeyesclosed
        Lay "Oh man, you're a bit stupid arent ya?"

        Lay "Anyways, I might as well show you around while you're here."

    "Idk":
        show laynormal
        Lay "Hmmm, sus..."

        show laysmile
        Lay "Anyways, I might as well show you around while you're here."

label after_menu:
  show laynormal
  "Lay grabs you by the arm and starts dragging you with her."


label lstanberg:
with dissolve
scene black
"Lay stops dragging you and shows you the water fountain."
show bg townsquare

with dissolve
"It was a statue of the town's mascot, the Trollface, standing in a pool of liquid gold that seemed to be coming from the mascots hands."
"There, a narrow cobblestone path was coming from the starboard ; a massive field of brightly coloured grass surrounding the fountain."
"Next to the fountain was a huge sign with \"cover yourself in OIL\" written on it."
"You suddenly feel the urge to cover yourself with the blissful fluid that was gently glistening in the sun."

show laysmile
with dissolve
Lay "Beautiful, isn't it?"
Lay "Average was so happy when it was installed."
Lay "It's the town's pride and joy. "
show laynormal


call screen flower with dissolve

label funny:
"What a funny looking sun."


F "fucking idiots."

show layangry
Lay "Oh fuck off!"

show laytalk
Lay "Don't mind him."
Lay "He always comes, starts shit and then disappears. Fucking coward."



show laysmile




Lay "Anyways where do you want to go next?"


menu:
    set menuset
    "Where do you want to go?"

    "General-1":
        hide laytalk
        hide laysmile
        show layeyesclosed
        Lay "Oh boy, my favourite place..."
        jump general1





    "General-2":
        hide laytalk
        hide laysmile
        show laynormal
        Lay "Not many people go here actually, but I'll still show you."
        jump general2






    "Lstanberg Art Department":
        hide laytalk
        hide laysmile
        show laysmile
        Lay "I love this place come on!"
        jump art



    "Can I leave instead?":
        hide laytalk
        hide laysmile
        show layangry
        Lay "Shit yourself!!"

        $ renpy.quit





## image button innit lmao
screen flower:
    imagebutton:
        idle "flower_idle.png"
        hover "flower_hover.png"
        xanchor 1
        yanchor 1
        xpos 0.11123
        ypos 3
        action Jump("funny")

label general1:
$ gen1 = True 
stop music fadeout 1.0
play music "Circ Of Quirk.mp3" fadein 1.0
scene bg gen1 with dissolve

"As you walk in #general, you can hear yelling, and what appears to be two people having an argument."
"You then see a mysterious purple figure throwing stupid pictures on what seems to be a poker table... that nobodys even playing poker on."
show dubsmug at right
Dubya "I love women."
show cloudnormal at left
Cloud "I hate women."
show dubangry at right
Dubya "I LOVE women."
show cloudangry at left
Cloud "Well, I HATE women."

Dubya "Your opinion won't make me not love women."
Cloud "It should, because I hate women!"
hide dubangry
hide cloudangry
hide dubsmug
hide cloudnormal
"You spot the commotion and go join in with Lay."
show cloudnormal
Cloud "New face around here eh?"
show cloudhappy
Cloud "Name's Cloud. Guy I was talkin' to Dubya"
hide cloudhappy
hide cloudnormal
show dubsmug
Dubya "I love women."
hide dubsmug
show cloudeyesclosed
Cloud "Hngh, he's getting on my nerves. Hey [name], whose opinion do you think is better?"


menu:
    set menuset
    "What clan are you willing to join?"


    "I love women.":
        hide cloudeyesclosed
        show laytalk
        Lay "Haha, sorry about this but you're not allowed to choose a clan without getting{color=#ACE599} verified{/color} yet. "
        show laysmile
        Lay "Maybe we can come back when you're done!"
        hide laysmile

    "I hate women.":
        hide cloudeyesclosed
        show laytalk
        Lay "Haha, sorry about this but you're not allowed to choose a clan without getting {color=#ACE599} verified{/color} yet. "
        show laysmile
        Lay "Maybe we can come back when you're done!"
        hide laysmile

hide laysmile
hide laytalk

show dubangry
Dubya "Well, that doesn’t matter because I love women!"
show cloudangry at left with easeinleft
Cloud "grr.. I HATE WOMEN!"
hide cloudangry
hide dubangry
"This goes on for another 10 minutes,"
with vpunch
"Until another man walks into the room and slams on the poker table, scattering the chips everywhere."
show dicoangry with dissolve
Dico "SHUT THE FUCK UP, YOU TWO!"
Dico "WE DON'T CARE ABOUT WOMEN!"
hide dicoangry
show cloudeyesclosed
Cloud "Well, it’s not MY fault that DUBYA loves women!!"
hide cloudeyesclosed
show dubtalk1
Dubya "Well, it’s not MY-"
hide dubtalk1
show dicoangry
Dico " I said SHUT UP ABOUT WOMEN!"
hide dicoangry
"Cloud and Dubya grumble and stop arguing about women."
show diconormal
Dico "Sorry about that, they tend to argue over women… "
show dicoangry
Dico " an unhealthy amount actually..."
hide diconormal
hide dicoangry

show dicosalute
Dico " My name is Dico, I’m a Trial mod and I’ll be happy to-"
Dico "oh… hey Lay."

hide dicosalute
hide dicoangry

with vpunch
show dicohappy at left with easeinleft
show layeyesclosed at right  with easeinright
Lay "Yeah, I’ll take it from here, just make sure those 2 stop fucking arguing about women."
"You could hear shouting from the background."
hide dicohappy
hide layeyesclosed

show cloudangry at left
Cloud "I HATE WOMEN."
show dubangry at right
Dubya "I LOVE WOMEN."

hide cloudangry
hide dubangry

show dicoangry
Dico "I’ll go deal with them."

if name == "Marcel":
    Dico "I hate [name]"

else:


    Dico "The only way it could possibly get any worse is if Marcel was here,"
    Dico "and he’s probably playing some furry game or something right now."


show dicohappy
Dico "Oh, sorry, I’m rambling again, I’ll go deal with them, see ya!"
hide dicohappy
hide dicoangry
show layeyesclosed at center with dissolve
Lay "Alright, where do want go to next?"

menu:
    set menuset

    "General-2":
        show layeyesclosed
        Lay "Oh boy..."
        jump general2

    "Lstanberg Art Department":
        show laysmile
        Lay "I'm so excited!"
        jump art







return







label general2:
stop music fadeout 1.0
play music "bitch.mp3" fadein 1.5
scene black
"As you and Lay walked through the bustling city, you wonder to yourself, What is General-2?"
"The city was abnormal. Everywhere you looked, a different scene was going on."
"Like when you saw a talking cheeseburger while you were passing through the market."
"Or when you saw a man dressed in a Megaman costume running around with bread in his mouth."
"Or the time you saw a \"Gangster\" screaming Bonk clan when you where passing the L'stanberg Art department."
"This city was truly cursed."


show laynormal
Lay "We're here!"
show bg gen2 with dissolve
hide laynormal
show laytalk
Lay "This is where everyone in the town goes when General 1 is locked..."

menu:

    set menuset
    "Why is General 1 locked?":
        show layeyesclosed
        Lay " {color=#ACE599}Riots...{/color}"
        Lay "lots and lots of riots."
        Lay "They always get angry so we have to shut everything down to make sure no one gets hurt..."

    "Why is it so empty right now?":
        show layeyesclosed
        Lay "We havent had a riot in a while..."

show laycry
Lay "Come on lets go.."
Lay "This place just makes me sad."
jump verfi





return


label art:
stop music fadeout 1.0
play music "Kingdom (Day Theme).mp3" fadein 2.0
scene bg art with dissolve
"Lay stops you."
show laysmile
Lay "I love this place! It's where all the artists live."
Lay "Look, there's one over there!!"
hide laysmile
show laytalk at right with easeinright
show crocnormal at left with easeinleft
Crocidy "Yo!"
hide laytalk
show laysmile at right
Lay "Hi, Crocidy!"
Lay "Long time no see!"
hide crocnormal
show crochappy at left
Crocidy "Yeah, it's been a while!"
hide crochappy
show croctalk at left
Crocidy "Who's this?"
hide laysmile
show laytalk at right

Lay "Oh this is [name]!"
Crocidy "OH SHIT! Welcome!"
if name == "Michealp" or name == "michealp":
    show crochappy at left
    Crocidy "HOLY SHIT!! MICHEAL P?"
    Crocidy "THE GUY FROM Every Micheal P Scream (As of 07_10_16): https://www.youtube.com/watch?v=sglcHw5OK88"
    Crocidy "YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    hide crochappy
show crocnormal at left
Crocidy "Although currently the art depo is busy so we have limited visits today. Maybe come back later! :)"
show layeyesclosed at right
Lay "Ah, that sucks. Welp let's get going [name]."
Lay "See ya croc!"

hide crocnormal
hide layeyesclosed
hide crochappy
hide croctalk
hide layeyesclosed
hide laytalk

"You and Lay get going, making your way towards General 2."

jump general2
return



jump art

label verfi:
stop music fadeout 1.5
scene black
"Lay grabs your hand and starts walking to a destination unbeknownst to you."
"You try asking her where you are going but she doesn't answer..."
"Finally she stops you, infront of you seemed to be a police station."
"Before you can say something, she starts talking."
show layeyesclosed
Lay "We have to do this."
show laycry
Lay "I'm sorry."

hide layeyesclosed
hide laycry

"She grabs your hand once more and you both step inside the police station"
scene bg pol
play music "AveragesTheme.mp3" fadein 1.0
with dissolve
"You see someone telling jokes to what seems to be the inmates of the police station."
show crinhappy
Crin "And then I said,"
Crin "Sussy Bal-"
hide crinhappy
show sourhappy at right with vpunch
show fbitroll at left with vpunch
show crinhappy
Crin "Oh Hi Lay!"
hide sourhappy
hide fbitroll
hide crinhappy
show crinhuh
Crin "Who the fuck is this??"
show laysmile at right with easeinright
Lay "This guy? they're new around here."
hide crinhuh
show crinnorm
show laynormal at right
Crin "Oohhh.. well what's this lad doing here then?"
hide laynormal at right
hide laysmile at right
show layeyesclosed at right
Lay "I'm gonna verify them to make them an official member."
show crintalk
Crin "Right then, bring them to the desk."
hide crintalk
hide layeyesclosed
hide crinnorm
"She brings you over to the police station's desk"
"2 people in the cells next to you, all with prison tags that read Sour and FBI."
Sour "Can't believe I got a bloody life sentence for beating up that stupid {color=#ACE599}Dream{/color} worshipper."
show crinhuh
Crin "Sour, you got a life sentence for police brutality. The fuck you on about?"
show layeyesclosed at right
Lay "Yikes..."
hide crinhuh
hide layeyesclosed

show laynormal

Lay "FBI, you still have another hour on your visit, and Sour, Well.."
hide laynormal
show fbinorm with dissolve
FBI "Got it."
hide fbinorm

show soursad
Sour "Yeah yeah.. piss off :(."
hide soursad
with vpunch
"Suddenly a man dressed in a green vneck sweater and a black fedora enters the station,"
"sits down and pulls back his matching fedora, rubbing a promise ring on his finger, and looks at you."
show layblush
Lay "Average."
hide layblush
show avehap
Average "Lay."
"How is this man talking?"
hide avehap
show avenorm
Average "I'm here to oversee this entire interrogation, Bring Dico in to play starboard with the inmates."
scene black
"..."
"What's happening?"

"Sorry mate Crin is shit at programming the funny mini game so you get sent to the chap 1 part 2lol!!"

scene black with dissolve
stop music fadeout 1.0
play music "tman.mp3" fadein 1.0

scene bg polo with dissolve
show laysmile with dissolve
Lay "Welcome to L'stanberg"
hide laysmile
show laytalk
Lay "I'm suprised you survived starboard!"

menu:
    "I didn't even play starboar-":
        You "I didn't even play starboar-"

        "Lay interupts you and continues speaking"

    "Thanks!":
        You "Thanks!!"

hide laytalk
show layeyesclosed
Lay "Oh Yeah!!{color=#7D00FF} Dico{/color} is gonna be joining us. "
if gen1 == False:
    You "Dico? Whose that?"
    Lay "He's a trial mod here."
    Lay "You were supposed to meet him back in general 1."
    You "Ooh. I hope he's nice..."
else:
    hide laytalk
hide layeyesclosed
show laytalk at left with easeinleft
show dicohappy at right  with easeinright
Dico "Yo!"
Dico "Average said I could come with you guys on the tour!"
menu What:
    "What should you say?"
    "That's Great!":
        You "That's Great, I can't wait to continue the tour with you!"
        $ dpoints = True
        hide dicohappy
        show diconormal at right
        Dico "I know right!!"
        $ dpoints += 1
        show over
        "{color=#ACE599}You just gained A Dico Relationship Point!{/color}"


    "Oh, for fuck sakes":
        You "Oh, for fuck sakes, why do you have to come?"
        $ dpoints = True
        hide dicohappy 
        show dicoangry at right
        Dico "Bro? What the fuck?"
        $ dpoints -= 2
        hide laytalk
        show layeyesclosed at left 
        Lay "Ignore them."
        show over
        "{color=#ACE599}You just lost A Dico Relationship Point!{/color}"

You "Where did that come from?"
"{color=#ACE599}Don't question it.{/color}"
"{color=#ACE599}Everyone in this game has relationship points{/color}"
"{color=#ACE599}The more points you have for that character, the more they trust you.{/color}"
"{color=#ACE599}If you have enough points with them, you can enter special scenes with them.{/color}"
"{color=#ACE599}And vice versa, If you have enough points in the negative numbers then{/color}"
"{color=#ACE599}You can also enter different scenes with that character.{/color}"
You "Cool."
hide over
hide layeyesclosed
hide laytalk 
hide dicoangry 
hide diconormal 
"You spot 2 people leaving the police station hand in hand."
"One of them you recognise."
You "Is that Crin?"
show laynormal
Lay "Wha?"

You "She dropped something"
hide laynormal
"You, Dico and Lay go to pick up what looks like a book of the ground."
show fan 
You "It looks like fanfiction."
Lay "Open it :troll:"
"You open the book. and start reading the pages."
"Chapter 4: Love has no bounds."
"'swep: i love u'"
"'crin: no i love u more'"
"'swep: not as much as i love u'"
"'crin: i still love u more'"
"'crin: then show it~'"
"'swep then kisses crin softly and deeply'-"
with vpunch 
"You immediately close the book in dread."
You "My eyes."
Lay "I-Im so fucking sorry."
Dico "I think we should leave it here."
Dico "Crin will get pretty {color=#ACE599}Angry{/color} if she sees you with that book."
default fan = False
menu:
    "Take the book?"
    "Yes":
        $ fan = True
        You "I think we will be fine..."
        "{color=#ACE599}Crin x Swep fanfiction has been added to your inventory.{/color}"
    "No":
        You "Yeah you're right."
        "You leave the book on the floor, leaving it for the next unlucky person to stumble upon this abomination."
hide fan with dissolve

scene bg lads with dissolve 

You "Where are we gonna go next??"
if gen1 == True:
    Lay "We're going back to General 1 to so you can join a clan. I told ya you can join on when you're verified. "
    You "Oh yeah, I forgot."
else:
   Lay "We are going to General 1 because I forgot to take you there."
   Lay "I must tell ya, that place is the most unfunniest place here. "
   You "Is it really that {color=#ACE599}bad?{/color}"
   Dico " Yeah it really is."
   You "Damn"
   Lay "{color=#ACE599}And dont get me started on how petty the mafia is.{/color}"
   "Wait wait wait, mafia?"  
   You"what?"  
   Dico "We will explain later..."

show black with dissolve
"They all make it to starboard. The area you found yourself at in the beginning."
stop music fadeout 2.0
play audio "damn.wav" volume 2.0
""
show laynormal with dissolve

Lay "Wait Hold on Guys."
Lay "I gotta get this."
label chappy2fr:
scene black with fade
show chap2 with dissolve
with Pause(2)
hide chap2 with dissolve

# AYO ITS THE ACTUAL FUCKING START OF TADL FINALLY OH MY FUCKING GOOOOOOOOOOOOOOOOOOOOOOOD. 
$ renpy.movie_cutscene("lay.ogv")
$ _skipping = False 

scene bg starboard with dissolve
"You see Lay with her phone in her hand looking frantically."
"As if she was about to cry."
show laycry with vpunch
Lay "{size=-2}dad...{/size}"
"You and Dico reach out for her."
You "{size=+12}LAY! Lay are you ok?!{/size}"
Dico "What happened??!"

Lay "we gotta go. Ave needs us."
scene black with dissolve
play music "panic.wav" fadein 4.0
"Lay wipes her tears and grabs you and Dico by the arm."
"They then start bolting to general 1 with you and dico closely behind her."
You "WHY WE ARE RUNNING???"
You "WHAT THE FUCK IS GOING ON???"
Lay "THERE'S NO FUCKING TIME TO EXPLAIN."
Lay "WE GOTTA SHUT THE PLACE DOWN."

"As the three of you run frantically towards the capital, you can't help but be scared."
"Your heart is racing."
"It's hard to breath."
"It is as if your whole body has switch on panic mode."
"Your mind is filled to the brim of questions,"
"Why are we running?"
"What's happening in Gen 1?"
"Why's Lay crying? Is she ok?"
"As you mind fill up with scared thoughts about your current situation, the sun stared down at you,"
"Flashing its mocking smile at you."
"'It definitely knows what's going on.' You think.'"
"'i just hope everyone is ok...'"



show over with fade
stop music
play music "Shore Side.mp3"
 
Crin "Hey!"
Crin "We probably haven't met before. I'm Crin."
Crin "I'm the lead dev of Tadl and I just wanted to quickly thank you for all this."
Crin "I also want to thank: Cary for helping with the animated cutscenes, Adel for the Music and All the people who has help with the game till this point"
Crin "I hope you enjoyed this mini update :)"
Crin "I dont have much time to work on this any more but its always really fun when i have the chance too."
Crin "Once again thank you for all of your suppport :)"
Crin "Be sure to expect alot more updates around christmas time. "
Crin "As I wont have school by then."
Crin "Alright its time for me to go. :))"
Crin "Goodbye!"
return 


label pilk:
stop music 
play music "milk.mp3"
scene bg pilk with dissolve
" "



































































































