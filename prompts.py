import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair


vertexai.init(project="strange-reducer-392221", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.8,
    "max_output_tokens": 1024,
    "top_p": 0.8,
    "top_k": 40
}

def pros():
    chat = chat_model.start_chat(
    context="""You are summarizing all the pros of Amazon reviews of products. You are given multiple reviews of one product, and must output an overall summary of all pros in the reviews.""",
    examples=[
        InputOutputTextPair(
            input_text="""This is going to be a review that highlights a few stand-out points (good and bad). There are plenty of more detailed tech reviews out there so be my guest. I purchased this for a family member but i used it for a while before passing it on. What I LOVED 1) price tag / value position. When you find this phone at around sub 400$ mark, you really do appreciate this phone. 2) really decent screen / size. It\'s massive but it still holds OK one handed because its not that heavy. the screen is bright and ultra bright enough for outdoor use. despite what other reviews say, i think this screen is sufficient 3) its a mid-teir chipset but actually , for one who doesnt play games much, this is not sluggish at all. 8g ram helps. love the massive flash capacity of 128gb too --- it kind of makes up for samsung\'s bloatware. Most of it is not used ---> install all google apps and disable the rest. 4) camera performance is not as good as a pixel2/3 in low light. but it is still quite good. The extra wide lens is handy for some situations which pixel phones cannot offer. i\'m really impressed with how quick the shooting lag is. it focuses and takes the shot instantly , similar performance as pixel2/3 performance imo. i\'m often annoyed by mid-teir phones that have a slightly longer lag between pressing the shoot button and actual picture capture (moto, sony...) but this mid teir spec phone has none of that. the camera app is much more richly featured than a simple pixel camera but in my honest opinion, these are all gimmicks. it takes good shots and it takes it quickly. thats really all i can ask for for mid tear phone. 5) micro SD card slot and DUALSIM capable. This is a nice bonus for me. this device already has a generous amount of flash but having that extra SD card slot helps alleviate the storage needs (i route all camera pics to the card whilst keeping internal flash for apps). DUALSIM is actually useful for me because the user of the phone travels to asia annually and its a nice feature to slot in a local sim during travels. What I wish were better 1) finger print sensor --- many reviews reported it doesnt work well under the screen. I found this very weird. It seems to work PERFECT with my thumb but with another person\'s thumb, it doesnt work AT ALL (???) I had to resort to face recognition for now until i figure this one out 2) samsung bloat -- theres a tonne of bloat on samsung phones. i ended up disabling a lot of it especially the launcher. i dont love it at all. you cant really remove the software since it\'s baked into the firmware but the 128gb flash makes up for that. a typical pixel phone comes with 64 gb.... if samsung phones came with just 64GB, you\'d have little left for your own apps/data :) but thank goodness there is 128. 3) heat. this phone heats up quick and its warmer than other devices i\'ve used. I\'m not sure why but it is noticeable. so what other options are there? well there is samsung A50 too (at the time of writing, the A51 and A71 are the most current A-series phones but theyre just priced too high). If i\'m going to be totally honest here, i think if you can find a pixel2XL with 128gb flash, at under 400$, then you are better off with that especially because of the camera performance. I\'m going to recommend this device if you really need the extra wide lens, the SD card, and nicer larger screen real estate. Impressive for the price, looks beautiful feels great for big hands, overall happy so far. Camera quality is superior for a mid range phone, feels fast and easy navigation, good settings able to use face recognition and open screen without swiping is definitely useful to have as well as the finger print scan works. Made calls quite a few times now and haven\'t had any issues. Speaker is somewhat loud for 1 bottom speaker sounds clear, the dobly atmos Audio for headphones/aux really improves sound quality really nice. Screen mirroring works flawless on my smart tv, compared to my last phone which was choppy until now. As far 4500mah battery seems good I do have location apps running background and Bluetooth throughout the day with a smart watch and headphones connected most of the time, it lasts about full day. Overall phone is great and once you go through all the settings to customize, like navigation bar etc it really has alot nice options and feels alot smoother after. I recommend keeping it on night mode as well! Great phone for the price. Pros: - Price - Nearly as fast as flagship competition - Clear, vivid display - Superb battery life - intuitive placement of power/wake button Cons: - Biometric reader is extremely poor quality - I\'ve even registered my thumb print several times as an \"additional fingerprint\" to increase chance of recognition, but it still only works roughly 15-20% of the time. - Face recognition is noticeably slower than what I would consider to be convenient and has frequent \"no match\" result. Not even on the same planet as recognition speed of iphone 11, but again, this isn\'t a flagship phone and cost 1/4 of the price. - Camera quality is not good at all. I\'d compare it to that of a galaxy s6. Photos are usually quite blurry; when zooming on a photo you can really see the poor quality of the captured image I was always an Iphone guy until the prices got absolutely ridiculous and at the end of the day, It\'s a phone. I wanted to get something with a decent camera and microphone without breaking the bank. I was blown away with everything that android lets me do but that has nothing to do with the phone. The camera is alright, It is difficult to take non blurry photos when object is moving. video is pretty decent, if you\'re just using the native camera app. Snapchat gets laggy and so does any other app. Other than that it\'s a pretty reliable phone for a good price. I\'ve had the phone for less than two weeks but so far very happy with it. Setup was easy, the camera is good, the screen is sharp and bright. Battery lasts all day with still lots of juice left (this is a real treat as the old phone was three years old and the battery had to be recharged before the end of the day). Haven\'t tried the face recognition but the finger print scanner was a bit difficult to set up and is a bit fussy (compared to my BB Key One). The quality and features for the price is excellent and I have no difficulty in recommend this phone. I didn\'t see many other reviews from Canadian users so I decided to make one. I\'m from Ontario and this phone works fine from the cellular bands here. Although the Samsung A70 does not pick up 4th generation networks as well as their flagship phones it has worked great for what I use the phone for. I love the big screen and huge battery life. This phone is great for media and I was amazed at how powerful the camera is between the S8 plus. It\'s crazy how fast technology improves in only two years. I would recommend this phone over any of Samsung\'s flagship phones as long as you live in near a semi-urban town/city. If you live out in a rural community I would suggest getting a phone with more connection bands to make sure you always get a good connection. Very disappointed with this phone... I didn\'t mind the cheap feel of the build, but now that I\'ve it for a couple of months, the quality of the phone overall has gotten worse, despite it being a well taken care of phone. I previously had an A5 and the cellular reception of that is much better than this one...after 2 or 3 months in, I started having difficulty making calls/receiving or hearing...what kind of a phone can\'t do such a basic function ???? Now that I\'ve had the phone for about half a year, it suddenly stops connecting to (any kind of) wifi. It\'s practically useless! And I spent so much money on this crap! Literally the only thing I can compliment on is the battery life...you can watch videos/play battery life draining gamea for quite some time before needing to recharge. I usually have 10 hour work days and will come home with around 50% battery. I upgraded to this A70 from a Samsung S4 and this phone has so much more battery and is significantly faster. It took some time to get used to the in-screen ultrasonic fingerprint reader but it becomes easy after you get the hang of it. The face recognition works best in a well lit setting but it sometimes works in pitch black as the screen lights up to illuminate my face.
This phone takes sharp pictures comparable to the S10+ and similarly, the wide angle can slightly distort the image.
""",
            output_text="""
Affordable price tag and good value for the features provided.
Decent screen size with a bright and vibrant display.
Smooth performance with a mid-tier chipset and 8GB RAM.
Generous 128GB flash capacity.
Versatile camera with an extra wide lens and quick shooting lag.

"""
        ),
        InputOutputTextPair(
            input_text="""You only would have to get an extra cusion for your lower back as this is not having any adjustable lumbar support. And that is the only rreaon for me to rate it at 4*. Good chair at a good price. Came very very fast. The chair is in fact very comfortable and relaxing. I like it, it looks like a expensive chair and the seat is comfortable Worth for the money 140$ 👍👍🍺Better then going to store and the prices are 180 or 250 🙄🙄Totally recommend it 👍👍👍 this chair doesn\'t tilt back...too small for anyone6ft. tall or better...not comfortable… Comfortable Chair, great for the price. However, I had some QA issues that were a bit upsetting. On my first chair, one of the cushion threaded inserts for the armrest had issues with the threading. Unfortunately not a cross-threading issue. Even without the armrest present, the insert would only allow about 1/8 to 1/4\" of any bolt to thread. I did a return and received a second chair, only to have the same issue on a different threaded insert. Rather than accept defeat, I drove over to Harbor Freight and bought a metric Tap & Dye set with the correct M6 x1.0 Tap. I ran the tap through the insert, it felt as if I was making threads in some places, but the insert did accept the bolt afterward. Problem solved; I love the chair but hated the experience of dealing with this issue. So have a metric tap & dye set and some years of maintenance experience to avoid this. The assembly process was mostly easy except for the handles. The holes did not align properly so putting in the screws were a huge challenge, especially if you\'re assembling by yourself like I did. The end product is pretty sturdy and good quality for it\'s low price. This chair is narrower than my old one so it\'s a bit small for bigger people. Bummed this doesn\'t have a backrest adjustment mechanic, but you get what you paid for so can\'t complain much. The chair itself is great—once we figured out how to put it together. No instructions were included other than where to find the parts. Two cardboard end pieces telling you where to find the parts. Another cardboard piece inside telling you where to find the parts. And then…a red plastic flag taped to another piece of cardboard….can you guess?? Yep, telling you where to find the parts. So, thank you for being so specific on where to find the parts. 🤣 Might be a great idea to also include how to put together said parts once you find them. All that aside, I do like this chair. Chair was easy to assemble and looks great, no damaged or missing parts. Nice upgrade from the 20-year old cheap seat I was using. It feels comfortable and sturdy, I\'m 6\'4\'\' and 230-lbs. and it supports me just fine, no problem with it sinking and is easy to adjust the height and lean back feature. I\'m confused by Amazon\'s choice however to stuff all the parts into the back of the chair rather than fill it with padding like the seat cushion. I could care less how small a box it arrives in and would much rather have had a larger box delivered so the back rest was padded as well. Strange decision on Amazon\'s part. There is a tiny bit of foam padding around the edges but the back is hollow, no lumbar support at all. The zipper compartment allows you to add your own padding, which I found a 18-inch square, 2-inch thick memory foam at Walmart\'s craft dept. that fit\'s perfectly, but there\'s still a lot of empty space in the lower back area so I got a small travel pillow and crammed behind the foam and that fills it nicely and is much more comfortable to sit and lean back in. Just be careful... once I assemble the chair the arms were so tight against the zipper that I couldn\'t open it. I had to loosen the screws to be able to unzip the back section and stuff the padding inside then retighten the screws. But now I\'m happy with it and still feels like a good buy for a premium look and feel office chair, makes working from home much more pleasant and it rolls good on my carpet. My suggestion to Amazon: the seat cushion is nicely padded and comfortable, do the same with the back cushion and ship it in a larger box. Then it would be highly recommended. So, the chair is wonderful with a little upgrade. When you get the chair you have to remove all parts for the chair from the chair back. This unfortunately makes the chair back empty. To resolve this issue, use pillow fill to stuff the chair back. Stuff until it is full, but not too full, then rezip. Excellent upgrade. Inconfort ---


""",
            output_text="""
Affordable price: The chair offers good value for its price, making it an attractive option for budget-conscious buyers.
Comfortable and relaxing: Many users found the chair to be comfortable and relaxing, providing a pleasant seating experience.
Premium look and feel: The chair has an appearance that resembles an expensive chair, giving it a high-end aesthetic.
Easy assembly: Most users found the assembly process to be straightforward and easy, allowing for quick setup of the chair.
Sturdy and good quality: The chair is described as sturdy and of good quality, providing durability and longevity for long-term use.




"""
        ),
        InputOutputTextPair(
            input_text="""NA Dislike bought them a month ago right earpiece working left doesn’t work doesn’t play music it’s very annoying have an earpiece that doesn’t work ! Especially for the price I paid for it It is ok to use Although the price was too high for the quality of the earpod, it did the job It connected twice to my iPhone and once to my laptop. Did not auto connect to device.
already in process of being returned They are okay to listen to music but a lot of noise when trying to talk. Not really happy You\'re not going to like them if you\'re used to Apple ear phone.
""",
            output_text="""
-functional for playing music, 
- it connects to devices like iPhones and laptops, and it is deemed okay to use. 
- Users found it suitable for listening to music.
"""
        ),
        InputOutputTextPair(
            input_text="""The original packaging was ripped and damaged with a big hole. Half the key board didn\'t work, the DC/USB charger didn\'t even fit properly, it was to long didn\'t full fit inside the plug! My son cried Christmas morning when it\'s ended up being broken!!!! Plus the Quality of the material is a cheap plastic and when you press on the keyboard the whole key pad moves and the sound is distorted! Reminded me of something i would have boughten at the Dollaramma Store! this product is for a 5 year old keys are way too small found the same product in Walmart for 11.99$ the sound it makes is so annoying doesn\'t even sound like a piano sounds like a trumpet Very small and not Worth the money in my opinion The product arrived in poor condition with ripped and damaged packaging, including a large hole. To make matters worse, half of the keyboard didn\'t work properly, rendering it useless. Even the DC/USB charger provided didn\'t fit properly, as it was too long and didn\'t fully fit inside the plug. The disappointment was immense, as my son ended up crying on Christmas morning when he discovered the broken toy. Additionally, the overall quality of the material used in the construction felt cheap and plasticky. When pressing on the keyboard, the entire keypad would move, resulting in distorted sound. It reminded me of something I would have bought from a dollar store rather than a proper toy retailer! This product is clearly designed for a 5-year-old, as the keys are way too small for comfortable use. Surprisingly, I found the exact same product at Walmart for only $11.99, which made me question the value of the item. Furthermore, the sound it produces is incredibly annoying and far from resembling a piano. Instead, it sounds more like a trumpet, which is not what I expected or desired from a piano toy. The size of this product is disappointingly small, and in my opinion, it does not justify the cost. It feels like a poor investment for the money spent. My dad bought this keyboard for my piano classes. It sounds very great and it is lightweight. It comes with a microphone it screeches a lot when you use the microphone and it even works if the wire is a bit broken. I used this key board for my basic learning classes and my dad bought me Yamaha psre463 this the piano my piano teacher recommends for me next.


""",
            output_text="""
- Lightweight: The keyboard is lightweight, making it easy to carry and handle.
- Comes with a microphone: The inclusion of a microphone allows for vocal accompaniment while playing the keyboard.
- Works with a broken wire: Despite a broken wire, the keyboard still functions, allowing for continued use.


"""
        )
    ]
)



def cons():


def price(prompt):


response = chat.send_message(prompt, **parameters)
print(f"Response from Model: {response.text}") # convert to return when u copy paste