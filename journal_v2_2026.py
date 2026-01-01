import random
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors

# A small set of Stoic quotes
stoic_quotes = [
    "You have power over your mind—not outside events. Realize this, and you will find strength. — Marcus Aurelius",
    "Waste no more time arguing what a good man should be. Be one. — Marcus Aurelius",
    "The happiness of your life depends upon the quality of your thoughts. — Marcus Aurelius",
    "Very little is needed to make a happy life; it is all within yourself, in your way of thinking. — Marcus Aurelius",
    "The impediment to action advances action. What stands in the way becomes the way. — Marcus Aurelius",
    "Reject your sense of injury and the injury itself disappears. — Marcus Aurelius",
    "The best revenge is to be unlike him who performed the injury. — Marcus Aurelius",
    "Choose not to be harmed—and you won’t feel harmed. Don’t feel harmed—and you haven’t been. — Marcus Aurelius",
    "You always own the option of having no opinion. — Marcus Aurelius",
    "Death smiles at us all; all a man can do is smile back. — Marcus Aurelius",
    "Our life is what our thoughts make it. — Marcus Aurelius",
    "It is not death that a man should fear, but he should fear never beginning to live. — Marcus Aurelius",
    "The things you think about determine the quality of your mind. — Marcus Aurelius",
    "Nothing happens to any man that he is not formed by nature to bear. — Marcus Aurelius",
    "At dawn, when you have trouble getting out of bed, tell yourself: I have to go to work—as a human being. — Marcus Aurelius",
    "The art of living is more like wrestling than dancing. — Marcus Aurelius",
    "Nowhere can man find a quieter or more untroubled retreat than in his own soul. — Marcus Aurelius",
    "How ridiculous and how strange to be surprised at anything which happens in life. — Marcus Aurelius",
    "If someone can prove me wrong and show me my mistake in any thought or action, I shall gladly change. — Marcus Aurelius",
    "The tranquility that comes when you stop caring what they say, or think, or do. Only what you do. — Marcus Aurelius",
    "Be tolerant with others and strict with yourself. — Marcus Aurelius",
    "The universe is change; our life is what our thoughts make it. — Marcus Aurelius",
    "Adapt yourself to the things among which your lot has been cast. — Marcus Aurelius",
    "Objective judgment, now. Unselfish action, now. Willing acceptance of all external events, now. That's all you need. — Marcus Aurelius",
    "Do every act of your life as though it were the very last act of your life. — Marcus Aurelius",
    "Never esteem anything as of advantage to you that will make you break your word or lose your self-respect. — Marcus Aurelius",
    "He who lives in harmony with himself lives in harmony with the universe. — Marcus Aurelius",
    "Time is a river of passing events, and strong is its current. — Marcus Aurelius",
    "The soul becomes dyed with the color of its thoughts. — Marcus Aurelius",
    "When you arise in the morning, think of what a precious privilege it is to be alive—to breathe, to think, to enjoy, to love. — Marcus Aurelius",
    "We suffer more often in imagination than in reality. — Seneca",
    "Luck is what happens when preparation meets opportunity. — Seneca",
    "It is not that we have a short time to live, but that we waste a lot of it. — Seneca",
    "True happiness is to enjoy the present, without anxious dependence upon the future. — Seneca",
    "Sometimes even to live is an act of courage. — Seneca",
    "Fire tests gold, misfortune tests brave men. — Seneca",
    "He who is brave is free. — Seneca",
    "The whole future lies in uncertainty: live immediately. — Seneca",
    "Life is long if you know how to use it. — Seneca",
    "Most powerful is he who has himself in his own power. — Seneca",
    "The point is, not how long you live, but how nobly you live. — Seneca",
    "Fate leads the willing and drags along the reluctant. — Seneca",
    "Hang on to your youthful enthusiasms—you’ll be able to use them better when you’re older. — Seneca",
    "You act like mortals in all that you fear, and like immortals in all that you desire. — Seneca",
    "No man is more unhappy than he who never faces adversity. For he is not permitted to prove himself. — Seneca",
    "It's not because things are difficult that we dare not venture. It's because we dare not venture that they are difficult. — Seneca",
    "There is no enjoying the possession of anything valuable unless one has someone to share it with. — Seneca",
    "Begin at once to live, and count each separate day as a separate life. — Seneca",
    "As is a tale, so is life: not how long it is, but how good it is, is what matters. — Seneca",
    "Anger, if not restrained, is frequently more hurtful to us than the injury that provokes it. — Seneca",
    "Enjoy present pleasures in such a way as not to injure future ones. — Seneca",
    "What progress have I made? I have begun to be a friend to myself. — Seneca",
    "Nothing is a better proof of a well-ordered mind than a man’s ability to pass time in his own company. — Seneca",
    "The greatest obstacle to living is expectancy, which hangs upon tomorrow and loses today. — Seneca",
    "Drunkenness is nothing but voluntary madness. — Seneca",
    "The day which we fear as our last is but the birthday of eternity. — Seneca",
    "It's not that we have little time, but more that we waste a good deal of it. — Seneca",
    "Let us prepare our minds as if we’d come to the very end of life. Let us postpone nothing. — Seneca",
    "While we wait for life, life passes. — Seneca",
    "It’s ruinous for the soul to be anxious about the future and miserable in advance of misery. — Seneca",
    "To bear trials with a calm mind robs misfortune of its strength and burden. — Seneca",
    "The man who has anticipated the coming of troubles takes away their power when they arrive. — Seneca",
    "Philosophy calls for simple living, not for doing penance. — Seneca",
    "Virtue is sufficient for happiness. — Seneca",
    "As long as you live, keep learning how to live. — Seneca",
    "Men are disturbed not by things, but by the views which they take of things. — Epictetus",
    "Don't explain your philosophy. Embody it. — Epictetus",
    "Wealth consists not in having great possessions, but in having few wants. — Epictetus",
    "There is only one way to happiness and that is to cease worrying about things which are beyond the power of our will. — Epictetus",
    "No man is free who is not master of himself. — Epictetus",
    "Any person capable of angering you becomes your master. — Epictetus",
    "Freedom is the only worthy goal in life. It is won by disregarding things that lie beyond our control. — Epictetus",
    "If you want to improve, be content to be thought foolish and stupid. — Epictetus",
    "The chief task in life is simply this: to identify and separate matters so that I can say clearly to myself which are externals not under my control, and which have to do with the choices I actually control. — Epictetus",
    "You become what you give your attention to. — Epictetus",
    "He is a wise man who does not grieve for the things which he has not, but rejoices for those which he has. — Epictetus",
    "Make the best use of what is in your power, and take the rest as it happens. — Epictetus",
    "Don't seek for everything to happen as you wish it would, but rather wish that everything happens as it actually will, and your life will flow well. — Epictetus",
    "No great thing is created suddenly. — Epictetus",
    "Events don’t hurt us, but our views of them do. — Epictetus",
    "Practice yourself in little things, and thence proceed to greater. — Epictetus",
    "The more we value things outside our control, the less control we have. — Epictetus",
    "Man is not worried by real problems so much as by his imagined anxieties about real problems. — Epictetus",
    "Progress is not achieved by luck or accident, but by working on yourself daily. — Epictetus",
    "You can be happy if you know this secret: Some things are within your power to control and some things are not. — Epictetus",
    "Know, first, who you are, and then adorn yourself accordingly. — Epictetus",
    "The two most powerful warriors are patience and time. — Seneca (often attributed, but originally Leo Tolstoy; included as commonly associated)",
    "Small-minded people blame others. Average people blame themselves. The wise see all blame as foolishness. — Epictetus",
    "Keep your attention focused entirely on what is truly your own concern. — Epictetus",
    "If evil be said of thee, and if it be true, correct thyself; if it be a lie, laugh at it. — Epictetus",
    "The essence of philosophy is that a man should so live that his happiness shall depend as little as possible on external things. — Epictetus",
    "We should always be asking ourselves: Is this something that is, or is not, in my control? — Epictetus",
    "Control thy passions lest they take vengeance on thee. — Epictetus",
    "We have two ears and one mouth so that we can listen twice as much as we speak. — Epictetus (often attributed to Zeno, but Epictetus echoes similar)",
    "It is not he who reviles or strikes you who insults you, but your opinion that these things are insulting. — Epictetus",
    "The greater the difficulty, the more glory in surmounting it. — Epictetus",
    "Discipline is the soul of an army. It makes small numbers formidable; procures success to the weak, and esteem to all. — George Washington",
    "Happiness and moral duty are inseparably connected. — George Washington",
    "Associate yourself with men of good quality if you esteem your own reputation; for 'tis better to be alone than in bad company. — George Washington",
    "It is better to offer no excuse than a bad one. — George Washington",
    "Be courteous to all, but intimate with few, and let those few be well tried before you give them your confidence. — George Washington",
    "Labor to keep alive in your breast that little spark of celestial fire called conscience. — George Washington",
    "Guard against the impostures of pretended patriotism. — George Washington",
    "The harder the conflict, the greater the triumph. — George Washington",
    "To persevere in one's duty and be silent is the best answer to calumny. — George Washington",
    "Few men have virtue to withstand the highest bidder. — George Washington",
    "If the freedom of speech is taken away then dumb and silent we may be led, like sheep to the slaughter. — George Washington",
    "Worry is the interest paid by those who borrow trouble. — George Washington",
    "It is far better to be alone, than to be in bad company. — George Washington",
    "Human happiness and moral duty are inseparably connected. — George Washington",
    "Liberty, when it begins to take root, is a plant of rapid growth. — George Washington",
    "The turning points of lives are not the great moments. The real crises are often concealed in occurrences so trivial in appearance that they pass unobserved. — George Washington",
    "A sensible woman can never be happy with a fool. — George Washington",
    "Truth will ultimately prevail where there is pains taken to bring it to light. — George Washington",
    "A free people ought not only to be armed, but disciplined. — George Washington",
    "99% of failures come from people who make excuses. — George Washington",
    "Discipline is choosing between what you want now and what you want most. — Thomas Jefferson (modern attribution, but aligned with founding principles)",
    "I find that the harder I work, the more luck I seem to have. — Thomas Jefferson",
    "Do you want to know who you are? Don't ask. Act! Action will delineate and define you. — Thomas Jefferson",
    "Nothing can stop the man with the right mental attitude from achieving his goal; nothing on earth can help the man with the wrong mental attitude. — Thomas Jefferson",
    "In matters of style, swim with the current; in matters of principle, stand like a rock. — Thomas Jefferson",
    "The most valuable of all talents is that of never using two words when one will do. — Thomas Jefferson",
    "Honesty is the first chapter in the book of wisdom. — Thomas Jefferson",
    "I cannot live without books. — Thomas Jefferson",
    "The price of freedom is eternal vigilance. — Thomas Jefferson",
    "He who knows best knows how little he knows. — Thomas Jefferson",
    "Timid men prefer the calm of despotism to the tempestuous sea of liberty. — Thomas Jefferson",
    "The glow of one warm thought is to me worth more than money. — Thomas Jefferson",
    "When angry, count ten before you speak; if very angry, a hundred. — Thomas Jefferson",
    "Determine never to be idle. No person will have occasion to complain of the want of time who never loses any. — Thomas Jefferson",
    "I’m a great believer in luck, and I find the harder I work the more I have of it. — Thomas Jefferson",
    "Pride costs us more than hunger, thirst, and cold. — Thomas Jefferson",
    "Nothing gives one person so much advantage over another as to remain always cool and unruffled under all circumstances. — Thomas Jefferson",
    "Do not bite at the bait of pleasure till you know there is no hook beneath it. — Thomas Jefferson",
    "The man who fears no truth has nothing to fear from lies. — Thomas Jefferson",
    "He who permits himself to tell a lie once, finds it much easier to do it the second time. — Thomas Jefferson",
    "Delay is preferable to error. — Thomas Jefferson",
    "The care of human life and happiness, and not their destruction, is the first and only object of good government. — Thomas Jefferson",
    "Never spend your money before you have it. — Thomas Jefferson",
    "Never trouble another for what you can do yourself. — Thomas Jefferson",
    "Never put off till tomorrow what you can do today. — Thomas Jefferson",
    "Never buy what you do not want, because it is cheap. — Thomas Jefferson",
    "We never repent of having eaten too little. — Thomas Jefferson",
    "How much pain have cost us the evils which have never happened! — Thomas Jefferson",
    "Take things always by their smooth handle. — Thomas Jefferson",
    "When you reach the end of your rope, tie a knot in it and hang on. — Thomas Jefferson",
    "Walking is the best possible exercise. Habituate yourself to walk very far. — Thomas Jefferson",
    "The legitimate powers of government extend to such acts only as are injurious to others. — Thomas Jefferson",
    "Experience demands that man is the only animal which devours his own kind. — Thomas Jefferson",
    "If a nation expects to be ignorant and free, it expects what never was and never will be. — Thomas Jefferson",
    "The tree of liberty must be refreshed from time to time with the blood of patriots and tyrants. — Thomas Jefferson",
    "I predict future happiness for Americans if they can prevent the government from wasting the labors of the people under the pretense of taking care of them. — Thomas Jefferson",
    "Commerce with all nations, alliance with none, should be our motto. — Thomas Jefferson",
    "It is neither wealth nor splendor, but tranquility and occupation which give happiness. — Thomas Jefferson",
    "Leave all the afternoon for exercise and recreation, which are as necessary as reading. — Thomas Jefferson",
    "An honest man can feel no pleasure in the exercise of power over his fellow citizens. — Thomas Jefferson",
    "The God who gave us life, gave us liberty at the same time. — Thomas Jefferson",
    "Educate and inform the whole mass of the people... They are the only sure reliance for the preservation of our liberty. — Thomas Jefferson",
    "Where the press is free and every man able to read, all is safe. — Thomas Jefferson",
    "I hold it that a little rebellion now and then is a good thing. — Thomas Jefferson",
    "The earth belongs to the living. — Thomas Jefferson",
    "Question with boldness even the existence of a God. — Thomas Jefferson",
    "I like the dreams of the future better than the history of the past. — Thomas Jefferson",
    "Conquest is not in our principles. It is inconsistent with our government. — Thomas Jefferson",
    "Peace, commerce, and honest friendship with all nations—entangling alliances with none. — Thomas Jefferson",
    "The boisterous sea of liberty is never without a wave. — Thomas Jefferson",
    "Error of opinion may be tolerated where reason is left free to combat it. — Thomas Jefferson",
    "Every generation needs a new revolution. — Thomas Jefferson",
    "The dead should not rule the living. — Thomas Jefferson",
    "I have sworn upon the altar of God eternal hostility against every form of tyranny over the mind of man. — Thomas Jefferson",
    "The government you elect is the government you deserve. — Thomas Jefferson",
    "That government is best which governs the least, because its people discipline themselves. — Thomas Jefferson",
    "A wise and frugal government, which shall restrain men from injuring one another, shall leave them otherwise free to regulate their own pursuits. — Thomas Jefferson",
    "The natural progress of things is for liberty to yield and government to gain ground. — Thomas Jefferson",
    "Were it left to me to decide whether we should have a government without newspapers, or newspapers without a government, I should not hesitate a moment to prefer the latter. — Thomas Jefferson",
    "My reading of history convinces me that most bad government results from too much government. — Thomas Jefferson",
    "I would rather be exposed to the inconveniences attending too much liberty than those attending too small a degree of it. — Thomas Jefferson",
    "Timid men prefer the calm of despotism to the boisterous sea of liberty. — Thomas Jefferson",
    "The strongest reason for the people to retain the right to keep and bear arms is, as a last resort, to protect themselves against tyranny in government. — Thomas Jefferson",
    "No free man shall ever be debarred the use of arms. — Thomas Jefferson",
    "The democracy will cease to exist when you take away from those who are willing to work and give to those who would not. — Thomas Jefferson",
    "When the people fear the government, there is tyranny. When the government fears the people, there is liberty. — Thomas Jefferson",
    "I never considered a difference of opinion in politics, in religion, in philosophy, as cause for withdrawing from a friend. — Thomas Jefferson",
    "The spirit of resistance to government is so valuable on certain occasions that I wish it to be always kept alive. — Thomas Jefferson",
    "Rightful liberty is unobstructed action according to our will within limits drawn around us by the equal rights of others. — Thomas Jefferson",
    "The policy of the American government is to leave their citizens free, neither restraining nor aiding them in their pursuits. — Thomas Jefferson",
    "A bill of rights is what the people are entitled to against every government on earth. — Thomas Jefferson",
    "I am not among those who fear the people. They, and not the rich, are our dependence for continued freedom. — Thomas Jefferson",
    "The people are the only sure reliance for the preservation of our liberty. — Thomas Jefferson",
    "It is incumbent on every generation to pay its own debts as it goes. — Thomas Jefferson",
    "To compel a man to furnish contributions of money for the propagation of opinions which he disbelieves is sinful and tyrannical. — Thomas Jefferson",
    "The equal rights of man, and the happiness of every human being, are the objects of government. — Thomas Jefferson",
    "We hold these truths to be self-evident: that all men are created equal; that they are endowed by their Creator with certain unalienable rights; that among these are life, liberty, and the pursuit of happiness. — Thomas Jefferson",
    "Government big enough to supply everything you need is big enough to take everything you have. — Thomas Jefferson (commonly attributed)",
    "The issue today is the same as it has been throughout all history, whether man shall be allowed to govern himself or be ruled by a small elite. — Thomas Jefferson",
    "A government that is big enough to give you all you want is big enough to take it all away. — Thomas Jefferson (variant)",
    "Rebellion to tyrants is obedience to God. — Thomas Jefferson",
    "The constitutions of most of our States assert that all power is inherent in the people. — Thomas Jefferson",
    "History, in general, only informs us what bad government is. — Thomas Jefferson",
    "Leave no authority to future generations that we do not possess ourselves. — Thomas Jefferson",
    "The people cannot be all, and always, well informed. — Thomas Jefferson",
    "Enlighten the people generally, and tyranny and oppressions of body and mind will vanish like evil spirits at the dawn of day. — Thomas Jefferson",
    "I know no safe depository of the ultimate powers of the society but the people themselves. — Thomas Jefferson",
    "Whenever the people are well-informed, they can be trusted with their own government. — Thomas Jefferson",
    "It is error alone which needs the support of government. Truth can stand by itself. — Thomas Jefferson",
    "A little rebellion now and then is a good thing, and as necessary in the political world as storms in the physical. — Thomas Jefferson",
    "The execution of the laws is more important than the making of them. — Thomas Jefferson",
    "The sacred rights of mankind are not to be rummaged for among old parchments or musty records. They are written, as with a sunbeam, in the whole volume of human nature. — Alexander Hamilton",
    "Those who stand for nothing fall for everything. — Alexander Hamilton",
    "A nation which can prefer disgrace to danger is prepared for a master, and deserves one. — Alexander Hamilton",
    "Men often oppose a thing merely because they have had no agency in planning it, or because it may have been planned by those whom they dislike. — Alexander Hamilton",
    "Power over a man's subsistence is power over his will. — Alexander Hamilton",
    "Why has government been instituted at all? Because the passions of men will not conform to the dictates of reason and justice without constraint. — Alexander Hamilton",
    "The sacred rights of mankind are not to be rummaged for among old parchments or musty records. — Alexander Hamilton",
    "Real firmness is good for everything. Strut is good for nothing. — Alexander Hamilton",
    "There is a certain enthusiasm in liberty, that makes human nature rise above itself, in acts of bravery and heroism. — Alexander Hamilton",
    "Constitutions should consist only of general provisions; the reason is that they must necessarily be permanent, and that they cannot calculate for the possible change of things. — Alexander Hamilton",
    "The voice of the people has been said to be the voice of God; and however generally this maxim has been quoted and believed, it is not true in fact. The people are turbulent and changing; they seldom judge or determine right. — Alexander Hamilton",
    "Give all power to the many, they will oppress the few. Give all power to the few, they will oppress the many. — Alexander Hamilton",
    "It is the advertiser who provides the paper for the subscriber. It is not to be disputed, that the publisher of a newspaper is entitled to his pay. — Alexander Hamilton",
    "Energy in the executive is a leading character in the definition of good government. — Alexander Hamilton",
    "Government is instituted for the common good; for the protection, safety, prosperity, and happiness of the people. — John Adams",
    "Facts are stubborn things; and whatever may be our wishes, our inclinations, or the dictates of our passions, they cannot alter the state of facts and evidence. — John Adams",
    "Liberty cannot be preserved without a general knowledge among the people. — John Adams",
    "Power always thinks it has a great soul and vast views beyond the comprehension of the weak. — John Adams",
    "Because power corrupts, society's demands for moral authority and character increase as the importance of the position increases. — John Adams",
    "There is danger from all men. The only maxim of a free government ought to be to trust no man living with power to endanger the public liberty. — John Adams",
    "Old minds are like old horses; you must exercise them if you wish to keep them in working order. — John Adams",
    "To be good, and to do good, is all we have to do. — John Adams",
    "Always stand on principle even if you stand alone. — John Adams",
    "Let us tenderly and kindly cherish, therefore, the means of knowledge. Let us dare to read, think, speak, and write. — John Adams",
    "You will never be alone with a poet in your pocket. — John Adams",
    "I must study politics and war that my sons may have liberty to study mathematics and philosophy. — John Adams",
    "The happiness of society is the end of government. — John Adams",
    "Our obligations to our country never cease but with our lives. — John Adams",
    "Children should be educated and instructed in the principles of freedom. — John Adams",
    "Posterity! You will never know how much it cost the present generation to preserve your freedom! I hope you will make a good use of it. — John Adams",
    "I read my eyes out and can't read half enough... the more one reads the more one sees we have to read. — John Adams",
    "Great is the guilt of an unnecessary war. — John Adams",
    "Power always sincerely, conscientiously believes itself right. — John Adams",
    "Remember, democracy never lasts long. It soon wastes, exhausts, and murders itself. There never was a democracy yet that did not commit suicide. — John Adams",
    "Abuse of words has been the great instrument of sophistry and chicanery, of party, faction, and division of society. — John Adams",
    "Let the human mind loose. It must be loose. It will be loose. Superstition and dogmatism cannot confine it. — John Adams",
    "There are only two creatures of value on the face of the earth: those with a commitment, and those who require the commitment of others. — John Adams",
    "A government of laws, and not of men. — John Adams",
    "Fear is the foundation of most governments. — John Adams",
    "The essence of a free government consists in an effectual control of rivalries. — John Adams",
    "Virtue is not always amiable. — John Adams",
    "No man is entirely free from weakness and imperfection in this life. — John Adams",
    "Duty is ours, results are God's. — John Adams",
    "The only maxim of a free government is to trust no man living with power to endanger the public liberty. — John Adams",
    "Let frugality and industry be our virtues. — Benjamin Franklin",
    "An investment in knowledge pays the best interest. — Benjamin Franklin",
    "Early to bed and early to rise makes a man healthy, wealthy, and wise. — Benjamin Franklin",
    "He that is good for making excuses is seldom good for anything else. — Benjamin Franklin",
    "Well done is better than well said. — Benjamin Franklin",
    "Diligence is the mother of good luck. — Benjamin Franklin",
    "Energy and persistence conquer all things. — Benjamin Franklin",
    "Lost time is never found again. — Benjamin Franklin",
    "By failing to prepare, you are preparing to fail. — Benjamin Franklin",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn. — Benjamin Franklin",
    "He that can have patience can have what he will. — Benjamin Franklin",
    "Three may keep a secret, if two of them are dead. — Benjamin Franklin",
    "God helps those who help themselves. — Benjamin Franklin (popularized)",
    "Honesty is the best policy. — Benjamin Franklin (popularized)",
    "Guests, like fish, begin to smell after three days. — Benjamin Franklin",
    "An ounce of prevention is worth a pound of cure. — Benjamin Franklin",
    "No gains without pains. — Benjamin Franklin",
    "He that lives upon hope will die fasting. — Benjamin Franklin",
    "There will be sleeping enough in the grave. — Benjamin Franklin",
    "Dost thou love life? Then do not squander time, for that is the stuff life is made of. — Benjamin Franklin",
    "The doors of wisdom are never shut. — Benjamin Franklin",
    "Tricks and treachery are the practice of fools that don't have brains enough to be honest. — Benjamin Franklin",
    "Content makes poor men rich; discontent makes rich men poor. — Benjamin Franklin",
    "He that falls in love with himself will have no rivals. — Benjamin Franklin",
    "Glass, china, and reputation are easily cracked, and never well mended. — Benjamin Franklin",
    "If you would keep your secret from an enemy, tell it not to a friend. — Benjamin Franklin",
    "A slip of the foot you may soon recover, but a slip of the tongue you may never get over. — Benjamin Franklin",
    "He that would live in peace and at ease must not speak all he knows or all he sees. — Benjamin Franklin",
    "The absent are never without fault, nor the present without excuse. — Benjamin Franklin",
    "The strictest law sometimes becomes the severest injustice. — Benjamin Franklin",
    "Anger is never without a reason, but seldom with a good one. — Benjamin Franklin",
    "Love your enemies, for they tell you your faults. — Benjamin Franklin",
    "If passion drives you, let reason hold the reins. — Benjamin Franklin",
    "Genius without education is like silver in the mine. — Benjamin Franklin",
    "The Constitution only gives people the right to pursue happiness. You have to catch it yourself. — Benjamin Franklin",
    "Whatever is begun in anger ends in shame. — Benjamin Franklin",
    "A man wrapped up in himself makes a very small bundle. — Benjamin Franklin",
    "He that composes himself is wiser than he that composes books. — Benjamin Franklin",
    "Reading makes a full man, meditation a profound man, discourse a clear man. — Benjamin Franklin",
    "Wish not so much to live long as to live well. — Benjamin Franklin",
    "There are three things extremely hard: steel, a diamond, and to know one's self. — Benjamin Franklin",
    "He that waits upon fortune is never sure of a dinner. — Benjamin Franklin",
    "Industry, perseverance, and frugality make fortune yield. — Benjamin Franklin",
    "If you know how to spend less than you get, you have the philosopher's stone. — Benjamin Franklin",
    "The used key is always bright. — Benjamin Franklin",
    "A learned blockhead is a greater blockhead than an ignorant one. — Benjamin Franklin",
    "A life of leisure and a life of laziness are two things. — Benjamin Franklin",
    "The best is the cheapest. — Benjamin Franklin",
    "Many a man thinks he is buying pleasure, when he is really selling himself to it. — Benjamin Franklin",
    "He that is of the opinion money will do everything may well be suspected of doing everything for money. — Benjamin Franklin",
    "Poverty often deprives a man of all spirit and virtue. — Benjamin Franklin",
    "Sloth, like rust, consumes faster than labor wears. — Benjamin Franklin",
    "The eye of the master will do more work than both his hands. — Benjamin Franklin",
    "Laziness travels so slowly that poverty soon overtakes him. — Benjamin Franklin",
    "Trouble springs from idleness, and grievous toil from needless ease. — Benjamin Franklin",
    "There are no gains without pains. — Benjamin Franklin",
    "Employ thy time well if thou meanest to gain leisure. — Benjamin Franklin",
    "Since thou art not sure of a minute, throw not away an hour. — Benjamin Franklin",
    "Leisure is time for doing something useful. — Benjamin Franklin",
    "He that idly loses 5s. worth of time loses 5s. — Benjamin Franklin",
    "Drive thy business, let not that drive thee. — Benjamin Franklin",
    "Industry pays debts, while despair increaseth them. — Benjamin Franklin",
    "A ploughman on his legs is higher than a gentleman on his knees. — Benjamin Franklin",
    "Be at war with your vices, at peace with your neighbors. — Benjamin Franklin",
    "Search others for their virtues, thyself for thy vices. — Benjamin Franklin",
    "Who is wise? He that learns from everyone. Who is powerful? He that governs his passions. Who is rich? He that is content. Who is that? Nobody. — Benjamin Franklin",
    "Temperance, industry, frugality, and virtue are the foundations of happiness. — Benjamin Franklin (summary of his philosophy)",
    "Remember that time is money. — Benjamin Franklin",
    "Rather go to bed without dinner than to rise in debt. — Benjamin Franklin",
    "Creditors have better memories than debtors. — Benjamin Franklin",
    "If you would know the value of money, go and try to borrow some. — Benjamin Franklin",
    "He that goes a borrowing goes a sorrowing. — Benjamin Franklin",
    "The second vice is lying, the first is running in debt. — Benjamin Franklin",
    "Lend money to an enemy, and thou will gain him; to a friend, and thou will lose him. — Benjamin Franklin",
    "The borrower is a slave to the lender. — Benjamin Franklin (proverb popularized)",
    "Pride breakfasted with plenty, dined with poverty, and supped with infamy. — Benjamin Franklin",
    "Pride is as loud a beggar as want, and a great deal more saucy. — Benjamin Franklin",
    "What maintains one vice would bring up two children. — Benjamin Franklin",
    "Avarice and happiness never saw each other, how then should they become acquainted? — Benjamin Franklin",
    "Who is strong? He that can conquer his bad habits. — Benjamin Franklin",
    "The best thing to give to your enemy is forgiveness; to an opponent, tolerance; to a friend, your heart; to your child, a good example; to a father, deference; to your mother, conduct that will make her proud of you; to yourself, respect; to all men, charity. — Benjamin Franklin (often attributed to Lord Avebury, but Franklin-aligned)",
    "Resolve to perform what you ought; perform without fail what you resolve. — Benjamin Franklin",
    "Virtue alone is happiness below. — Benjamin Franklin (from his writings)",
    "The nearest way to come at glory is to do that for conscience which we do for glory. — Benjamin Franklin",
    "Sin is not hurtful because it is forbidden, but it is forbidden because it is hurtful. — Benjamin Franklin",
    "Clean your finger before you point at my spots. — Benjamin Franklin",
    "He that best understands the world, least likes it. — Benjamin Franklin",
    "Many have been ruined by buying good pennyworths. — Benjamin Franklin",
    "He that buys by the penny maintains not only himself, but other people. — Benjamin Franklin",
    "The proud hate pride—in others. — Benjamin Franklin",
    "Pride that dines on vanity sups on contempt. — Benjamin Franklin",
    "He that sows thorns should never go barefoot. — Benjamin Franklin",
    "Love, and be loved. — Benjamin Franklin",
    "Keep your eyes wide open before marriage, half shut afterwards. — Benjamin Franklin",
    "Where there's marriage without love, there will be love without marriage. — Benjamin Franklin",
    "He that displays too often his wife and his purse is in danger of having both of them borrowed. — Benjamin Franklin",
    "One good husband is worth two good wives; for the scarcer things are, the more they're valued. — Benjamin Franklin",
    "A quarrelsome man has no good neighbors. — Benjamin Franklin",
    "The way to be safe is never to be secure. — Benjamin Franklin",
    "He that lies down with dogs shall rise up with fleas. — Benjamin Franklin",
    "There is no little enemy. — Benjamin Franklin",
    "Love your neighbor; yet don't pull down your hedge. — Benjamin Franklin",
    "He that would live in peace and ease must not speak all he knows nor judge all he sees. — Benjamin Franklin",
    "The sting of a reproach is the truth of it. — Benjamin Franklin",
    "A true friend is the best possession. — Benjamin Franklin",
    "No better relation than a prudent and faithful friend. — Benjamin Franklin",
    "Promises may get thee friends, but nonperformance will turn them into enemies. — Benjamin Franklin",
    "If you know how to spend less than you get, you have the philosopher's stone. — Benjamin Franklin",
    "A fat kitchen makes a lean will. — Benjamin Franklin",
    "Many estates are spent in the getting. — Benjamin Franklin",
    "Women and wine, game and deceit, make the wealth small and the wants great. — Benjamin Franklin",
    "He that is rich need not live sparingly, and he that can live sparingly need not be rich. — Benjamin Franklin",
    "Rather go to bed supperless than rise in debt. — Benjamin Franklin",
    "Experience keeps a dear school, yet fools will learn in no other. — Benjamin Franklin",
    "He that resolves to amend will amend. — Benjamin Franklin",
    "What you would seem to be, be really. — Benjamin Franklin",
    "Let honesty and industry be thy constant companions. — Benjamin Franklin",
    "Humility makes great men twice honorable. — Benjamin Franklin",
    "The honest man takes pains, and then enjoys pleasures; the knave takes pleasure, and then suffers pains. — Benjamin Franklin",
    "He that is conscious of a stink in his breeches is jealous of every wrinkle in another's nose. — Benjamin Franklin",
    "Half the truth is often a great lie. — Benjamin Franklin",
    "A lie stands on one leg, truth on two. — Benjamin Franklin",
    "He that speaks much is much mistaken. — Benjamin Franklin",
    "Silence is not always a sign of wisdom, but babbling is ever a mark of folly. — Benjamin Franklin",
    "Many foxes grow gray, but few grow good. — Benjamin Franklin",
    "He that has once done you a kindness will be more ready to do you another than he whom you yourself have obliged. — Benjamin Franklin",
    "You may delay, but time will not. — Benjamin Franklin",
    "Tomorrow every fault is to be amended; but that tomorrow never comes. — Benjamin Franklin",
    "The things which hurt, instruct. — Benjamin Franklin",
    "Search others for their virtues, thyself for thy vices. — Benjamin Franklin",
    "To lengthen thy life, lessen thy meals. — Benjamin Franklin",
    "Eat to live, and not live to eat. — Benjamin Franklin",
    "To bear other people's afflictions, everyone has courage enough and to spare. — Benjamin Franklin",
    "Many a man would have been worse if his estate had been better. — Benjamin Franklin",
    "He that drinks his cider alone, let him catch his horse alone. — Benjamin Franklin",
    "If you would not be forgotten as soon as you are dead, either write things worth reading or do things worth writing. — Benjamin Franklin",
    "If you would have a faithful servant, and one that you like, serve yourself. — Benjamin Franklin",
    "A good example is the best sermon. — Benjamin Franklin",
    "He that is known to pay punctually and exactly to the time he promises may at any time, and on any occasion, raise all the money his friends can spare. — Benjamin Franklin",
    "Think of three things: whence you came, where you are going, and to whom you must account. — Benjamin Franklin",
    "Be slow in choosing a friend, slower in changing. — Benjamin Franklin",
    "He that sells upon credit expects to lose 5 per cent by bad debts. — Benjamin Franklin",
    "The discontented man finds no easy chair. — Benjamin Franklin",
    "Having been poor is no shame, but being ashamed of it is. — Benjamin Franklin",
    "At the working man's house hunger looks in, but dares not enter. — Benjamin Franklin",
    "Industry pays debts, despair increases them. — Benjamin Franklin",
    "When prosperity was well mounted, she let go the bridle, and soon came tumbling out of the saddle. — Benjamin Franklin",
    "A small leak will sink a great ship. — Benjamin Franklin",
    "Who has deceived thee so often as thyself? — Benjamin Franklin",
    "There is no kind of dishonesty into which men can fall more easily than that of deceiving themselves. — Benjamin Franklin (paraphrase)",
    "He that is good at making excuses is seldom good for anything else. — Benjamin Franklin",
    "Constant complaint is the poorest sort of pay for all the comforts we enjoy. — Benjamin Franklin",
    "Many complain of their memory, few of their judgment. — Benjamin Franklin",
    "He that speaks ill of the mare will buy her. — Benjamin Franklin",
    "Admiration is the daughter of ignorance. — Benjamin Franklin",
    "A man is sometimes more generous when he has little money than when he has much. — Benjamin Franklin",
    "He does not possess wealth that allows it to possess him. — Benjamin Franklin",
    "Wealth is not his that has it, but his that enjoys it. — Benjamin Franklin",
    "If you desire many things, many things will seem few. — Benjamin Franklin",
    "Who is rich? He that rejoices in his portion. — Benjamin Franklin",
    "Content is the philosopher's stone, that turns all it touches into gold. — Benjamin Franklin",
    "He that is content is rich. — Benjamin Franklin (echoing Stoic sentiment)",
    "The virtue of humility is the foundation of all other virtues. — Founding era wisdom",
    "Self-mastery is the highest form of freedom. — Stoic-aligned founding principle"
]

def create_daily_journal_2026(filename="daily_journal_2026.pdf"):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    margin = 0.5 * inch
    line_spacing = 0.4 * inch
    
    total_days = 365  # 2026 is not a leap year

    # (1) Define exact start dates for seasons in 2026
    season_starts = [
        ("Winter",  datetime.date(2026, 1, 1)),   # Already winter
        ("Spring",  datetime.date(2026, 3, 20)),
        ("Summer",  datetime.date(2026, 6, 21)),
        ("Fall",    datetime.date(2026, 9, 22)),
        ("W",       datetime.date(2026, 12, 21)), # Next Winter label as just 'W'
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
        dte = datetime.date(2026, m, 1)
        doy = dte.timetuple().tm_yday
        label = month_labels[m]
        month_positions.append((label, doy))

    # ----------------------------------------------------------------
    # CHANGED HERE: Loop through ALL 365 days of 2026, not just January
    # ----------------------------------------------------------------
    for day in range(1, 366):
        # day=1 -> January 1, 2026  |  day=365 -> December 31, 2026
        dt = datetime.date(2026, 1, 1) + datetime.timedelta(days=day - 1)
        day_of_week = dt.strftime("%A")         # e.g. "Monday"
        date_str    = dt.strftime("%B %d, %Y")  # e.g. "January 06, 2026"
        
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
    create_daily_journal_2026()
