
class AttackEmotes:
    """
    Get the right attack emotes
    """
    def get_emote(emote, tn, which):
        
        if emote == "bite":
            return [
                "|r$You() get a mouthful of air, but little else.",
                "|r$pron(Your) bite causes minor abrasions on " + tn + ".",
                "|r$pron(Your) bite causes " + tn + " to bleed slightly.",
                "|r$You() $conj(tear) gaping holes in " + tn + " with $pron(your) teeth!",
                "|r$pron(Your) bite causes " + tn + " to bleed profusely.",
                "|r$pron(Your) bite cracks " + tn + "'s bones!",
                "|r$You() $conj(gnaw) mounds of flesh off " + tn + "!",
                "|r$You() $conj(bite) limbs off " + tn + "!!",
                "|r$You() $conj(crunch) up " + tn + " like a bug!!",
                "|r$You() $conj(bite) " + tn + " so hard that blood spatters around the room!!!",
                "|r$You() $conj(tear) the HELL OUT OF " + tn + " with $pron(your) razor sharp fangs!!!"
            ]
        if emote == "bite2":
            return [
                "|r$You() bite viciously at " + tn + ", but miss entirely.",
                "|r$You() $conj(bite) glancingly into " + tn + " and cause some minor scratches.",
                "|r$You() $conj(bite) hard into " + tn + " and draw some blood!",
                "|r$You() $conj(bite) visciously into " + tn + " and leave blood gushing!",
                "|r$You() $conj(bite) a massive chunk of flesh off of " + tn + "'s body!",
                "|r$pron(Your) bite rips a hole through " + tn + "!",
                "|r$You() $conj(bite) a vital appendage off " + tn + " nonchalantly!",
                "|r$You() $conj(hear) bones splinter as you bite into " + tn + "!!",
                "|r$pron(Your) bite smashes bones as you gnaw down on " + tn + "'s body!!",
                "|r$You() $conj(bite) right into " + tn + "'s body and reposition vital organs!!!",
                "|r$pron(Your) bite absolutely <SHREDS> " + tn + "!!!"
            ]
        if emote == "claw":
            return [
                "|r$You() $conj(claw) wildly into open air.",
                "|r$You() $conj(scratch) " + tn + " slightly with $pron(your) " + which + " claw.",
                "|r$You() $conj(scratch) " + tn + " deeply with $pron(your) " + which + " claw.",
                "|r$You() $conj(open) a large gash in " + tn + " with $pron(your) " + which + " claw.",
                "|r$You() $conj(tear) small patches of flesh off " + tn + ".",
                "|r$You() $conj(tear) pounds of flesh off " + tn + ".",
                "|r$You() $conj(tear) limbs off " + tn + "!",
                "|r$You() $conj(rake) $pron(your) " + which + " claw through " + tn + ", tearing muscle and sinew as $pron(you) go!",
                "|r$You() $conj(dig) $pron(your) " + which + " claw deep into " + tn + ", and blood shoots from vital arteries!"
            ]
        if emote == "paw":
            return [
                "|r$You() swat at " + tn + ", but hit nothing but air.",
                "|r$You() paw glancingly at " + tn + ".",
                "|r$You() leave some ugly bruises as you pound on " + tn + "!",
                "|r$You() smash your paws hard into " + tn + "'s body and draw blood!",
                "|r$You() hear bones smash as you pound on " + tn + "!",
                "|r$You() tear a hole in " + tn + "'s body with a vicious blow!",
                "|r$You() knock " + tn + "'s organs into unnatural positions with a vicious swat!",
                "|r$You() knock a bone out of " + tn + "'s body with a horrendous <CRUNCH>!",
                "|r$You() smash down on a joint and swat an appendage off of " + tn + "'s body!!",
                "|r$You() smash into " + tn + "'s head with a vicious blow that nearly knocks " + tn + " unconscious!!",
                "|r$You() swat at " + tn + ", <CRUSHING> " + tn + " with a MASSIVE blow!!!"
            ]
        if emote == "wing":
            return [
                "|r$You() merely tickle " + tn + "'s nose with your " + which + " wingfeathers.",
                "|r$You() knock " + tn + " in the face with your " + which + " wing.",
                "|r$You() knock " + tn + " hard in the face with your " + which + " wing.",
                "|r$Blood trickles from " + tn + "'s nose as you hit " + tn + " with your " + which + " wing.",
                "|r$Blood gushes from " + tn + "'s nose as you squarely hit " + tn + " with your " + which + " wing.",
                "|r$You() pummel upon " + tn + " furiously with your " + which + " wing.",
                "|r$The barrage your " + which + " wing delivers to " + tn + " leaves " + tn + " seeing stars!",
                "|r$The connection between your " + which + " wing and " + tn + "'s head sends " + tn + " reeling backwards in pain!",
                "|r$Several of " + tn + "'s ribs crack as you slam your " + which + " wing into " + tn + "!",
                "|r$Tendons audibly snap and bones break as you practically ram your " + which + " wing down " + tn + "'s throat!",
                "|r$" + tn + "'s spinal cord crumples like an overused accordian as a well-timed smash from your " + which + " wing piledrives " + tn + " into the ground!"
            ]
        if emote == "tail":
            return [
                "|r$You() swish your tail through the air, but it catches nothing.",
                "|r$You() nick " + tn + " with your tail.",
                "|r$You() thud into " + tn + ", knocking the wind out of " + tn + ".",
                "|r$You() cause " + tn + " to fall back in pain.",
                "|r$You() knock " + tn + " off " + tn + "'s feet!",
                "|r$You() strike " + tn + " so hard that " + tn + " belches up blood!",
                "|r$" + tn + "'s body makes a sickening <CRUNCH> as your tail slams into " + tn + ".",
                "|r$" + tn + " nearly implodes as your tail crushes " + tn + " like a wine glass.",
                "|r$With a <THUNDEROUS CLAP>, your tail rearranges the atoms in " + tn + "'s body.",
                "|r$" + tn + " initiates a full bodily release as your tail thunders into " + tn + "!",
                "|r$" + tn + " belches out a LUNG as your tail UTTERLY FLATTENS " + tn + "!!"
            ]
        if emote == "tail2":
            return [
                "|r$You() swing your tail, and bruise some air.",
                "|r$You() nick " + tn + " with a glancing blow.",
                "|r$You() bruise " + tn + "'s body with a nasty swipe of your tail!",
                "|r$You() rip into " + tn + " with your tail and draw blood!",
                "|r$You() slam your tail into " + tn + " with a vicious THUD!",
                "|r$You() tear a HUGE gash in " + tn + "'s body with a powerful flick of your tail!!",
                "|r$You() cause " + tn + "'s organs to implode as you SLAM your tail into " + tn + "'s body!",
                "|r$You() hear bones splinter as you CRUSH " + tn + "'s body with your tail!!",
                "|r$Your tail SHREDS vital appendages off " + tn + "'s pathetic body!!",
                "|r$You() THRASH " + tn + " with a MASSIVE blow from your tail!!!",
                "|r$Your tail ANNIHILATES " + tn + " with an earth shaking <BOOM>!!!"
            ]
        if emote == "horn":
            return [
                "|r$You() thrust your " + which + " horn wildly through the air.",
                "|r$pron(Your) " + which + " horn grazes " + tn + ".",
                "|r$pron(Your) " + which + " horn thuds into " + tn + ", knocking the wind out of " + tn + ".",
                "|r$You() puncture " + tn + "'s body with a small blow from your " + which + " horn.",
                "|r$pron(Your) shred " + tn + " with a blow from your " + which + " horn.",
                "|r$You() tear into " + tn + " with your " + which + " horn!",
                "|r$" + tn + "'s blood sprays everywhere as you impale " + tn + " with your " + which + " horn.",
                "|r$" + tn + " twitches as you spear " + tn + " with your " + which + " horn.",
                "|r$" + tn + " staggers as you SLAM into them solidly with your " + which + " horn!.",
                "|r$" + tn + " is THROWN backwards as you IMPALE them with your " + which + " horn!",
                "|r$You() IMPALE " + tn + " with a MASSIVE THRUST of your " + which + " horn!!!"
            ]
        if emote == "hug":
            return [
                "|r$You() give " + tn + " a warm fuzzy hug. (no dmg)",
                "|r$You() squeeze " + tn + " enough to make " + tn + " wince.",
                "|r$" + tn + " gasps for air as you squeeze.",
                "|r$You() hear ribs cracking as you crush " + tn + ".",
                "|r$" + tn + " screams out in pain as you crush " + tn + "'s body!",
                "|r$You() squeeze " + tn + " so hard that " + tn + "'s eyes almost pop out!",
                "|r$Ribs push out of " + tn + "'s skin as you crush " + tn + "!",
                "|r$" + tn + "'s body makes a horrifying *CRUNCH* as you lock your arms around " + tn + ".",
                "|r$" + tn + " gurgles and spits up blood as your grasp tightens!",
                "|r$Blood shoots out of " + tn + "'s eyes and mouth as you crush " + tn + "'s body!!",
                "|r$YOU CRUSH " + tn + " LIKE A FREAKING GRAPE!"
            ]
        if emote == "constrict":
            return [
                "|r$You() give " + tn + " a friendly squeeze (no dmg)",
                "|r$You() squeeze " + tn + " enough to make " + tn + " wince.",
                "|r$" + tn + " gasps for air as you squeeze " + tn + "'s neck.",
                "|r$You() hear ribs cracking as you crush " + tn + " in your coils.",
                "|r$" + tn + " screams out in pain as you crush " + tn + "'s body in your coils!",
                "|r$You() squeeze " + tn + " so hard that " + tn + "'s eyes almost pop out!",
                "|r$Ribs push out of " + tn + "'s skin as you crush " + tn + "!",
                "|r$" + tn + "'s body makes a horrifying *CRUNCH* as you constrict " + tn + " in your coils.",
                "|r$" + tn + " gurgles and spits up blood as you tighten your constriction!",
                "|r$An internal organ shoots out of " + tn + "'s throat as you crush " + tn + "'s body within your scaly grasp!!",
                "|r$You() squeeze 3 coils around " + tn + "'s neck, and " + tn + "'s eyes, ears, and nose spew forth an ocean of hemmorhagic fluid and blood!"
            ]
        if emote == "gaze":
            return [
                "|r$You() must have been looking elsewhere, " + tn + " is unaffected.",
                "|r" + tn + " |rgets a mild headache.",
                "|r" + tn + " |rgets a severe migrane.",
                "|r" + tn + " |rholds " + tn + "'s head and cowers in pain.",
                "|r" + tn + " |rscreams in agony trying to fight off the pain.",
                "|r" + tn + "|r's limbs fall limp for a second as " + tn + "'s brain ceases to function.",
                "|r$Blood oozes slowly from " + tn + "'s nose and ears.",
                "|r" + tn + "|r's body explodes in a spasm of uncontrolled activity as " + tn + "'s brain malfunctions.",
                "|r$Skull fragments and blood ooze from " + tn + "'s ears.",
                "|r$Blood shoots out of " + tn + "'s ears, followed by bits of brain matter!",
                "|r$Blood and brain matter fly everywhere as " + tn + "'s head EXPLODES!!"
            ]
        if emote == "hoof":
            return [
                "|r$You() wildly kick at the air.",
                "|r$You() barely nick " + tn + " with your " + which + " hoof.",
                "|r$pron(Your) " + which + " hoof glances off " + tn + ", causing minor abrasions.",
                "|r$pron(Your) " + which + " hoof slams into " + tn + ", but " + tn + " manages to get mostly out of the way.",
                "|r$You() send " + tn + " reeling with a swift kick from your " + which + " hoof.",
                "|r$You() hear bones break as you kick " + tn + " visciously with your " + which + " hoof.",
                "|r$You() kick " + tn + " into next week with your " + which + " hoof!",
                "|r$You() SLAM " + tn + " with your " + which + " hoof!",
                "|r" + tn + "|r is sent flying backwards as you SMASH your " + which + " hoof into " + tn + "!",
                "|r" + tn + "|r's body makes a sickening CRUNCH as you SLAM your " + which + " hoof into " + tn + "!!",
                "|r" + tn + "|r *EXPLODES* like week-old roadkill as you smash " + tn + " with your " + which + " hoof!!!"
            ]
        if emote == "sting":
            return [
                "|r$You() manage to sting nothing but air.",
                "|r$Your stinger brushes " + tn + ".",
                "|r$You() sting " + tn + " lightly.",
                "|r" + tn + " |rwinces as you sting " + tn + ".",
                "|r$pron(Your) sting causes " + tn + " to fall back in pain.",
                "|r" + tn + "|rstaggers as you sting " + tn + " visciously.",
                "|r" + tn + "|rcringes in pain as you land a solid sting on " + tn + "!",
                "|r" + tn + "|r's eyes bug out as you sting " + tn + " right where it hurts!",
                "|r" + tn + "|r's body goes limp for a moment as you sting " + tn + "!",
                "|r" + tn + "|r SPASMS violently as you sting " + tn + "!!",
                "|r" + tn + "|r SHUDDERS and WRITHES in agony as you sting " + tn + " visciously!!!"
            ]
        if emote == "stomp":
            return [
                "|r$You() dart out of the way and you stomp the ground.",
                "|r$You() barely nick " + tn + " with your " + which + " foot.",
                "|r$pron(Your) " + which + " foot glances off " + tn + ", causing minor abrasions.",
                "|r$pron(Your) " + which + " foot slams into " + tn + ", but " + tn + " manages to get mostly out of the way.",
                "|r" + tn + "|r screeches as you land your " + which + " foot right on top of " + tn + " head!",
                "|r" + tn + "|r stumbles back in agony as you land your " + which + " foot right on top of " + tn + "!",
                "|rGrey matter oozes from " + tn + "'s ears as you thrust your " + which + " foot into " + tn + " skull.",
                "|r" + tn + "|r cracks in half as you flatten " + tn + " with your " + which + " foot!",
                "|r$You() drive " + tn + " into the ground like a nail!",
                "|r" + tn + "|r crunches grossly under your thunderous " + which + " foot!!",
                "|r" + tn + "|r *EXPLODES* like week-old roadkill as you smash " + tn + " with your " + which + " foot!"
            ]
        if emote == "tackle":
            return [
                "|r$You() shoot past " + tn + " nearly slamming into the ground!",
                "|r$You() nick " + tn + ", as " + tn + " jumps out of the way.",
                "|r$You() smack into " + tn + " with minimal velocity.",
                "|r$You() run into " + tn + " causing " + tn + " to go 'Oof.'",
                "|r$You() knock the wind out of " + tn + " as you crash into " + tn + "!",
                "|rWith a solid *SMACK*, you smash into " + tn + "!",
                "|r*CRUNCH* You pulverize " + tn + "!",
                "|r$You() drop on " + tn + " like a Bowling Ball on a roach!",
                "|r->SHAZAM<- " + tn + " spits out " + tn + "'s duodenom as you thunder into " + tn + "!",
                "|r$You() crash into " + tn + " so hard that ribs shoot out " + tn + " back!!",
                "|r$You() *THUNDER* into " + tn + ", nearly causing " + tn + " to <IMPLODE>!!!"
            ]
        if emote == "tusk":
            return [
                "|r$You() impale air and little else.",
                "|r$You() jump out of the way of your tusk and are merely scratched.",
                "|r$You() scrape your tusk against " + tn + ".",
                "|r$You() manage to gash a hole in " + tn + " with your tusk.",
                "|r$You() throw your tusk into " + tn + " and knock " + tn + " down to the ground.",
                "|r$You() drive your tusk through a non-vital region of " + tn + "'s torso.",
                "|rBlood shoots out of a hole in " + tn + " that you created with your tusk!",
                "|rYour lungs make a sucking sound as you puncture one with your tusk!",
                "|rYou() scream out in agony as you drive your tusk through a vital organ!",
                "|rYou() impale " + tn + " on your tusk and shake " + tn + " like a rag doll!",
                "|rYou() tear a <GAPING HOLE> in " + tn + " with your tusk, spilling " + tn + "'s guts onto the ground!"
            ]
        if emote == "gore":
            return [
                "|r$You() gore air and little else.",
                "|r$You() jump out of the way of your horns and are merely scratched.",
                "|r$You() scrape your horns against " + tn + ".",
                "|r$You() manage to gash a hole in " + tn + " with your horns.",
                "|r$You() throw your horns into " + tn + " and knock " + tn + " down to the ground.",
                "|r$You() drive your horns through a non-vital region of " + tn + "'s torso.",
                "|rBlood shoots out of a hole in " + tn + " that you created with your horns!",
                "|rYour lungs make a sucking sound as you puncture one with your horns!",
                "|rYou() scream out in agony as you drive your horns through a vital organ!",
                "|rYou() impale " + tn + " on your horns and shake " + tn + " like a rag doll!",
                "|rYou() tear a <GAPING HOLE> in " + tn + " with your horns, spilling " + tn + "'s guts onto the ground!"
            ]
                