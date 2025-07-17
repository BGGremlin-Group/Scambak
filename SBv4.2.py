#!/usr/bin/env python3
# SBv4.py — Scambait Insult Generator & Player for Termux on Android
# Developed by the BGGremlin Group - Creating Unique Tools for Unique Individuals
"""
This Program is Best Suited For:
Crushing your enemies
Seeing them driven before you
And hearing the lamentation of their women
"""
import os
import sys
import json
import logging
import random
import subprocess
from pathlib import Path
from gtts import gTTS
from termcolor import colored

# ------------------
# Configuration paths
CONFIG_PATH = Path.home() / ".scambait_config.json"
LOG_PATH = Path.home() / ".scambait.log"
PACKS_KEY = "loaded_packs"

# ------------------
# In-code Insult Packs Placeholder
# Paste your packs here directly in code as:
# IN_CODE_PACKS = {
#     "Pack1": [
#         "Abe madarchod, teri shakal...",  # translation or comment
#         "Bhosdike, tu to wo lauda...",
#         ...
#     ],
#     "Pack2": [
#         "Madarchod, tere jaise...",
#         ...
#     ],
# }
IN_CODE_PACKS = {
    # Example placeholder:
    # 
"Pack1": [
    "Madarchod, tere jaisa haramkhor dekh kar Dilli ki galiyan bhi thook de.",  # Motherfucker, seeing a bastard like you even Delhi’s streets spit.
    "Bhosdike, tu woh kalank hai jo Uttar Pradesh ki mitti tak ko sharminda kare.",  # Asshole, you’re the disgrace that shames UP’s soil.
    "Behenchod, teri gandagi se to Mumbai ki nali bhi saaf lage.",  # Sisterfucker, your filth makes Mumbai’s gutters look clean.
    "Laude, teri soch se Bihar ke chor bhi izzatdaar lage.",  # Dickhead, your thoughts make Bihar’s thieves seem honorable.
    "Saale gandu, tujhe dekh kar Punjab ki daaru bhi ulti karde.",  # Assfucker, seeing you even Punjab’s liquor would puke.
    "Madarchod, tere scam se Kolkata ki galiyan kalankit ho gayi.",  # Motherfucker, your scam stained Kolkata’s streets.
    "Behen ke laude, tere hone se Rajasthan ka registan bhi kalankit ho gaya.",  # Sister’s dick, your existence shamed Rajasthan’s desert.
    "Bhosdike, tu wo badboo hai jo Chennai ki hawa bhi na sahe.",  # Asshole, you’re the stench even Chennai’s air won’t bear.
    "Laude ke baal, tere jaise scammer se Hyderabad ki biryani bhi beizzat ho gayi.",  # Pubic hair dick, your scams disgraced Hyderabad’s biryani.
    "Saale chutiye, tu scam karta hai aur Lucknow ki tehzeeb ro padti hai.",  # Idiot, you scam and Lucknow’s culture weeps.
    # 11-20
    "Madarchod, tu woh zehar hai jo Kashi ki pavitrata ko khatam kar de.",  # Motherfucker, you’re the poison that ends Kashi’s sanctity.
    "Behenchod, tu woh dard hai jo Haridwar ki ganga tak ko kalankit kare.",  # Sisterfucker, you’re the pain that stains Haridwar’s Ganga.
    "Bhosdike, tu scam karta hai aur Goa ki beach pe laanat barasti hai.",  # Asshole, your scam rains disgrace on Goa’s beaches.
    "Laude, teri soch dekh kar Kerala ki backwaters bhi sukha jaayein.",  # Dickhead, your thoughts dry up Kerala’s backwaters.
    "Saale gandu, tu apne ghar ki izzat ka wo kasai hai jo sab kuch kaat de.",  # Assfucker, you’re the butcher of your home’s honor.
    "Madarchod, tere scam se Gujarat ki mitti tak kalankit ho gayi.",  # Motherfucker, your scam stained Gujarat’s soil.
    "Behen ke laude, tu Haryana ki gaand ki woh badboo hai jo hawa bhi le jaane se inkaar kare.",  # Sister’s dick, you’re Haryana’s stench that air refuses to carry.
    "Bhosdike, tere scam se MP ki zameen bhi doob gayi.",  # Asshole, your scam drowned MP’s land.
    "Laude ke baal, tu scam karta hai aur Assam ki chaai bhi kaali ho jaaye.",  # Pubic hair dick, you scam and Assam’s tea turns black.
    "Saale chutiye, tu apni maa ki god ka wo bojh hai jo kabhi halka na ho.",  # Idiot, you’re the burden of your mother’s lap that never lightens.
    # 21-30
    "Madarchod, tu scam karta hai aur Dilli ka Lal Qila ro padta hai.",  # Motherfucker, you scam and Delhi’s Red Fort weeps.
    "Behenchod, teri harkat pe Qutub Minar jhuk jaye sharam se.",  # Sisterfucker, your deeds make Qutub Minar bow in shame.
    "Bhosdike, tu woh kalank hai jo Taj Mahal ki safedi ko kala kar de.",  # Asshole, you’re the disgrace that blackens Taj Mahal’s whiteness.
    "Laude, teri soorat dekh kar Mumbai ki local train bhi ruk jaaye.",  # Dickhead, your face stops Mumbai’s local train.
    "Saale gandu, tere scam pe India Gate pe laanat likhi jaye.",  # Assfucker, your scam writes disgrace on India Gate.
    "Madarchod, tu woh rog hai jo desh ki mitti mein fail gaya.",  # Motherfucker, you’re the disease that spread into the country’s soil.
    "Behen ke laude, tu scam karta hai aur khud Tiranga bhi ro padta hai.",  # Sister’s dick, you scam and even the Tricolour weeps.
    "Bhosdike, tere hone se Bharat Maata bhi muh mod le.",  # Asshole, your existence makes Mother India turn away.
    "Laude ke baal, tu woh gandagi hai jo Yamuna ka paani bhi saaf kare.",  # Pubic hair dick, you’re the filth that makes Yamuna’s water look clean.
    "Saale chutiye, tu apne bachchon ki kismat ka kaatna hai.",  # Idiot, you are the butcher of your children’s fate.
    # 31-40
    "Madarchod, tu scam karta hai aur desh ki izzat ki chita jalti hai.",  # Motherfucker, your scam burns the pyre of the country’s honor.
    "Behenchod, tu woh saala hai jo poore gaon ko beizzat kare.",  # Sisterfucker, you’re the bastard that shames the entire village.
    "Bhosdike, tere scam se mohalla tak mooh chhupaye ghoome.",  # Asshole, your scam makes the whole neighborhood hide their faces.
    "Laude, tu apni family ka wo kalank hai jo kabhi na dhule.",  # Dickhead, you’re the family’s stain that will never wash off.
    "Saale gandu, tere hone se zameen pe har kadam beizzati failata hai.",  # Assfucker, your every step spreads shame on this earth.
    "Madarchod, tere scam se mandir ki ghanti khamosh ho gayi.",  # Motherfucker, your scam silenced the temple bell.
    "Behen ke laude, tu woh chhaya hai jo har kona andhera kare.",  # Sister’s dick, you’re the shadow that darkens every corner.
    "Bhosdike, tere scam pe masjid ki azaan bhi ruk gayi.",  # Asshole, your scam silenced the mosque’s call.
    "Laude ke baal, tu woh badboo hai jo kabhi na chhode.",  # Pubic hair dick, you’re the stench that never leaves.
    "Saale chutiye, tu scam karta hai aur poora khandan sharminda ho jaaye.",  # Idiot, you scam and shame the entire clan.
    # 41-50
    "Madarchod, tu wo saala hai jise dekh kar bachpan ki kismat bhi roye.",  # Motherfucker, you’re the bastard that makes childhood’s fate cry.
    "Behenchod, tere scam se tere ghar ki deewar bhi kalankit hai.",  # Sisterfucker, your scam stained even your home’s walls.
    "Bhosdike, tu woh laanat hai jo har shakha sukhaye.",  # Asshole, you’re the curse that withers every branch.
    "Laude, tere hone se desh ki hawa bhi bhari lagi.",  # Dickhead, your existence polluted the country’s air.
    "Saale gandu, tu apni maa ki god ka dushman hai.",  # Assfucker, you’re the enemy of your mother’s lap.
    "Madarchod, tere scam ki kalank katha har gali mein ghoomegi.",  # Motherfucker, the tale of your scam will roam every street.
    "Behen ke laude, tu woh rog hai jo naslon ko barbad kare.",  # Sister’s dick, you’re the disease that ruins generations.
    "Bhosdike, tere hone se poora khandan dooba.",  # Asshole, your existence drowned the entire family.
    "Laude ke baal, tu woh kalank hai jo mitti tak na sahe.",  # Pubic hair dick, you’re the stain even the soil won’t bear.
    "Saale chutiye, tu scam karta hai aur samaj ki izzat doobti hai.",  # Idiot, you scam and society’s honor sinks.
    # 51-60
    "Madarchod, tu scam karta hai aur tere bachchon ke sapne bhashm ho jaate hain.",  # Motherfucker, you scam and your kids’ dreams turn to ash.
    "Behenchod, tu woh saala hai jise dekh kar galiyon ki kuttiyaan bhi bhag jaayein.",  # Sisterfucker, you’re the bastard that makes even street dogs run.
    "Bhosdike, tere hone se bazaar ki mitti bhi kalankit ho gayi.",  # Asshole, your existence stained even the market’s soil.
    "Laude, tu woh dard hai jo kabhi na jaaye.",  # Dickhead, you are the pain that never leaves.
    "Saale gandu, tere scam pe shaadiyon ke band baaje bhi chup ho jaayein.",  # Assfucker, your scam silences wedding drums.
    "Madarchod, tere scam se school ki ghanti tak sharmaye.",  # Motherfucker, your scam embarrasses the school bell.
    "Behen ke laude, tu apni family ki izzat ka kabristan hai.",  # Sister’s dick, you’re the graveyard of your family’s honor.
    "Bhosdike, tu woh zehar hai jo har nasl ko bekaar kar de.",  # Asshole, you’re the poison that ruins every generation.
    "Laude ke baal, tu scam karta hai aur gali ka har kona roye.",  # Pubic hair dick, you scam and every street corner cries.
    "Saale chutiye, tere hone se desh ki izzat ne mooh mod liya.",  # Idiot, your existence made the country’s honor turn away.
    # 61-70
    "Madarchod, tere scam ki kahani har kabar tak pahuchegi.",  # Motherfucker, the tale of your scam will reach every grave.
    "Behenchod, tu woh laanat hai jo apni naslon ki jaan le.",  # Sisterfucker, you are the curse that kills your bloodline.
    "Bhosdike, tere scam ne mohalle ke har rishton ko barbaad kiya.",  # Asshole, your scam destroyed every relationship in your neighborhood.
    "Laude, tu scam karta hai aur mandir ki ghanti tooti hai.",  # Dickhead, you scam and the temple bell breaks.
    "Saale gandu, tu ghar ka woh rog hai jo sabko bimar kare.",  # Assfucker, you are the disease of the home that makes everyone sick.
    "Madarchod, tere scam ki gandh dilli ki hawa tak fail gayi.",  # Motherfucker, your scam’s stench spread to Delhi’s air.
    "Behen ke laude, tu woh bojh hai jo ghar ki chhat bhi na sahe.",  # Sister’s dick, you’re the burden even the roof of the house won’t bear.
    "Bhosdike, tere scam ne poore khandan ki izzat zameen mein mila di.",  # Asshole, your scam buried the honor of the whole family.
    "Laude ke baal, tu woh kalank hai jo kabhi na saaf ho.",  # Pubic hair dick, you’re the stain that can never be cleaned.
    "Saale chutiye, tu scam karta hai aur log teri galiyon ko chor dein.",  # Idiot, you scam and people abandon your street.
    # 71-80
    "Madarchod, tu scam karta hai aur mohalla tujhe dekh kar roye.",  # Motherfucker, you scam and your neighborhood weeps seeing you.
    "Behenchod, tu ghar ki izzat ka woh chor hai jo sab loot le.",  # Sisterfucker, you are the thief of your home’s honor.
    "Bhosdike, tere scam se shadiyon ka mandap gir jaaye.",  # Asshole, your scam makes wedding mandaps collapse.
    "Laude, tere hone se har gali ki hawa tez ho gayi tujh se bachne ko.",  # Dickhead, your existence made the wind blow harder just to escape you.
    "Saale gandu, tere scam se tere bachchon ki maang ujadd gayi.",  # Assfucker, your scam destroyed your children’s future.
    "Madarchod, tu scam karta hai aur bazaar ki dukanein band ho jaayein.",  # Motherfucker, you scam and the shops of the market shut down.
    "Behen ke laude, tere hone se purkhe kabar mein palat gaye.",  # Sister’s dick, your existence made your ancestors turn in their graves.
    "Bhosdike, tu ghar ka wo dhabba hai jo har deewar pe laga hai.",  # Asshole, you are the stain splattered on every wall of the house.
    "Laude ke baal, tu woh rog hai jo har nasl mein failta rahe.",  # Pubic hair dick, you’re the disease that spreads in every generation.
    "Saale chutiye, tu scam karta hai aur samaj ka sir jhukta hai.",  # Idiot, you scam and society bows its head.
    # 81-90
    "Madarchod, tere scam pe desh ki zameen bhi toote.",  # Motherfucker, your scam cracks the nation’s ground.
    "Behenchod, tu woh zehar hai jo poori basti ko barbad kare.",  # Sisterfucker, you’re the poison that ruins the whole colony.
    "Bhosdike, tu scam karta hai aur school ke bacche rote hain.",  # Asshole, you scam and schoolchildren cry.
    "Laude, tere hone se izzat khud zameen mein ghus jaaye.",  # Dickhead, your existence makes honor bury itself.
    "Saale gandu, tu ghar ka woh bojh hai jo sab pe bhari padta hai.",  # Assfucker, you are the burden that weighs down everyone at home.
    "Madarchod, tere scam se mandir ki ghanti tak tut gayi.",  # Motherfucker, your scam broke the temple bell.
    "Behen ke laude, tere scam pe izzat ne apna gala ghot diya.",  # Sister’s dick, your scam made honor strangle itself.
    "Bhosdike, tere hone se gali ka naam hi badnaam ho gaya.",  # Asshole, your existence disgraced the name of your street.
    "Laude ke baal, tu woh kalank hai jo har nasl ko dard de.",  # Pubic hair dick, you’re the stain that hurts every generation.
    "Saale chutiye, tu scam karta hai aur poora ilaqa sharm se doob jaye.",  # Idiot, you scam and the whole area drowns in shame.
    # 91-100
    "Madarchod, tu scam karta hai aur desh ka har kona andhera ho jaye.",  # Motherfucker, you scam and every corner of the country goes dark.
    "Behenchod, tere hone se ghar ki roshni bujh gayi.",  # Sisterfucker, your existence snuffed out the house’s light.
    "Bhosdike, tu scam karta hai aur log apni zubaan band kar lein.",  # Asshole, you scam and people seal their lips.
    "Laude, tu woh saala hai jise dekh kar mohalle ki galiyan khali ho jayein.",  # Dickhead, you’re the bastard that empties the streets of your neighborhood.
    "Saale gandu, tu scam karta hai aur desh ki hawa badboo failaye.",  # Assfucker, you scam and stink up the nation’s air.
    "Madarchod, tu ghar ka woh rog hai jo har saans dard de.",  # Motherfucker, you’re the disease of the house that makes every breath hurt.
    "Behen ke laude, tere scam se log apni aankhen chhupayein.",  # Sister’s dick, your scam makes people hide their eyes.
    "Bhosdike, tu woh kalank hai jise zameen bhi na sahe.",  # Asshole, you’re the stain the earth itself won’t bear.
    "Laude ke baal, tu scam karta hai aur poori duniya tujhe thooke.",  # Pubic hair dick, you scam and the whole world spits on you.
    "Saale chutiye, tu scam karta hai aur tere baap dada ki rooh cheekh uthe.",  # Idiot, you scam and your ancestors’ souls scream.
],

"Pack2": [
    "Madarchod, tere scam ki kalank ki lakeer tere bachchon ke chehre pe likhi hai.",  # Motherfucker, the mark of disgrace from your scam is written on your kids’ faces.
    "Behenchod, tujhe dekh kar tere bachche bhi sharam se mooh chhupayenge.",  # Sisterfucker, seeing you, even your children will hide their faces in shame.
    "Bhosdike, teri gandagi ka bojh tere bachchon ki gardan tod dega.",  # Asshole, the weight of your filth will break your kids’ necks.
    "Laude, tu scam karke apni aulad ki zindagi andheron mein daal raha hai.",  # Dickhead, you are throwing your children’s lives into darkness with your scams.
    "Saale chutiye, tere bacche tere naam se nafrat karenge.",  # Idiot, your kids will hate your name.
    "Madarchod, tere scam se tere bachchon ki kismat par kalank lag gaya.",  # Motherfucker, your scam has stained your children’s fate.
    "Behen ke laude, tere scam ka dard tere bachchon ki rooh tak jaayega.",  # Sister’s dick, the pain of your scam will reach your kids’ souls.
    "Bhosdike, tere hone se tere bachchon ki izzat zameen mein mil gayi.",  # Asshole, your existence buried your children’s honor in the dirt.
    "Laude ke baal, tu woh bojh hai jo tere bachchon ki kamar tod de.",  # Pubic hair dick, you’re the burden that will break your kids’ backs.
    "Saale gandu, tere scam ne tere bachchon ke sapne bhi jala diye.",  # Assfucker, your scam burned your children’s dreams.
    "Madarchod, tere bachche zindagi bhar tere paapon ki saza bhugtenge.",  # Motherfucker, your kids will pay for your sins all their lives.
    "Behenchod, tere scam se tere bachchon ko duniya mein jhukti gardan mil gayi.",  # Sisterfucker, your scam gave your kids bowed heads in the world.
    "Bhosdike, tere naam ki kalank ki chhaap tere bachchon ke bachpan pe lagi hai.",  # Asshole, the stamp of disgrace from your name is on your kids’ childhoods.
    "Laude, tere scam se tere bachche kabhi sar utha ke na jee sakein.",  # Dickhead, because of your scam your kids will never live with their heads high.
    "Saale chutiye, tere bacchon ki pehchan sirf teri gandagi ban gayi hai.",  # Idiot, your filth became your kids’ identity.
    "Madarchod, tu scam karke apni aulad ko narak ka rasta dikha raha hai.",  # Motherfucker, your scam is leading your kids to hell.
    "Behen ke laude, tere hone se tere bachchon ki rooh bhi kalankit ho gayi.",  # Sister’s dick, your existence stained even your children’s souls.
    "Bhosdike, tu woh dhabba hai jo tere bachchon ki zindagi bhar saath rahega.",  # Asshole, you’re the stain that will stay with your kids forever.
    "Laude ke baal, tere scam ki badboo tere bachchon ke saath kabar tak jaayegi.",  # Pubic hair dick, the stench of your scam will follow your kids to their graves.
    "Saale gandu, tu apne bachchon ki izzat ka kaatna ban gaya.",  # Assfucker, you became the butcher of your children’s honor.
    "Madarchod, tere scam se tere bachchon ka naam bhi gali ban gaya.",  # Motherfucker, your scam turned your children’s name into a curse.
    "Behenchod, tere scam ki kalank kahani tere bachchon tak pahunchegi.",  # Sisterfucker, the tale of your disgrace will reach your kids.
    "Bhosdike, tere hone se tere bachche har jagah beizzati se jiyenge.",  # Asshole, because of you your kids will live in shame everywhere.
    "Laude, tere scam se tere bachchon ka har rishta toot gaya.",  # Dickhead, your scam broke every bond your kids had.
    "Saale chutiye, tu woh bojh hai jo tere bachchon ki rooh tak ghus gaya.",  # Idiot, you are the burden that sank into your kids’ souls.
    "Madarchod, tere scam ki wajah se tere bachche kabhi sukoon na paayenge.",  # Motherfucker, your scam will never let your kids find peace.
    "Behen ke laude, tere scam se tere bachchon ka kal andhera ho gaya.",  # Sister’s dick, your scam darkened your children’s future.
    "Bhosdike, tere hone se tere bachchon ka har din ek saza ban gaya.",  # Asshole, your existence turned your kids’ every day into a punishment.
    "Laude ke baal, tere scam ne tere bachchon ka bachpan cheen liya.",  # Pubic hair dick, your scam stole your kids’ childhood.
    "Saale gandu, tu woh zehar hai jo tere bachchon ki naso mein fail gaya.",  # Assfucker, you’re the poison that spread into your kids’ veins.
    "Madarchod, tu apni aulad ki shakal pe kalank ban gaya.",  # Motherfucker, you became the stain on your kids’ faces.
    "Behenchod, tere scam ki chhaap tere bachchon ki kabar tak pahunchegi.",  # Sisterfucker, the mark of your scam will follow your kids to their graves.
    "Bhosdike, tu apni aulad ki kismat ka kasai ban gaya.",  # Asshole, you became the butcher of your kids’ fate.
    "Laude, tere scam se tere bachchon ko izzat kabhi naseeb na ho.",  # Dickhead, because of your scam your kids will never know honor.
    "Saale chutiye, tere hone se tere bachchon ke sapne mar gaye.",  # Idiot, your existence killed your kids’ dreams.
    "Madarchod, tere scam ne tere bachchon ka maang bhar diya kalank se.",  # Motherfucker, your scam filled your kids’ lives with disgrace.
    "Behen ke laude, tu woh saaya hai jo tere bachchon ka jeevan andhera kare.",  # Sister’s dick, you are the shadow that darkens your kids’ lives.
    "Bhosdike, tu woh chhaya hai jo tere bachchon ko kabhi sukh na de.",  # Asshole, you’re the shade that will never give your kids peace.
    "Laude ke baal, tere scam se tere bachchon ka naam bhi kali kitaabon mein likha gaya.",  # Pubic hair dick, your scam wrote your kids’ names in black books.
    "Saale gandu, tu apni aulad ki izzat ka dushman hai.",  # Assfucker, you are the enemy of your kids’ honor.
    "Madarchod, tere scam ki badboo tere bachchon ki naslon tak jaayegi.",  # Motherfucker, the stench of your scam will reach your children’s descendants.
    "Behenchod, tere scam ne tere bachchon ki maa ki god suni kar di.",  # Sisterfucker, your scam emptied your kids’ mother’s lap.
    "Bhosdike, tu woh bojh hai jo tere bachchon ki haddi tod dega.",  # Asshole, you’re the burden that will break your kids’ bones.
    "Laude, tere scam ne tere bachchon ki duniya andheri kar di.",  # Dickhead, your scam darkened your children’s world.
    "Saale chutiye, tu woh laanat hai jo tere bachchon ko zindagi bhar sataayega.",  # Idiot, you’re the curse that will haunt your kids forever.
    "Madarchod, tere scam ki wajah se tere bachchon ko sirf beizzati milegi.",  # Motherfucker, because of your scam your kids will only find shame.
],

"Pack3": [
    "Madarchod, tere scam ne tere ghar ke darwazon tak ko badnaam kar diya.",  # Motherfucker, your scam disgraced even your home’s doors.
    "Behenchod, tujhe dekh kar tere ghar ki deewarein bhi laanat bhejein.",  # Sisterfucker, seeing you even your house’s walls curse you.
    "Bhosdike, tu wo gandagi hai jisse tere ghar ka har kone kalankit hai.",  # Asshole, you are the filth that stained every corner of your home.
    "Laude, teri harkatein tere ghar ki izzat ka janaza nikal gayi.",  # Dickhead, your deeds carried your home’s honor to its funeral.
    "Saale chutiye, tere scam se tere ghar ki zameen bhi sharminda hai.",  # Idiot, your scam shamed even the ground your house stands on.
    "Madarchod, tere ghar ka darwaza tujhe dekh kar band ho jaye toh behtar hai.",  # Motherfucker, better if your home’s door shuts at your sight.
    "Behen ke laude, tu woh dhoop hai jo ghar ki chhat tak ko jala de.",  # Sister’s dick, you’re the sun that scorches even your family’s roof.
    "Bhosdike, tere hone se ghar ka har rishte ka rang kala ho gaya.",  # Asshole, your existence blackened every family bond.
    "Laude ke baal, tu ghar ki mitti tak ko kalankit kar gaya.",  # Pubic hair dick, you disgraced even the soil of your home.
    "Saale gandu, tere scam ne ghar ke naam ko gali banaya.",  # Assfucker, your scam turned your family’s name into a curse.
    "Madarchod, tere ghar ki hawa bhi tujhe dekh kar gandh failaye.",  # Motherfucker, even your home’s air stinks seeing you.
    "Behenchod, tere hone se tere ghar ka diya bujh gaya.",  # Sisterfucker, your existence extinguished the lamp of your house.
    "Bhosdike, tu woh rog hai jo tere ghar ki naso mein fail gaya.",  # Asshole, you’re the disease that spread through your home’s veins.
    "Laude, tere scam pe ghar ki roshni ne andhera maang liya.",  # Dickhead, your scam made your home’s light beg for darkness.
    "Saale chutiye, tu ghar ka woh bojh hai jo kabhi na uthe.",  # Idiot, you’re the burden your house can never lift.
    "Madarchod, tere ghar ki izzat ne tere scam pe apni maut maang li.",  # Motherfucker, your family’s honor begged for death because of your scam.
    "Behen ke laude, tu ghar ka woh dhabba hai jo kabhi dhule na.",  # Sister’s dick, you are the stain that will never wash off your home.
    "Bhosdike, tere hone se tere ghar ki deewar bhi cheekh uthi.",  # Asshole, your existence made even your walls scream.
    "Laude ke baal, tere ghar ka naam sunte hi log thook de.",  # Pubic hair dick, people spit hearing your family’s name.
    "Saale gandu, tu ghar ka woh kalank hai jo har peedhi ko jaleel kare.",  # Assfucker, you’re the disgrace that humiliates every generation of your family.
    "Madarchod, tere scam ne ghar ki chhat tak ko zameen pe gira diya.",  # Motherfucker, your scam brought even your roof crashing down.
    "Behenchod, tu ghar ki izzat ka wo bojh hai jo sab uthate uthate tut gaye.",  # Sisterfucker, you’re the burden of honor that broke everyone trying to lift it.
    "Bhosdike, tu ghar ki mitti pe woh kalank hai jo baarish bhi na dho sake.",  # Asshole, you’re the stain on your home’s soil that no rain can wash.
    "Laude, tere scam ne ghar ki har deewar pe laanat likhwa di.",  # Dickhead, your scam etched a curse on every wall of your home.
    "Saale chutiye, tere hone se ghar ka har kona andhera ho gaya.",  # Idiot, your existence darkened every corner of your house.
    "Madarchod, tu ghar ki rooh ka woh zakham hai jo kabhi bhare na.",  # Motherfucker, you are the wound in your home’s soul that will never heal.
    "Behen ke laude, tu ghar ka woh saaya hai jo andhera hi failaye.",  # Sister’s dick, you are the shadow that only spreads darkness at home.
    "Bhosdike, tere scam se ghar ka har rishta toot gaya.",  # Asshole, your scam broke every bond in your family.
    "Laude ke baal, tu ghar ka naam mitti mein mila kar khud bacha baitha.",  # Pubic hair dick, you dragged your family’s name through the mud and sat safe.
    "Saale gandu, tere hone se ghar ka har diya bujh gaya.",  # Assfucker, your existence snuffed out every lamp in your house.
    "Madarchod, tu ghar ki deewar pe wo kalank hai jo sirf dard de.",  # Motherfucker, you are the stain on your house’s walls that only brings pain.
    "Behenchod, tere scam pe ghar ki roshni ne mooh mod liya.",  # Sisterfucker, your scam made the light of your house turn away.
    "Bhosdike, tu ghar ki chhat ka woh bojh hai jo kabhi na uthe.",  # Asshole, you are the burden on your home’s roof that never lifts.
    "Laude, tere scam se ghar ki izzat ki chita jal gayi.",  # Dickhead, your scam burned the pyre of your family’s honor.
    "Saale chutiye, tu ghar ka wo laanat hai jo kabhi na mite.",  # Idiot, you are the curse on your home that will never be erased.
    "Madarchod, tu ghar ki rooh tak ko kalankit kar gaya.",  # Motherfucker, you disgraced even the soul of your house.
    "Behen ke laude, tere hone se ghar ki mitti bhi royi.",  # Sister’s dick, your existence made your home’s soil cry.
    "Bhosdike, tere scam ne ghar ki chhat tak ko thook dilaya.",  # Asshole, your scam made even your roof get spit upon.
    "Laude ke baal, tu ghar ki izzat ka wo bojh hai jo sab tod de.",  # Pubic hair dick, you’re the burden of honor that breaks everyone.
    "Saale gandu, tere scam se ghar ki deewaron ne mooh chhupa liya.",  # Assfucker, your scam made your house’s walls hide their faces.
    "Madarchod, tere hone se ghar ka naam logon ki gali ban gaya.",  # Motherfucker, your family’s name became a curse on people’s lips because of you.
    "Behenchod, tu ghar ki izzat ki wo chhaya hai jo kabhi roshni na de.",  # Sisterfucker, you’re the shadow of honor that never gives light.
    "Bhosdike, tu ghar ki mitti ka wo kalank hai jo peedhi dar peedhi lage.",  # Asshole, you’re the stain on your family’s soil that sticks for generations.
    "Laude, tere scam ne ghar ki roshni ko andhera de diya.",  # Dickhead, your scam gave darkness to your home’s light.
    "Saale chutiye, tu ghar ka woh dard hai jo kabhi na theek ho.",  # Idiot, you are the pain of your house that never heals.
    "Madarchod, tu ghar ka woh rog hai jo sabko barbaad kare.",  # Motherfucker, you are the disease of your house that ruins everyone.
    "Behen ke laude, tu ghar ki izzat ka woh dushman hai jo kabhi na hare.",  # Sister’s dick, you are the enemy of your family’s honor that never loses.
],

"Pack4": [
    "Behenchod, tujhe paida kar ke mainne hi sabse bada paap kiya.",  # Sisterfucker, birthing you was my greatest sin.
    "Madarchod, tu mera lahu nahi ho sakta, itna gira hua insaan ban gaya.",  # Motherfucker, you can’t be my blood—you’ve fallen so low.
    "Bhosdike, tere scam dekh kar mainne baap hone ka hak kho diya.",  # Asshole, your scams stripped me of the right to be called a father.
    "Laude, tujhe paida karte waqt hi zameen phatni chahiye thi.",  # Dickhead, the ground should’ve swallowed you at birth.
    "Saale chutiye, tujhe sikha ke mainne apni izzat doobayi.",  # Idiot, teaching you drowned my own honor.
    "Behen ke laude, tu har din meri rooh ko dard deta hai.",  # Sister’s dick, every day you bring pain to my soul.
    "Madarchod, tu mere liye zinda laash hai.",  # Motherfucker, to me you are a living corpse.
    "Bhosdike, mainne tujhe insaan banaya, tu dhokebaaz ban gaya.",  # Asshole, I raised you a man, you became a fraud.
    "Laude ke baal, tujhe baap kehne mein ab sharam aati hai.",  # Pubic hair dick, now I’m ashamed to be called your father.
    "Saale gandu, tere scam dekh kar khud shaitan bhi haansa hoga.",  # Assfucker, even the devil must have laughed at your scams.
    "Behenchod, tu har din meri umr ghaata hai.",  # Sisterfucker, every day you shorten my life.
    "Madarchod, tu ghar ka kalank ban gaya hai.",  # Motherfucker, you’ve become the disgrace of the house.
    "Bhosdike, tere scam ki wajah se log mere muh pe thookte hain.",  # Asshole, because of your scams people spit on my face.
    "Laude, main tujhe paida na karta to behtar hota.",  # Dickhead, better if I’d never fathered you.
    "Saale chutiye, tere scam se ghar ki deewar bhi sharmati hai.",  # Idiot, even the walls of the house are ashamed of your scams.
    "Behen ke laude, tere hone se mera sir jhuka hai duniya ke samne.",  # Sister’s dick, your existence has bowed my head in front of the world.
    "Madarchod, tere scam ki badbu purkho ki kabar tak ja rahi hai.",  # Motherfucker, the stench of your scams reaches the ancestors’ graves.
    "Bhosdike, main tujhe dafan kar doon to zameen bhi naraz ho jaye.",  # Asshole, if I bury you, even the earth will be angry.
    "Laude ke baal, tere scam se tere bhai ki izzat doob gayi.",  # Pubic hair dick, your scams ruined your brother’s honor.
    "Saale gandu, tu mere lahu ki sabse ghatiya misaal hai.",  # Assfucker, you’re the worst example of my blood.
    "Behenchod, tujhe paida karne ki soch bhi shraap ban gayi.",  # Sisterfucker, even the thought of fathering you became a curse.
    "Madarchod, tu mere sapno ka laash hai.",  # Motherfucker, you are the corpse of my dreams.
    "Bhosdike, tere scam dekh kar mainne baap banne se nafrat ki.",  # Asshole, your scams made me hate being a father.
    "Laude, tu ghar ka bojh hai jo uthate uthate kamar toot gayi.",  # Dickhead, you are the burden that broke my back.
    "Saale chutiye, tu woh dard hai jo kabhi mita na sake.",  # Idiot, you’re the pain that can never be erased.
    "Behen ke laude, teri harkaton se ghar ka diya bujh gaya.",  # Sister’s dick, your deeds extinguished the family’s light.
    "Madarchod, tere scam se maa ki god suni pad gayi.",  # Motherfucker, your scam left your mother’s lap empty.
    "Bhosdike, tu woh beta hai jise dekh kar maut bhi ghabraye.",  # Asshole, you’re the son that makes death itself afraid.
    "Laude ke baal, tu scam karta hai aur main zameen mein girta hoon.",  # Pubic hair dick, you scam and I sink into the ground.
    "Saale gandu, teri wajah se apni beti ka rishta tod diya.",  # Assfucker, because of you I had to break my daughter’s engagement.
    "Behenchod, tu ghar ki izzat ka dushman hai.",  # Sisterfucker, you are the enemy of the family’s honor.
    "Madarchod, tu wo putra hai jo vanshajon ki gardan jhukata hai.",  # Motherfucker, you are the son who bows your descendants’ heads.
    "Bhosdike, tujhe paida karke maine apni zindagi barbad ki.",  # Asshole, I ruined my life birthing you.
    "Laude, tere scam ne mere doodh ka rang kala kar diya.",  # Dickhead, your scam blackened the milk I fed you.
    "Saale chutiye, tu scam karta hai aur ghar ki chhat girne ko tayyar ho jati hai.",  # Idiot, you scam and the roof prepares to fall.
    "Behen ke laude, tu vansh ka wo rog hai jo har shakha sukhaye.",  # Sister’s dick, you are the disease that withers every branch of the family tree.
    "Madarchod, tere scam ne har rishte ka gala ghont diya.",  # Motherfucker, your scam strangled every family tie.
    "Bhosdike, tujhe beta bolna mere muh pe kalank hai.",  # Asshole, calling you son is a stain on my mouth.
    "Laude ke baal, tu scam kar ke maa ki god se izzat cheenta hai.",  # Pubic hair dick, your scam robs honor from your mother’s lap.
    "Saale gandu, tere scam se ghar ki roshni bujh gayi.",  # Assfucker, your scam snuffed out the light of the house.
    "Behenchod, tu woh dhabba hai jo kabhi dhule na.",  # Sisterfucker, you are the stain that will never wash away.
    "Madarchod, tere scam pe ghar ki deewarein cheekh uthi.",  # Motherfucker, your scam made the house’s walls scream.
    "Bhosdike, tu woh kalank hai jo har purkhe ko sharminda kare.",  # Asshole, you are the disgrace that shames every ancestor.
    "Laude, tere scam ne mere sapne ka chirag bujha diya.",  # Dickhead, your scam snuffed out the lamp of my dreams.
    "Saale chutiye, tu ghar ka bojh hai jo kabhi na uthe.",  # Idiot, you are the burden the house can never lift.
    "Behen ke laude, tujhe paida karna hi sabse bada apmaan tha.",  # Sister’s dick, birthing you was the greatest insult of all.
    "Madarchod, tere scam pe ghar ki mitti bhi roye.",  # Motherfucker, even the soil of the house cries over your scam.
],

"Pack5": [
    "Madarchod, tu wo kalank hai jiska bojh tere bachchon ko bhi uthana padega.",  # Motherfucker, you're the disgrace your kids will be forced to carry.
    "Bhosdike, teri har harqat teri aane wali naslon pe thook hai.",  # Asshole, your every act spits on your future generations.
    "Behenchod, tere bachche tujhe baap kehne se sharamayenge.",  # Sisterfucker, your kids will be ashamed to call you father.
    "Laude, tu scam kar ke apne bachchon ka sir jhuka raha hai.",  # Dickhead, your scamming bows your kids’ heads in shame.
    "Saale chutiye, tere bacchon ko teri gandagi dhona padega.",  # Idiot, your kids will have to clean up your filth.
    "Madarchod, tere scam se teri aane wali naslein badnaam hongi.",  # Motherfucker, your scam will disgrace all your descendants.
    "Bhosdike, tujhe dekh kar tere bachchon ki zindagi pe dhabba lagta hai.",  # Asshole, seeing you stains your kids’ lives.
    "Behen ke laude, teri harkaton se tera vansh apna mooh chhupaye.",  # Sister’s dick, your deeds make your bloodline hide its face.
    "Laude ke baal, tu scam karta hai aur apne bachchon ki izzat ko zinda gaad deta hai.",  # Pubic hair dick, your scam buries your kids’ honor alive.
    "Saale randi ke bacche, teri wajah se teri maa baap ki rooh kabar mein tadapti hai.",  # Son of a whore, because of you your parents’ souls suffer in their graves.
    "Madarchod, tere bachche tujhe apni zindagi ka kalank manenge.",  # Motherfucker, your kids will consider you the shame of their life.
    "Behenchod, tere scam ne teri maa ki izzat ko mitti mein mila diya.",  # Sisterfucker, your scam dragged your mother’s honor into the dirt.
    "Bhosdike, teri wajah se tere pita ka sar kab ka jhuk chuka hai.",  # Asshole, because of you your father’s head has long bowed in shame.
    "Laude, tere hone se teri aane wali peedhiyaan badnaam ho gayi.",  # Dickhead, your existence disgraced future generations.
    "Saale gandu, teri har harkat teri family ke muh pe kalank hai.",  # Assfucker, your every action is a stain on your family’s face.
    "Madarchod, teri maa ki god teri wajah se kab ka suni ho gayi.",  # Motherfucker, your mother’s lap has long been empty because of you.
    "Behen ke laude, tere scam se tujhe dekh kar tera beta bhi ro padta.",  # Sister’s dick, seeing your scams even your son would cry.
    "Bhosdike, tu wo kalank hai jise teri aulad kabhi mita na sake.",  # Asshole, you're the stain your kids can never erase.
    "Laude ke baal, tu scam kar ke apne vansh pe pathar daal raha hai.",  # Pubic hair dick, your scam is casting stones on your family name.
    "Saale chutiye, tere scam ki badbu teri naslon tak jaayegi.",  # Idiot, the stench of your scam will reach your descendants.
    "Madarchod, tujhe dekh kar teri maa ki rooh bhi roti hai.",  # Motherfucker, seeing you even your mother's soul weeps.
    "Behenchod, tere scam se tere dada ki kabar ki mitti bhi kalankit ho gayi.",  # Sisterfucker, your scam disgraced your grandfather’s grave soil.
    "Bhosdike, teri wajah se tera vansh kab ka mitti mein mil gaya.",  # Asshole, your family’s name was buried because of you.
    "Laude, teri aulad tujhe apna laash manegi.",  # Dickhead, your kids will see you as their corpse.
    "Saale randi ke bacche, tu scam karta hai aur teri purkhon ki rooh cheekh uthti hai.",  # Son of a whore, your scam makes your ancestors’ souls scream.
    "Madarchod, tere hone se teri family ka har rishte ka gala ghut gaya.",  # Motherfucker, your existence choked every family relationship.
    "Behen ke laude, tujhe dekh kar teri beti bhi apna naam badalne ki soche.",  # Sister’s dick, seeing you even your daughter will want to change her name.
    "Bhosdike, teri maa baap ki poori izzat teri harkaton se doob gayi.",  # Asshole, your actions drowned your parents’ entire honor.
    "Laude ke baal, teri gandagi vanshajon ki naso tak fail gayi.",  # Pubic hair dick, your filth has spread into your descendants’ veins.
    "Saale chutiye, tu wo rog hai jo har nasl ko beizzat kare.",  # Idiot, you're the disease that shames every generation.
    "Madarchod, tere scam se teri aane wali naslein kab ka narak mein jhulsi.",  # Motherfucker, your scams burned your descendants in hell.
    "Behenchod, tu wo karz hai jo tere bachchon ki jaan le lega.",  # Sisterfucker, you’re the debt that will take your kids’ lives.
    "Bhosdike, tere hone se teri maa baap ki chita jal gayi.",  # Asshole, your existence burned your parents’ funeral pyre.
    "Laude, tere bachchon ka bhavishya teri harqaton se andhere mein hai.",  # Dickhead, your deeds have cast your kids’ future into darkness.
    "Saale gandu, tere scam pe purkhon ne apna naam mitaa diya.",  # Assfucker, your scam made your ancestors erase their names.
    "Madarchod, tere ghar ka naam tujhe dekh kar logon ki zubaan se gayab ho gaya.",  # Motherfucker, your family’s name disappeared from people’s tongues seeing you.
    "Behen ke laude, tu wo dard hai jo tere bachchon ki rooh tak jaayega.",  # Sister’s dick, you’re the pain that will reach your kids’ souls.
    "Bhosdike, tere scam pe vansh ka har patta murjha gaya.",  # Asshole, your scam wilted every leaf of your family tree.
    "Laude ke baal, tu wo kalank hai jo aane wali peedhi ko zameen mein mila de.",  # Pubic hair dick, you’re the disgrace that buries future generations.
    "Saale chutiye, tu scam karta hai aur izzat kab ka marr chuki hai.",  # Idiot, you scam and honor has long been dead.
    "Madarchod, tere scam pe tere bachchon ki zindagi ujadd gayi.",  # Motherfucker, your scam ruined your kids’ lives.
    "Behenchod, tu wo andhera hai jo vanshajon ki roshni bujha de.",  # Sisterfucker, you’re the darkness that extinguishes descendants’ light.
    "Bhosdike, tere hone se har rishte ka bandhan toot gaya.",  # Asshole, your existence broke every family bond.
    "Laude, tere scam pe tera ghar barbad ho gaya.",  # Dickhead, your scam destroyed your home.
    "Saale randi ke bacche, tu wo dhabba hai jo kabhi dhula na jaaye.",  # Son of a whore, you’re the stain that can never be cleaned.
    "Madarchod, tu scam karta hai aur vanshajon ki kismat jala deta hai.",  # Motherfucker, your scam burns your descendants’ fate.
    "Behen ke laude, tu wo bojh hai jo tere bachchon ki kamar tod de.",  # Sister’s dick, you’re the burden that breaks your kids’ backs.
],

"Pack6": [
    "Madarchod, tere jaise scammer ki vajah se vanshaj shraap le kar paida hote hain.",  # Motherfucker, because of scammers like you, descendants are born cursed.
    "Bhosdike, teri maa ki kasam, tere scam ne ghar ki har izzat ko zameen mein ghusa diya.",  # Asshole, your scam buried all your family's honor.
    "Behenchod, tere scam pe teri poori family ki rooh kabar mein karahi maare.",  # Sisterfucker, your scam makes your entire family’s souls scream in their graves.
    "Laude, tu wo dhabba hai jo har peedhi ke mooh pe lag kar baitha hai.",  # Dickhead, you’re the stain smeared on every generation’s face.
    "Saale chutiye, tere scam ne vanshajon ko sharam se zameen mein mila diya.",  # Idiot, your scam made your descendants sink into shame.
    "Madarchod, teri wajah se purkhe bhi naam badal kar jeene ko majboor hain.",  # Motherfucker, because of you even ancestors want to change their names.
    "Bhosdike, teri maa ne tujhe janm de kar sabse bada paap kiya.",  # Asshole, your mother sinned the most by birthing you.
    "Behen ke laude, tu scam karta hai aur izzat gaand me ghus jati hai.",  # Sister’s dick, you scam and honor gets fucked.
    "Laude, tere hone se vanshaj apni kabar khud khodne lage.",  # Dickhead, your existence makes descendants dig their own graves.
    "Saale gandu, tere ghar ki deewarein bhi tujhe dekh kar toot jaayein.",  # Assfucker, even your house’s walls would collapse seeing you.
    "Madarchod, tu scam karte hi izzat ki laash uthata hai.",  # Motherfucker, you lift honor’s corpse the moment you scam.
    "Behenchod, tere scam ki badbu saari duniya mehsoos kare.",  # Sisterfucker, the stench of your scam is felt by the whole world.
    "Bhosdike, tere ghar ka darwaza bhi tujhe dekh kar band ho jaaye.",  # Asshole, even your door slams shut at the sight of you.
    "Laude ke baal, tu wo daag hai jo sabki roohon tak chipka hai.",  # Pubic hair dick, you’re the stain that clings to everyone’s soul.
    "Saale randi ke bacche, tere scam ne ghar ki izzat ko zinda jala diya.",  # Son of a whore, your scam burned your family’s honor alive.
    "Madarchod, teri maa ki god se izzat kab ka nikal gayi.",  # Motherfucker, honor left your mother’s lap long ago.
    "Behen ke laude, tu wo kalank hai jo vanshajon ki chhati pe chipka hai.",  # Sister’s dick, you’re the disgrace stuck on your descendants’ chest.
    "Bhosdike, tu scam karta hai aur purkhe kabar se bhaag jaate hain.",  # Asshole, your scamming makes ancestors flee their graves.
    "Laude, teri shakal dekh kar maut bhi darr ke door bhage.",  # Dickhead, seeing your face even death runs away in fear.
    "Saale chutiye, tu scam se izzat ki aakhri chingari bujha deta hai.",  # Idiot, your scam extinguishes the last spark of honor.
    "Madarchod, tere ghar ka naam to dharti se mita diya gaya hota to behtar tha.",  # Motherfucker, better if your family’s name was erased from the earth.
    "Behenchod, tere scam ne shaitaan ki izzat badha di.",  # Sisterfucker, your scam raised the devil’s honor.
    "Bhosdike, tere hone se vansh ki peedhi pe peedhi barbaad hui.",  # Asshole, your existence ruined generation after generation.
    "Laude, teri har saans pe vanshajon ki rooh kaapti hai.",  # Dickhead, every breath you take makes your descendants’ souls tremble.
    "Saale gandu, tu scam karta hai aur insaniyat ko thookna padta hai.",  # Assfucker, you scam and humanity has to spit.
    "Madarchod, tere scam pe izzat kab ka mar gayi.",  # Motherfucker, honor has long died because of your scam.
    "Behen ke laude, tu vansh ka wo ghaav hai jo kabhi bhare na.",  # Sister’s dick, you’re the wound of your family that never heals.
    "Bhosdike, tere ghar ki chhat tujhe dekh kar girne ko tayyar rahe.",  # Asshole, your roof stays ready to collapse seeing you.
    "Laude, tu wo gandagi hai jo vanshajon ke lahu tak fail gayi.",  # Dickhead, you’re the filth that spread into your descendants’ blood.
    "Saale chutiye, tu scam karta hai aur izzat apna gala ghot leti hai.",  # Idiot, your scam makes honor strangle itself.
    "Madarchod, tere scam pe vanshaj sapne dekhna chhod dein.",  # Motherfucker, your scam made your descendants stop dreaming.
    "Behenchod, tu wo rog hai jo har nasl ko barbaad kar de.",  # Sisterfucker, you’re the disease that ruins every generation.
    "Bhosdike, tu scam karta hai aur rooh kabar mein cheekhne lage.",  # Asshole, your scam makes souls scream in their graves.
    "Laude ke baal, tu vansh ka wo saala hai jise shaitan bhi bhool jaye.",  # Pubic hair dick, you’re the bastard of your family the devil forgets.
    "Saale randi ke bacche, tere hone se zameen pe dharti bhi pighal jaye.",  # Son of a whore, your existence melts the ground beneath you.
    "Madarchod, tu scam karta hai aur sharam zameen mein samajh jaye.",  # Motherfucker, your scam buries shame deep into the earth.
    "Behen ke laude, tere jaise ko dekh kar purkhe apni mitti chhod dein.",  # Sister’s dick, your ancestors would abandon their graves seeing you.
    "Bhosdike, tere hone se izzat ne tere ghar ka rasta bhool gaya.",  # Asshole, your existence made honor forget your home’s path.
    "Laude, tu wo kalank hai jo har peedhi ka sir jhuka de.",  # Dickhead, you’re the disgrace that bows every generation’s head.
    "Saale chutiye, tu scam karta hai aur vansh ka ped sookh jata hai.",  # Idiot, your scam withers your family tree.
    "Madarchod, tu scam karta hai aur purkhon ki roohon ko laanat lagti hai.",  # Motherfucker, your scam curses your ancestors’ souls.
    "Behenchod, tere ghar ki mitti bhi tujhe dekh kar saaf hone se inkaar kare.",  # Sisterfucker, even your home’s soil refuses to clean seeing you.
    "Bhosdike, tu wo bojh hai jo har peedhi uthate uthate toot jaye.",  # Asshole, you’re the burden that breaks every generation.
    "Laude, tere scam ne vanshajon ke muh pe kaala kar diya.",  # Dickhead, your scam blackened your descendants’ faces.
    "Saale gandu, tu wo laanat hai jo kabhi mita na sake.",  # Assfucker, you’re the curse that can never be erased.
    "Madarchod, tere hone se har purkha apni kabar mein sharmaye.",  # Motherfucker, your existence makes every ancestor ashamed in their grave.
],

"Pack7": [
    "Madarchod, tere ghar ka har peedhi ka naam kalank hai, aur tu sabse bada dhabba.",  # Motherfucker, your whole lineage is a disgrace, and you’re the biggest stain.
    "Bhosdike, tujhe dekh kar teri aane wali saat naslein apni pehchan chhupaengi.",  # Asshole, seeing you, seven generations after you will hide their identity.
    "Behenchod, tujhe paida karke teri maa ne apni maa ka naam dooba diya.",  # Sisterfucker, your birth shamed your mother’s mother.
    "Saale scammer ke bacche, tujhe dekh kar toh chor bhi imandari ki kasam khayein.",  # Son of a scammer, even thieves swear honesty seeing you.
    "Laude, tu wo haramkhor hai jise dekh kar dhokebaazi bhi sharmaye.",  # Dickhead, you're the bastard that makes betrayal itself feel shame.
    "Madarchod, teri har saans tere baap dada pe thook hai.",  # Motherfucker, every breath you take spits on your ancestors.
    "Behen ke laude, tujhe dekh kar to kabristan ki roohen bhi karahi maarein.",  # Sister’s dick, seeing you even souls in graves groan.
    "Bhosdike, tera poora vansh sirf beizzati ka mausam hai.",  # Asshole, your whole bloodline is a season of disgrace.
    "Saale randi ke bacche, tere ghar ki izzat to tujhe dekh kar suicide kar gayi.",  # Son of a whore, your family's honor killed itself seeing you.
    "Laude, teri soch pe teri aane wali naslein case karengi.",  # Dickhead, your descendants will sue your thoughts.
    "Madarchod, scam karte waqt tujhe apni maa ki kasam bhi sharminda karti hogi.",  # Motherfucker, even your mother’s name feels ashamed while you scam.
    "Behenchod, teri wajah se teri purkhon ki rooh bhatakti hai.",  # Sisterfucker, your ancestors’ souls wander restless because of you.
    "Bhosdike, tere scam pe to shaitaan bhi hath jod kar mafi maange.",  # Asshole, even the devil would beg forgiveness seeing your scams.
    "Laude ke baal, tu wo dhabba hai jo vansh ke kabhi na dho sake.",  # Pubic hair dick, you’re the stain your lineage can never wash off.
    "Saale chutiye, tere ghar ki diwaron ne teri harkaton pe rona seekh liya.",  # Idiot, your house’s walls have learned to weep because of your deeds.
    "Madarchod, tere scam se to teri maa ki god bhi badnaam hui.",  # Motherfucker, your scam shamed even your mother’s lap.
    "Behen ke laude, tu scam karta hai aur teri purkhon ki roohen zameen mein kaanp uthti hain.",  # Sister’s dick, your scamming makes your ancestors’ souls tremble.
    "Bhosdike, tere ghar ka har insaan tere naam pe gaali ban gaya.",  # Asshole, everyone in your family has become a curse because of your name.
    "Laude, tere jaise ko dekh kar bhagwan ne banawat pe pachtaya hoga.",  # Dickhead, seeing you God must’ve regretted creation.
    "Saale gandu, tu wo shraap hai jo vanshajon ki zindagi barbaad kar de.",  # Assfucker, you’re the curse that ruins your descendants’ lives.
    "Madarchod, tere scam pe toh kabristan ki mitti bhi kalank kahe.",  # Motherfucker, even graveyard soil calls your scams a disgrace.
    "Behenchod, tere ghar ka darwaza bhi tujhe dekh kar band ho jaye.",  # Sisterfucker, even your home’s door shuts seeing you.
    "Bhosdike, tere scam se to insaniyat ne teri family ka naam kaat diya.",  # Asshole, your scamming made humanity disown your family.
    "Laude, tu wo saala hai jiske hone pe purkhon ne ro ro ke aankhien kho di.",  # Dickhead, you’re the bastard that made ancestors weep their eyes out.
    "Saale chutiye, teri harkaton pe vanshaj apni kabar mein palat palat ke sochte hain.",  # Idiot, your actions make your ancestors turn over in their graves.
    "Madarchod, tu scam karta hai aur teri maa ki god se izzat chhink jati hai.",  # Motherfucker, your scams snatch the honor from your mother’s lap.
    "Behen ke laude, tere naam ka zikr hote hi izzat khud ko khatam kar le.",  # Sister’s dick, hearing your name makes honor kill itself.
    "Bhosdike, tere ghar ki nali se izzat ka paani kab ka beh chuka hai.",  # Asshole, the water of honor has long flown out of your house’s drain.
    "Laude, tu wo haramkhor hai jiske liye rishte todne ko sab haan karein.",  # Dickhead, you’re the bastard people break ties over.
    "Saale scammer, tere kaam dekh kar chor bhi izzat bachayein.",  # Scammer, seeing your deeds even thieves protect their honor.
    "Madarchod, tere baap dada ki izzat tere scam se mitti mein mil gayi.",  # Motherfucker, your scamming buried your ancestors’ honor in dirt.
    "Behenchod, tu vansh ka wo kalank hai jise kabhi mita na sake.",  # Sisterfucker, you’re the curse of the family that can never be erased.
    "Bhosdike, tere ghar ki chhat bhi tujhe dekh kar gir padti hai.",  # Asshole, even your roof collapses seeing you.
    "Laude, tere scam se duniya ne teri maa ke doodh pe sawaal uthaya.",  # Dickhead, your scams made the world question your mother’s milk.
    "Saale chutiye, tere hone se vansh ki har shakha sookh gayi.",  # Idiot, your existence dried up every branch of your family tree.
    "Madarchod, tu wo dhokebaaz hai jise dekh kar saala imaan bhi ro de.",  # Motherfucker, you’re the traitor that makes loyalty itself cry.
    "Behen ke laude, tere scam dekh kar shaitan bhi sidha ho gaya.",  # Sister’s dick, your scams made the devil go straight.
    "Bhosdike, tu wo bojh hai jo vanshaj sambhal na sake.",  # Asshole, you’re the burden your descendants can’t bear.
    "Laude ke baal, teri gandagi vanshajon tak pahunchegi.",  # Pubic hair dick, your filth will reach your descendants.
    "Saale scammer, teri har harkat par bhagwan bhi sar pakad le.",  # Scammer, God holds his head at your every act.
    "Madarchod, tere scam ne har purkhe ko zaleel kar diya.",  # Motherfucker, your scam humiliated every ancestor.
    "Behenchod, tu wo dhabba hai jo vanshajon ki peeth pe chipka hai.",  # Sisterfucker, you’re the stain stuck on your descendants’ backs.
    "Bhosdike, tere scam se izzat ne tere ghar se muh mod liya.",  # Asshole, your scams made honor turn away from your home.
    "Laude, tu vansh ka wo soop hai jisme sirf gandagi bachi hai.",  # Dickhead, you’re the sieve of your family that only holds filth.
    "Saale chutiye, tujhe dekh kar izzat khud ko zameen mein gaad de.",  # Idiot, seeing you, honor buries itself underground.
],

"Pack8": [
    "Madarchod, tu wo gandi nali hai jisme keede bhi na padna chahein.",  # Motherfucker, you're that filthy drain even maggots avoid.
    "Behenchod, teri maa ki chut pe to jhaadu bhi toot jaye.",  # Sisterfucker, even a broom would break on your mother's cunt.
    "Bhosdike, teri zindagi to ek bikhari ka sapna hai—beizzat aur bekaar.",  # Asshole, your life is like a beggar’s dream—humiliating and useless.
    "Laude, tu to wo haath ka mail hai jise sab mitana chahen.",  # Dickhead, you’re the dirt on hands everyone wants to wipe off.
    "Saale chutiye, tere jaise haramkhor ko to zameen bhi apna bojh na samjhe.",  # Idiot, even the ground shouldn’t bear the burden of a bastard like you.
    "Oye madarchod, teri aukat ek sadak ke kachre se kam hai.",  # Motherfucker, your worth is less than roadside trash.
    "Behen ke laude, tu wo thook hai jo zameen pe girte hi sukh jaye.",  # Sister’s dick, you’re the spit that dries the moment it hits the ground.
    "Bhosdike, tu to janm ke waqt hi galti tha jo ho gaya.",  # Asshole, you were a mistake at birth that just happened.
    "Laude ke baal, tere jaise ko dekh kar andhe bhi aankhein dhoondhne lage.",  # Pubic hair dick, even the blind would look for their eyes seeing you.
    "Saale randi ke bacche, tere hone se zyada bekaar to andhera hai.",  # Son of a whore, even darkness is more useful than your existence.
    "Madarchod, tu wo phaila hua cancer hai jise dekh kar maut bhi ghabra jaaye.",  # Motherfucker, you're that spreading cancer that scares even death.
    "Behenchod, tere jaise harami ko dekh kar to randi bhi ro padti hai.",  # Sisterfucker, even a whore cries seeing a bastard like you.
    "Bhosdike, tu to wo gandagi hai jo na gutter saaf kare na dharti sahe.",  # Asshole, you’re filth no gutter cleans and no earth bears.
    "Laude, teri soorat dekh kar to uljhan ho jaaye insaniyat ko.",  # Dickhead, seeing your face confuses humanity itself.
    "Saale chutiye, teri aukat ek jale hue mombatti ki tarah hai—bina roshni ke jalte rehna.",  # Idiot, your worth is like a burnt-out candle—burning without light.
    "Oye madarchod, tu wo laanat hai jo kisi pe bhi na aaye.",  # Motherfucker, you’re the curse no one should ever get.
    "Behen ke laude, tere jaise ko dekh kar zindagi bhi suicide kar le.",  # Sister’s dick, seeing you even life would commit suicide.
    "Bhosdike, tu to zameen pe gira hua wo cheez hai jise uthana bhi paap hai.",  # Asshole, you’re the thing fallen on the ground that picking up is sin.
    "Laude ke baal, tu wo chhata hua kachra hai jo hawa bhi na uda paye.",  # Pubic hair dick, you’re the spread trash the wind can’t even blow away.
    "Saale randi ke bacche, teri soch sun kar buddhi bhi pagal ho jaaye.",  # Son of a whore, hearing your thoughts even wisdom goes mad.
    "Madarchod, tu wo jale hue kabutar ki tarah hai jo na ud paye na mare.",  # Motherfucker, you're like a burnt pigeon that can neither fly nor die.
    "Behenchod, teri baat sun kar kaan todne ka mann kare.",  # Sisterfucker, hearing you makes me want to break my ears.
    "Bhosdike, tu to zindagi ka wo dard hai jo kabhi mit na sake.",  # Asshole, you’re the pain of life that can never be cured.
    "Laude, teri shakal dekh kar to sapne bhi toot jaayein.",  # Dickhead, seeing your face even dreams shatter.
    "Saale chutiye, tere hone se zyada bekaar to hawa ka jhatka hai.",  # Idiot, even a gust of air is more useful than your existence.
    "Oye madarchod, tu wo zehar hai jo peene se pehle hi mar de.",  # Motherfucker, you're the poison that kills before drinking.
    "Behen ke laude, tere jaise haramkhor ko to maut bhi ignore kare.",  # Sister’s dick, even death ignores a bastard like you.
    "Bhosdike, tu wo gand hai jo saaf karne se aur fail jaye.",  # Asshole, you’re the filth that spreads more when cleaned.
    "Laude ke baal, teri maa ki gaand se to makkhiyan bhi na guzrein.",  # Pubic hair dick, even flies wouldn’t pass your mother’s ass.
    "Saale randi ke bacche, tu to zindagi ka bekaar joke hai.",  # Son of a whore, you’re life’s useless joke.
    "Madarchod, tu wo lauda hai jo kutte ki chhatri mein atak gaya ho.",  # Motherfucker, you’re the dick stuck in a dog’s shelter.
    "Behenchod, teri maa ki chut ka map banakar randi khana khol dena chahiye.",  # Sisterfucker, your mother’s cunt should be mapped to open a brothel.
    "Bhosdike, tu wo kachra hai jise dekhkar kachra bhi sharmaye.",  # Asshole, you’re the trash that makes trash itself ashamed.
    "Laude, tu wo laanat hai jo andheron ko bhi dara de.",  # Dickhead, you’re the curse that scares even darkness.
    "Saale chutiye, tu wo beizzati hai jo gaand se chipak jaye.",  # Idiot, you’re the disgrace that sticks to the ass.
    "Oye madarchod, tu wo jale hue akhbaar ki tarah hai jisme kuch bhi padhne layak na bache.",  # Motherfucker, you’re like a burnt newspaper with nothing worth reading.
    "Behen ke laude, tu wo mooh hai jisme gaali dena bhi bekaar hai.",  # Sister’s dick, your mouth isn’t even worth cursing.
    "Bhosdike, tu wo chamdi hai jo faaltu latakti rahe.",  # Asshole, you’re that useless skin that just hangs.
    "Laude ke baal, tere hone se zyada zaroori to machhar marna hai.",  # Pubic hair dick, killing a mosquito is more important than your existence.
    "Saale randi ke bacche, teri maa ne tujhe paida kar ke duniya ko sabse bada bojh diya.",  # Son of a whore, your mother gave the world its biggest burden birthing you.
    "Madarchod, tu wo thook hai jo zameen pe girte hi badboo de.",  # Motherfucker, you’re that spit that stinks as soon as it hits the ground.
    "Behenchod, tu wo gaand ka daag hai jo kabhi dhule na.",  # Sisterfucker, you’re the ass stain that never washes out.
    "Bhosdike, tu wo nalayak hai jise zindagi ne galti se paida kiya.",  # Asshole, you’re the mistake life accidentally gave birth to.
    "Laude, tu wo badboo hai jo sabko ulti karne pe majboor kar de.",  # Dickhead, you’re that stench that forces everyone to vomit.
    "Saale chutiye, tu wo haarkhor hai jo haar kar bhi seekh na paye.",  # Idiot, you’re the loser who never learns from defeat.
    "Oye madarchod, tu wo kalank hai jo sirf sharmindagi de.",  # Motherfucker, you’re that stain that only gives shame.
    "Behen ke laude, tu wo bakwaas hai jo sunte hi dimag ka fuse uda de.",  # Sister’s dick, you’re the nonsense that blows the brain’s fuse.
    "Bhosdike, tu wo jehar hai jo chhune se pehle hi maar de.",  # Asshole, you’re that poison that kills before touching.
    "Laude ke baal, tu wo fart hai jiska awaz na ho sirf badboo ho.",  # Pubic hair dick, you’re that fart with no sound, only stink.
],


"Pack9": [
    "Madarchod, tere jaise laude ko zinda chodna insaniyat pe kalank hai.",  # Motherfucker, letting a dick like you live is a stain on humanity.
    "Bhosdike, teri maa ki chut ka mooh dekhkar chhodi hui zindagi bhi sharam se mar jaye.",  # Asshole, seeing your mother’s cunt even a discarded life would die of shame.
    "Behenchod, tu to wo gaand hai jisme se badboo bhi dur bhage.",  # Sisterfucker, you’re the asshole even stench runs from.
    "Saale randi ke bacche, teri maa ki chut se nikalte hi duniya ne thook diya hota.",  # Son of a whore, the world should’ve spat on you the moment you came out of your mother’s cunt.
    "Oye madarchod, tere jaise haram ke pille ke liye zameen pe jagah nahi honi chahiye.",  # Motherfucker, bastards like you don’t deserve a place on this earth.
    "Laude, teri soorat dekh kar maut bhi ulte kadam bhage.",  # Dickhead, even death runs away seeing your face.
    "Behen ke laude, tere jaise kutte ko dekh kar to kutte bhi apna dharm badal lein.",  # Sister’s dick, even dogs would change their faith seeing a dog like you.
    "Bhosdike, tere jaise kachre ki jagah to gutter mein bhi nahi.",  # Asshole, trash like you doesn’t even deserve space in the sewer.
    "Saale chutiye, tere jaise beghairat ko dekh kar beizzati bhi roti hai.",  # Idiot, seeing a shameless fuck like you even humiliation itself cries.
    "Madarchod, tu to wo laanat hai jo kisi maa ki god ko kabhi na mile.",  # Motherfucker, you’re the curse no mother’s lap should ever receive.
    "Laude ke baal, teri maa ne tujhe janam de kar sabse bada gunah kiya.",  # Pubic hair dick, your mother committed the greatest sin by birthing you.
    "Behenchod, tu wo harami hai jise gaali dena bhi gaaliyon ka apmaan hai.",  # Sisterfucker, you’re such a bastard that cursing you is an insult to curses.
    "Saale gandu, tere jaise kameene ko dekh kar andhkar bhi roshni maange.",  # Assfucker, seeing a scum like you even darkness asks for light.
    "Oye madarchod, teri aukat ek thook ki boond se kam hai.",  # Motherfucker, your worth is less than a drop of spit.
    "Bhosdike, tu wo gandagi hai jo paani bhi dho kar saaf na kar sake.",  # Asshole, you’re the filth even water can’t clean.
    "Saale nalayak, tu to wo chhata hua harami hai jise dekh kar gaand bhi band ho jaaye.",  # Useless bastard, you’re so filthy even an asshole would shut tight seeing you.
    "Behen ke laude, tere jaise ko dekh kar to maut bhi sochti hai ki thoda ruk jaaye.",  # Sister’s dick, seeing you even death pauses to reconsider.
    "Madarchod, tu wo kalank hai jo insaaniyat ne kabhi na socha ho.",  # Motherfucker, you’re the disgrace humanity never imagined.
    "Bhosdike, tere jaise haramkhor ko dekh kar kutti bhi apne bacche chhod de.",  # Asshole, seeing a bastard like you even a bitch would abandon her pups.
    "Laude, tu to zindagi ka wo black spot hai jise mita dena chahiye.",  # Dickhead, you’re the black spot of life that should be erased.
],

"Pack10": [
    "Abe madarchod, teri shakal dekhkar to zindagi bhar ka condom company bhi roya hoga.",  # Motherfucker, even a condom company must've wept seeing your face.
    "Bhosdike, tu to wo lauda hai jo ulti hone pe bhi pet mein reh gaya.",  # Asshole, you’re the dick that even stayed behind during vomiting.
    "Behenchod, tere jaise gawar se to gaand marwana bhi beizzati hai.",  # Sisterfucker, getting fucked by an idiot like you is an insult.
    "Saale randi ke bachhe, teri maa ko bhi sharam aati hogi tujhe janam de kar.",  # Son of a whore, even your mother must be ashamed she gave birth to you.
    "Teri aukat to itni hai ki kutte bhi teri taraf dekhke moo ghumaa lein.",  # Your worth is so low even dogs turn away from you.
    "Oye chutiye, tu to wo gaand hai jisme latrine bhi na jaaye.",  # You idiot, you’re the asshole that even shit refuses to enter.
    "Laude, teri soorat dekh kar to shaitan bhi religion badal le.",  # Dickhead, seeing your face even the devil would change religion.
    "Madarchod, tere jaise ke liye to gaali bhi bekar hai, tere liye to thook bhi zyada hai.",  # Motherfucker, even a curse is wasted on you, spit is too much for you.
    "Bhosdike, tu to wo bakchod hai jisko dekhkar bakchodi bhi sharmaye.",  # Asshole, you’re the kind of fool that even nonsense is ashamed of.
    "Behenchod, tu to itna nikamma hai ki zindagi bhi tujhse dur bhage.",  # Sisterfucker, you’re so useless that even life itself runs from you.
    "Saale gandu, teri maa ne tujhe paida kar ke hi pap kiya hai.",  # Assfucker, your mother sinned just by birthing you.
    "Tere jaise laude ko dekh kar condom ki importance samajh aati hai.",  # Seeing a dick like you makes people understand why condoms matter.
    "Chutiya kahin ka, teri bakwas se to khud gaaliyan bhi pagal ho jaati hain.",  # You fuckwit, even insults go mad hearing your nonsense.
    "Oye madarchod, teri soorat pe toh gobar bhi decorate lage.",  # Motherfucker, cow dung would look like decoration on your face.
    "Laude ke baal, tu to wo chutiya hai jise dekh kar andhe log bhi aankh dhoondhne lage.",  # Pubic hair dick, you’re such an idiot even blind people start looking for their eyes.
    "Behen ke laude, teri shakal dekh kar sapne bhi toot jaayein.",  # Sister’s dick, seeing your face would shatter dreams.
    "Madarchod, tu to wo kachra hai jo kachra gadi bhi refuse kare.",  # Motherfucker, you’re the garbage even the garbage truck rejects.
    "Bhosdike, tere jaise ko gaali dene se zyada accha hai moot diya jaye.",  # Asshole, better to piss on you than to waste a curse.
    "Saale chutiye, teri soch dekh kar keede bhi suicide kar lein.",  # Idiot, seeing your thoughts even maggots would commit suicide.
    "Tujhe dekh kar lagta hai ki shayad gaand marwana bhi izzat ki baat ho.",  # Looking at you makes it seem that even getting fucked is an honor.
]
# }
    # "InsultPack1": [
    #     "Abe madarchod, teri shakal dekh...",
    #     "Bhosdike, tu to wo lauda...",
    # ],
}

# ------------------
# Setup logging: DEBUG+ to file, WARNING+ to console

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # File handler: record everything
    fh = logging.FileHandler(LOG_PATH, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    logger.addHandler(fh)

    # Console handler: only warnings and above
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.WARNING)
    ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    logger.addHandler(ch)

# ------------------
# Load or initialize config
def load_config():
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Failed to parse config: {e}")
    return {PACKS_KEY: []}

# Save config
def save_config(cfg):
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, indent=2, ensure_ascii=False)
        logging.info("Configuration saved.")
    except Exception as e:
        logging.error(f"Failed to save config: {e}")

# Parse insult pack file
def parse_pack(path_str):
    path = Path(path_str).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Insult pack file not found: {path}")
    ext = path.suffix.lower()
    if ext == '.json':
        data = json.loads(path.read_text(encoding='utf-8'))
        if not isinstance(data, list) or not all(isinstance(i, str) for i in data):
            raise ValueError("JSON pack must be a list of strings.")
        return data
    elif ext == '.txt':
        return [l.strip() for l in path.read_text(encoding='utf-8').splitlines() if l.strip()]
    else:
        raise ValueError("Unsupported insult pack format; use .json or .txt")

# ------------------
# Global state management
def reset_state():
    return {
        'packs': {},           # name -> insults list
        'current_pack': None,  # name of selected pack or 'ALL'
    }
state = reset_state()
config = None

# Load all packs: in-code then from config
def load_packs():
    for name, insults in IN_CODE_PACKS.items():
        state['packs'][name] = insults.copy()
        logging.info(f"Loaded in-code pack '{name}' with {len(insults)} insults.")
    for pack_path in config.get(PACKS_KEY, []):
        try:
            insults = parse_pack(pack_path)
            name = Path(pack_path).stem
            state['packs'][name] = insults
            logging.info(f"Loaded insult  pack '{name}' with {len(insults)} insults.")
        except Exception as e:
            logging.error(f"Error loading insult  pack {pack_path}: {e}")
    state['current_pack'] = 'ALL' if state['packs'] else None

# Add pack to config
def add_pack_to_config(pack_path):
    if pack_path in config[PACKS_KEY]:
        logging.warning("Insult pack already loaded in config.")
        return False
    config[PACKS_KEY].append(pack_path)
    save_config(config)
    return True

# Get insults for current selection
def get_insults():
    if state['current_pack'] == 'ALL':
        all_insults = []
        for insults in state['packs'].values(): all_insults.extend(insults)
        return all_insults
    return state['packs'].get(state['current_pack'], [])

# ------------------
# Banner logic
BANNER_FRAMES = [
    r"""
░▒█▀▄▀█░█▀▀▄░▒█░▄▀░▒█▀▀▀░░░▀▀█▀▀░▒█░▒█░▒█▀▀▀░▒█▀▄▀█░░░▒█▀▀▄░▒█▀▀▄░▒█░░▒█
░▒█▒█▒█▒█▄▄█░▒█▀▄░░▒█▀▀▀░░░░▒█░░░▒█▀▀█░▒█▀▀▀░▒█▒█▒█░░░▒█░░░░▒█▄▄▀░▒▀▄▄▄▀
░▒█░░▒█▒█░▒█░▒█░▒█░▒█▄▄▄░░░░▒█░░░▒█░▒█░▒█▄▄▄░▒█░░▒█░░░▒█▄▄▀░▒█░▒█░░░▒█░░
""",
    r"""
 ___        _        _          _____  _          _             _____                     
|   \  _ _ (_) _ _  | |__      |_   _|| |_   ___ (_) _ _       |_   _| ___  __ _  _ _  ___
| |) || '_|| || ' \ | / /        | |  |   \ / -_)| || '_|        | |  / -_)/ _` || '_|(_-/
|___/ |_|  |_||_||_||_\_\        |_|  |_||_|\___||_||_|          |_|  \___|\__/_||_|  /__/
""",
    r"""
 _____ _                  _____                                    ____      _ _     
|  _  | |_ _ _ ___ ___   |   __|___  __ _____ _____ ___ ___ ___   |    \  __|_| |_ _ 
|     | . | | |_ -| -_|  |__   |  _||. |     |     | -_|  _|_ -|  |  |  ||. | | | | |
|__|__|___|___|___|___|  |_____|___|___|_|_|_|_|_|_|___|_| |___|  |____/|___|_|_|_  |
                                                                                |___|
"""
]

def print_banner():
    frame = random.choice(BANNER_FRAMES)
    print(colored(frame, 'cyan'))

def show_help():
    print(colored("""
Available commands:
  1. Next Insult    — show next insult in sequence
  2. Random Insult  — show a random insult
  3. Load Pack      — add a pack via path (.json or .txt)
  4. List Packs     — list loaded packs and counts
  5. Choose Pack    — select a pack or ALL (combines all)
  6. Help           — display this help
  7. Exit           — quit the program
""", 'yellow'))

# TTS play function
def play_insult(insult_text: str):
    mp3_path = Path.home() / "insult.mp3"
    try:
        tts = gTTS(insult_text, lang='hi')
        tts.save(str(mp3_path))
        subprocess.run(["termux-media-player", "play", str(mp3_path)], check=True)
    except Exception:
        subprocess.run(["mpg123", str(mp3_path)], check=False)

# ------------------
# Main loop
def main():
    setup_logging()
    global config
    config = load_config()
    load_packs()

    print_banner()
    show_help()

    sequence, seq_index = [], 0

    while True:
        choice = input(colored("Enter choice (1-7): ", 'yellow')).strip()
        if choice == '1':
            insults = get_insults()
            if not insults:
                print(colored("No insults loaded.", 'red'))
                continue
            if not sequence:
                sequence = insults.copy()
                random.shuffle(sequence)
            insult = sequence[seq_index % len(sequence)]
            seq_index += 1
            print(colored(insult, 'red'))
            play_insult(insult)
        elif choice == '2':
            insults = get_insults()
            if not insults:
                print(colored("No insults loaded.", 'red'))
                continue
            insult = random.choice(insults)
            print(colored(insult, 'red'))
            play_insult(insult)
        elif choice == '3':
            path = input(colored("Enter path to pack (.json or .txt): ", 'cyan')).strip()
            try:
                insults = parse_pack(path)
                name = Path(path).stem
                state['packs'][name] = insults
                if add_pack_to_config(path):
                    print(colored(f"Pack '{name}' loaded successfully.", 'green'))
                else:
                    print(colored(f"Pack '{name}' already in config.", 'yellow'))
            except Exception as e:
                print(colored(f"Failed to load pack: {e}", 'red'))
        elif choice == '4':
            if not state['packs']:
                print(colored("No packs loaded.", 'yellow'))
            else:
                for name, insults in state['packs'].items():
                    print(colored(f"{name}: {len(insults)} insults", 'green'))
        elif choice == '5':
            options = ['ALL'] + list(state['packs'].keys())
            for idx, name in enumerate(options, 1): print(colored(f"{idx}. {name}", 'cyan'))
            sel = input(colored("Select pack number: ", 'yellow')).strip()
            try:
                idx = int(sel) - 1
                state['current_pack'] = options[idx]
                print(colored(f"Current pack set to '{state['current_pack']}'", 'green'))
                sequence.clear(); seq_index = 0
            except:
                print(colored("Invalid selection.", 'red'))
        elif choice == '6':
            show_help()
        elif choice == '7':
            print(colored("Thank You For Abusing Scammers!", 'green'))
            break
        else:
            print(colored("Invalid choice. Enter 1-7.", 'red'))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\nThank You For Abusing Scammers!", 'yellow'))
        sys.exit(0)
