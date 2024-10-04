class AttackEmotes:
    """
    Get the right attack emotes
    """

    def get_emote(attacker, emote, tn, which):
        color = "|r"

        if emote == "bite":
            return [
                f"{color}$You() get a mouthful of air, but little else.",
                f"{color}$pron(Your) bite causes minor abrasions on {tn}{color}.",
                f"{color}$pron(Your) bite causes {tn}{color} to bleed slightly.",
                f"{color}$You() $conj(tear) gaping holes in {tn}{color} with $pron(your) teeth!",
                f"{color}$pron(Your) bite causes {tn}{color}{color} to bleed profusely.",
                f"{color}$pron(Your) bite cracks {tn}{color}'s bones!",
                f"{color}$You() $conj(gnaw) mounds of flesh off {tn}{color}!",
                f"{color}$You() $conj(bite) limbs off {tn}{color}!!",
                f"{color}$You() $conj(crunch) up {tn}{color} like a bug!!",
                f"{color}$You() $conj(bite) {tn}{color} so hard that blood spatters around the room!!!",
                f"{color}$You() $conj(tear) the HELL OUT OF {tn}{color} with $pron(your) razor sharp fangs!!!",
            ]
        if emote == "bite2":
            return [
                f"{color}$You() bite viciously at {tn}{color}, but miss entirely.",
                f"{color}$You() $conj(bite) glancingly into {tn}{color} and cause some minor scratches.",
                f"{color}$You() $conj(bite) hard into {tn}{color} and draw some blood!",
                f"{color}$You() $conj(bite) visciously into {tn}{color} and leave blood gushing!",
                f"{color}$You() $conj(bite) a massive chunk of flesh off of {tn}{color}'s body!",
                f"{color}$pron(Your) bite rips a hole through {tn}{color}!",
                f"{color}$You() $conj(bite) a vital appendage off {tn}{color} nonchalantly!",
                f"{color}$You() $conj(hear) bones splinter as you bite into {tn}{color}!!",
                f"{color}$pron(Your) bite smashes bones as you gnaw down on {tn}{color}'s body!!",
                f"{color}$You() $conj(bite) right into {tn}{color}'s body and reposition vital organs!!!",
                f"{color}$pron(Your) bite absolutely <SHREDS> {tn}{color}!!!",
            ]
        if emote == "claw":
            return [
                f"{color}$You() $conj(claw) wildly into open air.",
                f"{color}$You() $conj(scratch) {tn}{color} slightly with $pron(your) {which} claw.",
                f"{color}$You() $conj(scratch) {tn}{color} deeply with $pron(your) {which} claw.",
                f"{color}$You() $conj(open) a large gash in {tn}{color} with $pron(your) {which} claw.",
                f"{color}$You() $conj(tear) small patches of flesh off {tn}{color}.",
                f"{color}$You() $conj(tear) pounds of flesh off {tn}{color}.",
                f"{color}$You() $conj(tear) limbs off {tn}{color}!",
                f"{color}$You() $conj(rake) $pron(your) {which} claw through {tn}{color}, tearing muscle and sinew as $pron(you) go!",
                f"{color}$You() $conj(dig) $pron(your) {which} claw deep into {tn}{color}, and blood shoots from vital arteries!",
                f"{color}$You() $conj(shred) {tn}{color} like a Watergate document!",
                f"{color}$You() $conj(slice) {tn}{color} into pieces like Sylvester on a bad cartoon!!",
            ]
        if emote == "paw":
            return [
                f"{color}$You() swat at {tn}{color}, but hit nothing but air.",
                f"{color}$You() paw glancingly at {tn}{color}.",
                f"{color}$You() leave some ugly bruises as you pound on {tn}{color}!",
                f"{color}$You() smash your paws hard into {tn}{color}'s body and draw blood!",
                f"{color}$You() hear bones smash as you pound on {tn}{color}!",
                f"{color}$You() tear a hole in {tn}{color}'s body with a vicious blow!",
                f"{color}$You() knock {tn}{color}'s organs into unnatural positions with a vicious swat!",
                f"{color}$You() knock a bone out of {tn}{color}'s body with a horrendous <CRUNCH>!",
                f"{color}$You() smash down on a joint and swat an appendage off of {tn}{color}'s body!!",
                f"{color}$You() smash into {tn}{color}'s head with a vicious blow that nearly knocks them{color} unconscious!!",
                f"{color}$You() swat at {tn}{color}, <CRUSHING> {tn}{color} with a MASSIVE blow!!!",
            ]
        if emote == "wing":
            return [
                f"{color}$You() merely tickle {tn}{color}'s nose with your {which} wingfeathers.",
                f"{color}$You() knock {tn}{color} in the face with your {which} wing.",
                f"{color}$You() knock {tn}{color} hard in the face with your {which} wing.",
                f"{color}Blood trickles from {tn}{color}'s nose as you hit {tn}{color} with your {which} wing.",
                f"{color}Blood gushes from {tn}{color}'s nose as you squarely hit {tn}{color} with your {which} wing.",
                f"{color}$You() pummel upon {tn}{color} furiously with your {which} wing.",
                f"{color}The barrage your {which} wing delivers to {tn}{color} leaves {tn}{color} seeing stars!",
                f"{color}The connection between your {which} wing and {tn}{color}'s head sends {tn}{color} reeling backwards in pain!",
                f"{color}Several of {tn}{color}'s ribs crack as you slam your {which} wing into {tn}{color}!",
                f"{color}Tendons audibly snap and bones break as you practically ram your {which} wing down {tn}{color}'s throat!",
                f"{color}${tn}{color}'s spinal cord crumples like an overused accordian as a well-timed smash from your {which} wing piledrives {tn}{color} into the ground!",
            ]
        if emote == "tail":
            return [
                f"{color}$You() swish your tail through the air, but it catches nothing.",
                f"{color}$You() nick {tn}{color} with your tail.",
                f"{color}$You() thud into {tn}{color}, knocking the wind out of them{color}.",
                f"{color}$You() cause {tn}{color} to fall back in pain.",
                f"{color}$You() knock {tn}{color} off their{color}'s feet!",
                f"{color}$You() strike {tn}{color} so hard that they {color} belch up blood!",
                f"{color}{tn}{color}'s body makes a sickening <CRUNCH> as your tail slams into {tn}{color}.",
                f"{color}{tn}{color} nearly implodes as your tail crushes {tn}{color} like a wine glass.",
                f"{color}With a <THUNDEROUS CLAP>, your tail rearranges the atoms in {tn}{color}'s body.",
                f"{color}{tn}{color} initiates a full bodily release as your tail thunders into {tn}{color}!",
                f"{color}{tn}{color} belches out a LUNG as your tail UTTERLY FLATTENS {tn}{color}!!",
            ]
        if emote == "tail2":
            return [
                f"{color}$You() swing your tail, and bruise some air.",
                f"{color}$You() nick {tn}{color} with a glancing blow.",
                f"{color}$You() bruise {tn}{color}'s body with a nasty swipe of your tail!",
                f"{color}$You() rip into {tn}{color} with your tail and draw blood!",
                f"{color}$You() slam your tail into {tn}{color} with a vicious THUD!",
                f"{color}$You() tear a HUGE gash in {tn}{color}'s body with a powerful flick of your tail!!",
                f"{color}$You() cause {tn}{color}'s organs to implode as you SLAM your tail into {tn}{color}'s body!",
                f"{color}$You() hear bones splinter as you CRUSH {tn}{color}'s body with your tail!!",
                f"{color}Your tail SHREDS vital appendages off {tn}{color}'s pathetic body!!",
                f"{color}$You() THRASH {tn}{color} with a MASSIVE blow from your tail!!!",
                f"{color}$Your tail ANNIHILATES {tn}{color} with an earth shaking <BOOM>!!!",
            ]
        if emote == "horn":
            return [
                f"{color}$You() thrust your {which} horn wildly through the air.",
                f"{color}$pron(Your) {which} horn grazes {tn}{color}.",
                f"{color}$pron(Your) {which} horn thuds into {tn}{color}, knocking the wind out of {tn}{color}.",
                f"{color}$You() puncture {tn}{color}'s body with a small blow from your {which} horn.",
                f"{color}$pron(Your) shred {tn}{color} with a blow from your {which} horn.",
                f"{color}$You() tear into {tn}{color} with your {which} horn!",
                f"{color}${tn}{color}'s blood sprays everywhere as you impale {tn}{color} with your {which} horn.",
                f"{color}${tn}{color} twitches as you spear {tn}{color} with your {which} horn.",
                f"{color}${tn}{color} staggers as you SLAM into them solidly with your {which} horn!.",
                f"{color}${tn}{color} is THROWN backwards as you IMPALE them with your {which} horn!",
                f"{color}$You() IMPALE {tn}{color} with a MASSIVE THRUST of your {which} horn!!!",
            ]
        if emote == "hug":
            return [
                f"{color}$You() give {tn}{color} a warm fuzzy hug. (no dmg)",
                f"{color}$You() squeeze {tn}{color} enough to make {tn}{color} wince.",
                f"{color}${tn}{color} gasps for air as you squeeze.",
                f"{color}$You() hear ribs cracking as you crush {tn}{color}.",
                f"{color}${tn}{color} screams out in pain as you crush {tn}{color}'s body!",
                f"{color}$You() squeeze {tn}{color} so hard that {tn}{color}'s eyes almost pop out!",
                f"{color}Ribs push out of {tn}{color}'s skin as you crush {tn}{color}!",
                f"{color}${tn}{color}'s body makes a horrifying *CRUNCH* as you lock your arms around {tn}{color}.",
                f"{color}${tn}{color} gurgles and spits up blood as your grasp tightens!",
                f"{color}Blood shoots out of {tn}{color}'s eyes and mouth as you crush {tn}{color}'s body!!",
                f"{color}YOU CRUSH {tn}{color} LIKE A FREAKING GRAPE!",
            ]
        if emote == "constrict":
            return [
                f"{color}$You() give {tn}{color} a friendly squeeze (no dmg)",
                f"{color}$You() squeeze {tn}{color} enough to make {tn}{color} wince.",
                f"{color}{tn}{color} gasps for air as you squeeze {tn}{color}'s neck.",
                f"{color}$You() hear ribs cracking as you crush {tn}{color} in your coils.",
                f"{color}{tn}{color} screams out in pain as you crush {tn}{color}'s body in your coils!",
                f"{color}$You() squeeze {tn}{color} so hard that {tn}{color}'s eyes almost pop out!",
                f"{color}Ribs push out of {tn}{color}'s skin as you crush {tn}{color}!",
                f"{color}${tn}{color}'s body makes a horrifying *CRUNCH* as you constrict {tn}{color} in your coils.",
                f"{color}${tn}{color} gurgles and spits up blood as you tighten your constriction!",
                f"{color}An internal organ shoots out of {tn}{color}'s throat as you crush {tn}{color}'s body within your scaly grasp!!",
                f"{color}$You() squeeze 3 coils around {tn}{color}'s neck, and {tn}{color}'s eyes, ears, and nose spew forth an ocean of hemmorhagic fluid and blood!",
            ]
        if emote == "gaze":
            return [
                f"{color}$You() must have been looking elsewhere, {tn}{color} is unaffected.",
                f"{color}{tn}{color} {color}gets a mild headache.",
                f"{color}{tn}{color} {color}gets a severe migrane.",
                f"{color}{tn}{color} {color}holds {tn}{color}'s head and cowers in pain.",
                f"{color}{tn}{color} {color}screams in agony trying to fight off the pain.",
                f"{color}{tn}{color}{color}'s limbs fall limp for a second as {tn}{color}'s brain ceases to function.",
                f"{color}Blood oozes slowly from {tn}{color}'s nose and ears.",
                f"{color}{tn}{color}{color}'s body explodes in a spasm of uncontrolled activity as {tn}{color}'s brain malfunctions.",
                f"{color}Skull fragments and blood ooze from {tn}{color}'s ears.",
                f"{color}Blood shoots out of {tn}{color}'s ears, followed by bits of brain matter!",
                f"{color}Blood and brain matter fly everywhere as {tn}{color}'s head EXPLODES!!",
            ]
        if emote == "hoof":
            return [
                f"{color}$You() wildly kick at the air.",
                f"{color}$You() barely nick {tn}{color} with your {which} hoof.",
                f"{color}$pron(Your) {which} hoof glances off {tn}{color}, causing minor abrasions.",
                f"{color}$pron(Your) {which} hoof slams into {tn}{color}, but {tn}{color} manages to get mostly out of the way.",
                f"{color}$You() send {tn}{color} reeling with a swift kick from your {which} hoof.",
                f"{color}$You() hear bones break as you kick {tn}{color} visciously with your {which} hoof.",
                f"{color}$You() kick {tn}{color} into next week with your {which} hoof!",
                f"{color}$You() SLAM {tn}{color} with your {which} hoof!",
                f"{color}{tn}{color}{color} is sent flying backwards as you SMASH your {which} hoof into {tn}{color}!",
                f"{color}{tn}{color}{color}'s body makes a sickening CRUNCH as you SLAM your {which} hoof into {tn}{color}!!",
                f"{color}{tn}{color}{color} *EXPLODES* like week-old roadkill as you smash {tn}{color} with your {which} hoof!!!",
            ]
        if emote == "sting":
            return [
                f"{color}$You() manage to sting nothing but air.",
                f"{color}$Your stinger brushes {tn}{color}.",
                f"{color}$You() sting {tn}{color} lightly.",
                f"{color}{tn}{color} {color}winces as you sting {tn}{color}.",
                f"{color}$pron(Your) sting causes {tn}{color} to fall back in pain.",
                f"{color}{tn}{color}{color}staggers as you sting {tn}{color} visciously.",
                f"{color}{tn}{color}{color}cringes in pain as you land a solid sting on {tn}{color}!",
                f"{color}{tn}{color}{color}'s eyes bug out as you sting {tn}{color} right where it hurts!",
                f"{color}{tn}{color}{color}'s body goes limp for a moment as you sting {tn}{color}!",
                f"{color}{tn}{color}{color} SPASMS violently as you sting {tn}{color}!!",
                f"{color}{tn}{color}{color} SHUDDERS and WRITHES in agony as you sting {tn}{color} visciously!!!",
            ]
        if emote == "engulf":
            return [
                f"{color}$You() try to engulf {tn}{color}, but miss entirely.",
                f"{color}$You() engulf {tn}{color}, causing acidic burns and damage.",
                f"{color}$You() sting {tn}{color} with your acidic touch.",
                f"{color}{tn}{color} staggers as you engulf {tn}{color} visciously.",
                f"{color}{tn}{color} cringes in pain as you engulf {tn}{color}!",
                f"{color}$pron(Your) acidic touch causes {tn}{color} to fall back in pain.",
                f"{color}{tn}{color}'s eyes bug out as you engulf {tn}{color} right where it hurts!",
                f"{color}{tn}{color}'s body goes limp for a moment as you engulf {tn}{color}!",
                f"{color}{tn}{color} SPASMS violently as you engulf {tn}{color}!!",
                f"{color}{tn}{color} SHUDDERS and WRITHES in agony as you engulf {tn}{color} visciously!!!",
                f"{color}{tn}{color}'s body EXPLODES in a shower of gore as you engulf {tn}{color} visciously!!!",
            ]

        if emote == "stomp":
            return [
                f"{color}$You() dart out of the way and you stomp the ground.",
                f"{color}$You() barely nick {tn}{color} with your {which} foot.",
                f"{color}$pron(Your) {which} foot glances off {tn}{color}, causing minor abrasions.",
                f"{color}$pron(Your) {which} foot slams into {tn}{color}, but {tn}{color} manages to get mostly out of the way.",
                f"{color}{tn}{color} screeches as you land your {which} foot right on top of {tn}{color} head!",
                f"{color}{tn}{color} stumbles back in agony as you land your {which} foot right on top of {tn}{color}!",
                f"{color}Grey matter oozes from {tn}{color}'s ears as you thrust your {which} foot into {tn}{color} skull.",
                f"{color}{tn}{color} cracks in half as you flatten {tn}{color} with your {which} foot!",
                f"{color}$You() drive {tn}{color} into the ground like a nail!",
                f"{color}{tn}{color} crunches grossly under your thunderous {which} foot!!",
                f"{color}{tn}{color} *EXPLODES* like week-old roadkill as you smash {tn}{color} with your {which} foot!",
            ]
        if emote == "tackle":
            return [
                f"{color}$You() shoot past {tn}{color} nearly slamming into the ground!",
                f"{color}$You() nick {tn}{color}, as {tn}{color} jumps out of the way.",
                f"{color}$You() smack into {tn}{color} with minimal velocity.",
                f"{color}$You() run into {tn}{color} causing {tn}{color} to go 'Oof.'",
                f"{color}$You() knock the wind out of {tn}{color} as you crash into {tn}{color}!",
                f"{color}With a solid *SMACK*, you smash into {tn}{color}!",
                f"{color}*CRUNCH* You pulverize {tn}{color}!",
                f"{color}$You() drop on {tn}{color} like a Bowling Ball on a roach!",
                f"{color}->SHAZAM<- {tn}{color} spits out {tn}{color}'s duodenom as you thunder into {tn}{color}!",
                f"{color}$You() crash into {tn}{color} so hard that ribs shoot out {tn}{color} back!!",
                f"{color}$You() *THUNDER* into {tn}{color}, nearly causing {tn}{color} to <IMPLODE>!!!",
            ]
        if emote == "tusk":
            return [
                f"{color}$You() impale air and little else.",
                f"{color}$You() jump out of the way of your tusk and are merely scratched.",
                f"{color}$You() scrape your tusk against {tn}{color}.",
                f"{color}$You() manage to gash a hole in {tn}{color} with your tusk.",
                f"{color}$You() throw your tusk into {tn}{color} and knock {tn}{color} down to the ground.",
                f"{color}$You() drive your tusk through a non-vital region of {tn}{color}'s torso.",
                f"{color}Blood shoots out of a hole in {tn}{color} that you created with your tusk!",
                f"{color}Your lungs make a sucking sound as you puncture one with your tusk!",
                f"{color}You() scream out in agony as you drive your tusk through a vital organ!",
                f"{color}You() impale {tn}{color} on your tusk and shake {tn}{color} like a rag doll!",
                f"{color}You() tear a <GAPING HOLE> in {tn}{color} with your tusk, spilling {tn}{color}'s guts onto the ground!",
            ]
        if emote == "gore":
            return [
                f"{color}$You() gore air and little else.",
                f"{color}$You() jump out of the way of your horns and are merely scratched.",
                f"{color}$You() scrape your horns against {tn}{color}.",
                f"{color}$You() manage to gash a hole in {tn}{color} with your horns.",
                f"{color}$You() throw your horns into {tn}{color} and knock {tn}{color} down to the ground.",
                f"{color}$You() drive your horns through a non-vital region of {tn}{color}'s torso.",
                f"{color}Blood shoots out of a hole in {tn}{color} that you created with your horns!",
                f"{color}Your lungs make a sucking sound as you puncture one with your horns!",
                f"{color}You() scream out in agony as you drive your horns through a vital organ!",
                f"{color}You() impale {tn}{color} on your horns and shake {tn}{color} like a rag doll!",
                f"{color}You() tear a <GAPING HOLE> in {tn}{color} with your horns, spilling {tn}{color}'s guts onto the ground!",
            ]
        if emote == "peck":
            return [
                f"{color}$You() peck air and little else.",
                f"{color}{tn}{color} jumps out of the way of {attacker}'s beak and is merely scratched.",
                f"{color}$You() scrape your beak against {tn}{color}.",
                f"{color}$You() manage to gash a hole in {tn}{color} with your beak.",
                f"{color}$You() throw your beak into {tn}{color} and knock {tn}{color} down to the ground.",
                f"{color}$You() drive your beak through a non-vital region of {tn}{color}'s torso.",
                f"{color}Blood shoots out of a hole in {tn}{color} that you created with your beak!",
                f"{color}Your lungs make a sucking sound as you puncture one with your beak!",
                f"{color}You() scream out in agony as you drive your beak through a vital organ!",
                f"{color}You() impale {tn}{color} on your beak and shake {tn}{color} like a rag doll!",
                f"{color}You() tear a <GAPING HOLE> in {tn}{color} with your beak, spilling {tn}{color}'s guts onto the ground!",
            ]
        if emote == "punch":
            return [
                f"{color}$You() punch air and little else.",
                f"{color}{tn}{color} jumps out of the way of your fist and is merely scratched.",
                f"{color}$You() scrape your fist against {tn}{color}.",
                f"{color}$You() manage to gash a hole in {tn}{color} with your fist.",
                f"{color}$You() throw your fist into {tn}{color} and knock {tn}{color} down to the ground.",
                f"{color}$You() drive your fist through a non-vital region of {tn}{color}'s torso.",
                f"{color}Blood shoots out of a hole in {tn}{color} that you created with your fist!",
                f"{color}Your lungs make a sucking sound as you puncture one with your fist!",
                f"{color}{tn}{color}screams out in agony as you drive your fist through a vital organ!",
                f"{color}You() impale {tn}{color} on your fist and shake {tn}{color} like a rag doll!",
                f"{color}You() tear a <GAPING HOLE> in {tn}{color} with your fist, spilling {tn}{color}'s guts onto the ground!",
            ]
        if emote == "burn":
            return [
                f"{color}$You() emit a burst of heat, but it dissipates harmlessly.",
                f"{color}$You() singe {tn}{color} slightly with a flicker of flame.",
                f"{color}$You() scorch {tn}{color}'s skin with a brief flare.",
                f"{color}$You() sear a painful burn into {tn}{color}'s flesh.",
                f"{color}$You() engulf {tn}{color} in a wave of intense heat, causing them to stagger.",
                f"{color}$You() char {tn}{color}'s arm, leaving a deep burn mark.",
                f"{color}Smoke rises as you roast {tn}{color}, leaving their skin blistered and raw!",
                f"{color}You() ignite {tn}{color}'s clothing, causing them to frantically pat out the flames!",
                f"{color}You() unleash a fiery blast that engulfs {tn}{color}, making them scream in agony!",
                f"{color}You() incinerate {tn}{color} with a powerful burst of flame, leaving them writhing in pain!",
                f"{color}You() reduce {tn}{color} to a smoldering heap, their body charred and smoking!",
            ]
        if emote == "toast_attack":
            return [
                f"{color}$You() launch a piece of toast at {tn}{color}, but it harmlessly bounces off.",
                f"{color}$You() pop up a slice of toast that lightly taps {tn}{color} on the head.",
                f"{color}$You() fling a piece of toast at {tn}{color}, leaving a small, buttery mark.",
                f"{color}$You() send a slice of toast flying into {tn}{color}'s face, causing them to flinch.",
                f"{color}$You() pop up a perfectly toasted slice that smacks {tn}{color} squarely on the nose.",
                f"{color}$You() launch a piece of toast with such force that it leaves a red mark on {tn}{color}'s cheek.",
                f"{color}A slice of toast pops up and hits {tn}{color} in the eye, making them blink rapidly!",
                f"{color}You() send a barrage of toast slices at {tn}{color}, causing them to stumble back!",
                f"{color}You() pop up a slice of toast that hits {tn}{color} so hard, it leaves a toasty imprint!",
                f"{color}You() launch a flaming piece of toast at {tn}{color}, singeing their hair!",
                f"{color}You() pop up a slice of toast with such precision that it knocks {tn}{color} off their feet!",
            ]
