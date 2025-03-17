import random
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors

# A small set of Stoic quotes
stoic_quotes = [
"You have power over your mind - not outside events. Realize this, and you will find strength. — Marcus Aurelius",
"He who fears death will never do anything worth of a man who is alive. — Seneca",
"We suffer more often in imagination than in reality. — Seneca",
"It is not what happens to you, but how you react to it that matters. — Epictetus",
"No man is free who is not master of himself. — Epictetus",
"If it is not right, do not do it; if it is not true, do not say it. — Marcus Aurelius",
"The best revenge is not to be like your enemy. — Marcus Aurelius",
"Begin at once to live, and count each separate day as a separate life. — Seneca",
"Don’t explain your philosophy. Embody it. — Epictetus",
"Waste no more time arguing what a good man should be. Be one. — Marcus Aurelius",
"The only way to do great work is to love what you do. — Steve Jobs",
"What lies behind us and what lies before us are tiny matters compared to what lies within us. — Ralph Waldo Emerson",
"Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
"Do what you can, with what you have, where you are. — Theodore Roosevelt",
"Whether you think you can or you think you can’t, you’re right. — Henry Ford",
"Hardships often prepare ordinary people for an extraordinary destiny. — C.S. Lewis",
"In the middle of every difficulty lies opportunity. — Albert Einstein",
"Courage is not having the strength to go on; it is going on when you don’t have the strength. — Theodore Roosevelt",
"The only limit to our realization of tomorrow will be our doubts of today. — Franklin D. Roosevelt",
"Fall seven times and stand up eight. — Japanese Proverb",
"Believe you can and you're halfway there. — Theodore Roosevelt",
"Everything you’ve ever wanted is on the other side of fear. — George Addair",
"The future belongs to those who believe in the beauty of their dreams. — Eleanor Roosevelt",
"It always seems impossible until it’s done. — Nelson Mandela",
"Happiness is not something ready made. It comes from your own actions. — Dalai Lama",
"Do not go where the path may lead, go instead where there is no path and leave a trail. — Ralph Waldo Emerson",
"Life isn’t about finding yourself. It’s about creating yourself. — George Bernard Shaw",
"The way to get started is to quit talking and begin doing. — Walt Disney",
"Our greatest glory is not in never falling, but in rising every time we fall. — Confucius",
"Health is the greatest possession. Contentment is the greatest treasure. Confidence is the greatest friend. — Lao Tzu",
"The only thing standing between you and your goal is the story you keep telling yourself as to why you can’t achieve it. — Jordan Belfort",
"Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau",
"Act as if what you do makes a difference. It does. — William James",
"Happiness depends upon ourselves. — Aristotle",
"Don’t wait. The time will never be just right. — Napoleon Hill",
"What you get by achieving your goals is not as important as what you become by achieving your goals. — Zig Ziglar",
"When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. — Henry Ford",
"Do not pray for an easy life, pray for the strength to endure a difficult one. — Bruce Lee",
"You may have to fight a battle more than once to win it. — Margaret Thatcher",
"Perseverance is not a long race; it is many short races one after the other. — Walter Elliot",
"Gratitude turns what we have into enough. — Anonymous",
"Joy does not simply happen to us. We have to choose joy and keep choosing it every day. — Henri Nouwen",
"Happiness is not something you postpone for the future; it is something you design for the present. — Jim Rohn",
"Let us be grateful to people who make us happy; they are the charming gardeners who make our souls blossom. — Marcel Proust",
"Count your age by friends, not years. Count your life by smiles, not tears. — John Lennon",
"Difficulty shows what men are. — Epictetus",
"How long are you going to wait before you demand the best for yourself? — Epictetus",
"A gem cannot be polished without friction, nor a man perfected without trials. — Seneca",
"True happiness is to enjoy the present, without anxious dependence upon the future. — Seneca",
"What we do now echoes in eternity. — Marcus Aurelius",
"Do one thing every day that scares you. — Eleanor Roosevelt",
"Opportunities don't happen. You create them. — Chris Grosser",
"The secret of success is to do the common thing uncommonly well. — John D. Rockefeller Jr.",
"I find that the harder I work, the more luck I seem to have. — Thomas Jefferson",
"Success is not in what you have, but who you are. — Bo Bennett",
"Be yourself; everyone else is already taken. — Oscar Wilde",
"To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. — Ralph Waldo Emerson",
"Life is not measured by the number of breaths we take, but by the moments that take our breath away. — Maya Angelou",
"The best way to predict your future is to create it. — Peter Drucker",
"The biggest risk is not taking any risk. — Mark Zuckerberg",
"Success is walking from failure to failure with no loss of enthusiasm. — Winston Churchill",
"The only place where success comes before work is in the dictionary. — Vidal Sassoon",
"If you really look closely, most overnight successes took a long time. — Steve Jobs",
"Don’t be afraid to give up the good to go for the great. — John D. Rockefeller",
"I never dreamed about success, I worked for it. — Estée Lauder",
"The harder the conflict, the greater the triumph. — George Washington",
"It is our choices that show what we truly are, far more than our abilities. — J.K. Rowling",
"It’s not the years in your life that count. It’s the life in your years. — Abraham Lincoln",
"You miss 100% of the shots you don’t take. — Wayne Gretzky",
"The purpose of our lives is to be happy. — Dalai Lama",
"Life is what happens when you’re busy making other plans. — John Lennon",
"Get busy living or get busy dying. — Stephen King",
"You only live once, but if you do it right, once is enough. — Mae West",
"Many of life’s failures are people who did not realize how close they were to success when they gave up. — Thomas Edison",
"If you want to live a happy life, tie it to a goal, not to people or things. — Albert Einstein",
"Never let the fear of striking out keep you from playing the game. — Babe Ruth",
"Money and success don’t change people; they merely amplify what is already there. — Will Smith",
"Keep your face always toward the sunshine—and shadows will fall behind you. — Walt Whitman",
"The best time to plant a tree was 20 years ago. The second best time is now. — Chinese Proverb",
"An unexamined life is not worth living. — Socrates",
"Turn your wounds into wisdom. — Oprah Winfrey",
"Happiness is not something you postpone for the future; it is something you design for the present. — Jim Rohn",
"To accomplish great things, we must not only act, but also dream, not only plan, but also believe. — Anatole France",
"If life were predictable it would cease to be life, and be without flavor. — Eleanor Roosevelt",
"Life is a succession of lessons which must be lived to be understood. — Ralph Waldo Emerson",
"Your time is limited, so don’t waste it living someone else’s life. — Steve Jobs",
"Life is either a daring adventure or nothing at all. — Helen Keller",
"Keep smiling, because life is a beautiful thing and there’s so much to smile about. — Marilyn Monroe",
"Life is made of ever so many partings welded together. — Charles Dickens",
"You have within you right now, everything you need to deal with whatever the world can throw at you. — Brian Tracy",
"Believe you can and you're halfway there. — Theodore Roosevelt",
"Do what you feel in your heart to be right—for you’ll be criticized anyway. — Eleanor Roosevelt",
"Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. — Buddha",
"Life is really simple, but we insist on making it complicated. — Confucius",
"Life itself is the most wonderful fairy tale. — Hans Christian Andersen",
"The greatest glory in living lies not in never falling, but in rising every time we fall. — Nelson Mandela",
"The way to get started is to quit talking and begin doing. — Walt Disney",
"In the end, it’s not the years in your life that count. It’s the life in your years. — Abraham Lincoln",
"Life is what happens when you’re busy making other plans. — John Lennon",
"Your time is limited, so don’t waste it living someone else’s life. — Steve Jobs",
"Life is either a daring adventure or nothing at all. — Helen Keller",
"You only live once, but if you do it right, once is enough. — Mae West",
"The unexamined life is not worth living. — Socrates",
"Keep your face always toward the sunshine—and shadows will fall behind you. — Walt Whitman",
"Happiness is not something ready-made. It comes from your own actions. — Dalai Lama",
"Don’t count the days, make the days count. — Muhammad Ali",
"The only impossible journey is the one you never begin. — Tony Robbins",
"Success is not how high you have climbed, but how you make a positive difference to the world. — Roy T. Bennett",
"Act as if what you do makes a difference. It does. — William James",
"With the new day comes new strength and new thoughts. — Eleanor Roosevelt",
"The question isn’t who is going to let me; it’s who is going to stop me. — Ayn Rand",
"The harder the battle, the sweeter the victory. — Les Brown",
"Strive not to be a success, but rather to be of value. — Albert Einstein",
"What lies behind us and what lies before us are tiny matters compared to what lies within us. — Ralph Waldo Emerson",
"The best revenge is massive success. — Frank Sinatra",
"In order to write about life first you must live it. — Ernest Hemingway",
"Not how long, but how well you have lived is the main thing. — Seneca",
"Turn your wounds into wisdom. — Oprah Winfrey",
"What you get by achieving your goals is not as important as what you become by achieving your goals. — Zig Ziglar",
"Try to be a rainbow in someone’s cloud. — Maya Angelou",
"When you cease to dream, you cease to live. — Malcolm Forbes",
"No matter what people tell you, words and ideas can change the world. — Robin Williams",
"Only a life lived for others is a life worthwhile. — Albert Einstein",
"Life is really simple, but we insist on making it complicated. — Confucius",
"Live in the sunshine, swim the sea, drink the wild air. — Ralph Waldo Emerson",
"The best view comes after the hardest climb. — Unknown",
"You are never too old to set another goal or to dream a new dream. — C.S. Lewis",
"Do what is right, not what is easy nor what is popular. — Roy T. Bennett",
"Success isn’t about how much money you make; it’s about the difference you make in people’s lives. — Michelle Obama",
"Dream big and dare to fail. — Norman Vaughan",
"Start where you are. Use what you have. Do what you can. — Arthur Ashe",
"It does not matter how slowly you go as long as you do not stop. — Confucius",
"Everything you’ve ever wanted is on the other side of fear. — George Addair",
"Success is the sum of small efforts, repeated day-in and day-out. — Robert Collier",
"Success is how high you bounce when you hit bottom. — George S. Patton",
"Do not let what you cannot do interfere with what you can do. — John Wooden",
"Motivation is what gets you started. Habit is what keeps you going. — Jim Ryun"
]

def create_daily_journal_jan2025(filename="daily_journal_2025.pdf"):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    margin = 0.5 * inch
    line_spacing = 0.4 * inch
    
    total_days = 365  # 2025 is not a leap year

    # (1) Define exact start dates for seasons in 2025
    season_starts = [
        ("Winter",  datetime.date(2025, 1, 1)),   # Already winter
        ("Spring",  datetime.date(2025, 3, 20)),
        ("Summer",  datetime.date(2025, 6, 21)),
        ("Fall",    datetime.date(2025, 9, 23)),
        ("W",       datetime.date(2025, 12, 21)), # Next Winter label as just 'W'
    ]

    season_positions = []
    for label, dte in season_starts:
        doy = dte.timetuple().tm_yday
        season_positions.append((label, doy))

    # (2) Define month labels precisely by date
    month_labels = {
        1:  "J", 2:  "F", 3:  "M", 4:  "A", 
        5:  "M", 6:  "J", 7:  "J", 8:  "A", 
        9:  "S", 10: "O", 11: "N", 12: "D"
    }

    month_positions = []
    for m in range(1, 13):
        dte = datetime.date(2025, m, 1)
        doy = dte.timetuple().tm_yday
        label = month_labels[m]
        month_positions.append((label, doy))

    # ----------------------------------------------------------------
    # CHANGED HERE: Loop through ALL 365 days of 2025, not just January
    # ----------------------------------------------------------------
    for day in range(1, 366):
        # day=1 -> January 1, 2025  |  day=365 -> December 31, 2025
        dt = datetime.date(2025, 1, 1) + datetime.timedelta(days=day - 1)
        day_of_week = dt.strftime("%A")         # e.g. "Monday"
        date_str    = dt.strftime("%B %d, %Y")  # e.g. "January 06, 2025"
        
        day_of_year = dt.timetuple().tm_yday
        fraction    = day_of_year / total_days

        # ---------------------------
        # TOP-LEFT: Day of Week + Date
        # ---------------------------
        c.setFont("Helvetica-Bold", 14)
        c.drawString(margin, height - margin, f"{day_of_week}, {date_str}")

        # ---------------------------
        # TOP-RIGHT: Precise Bar
        # ---------------------------
        bar_width  = 3.5 * inch
        bar_height = 0.5 * inch
        
        x_bar = width - margin - bar_width
        y_bar = height - margin - 0.2 * inch

        # 1) Outline the bar
        c.setStrokeColor(colors.black)
        c.setLineWidth(1)
        c.rect(x_bar, y_bar, bar_width, bar_height, stroke=1, fill=0)

        # 2) Fill portion for fraction of year passed
        filled_width = fraction * bar_width
        c.setFillColor(colors.black)
        c.rect(x_bar, y_bar + (0.15 * inch), filled_width, bar_height - (0.3 * inch), stroke=0, fill=1)

        # 3) Place the season labels at exact day-of-year
        c.setFont("Helvetica-Bold", 8)
        for (season_label, doy) in season_positions:
            frac = doy / total_days
            x_label = x_bar + frac * bar_width
            y_label = y_bar + bar_height - 10
            c.drawString(x_label, y_label, season_label)

        # 4) Place the month labels at exact day-of-year
        c.setFont("Helvetica", 8)
        for (m_label, doy) in month_positions:
            frac = doy / total_days
            x_label = x_bar + frac * bar_width
            y_label = y_bar + 2
            c.drawString(x_label, y_label, m_label)

        # ---------------------------
        # Journal Prompts
        # ---------------------------
        y_pos = height - margin - 1.2 * inch
        c.setFont("Helvetica", 12)

        # Today's Focus
        c.drawString(margin, y_pos, "Today’s Focus:")
        c.line(margin, y_pos - 0.1 * inch, width - margin, y_pos - 0.1 * inch)
        
        # Top 3 Priorities
        y_pos -= 0.5 * inch
        c.drawString(margin, y_pos, "Top 3 Priorities:")
        y_pos -= 0.3 * inch
        for _ in range(3):
            c.circle(margin + 0.2 * inch, y_pos, 2, fill=0)
            c.line(margin + 0.4 * inch, y_pos, width - margin, y_pos)
            y_pos -= 0.4 * inch

        # Morning Thoughts
        c.drawString(margin, y_pos, "Morning Thoughts (Gratitude/Goals/Intentions):")
        y_pos -= 0.3 * inch
        for _ in range(4):
            c.line(margin, y_pos, width - margin, y_pos)
            y_pos -= line_spacing

        # Evening Reflections
        c.drawString(margin, y_pos, "Evening Reflections (Wins/Lessons/Notes):")
        y_pos -= 0.3 * inch
        for _ in range(4):
            c.line(margin, y_pos, width - margin, y_pos)
            y_pos -= line_spacing

        # ---------------------------
        # Random Stoic Quote (Bottom)
        # ---------------------------
        quote = random.choice(stoic_quotes)
        c.setFont("Helvetica-Oblique", 10)
        c.drawCentredString(width / 2, margin, quote)

        # Next page
        c.showPage()

    # Save
    c.save()

if __name__ == "__main__":
    create_daily_journal_jan2025()
