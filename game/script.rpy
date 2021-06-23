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

default trollars = True
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



define Average = Character("Average",
                    who_color="#ACE599", callback = callback)

define FBI = Character("FBI",
                    who_color="#99E09F", callback = callback)



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

Lay "Hey?"
"You hear a strange voice from out of nowhere."
show laynormal
with dissolve

with zoomin
show laytalk
Lay "You seem new?"
Lay "What's your name??"

python:

    name = renpy.input("What is your name?", length=32)
    name = name.strip()

    if not name:
        name = "Dumbass"

if name == "rnexus":
    Lay "Lol stupid!!111"


if name == "Rnexus":
    Lay "Lol stupid!!111"

if name == "agata":
    show layangry
    Lay "We are going to turn you into a smoothie. :D"
    $ renpy.quit()



if name == "Agata":
    show layangry
    Lay "We are going to turn you into a smoothie. :D"
    $ renpy.quit()




if name == "Jfify":
    show layangry
    Lay "Go suicide bait some where else you git."
    $ renpy.quit()

if name == "jfify":
    show layangry
    Lay "Go suicide bait some where else you git."
    $ renpy.quit()

if name == "cary":
    Lay "wtf cary!?!?!?!?!???!!!!"
    Lay "Adobe Flash CS6 Cracked Free 2020 Google Drive.rar"

if name == "Cary":
    Lay "wtf cary!?!?!?!?!???!!!!"
    Lay "Adobe Flash CS6 Cracked Free 2020 Google Drive.rar"


if name == "Crin":
    Lay "Oh hi crin :)"


if name == "crin":
    Lay "Oh hi crin :)"

if name == "Average":
    show laysmile
    Lay "AWOOGA HUMANA HUMANA AVERAGE ME AMOR :HEART: :HEART:"


if name == "average":
    show laysmile
    Lay "AWOOGA HUMANA HUMANA AVERAGE ME AMOR :HEART: :HEART:"

if name == "Gerno":
    Lay "Gerno stop playing KSP 24/7"


if name == "gerno":
    Lay "Gerno stop playing KSP 24/7"


if name == "schloob":
    Lay "schloob"

if name == "Kosma":
    $ renpy.quit()

if name == "Texas": 
    $ renpy.quit()


if name == "Dream":
    python:
        try: sys.modules['renpy.error'].report_exception("LOL, GET FUCKED! Man, i used to be such a big fan of you dream. Why are you so scared to call out your fans. Stop hiding behind 'Its only a small perrcentage of my community. Fuck off. Choose a new name.", False)
        except: pass
      
    
    $ renpy.quit()

if name == "dream":
    python:
        try: sys.modules['renpy.error'].report_exception("LOL, GET FUCKED! Man, i used to be such a big fan of you dream. Why are you so scared to call out your fans. Stop hiding behind 'Its only a small perrcentage of my community. Fuck off. Choose a new name.", False)
        except: pass
      
    
    $ renpy.quit()

if name == "Dreamwastaken":
    python:
        try: sys.modules['renpy.error'].report_exception("LOL, GET FUCKED! Man, i used to be such a big fan of you dream. Why are you so scared to call out your fans. Stop hiding behind 'Its only a small perrcentage of my community. Fuck off. Choose a new name.", False)
        except: pass
      
    
    $ renpy.quit()


if name == "Gogy":
    $ renpy.quit()


if name == "gogy":
    $ renpy.quit()

if name == "CD":
    Lay "Cracker balls"
    $ renpy.quit()

if name == "cd":
    Lay "Cracker dick"
    $ renpy.quit()

if name == "Cloud":
    Lay "I hate women."



else:

    show laysmile

    Lay "Nice to meet ya [name]!"
    # bro
    show laynormal
Lay "Wait a minute... How did you get here?"

menu:

    set menuset
    "How did you get here?"

    "You got lost.":
        show layeyesclosed
        Lay "Oh man, you're a bit stupid arent ya?"

        Lay "Anyways, i might as well show you around while you're here."

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
"It was a statue of the town's mascot, the trollface, standing in a pool of liquid gold that seemed to be coming from the mascots hands."
"There, a narrow cobblestone path was coming from the starboard ; a massive field of brightly coloured grass surrounding the fountain."
"Next to the fountain was a huge sign with \"cover yourself in OIL\" written on it."
"You suddenly feel the urge to cover yourself with the blissful fluid that was gently glistening in the sun."

show laysmile
with dissolve
Lay "Beautiful, isn't it?"
Lay "Average was so happy when it was installed."
Lay "It's the town's pride and joy. "
show laynormal


call screen flower
with dissolve

label funny:
"What a funny looking sun."


F "fucking idiots."

show layangry
Lay "Oh fuck off!"

show laytalk
Lay "Don't mind him."
Lay "He always comes, starts shit and then disapear. Fucking coward."

show laysmile




Lay "Anyways where do you want to go next?"


menu:
    set menuset
    "Where do you want to go?"

    "General-1":
        show layeyesclosed
        Lay "Oh boy, my favourite place..."
        jump general1





    "General-2":
        show laynormal
        Lay "Not many people go here actually, but i'll still show you either way."
        jump general2






    "Lstanberg Art Department":
        show laysmile
        Lay "i love this place come on!"
        jump art






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
stop music fadeout 1.0
play music "Circ Of Quirk.mp3" fadein 1.0
scene black

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

Dubya "Your opinion won't make me want to not love women."
Cloud "It should, because I hate women!"
hide dubangry
hide cloudangry
hide dubsmug
hide cloudnormal
"You spot the commotion and go join in with Lay."
show cloudnormal
Cloud "New face around here eh?"
show cloudhappy
Cloud "Name's Cloud. Guy I was talkin' to's Dubya"
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
"Until another man walks into the room and slams on the poker table, splattering the chips everywhere."
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


    Dico "The only way it could get worse is if marcel was here,"
    Dico "and he’s probably playing some furry game or something right now."


show dicohappy
Dico "Oh, sorry, i’m rambling again, I’ll go deal with them, see ya!"
hide dicohappy
hide dicoangry
show layeyesclosed at center with dissolve
Lay "Hey, how about we head to the shop? I'm starving."

menu:
    set menuset

    "General-2":
        show laynormal
        Lay "I guess eating could wait, come on Let's go."
        jump general2

    "Shop":
        show laysmile
        Lay "Man, wait till you see the food here!"
        jump shop







return







label general2:
stop music fadeout 1.0
play music "bitch.mp3" fadein 1.5
scene black
"As you and Lay walked through the busingling city, you wonder to your self, What is General-2?"
"The city was abnormal. Every where you looked, a different scene was going on."
"For example of when you saw a talking cheeseburger while you were passing through the market with Lay."
"Or when you saw a man dressed in a megaman costume running around with bread in his mouth."
"Or the time you saw a \"Gangster\" screaming Bonk clan when you where passing the L'stanberg Art department."
"This city was truly cursed."


show laynormal
Lay "We're here!"
show bg gen2 with dissolve
hide laynormal
show laytalk
Lay "This is where everyone one in the town goes when General1 is locked..."

menu:

    set menuset
    "Why is General1 locked?":
        show layeyesclosed
        Lay " {color=#ACE599}Riots...{/color}"
        Lay "lots and lots of riots."
        Lay "They always get angry so we have to shut everything down to make sure no one gets hurt..."
    
    "Why is it so empty right now?":
        show layeyesclosed
        Lay "We havent had a contraversy in a while..."

show laycry
Lay "Come on lets go.."
Lay "This place makes me more than sad."
jump verfi





return


label art:
stop music fadeout 1.0
scene bg art with dissolve 
"Lay stops you."
show laysmile
Lay "I love this place! It's where all the artist live."
Lay "Look! There's one over there!!"
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
show crocnormal at left
Crocidy "Although currently the art depo is busy so we have limited visits today. Maybe come back later! :)"
show layeyesclosed at right
Lay "Ah, that sucks. Welp lets get going [name]."
Lay "See ya croc!"

hide crocmad
hide layeyesclosed
"You and Lay get going, making your way to General2."

jump general2
return

label shop:
scene black 
hide laysmile
hide layeyesclosed
hide dicoangry

stop music fadeout 1.0
play music "lstanberg_shop.mp3" fadein 1.0 fadeout 1.0

"You and Lay start walking over to the market place, a certain place outshining the rest."

show laynormal with dissolve
Lay "You're probably hungry too, let me see if I have any spare cash."
"Lay digs through her pockets, looking for spare change."
show laysmile
Lay "Here we go. 20 {color=#ACE599}trollars{/color}!"
$ trollars += 20
"{color=#ACE599}You've just recieved 20 trollars!{/color}"




jump art 

label verfi:
stop music fadeout 1.5
scene black 
"Lay grabs your hand and starts walking to a destination unbeknownst to you."
"You try asking her where u are going but she doesn't answer..."
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
with dissolve
"You see someone telling some jokes to what it seems the inamtes of this police station."
show crinhappy
Crin "And then I said,"
Crin "Sussy Bal-"
hide crinhappy
"sour and fbi laughs (placeholder)"
show crinhappy
Crin "Oh Hi Lay!"
hide crinhappy
show crinhuh
Crin "Who the fuck is this??"
show laysmile at right with easeinright
Lay "This guy? He's new around here."
hide crinhuh
show crinnorm
show laynormal at right
Crin "Oohhh.. well what's this lad doing here then?"
hide laynormal at right 
hide laysmile at right
show layeyesclosed at right
Lay "I'm gonna verify them to make them an official member."
show crintalk
Crin "Right then, bring him to the desk."
hide crintalk
hide layeyesclosed
hide crinnorm 
"She brings you over to the police station's desk."
"2 people in the cells next to you, all with prison tags that read Sour and FBI."
Sour "Can't believe I got a bloody life sentence for beating up that stupid {color=#ACE599}Dream{/color} worshipper."
show crinhuh
Crin "Sour, you got a life sentance for police brutality. The fuck you on about?"
show layeyesclosed at right
Lay "Yikes..."
hide crinhuh
hide layeyesclosed

show laynormal

Lay "FBI, you still have another hour on your visit, and Sour, Well.."
hide laynormal
FBI "Got it."
Sour "Yeah yeah.. piss off :(."

with vpunch 
"Suddenly a man dressed in a white suit with green pinstripes enters the station,"
"sits down and pulls back his matching fedora, rubbing a promise ring on his finger, and looks at you."
show layblush

Lay "Average."
hide layblush
Average "Lay."
Average "I'm here to oversee this entire interrogation, Bring Dico in to play starboard with the inmates."










return 
