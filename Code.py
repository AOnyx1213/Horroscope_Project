

def Horoscope():
    
            if zodiac == 'Aries':
                print("""
                Today, you may be more attracted towards outstanding, 
                expensive and beautiful things and think about splurging a bit. 
                If you have big plans on your mind, you may try to execute them. 
                Some may try to break monotonous routines and plan a get-together or a 
                party at home.  Desired outcomes can be fetched with proper planning on 
                the business front. You may not feel exhausted 
                and keep your mind active and sharp.
                 """)
            elif zodiac == 'Taurus':
                print("""
                Day seems wonderful for people born under the sign of Taurus. 
                Financial conditions seem good for some and new opportunities 
                to earn more may knock your door and prove profitable in the 
                long run. Some may make changes in their houses structurally. 
                You should try to be flexible and creative in order to complete 
                tasks on time and boost your productivity. Those who have been 
                hitting the gym may get their performance and flexibility 
                improved.
                """)
            elif zodiac == 'Gemini':
                print("""
                Today, you may get a chance to surprise people with your 
                creative ideas, amazing problem-solving abilities 
                and outstanding skills on the professional front. 
                You may be unsure about some investments on the financial 
                front. Someone in the family may check your patience, 
                so try not to give a cold reaction. You may make some 
                tough decisions at work, but you need not to worry 
                about anything. No health issues are indicated. 
                """)
            elif zodiac == 'Cancer':
                print("""
                This day may bring lots of opportunities, so try to keep a 
                bright outlook. Good news about financial gains or profit 
                in business is predicted.  You can deal with anything
                 destiny throws at you with a little compassion. Organizing 
                 and planning tasks should be your first priority today. 
                 Those who have been taking care of their daily food habits, 
                 they may enjoy good health and achieve fitness goals soon.
                 """)
            elif zodiac == 'Leo':
                print("""
                This may be a favorable day for you. Some may have a scope of boosting 
                their income.  Your presence in a social-gathering may be appreciated 
                by your parents. Your hard work may get you appreciation or recognition, 
                so get ready to hear praise from colleagues or superiors. A sense of
                 general well-being and joy may make your day wonderful. Some may be 
                 able to attract others with their pleasing personality.
                 """
                )
            elif zodiac == 'Virgo':
                print("""
                This day can bring mixed results for you. Your business associates, 
                bosses, co-workers or friends can prove beneficial to you by getting 
                you benefits in a big way. You may enjoy the togetherness and company 
                of loved ones. Those who are planning to start a new business or switch 
                jobs, they should wait a bit longer. Your energy may allow you to 
                complete all the pending work at home or office.
                """)
            elif zodiac == 'Libra':
                print("""
                It's a favorable day to reveal your romantic side and enjoy the company of someone 
                special. Your hard work and consistent efforts may get you gains or 
                financial opportunities. Family members may be in a party mood today, 
                so try to be a part of a wonderful event and create amazing memories. 
                Someone may test your intellectual power on the professional front. 
                Your energy and positive attitude may let you enjoy a party with 
                friends or loved ones. 
                """)
            elif zodiac == 'Scorpio':
                print("""
                 You just need to maintain a positive outlook about the things 
                 happening around. Day seems favorable for negotiations and you 
                 may know exactly how much you should invest in property or other 
                 investmen schemes. You may find it hard to enjoy a day with family members 
                 due to some reasons. This is a suitable day for everything you do on the 
                 business front.  You are advised not to waste your energy or time on 
                 unnecessary tasks.
                 """)
            elif zodiac == 'Saggittarius':
                print("""
                This is a favorable day and you should make the most of it.  Those who are waiting for 
                good news on the financial fronts, they can get it. You may be able to 
                enjoy a peaceful and joyful time with family members. Some may have to 
                devote extra hours and work hard to complete a project on time. Some 
                home remedies can prove effective in dealing with minor health issues.
                """ )
            elif zodiac == 'Capricorn':
                print("""
                This day may bring mixed results. You may expect good deals or 
                gains on the property front. You need to be calculative when 
                it comes to financial matters. Some positive factors on the home 
                front may keep you filled with positivity and energy. Stars are not 
                favoring you today, so you may feel a bit stressed on the 
                professional front. Some may find themselves in low spirits, 
                so it's a good idea to practice breathing exercises and meditation.
                """)  
            elif zodiac == 'Aquarius':
                print("""
                This may be a hectic day for you as you may have to deal 
                with a number of matters and all of them may be very 
                important. Some may get commission or good profit for providing their 
                services to some institutes or clients. You may try some amazing ways 
                to surprise your parents. Day seems to be very productive on the 
                professional front. Some may schedule body massage or 
                read motivational books.
                """)
            elif zodiac == 'Pisces':
                print("""
                This may be a hectic day for you as you may 
                have to deal with a number of matters and all of them may be very 
                important. Some may get commission or good profit for providing their 
                services to some institutes or clients. You may try some amazing ways 
                to surprise your parents. Day seems to be very productive on the 
                professional front. Some may schedule body massage or read motivational 
                books.
                """)
  
   
name = input("Enter your name:")
print("Hi" + name + "!")
zodiac = input("Enter Zodiac:")
Horoscope()
