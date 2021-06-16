image bg starboard = "bg starboard.png"
image bg townsquare = "bg townsquare.png"
image laynormal = "Lay1.png"
image laytalk = "Lay2.png"
image layangry = "Lay3.png"
image layeyesclosed = "Lay4.png"
image laycry = "Lay5.png"
image laysmile = "Lay6.png"
image flower1 = "flower1.png"
image splashscreen = "splash.png"
image dicoangry = "Dico1.png"
image dicohappy = "Dico2.png"
image dicosalute = "Dico3.png"
image dicogun = "Dico5.png"
image diconormal = "Dico4.png"



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








label splashscreen:
 scene black
with Pause (1)

show splashscreen with dissolve

with Pause(2)


return


label start:
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
        name = "Crin"

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
Dubya "I love women."
Cloud "I hate women."
Dubya "I LOVE women."
Cloud "Well, I HATE women."
Dubya "Your opinion won't make me want to not love women."
Cloud "It should, because I hate women!"
"You spot the commotion and go join in with Lay."
Cloud "New face around here eh?"
Cloud "Name's Cloud. Guy I was talkin' to's Dubya"
Dubya "I love women."
Cloud "Hngh, he's getting on my nerves. Hey [name], whose opinion do you think is better?"


menu:
    set menuset
    "What clan are you willing to join?"

    "I love women.":
        show laytalk
        Lay "Haha, sorry about this but you're not allowed to choose a clan without getting{color=#ACE599} verified{/color} yet. "
        show laysmile
        Lay "Maybe we can come back when you're done!"
        hide laysmile

    "I hate women.":
        show laytalk
        Lay "Haha, sorry about this but you're not allowed to choose a clan without getting {color=#ACE599} verified{/color} yet. "
        show laysmile
        Lay "Maybe we can come back when you're done!"
        hide laysmile

hide laysmile
hide laytalk

Dubya "Well, that doesn’t matter because I love women!"
Cloud "grr.. I HATE WOMEN!"
"This goes on for another 10 minutes,"
with vpunch
"Until another man walks into the room and slams on the poker table, splattering the chips everywhere."
show dicoangry with dissolve
Dico "SHUT THE FUCK UP, YOU TWO!"
Dico "WE DON'T CARE ABOUT WOMEN!"
hide dicoangry
Cloud "Well, it’s not MY fault that DUBYA loves women!!"
Dubya "Well, it’s not MY-"
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

Cloud "I HATE WOMEN."
Dubya "I LOVE WOMEN."

show dicoangry
Dico "I’ll go deal with them."
Dico "The only way it could get worse is if marcel was here,"
Dico "and he’s probably playing some furry game or something right now."
show dicohappy
Dico "Oh, sorry, i’m rambling again, I’ll go deal with them, see ya!"
hide dicohappy
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
scene black
"As you and Lay walked through the busingling city, you wonder to your self, What is General-2?"
"The city was abnormal. Every where you looked, a different scene was going on."
"For example of when you saw a talking cheeseburger while you were passing through the market with Lay."
"Or when you saw a man dressed in a megaman costume running around with bread in his mouth."
"Or the time you saw a \"Gangster\" screaming Bonk clan when you where passing the L'stanberg Art department."
"This city was truly cursed."


show laynormal
Lay "We're here!"
"update over"

return


label art:
stop music fadeout 1.0
scene black
"hello"
return

label shop:
stop music fadeout 1.0
"helo"
"update do be over doe"



return
