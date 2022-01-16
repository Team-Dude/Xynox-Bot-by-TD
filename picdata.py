import discord
from discord.ext import commands
import asyncio
import random


#Pics
#Killjoy
killjoy_pics=['https://i.imgur.com/TmIcF2S.png','https://i.imgur.com/MjLzO55.png','https://i.imgur.com/e4VKop4.png','https://64.media.tumblr.com/686a744791d268b908329f762ec777b4/b322b762d931c394-7c/s540x810/fb3158a36d30bad6e53953ae0a50046b1851638d.gif']

#Raze
raze_pics=['https://64.media.tumblr.com/3298a3ee21fcbfa37042b4f219579d22/a59016cb1d0700eb-f8/s1280x1920/a050497dd41ffed84e8aba88eba8cddadc541712.jpg','https://i.ytimg.com/vi/uRHPHv3i8-U/maxresdefault.jpg','https://images.wallpapersden.com/image/download/raze-new-valorant_bGxqa2yUmZqaraWkpJRobWllrWdma2U.jpg','https://64.media.tumblr.com/a8b2b8c02c05908c8f712d6a15b389fb/3a72a40c3b347f59-f1/s540x810/bde3497fbb0b1df5cb69b9e3488176d4294a3057.gif']

#Jett
jett_pics=['https://images.hdqwalls.com/download/valorant-jett-4k-rz-800x1280.jpg','https://cdn.statically.io/img/i.pinimg.com/originals/8f/58/6f/8f586f7bcb4502d70cb7b774bad69208.jpg','https://i.pinimg.com/474x/23/57/e4/2357e49158238645e21e1e85f11affa9.jpg','https://64.media.tumblr.com/4fbbef14b3415b549d34069e5be2459a/ca8ac3db5472a7d0-72/s500x750/a77e69c00a997fc89a96d011dfb693a19f2eeb4a.png','https://i.pinimg.com/originals/2f/b8/52/2fb8526ff792864fd5793a2b79c527bb.gif','https://steamuserimages-a.akamaihd.net/ugc/1796352269513567345/BBAA96EF1A6B95B1CB1FA8D6618E0311B3C0022F/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false']

#Viper
viper_pics=['https://images.wallpapersden.com/image/wl-valorant-viper-cinematic_75823.jpg','https://images.alphacoders.com/114/1149327.jpg','https://www.enjpg.com/img/2020/valorant-2.png','https://i.imgur.com/Wc5IsWs.png','https://64.media.tumblr.com/4fdfecb21875a6f99240e254adfee3ef/9c205c61cd9bbec8-33/s400x600/9b2ba12bc84c02963a7609384310e29f0c5eea5c.gif']

#Sage
sage_pics=['https://i.imgur.com/vNFhmBy.png','https://pbs.twimg.com/media/EWDu1OfWoAIZ-Ue.jpg','https://cdnb.artstation.com/p/assets/images/images/026/329/527/large/tristan-yajuu-bour-sage0.jpg?1588497968','https://i.pinimg.com/originals/52/53/50/5253503c2678ef2a253b71aa794b0e5d.jpg']

#Astra
astra_pics=['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqoJnfSRDMYflfNchBom4TfJ9mLgo8ilb5bg67vwuC7PpR4ZeK3tlvKfciovMEhf8Rf6c&usqp=CAU','https://images4.alphacoders.com/114/1149781.jpg','https://64.media.tumblr.com/a837413a2247f3d7f97550de8f770731/c66c33c9bc1a145d-25/s500x750/b6d66583bc7572358526023337dac32902471dc8.gif']

#Chamber
chamber_pics=['https://static0.srcdn.com/wordpress/wp-content/uploads/2021/10/Valorants-new-Agent-is-a-weapon-designer-named-Chamber.png','https://www.gamespot.com/a/uploads/scale_landscape/1352/13527689/3901057-l%E2%80%99accord-chamberagenttrailer__valorant.mp4.00_00_35_05.still002.jpg','https://64.media.tumblr.com/ff38f319161209ca0f64b3657d2e41b4/60c664c6a388823d-a9/s540x810/172aee61fcb34820e793c95c024434277cde8047.gif','https://64.media.tumblr.com/c5c0ef10941329246b8f8dd1567aa998/f9bc3832473eb90a-af/s540x810/aae6dcbedb02102c9003ee6572771f6309a469ff.gif']

#Asuka
asuka_pics=['https://media.discordapp.net/attachments/472313197836107780/700174572217040947/NwMawJG.png','https://static.wikia.nocookie.net/tekken/images/b/b2/T7FR_Asuka.jpg/revision/latest?cb=20201009044443&path-prefix=en','https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/41939d92-a9f4-42af-9dd7-e4d6457937ef/d6yhb8e-1af51594-eadc-4b18-8054-915a3949be26.png','https://c.tenor.com/7r176K1mkzgAAAAC/tekken-asuka.gif','https://static.zerochan.net/Kazama.Asuka.full.2409816.gif','https://i.imgur.com/8L5t9FY.gif']

#John Cena
jc_pics=['https://static01.nyt.com/images/2021/05/25/multimedia/25xp-johncena/25xp-johncena-mobileMasterAt3x.jpg','https://i.imgur.com/5fU4u0C.png']

#Dua Lipa
dl_pics=['https://media.gq.com/photos/5a5f79d835be9e1aebeceecf/16:9/w_2560%2Cc_limit/Dua_Lipa_01.jpg','https://i.imgur.com/rYhCPAM.png','https://www.biography.com/.image/t_share/MTg1NjUxMjM2MTY5NTkwMTY0/gettyimages-1356296274.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZt9UNvA2RoBB-j5DclLMJpw_T7taV_IQ9BSaoqgIyvy-iuhy3FtMzonRLT9tkmJrlg_A&usqp=CAU']

#James Charles
jc_pics=['https://i.imgur.com/Dq7yOkd.png','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxRX8DmPgnsPAc-dLAPMgFgtanbzYKHE7wp0dPdHTB1nCVmypLhxFpWOHnvN3jf6Jr6Yg&usqp=CAU']



#Random
random_killjoy_pic=random.choice(killjoy_pics)
random_raze_pic=random.choice(raze_pics)
random_jett_pic=random.choice(jett_pics)
random_viper_pic=random.choice(viper_pics)
random_astra_pic=random.choice(astra_pics)
random_chamber_pic=random.choice(chamber_pics)
random_jc_pic=random.choice(jc_pics)
random_dl_pic=random.choice(dl_pics)
random_asuka_pic = random.choice(asuka_pics)