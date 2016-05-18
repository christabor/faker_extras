"""Faker data providers for binary data."""

from __future__ import absolute_import

from random import choice

from faker.providers import BaseProvider


class HumanProvider(BaseProvider):
    """Provide binary data."""

    def pos_attribute(self):
        """Return a positive attribute.

        Source: http://examples.yourdictionary.com/examples-of-attributes.html
        """
        return choice([
            'Achiever',
            'Active',
            'Adaptable',
            'Ambitious',
            'Balanced',
            'Candid',
            'Cheerful',
            'Communicative',
            'Compassionate',
            'Competitive',
            'Consistent',
            'Cooperative',
            'Courageous',
            'Curious',
            'Devoted',
            'Diplomatic',
            'Easy going',
            'Emotional',
            'Enterprising',
            'Enthusiastic',
            'Entrepreneurial',
            'Exciting',
            'Facilitator',
            'Fast',
            'Flexible',
            'Focused',
            'Forgiving',
            'Generous',
            'Genuine',
            'Good listener',
            'Helpful',
            'Imaginative',
            'Incredible',
            'Independent',
            'Industrious',
            'Initiator',
            'Insightful',
            'Interesting',
            'Inventive',
            'Knowledgeable',
            'Leader',
            'Literate',
            'Logical',
            'Meditative',
            'Mediator',
            'Modest',
            'Open Minded',
            'Organized',
            'Original',
            'Outgoing',
            'Particular',
            'Patient',
            'Perceptive',
            'Personable',
            'Persuasive',
            'Pleasant',
            'Political',
            'Positive',
            'Powerful',
            'Practical',
            'Proactive',
            'Productive',
            'Professional',
            'Quality',
            'Quick',
            'Quirky',
            'Quixotic',
            'Racy',
            'Rebellious',
            'Responsible',
            'Results-driven',
            'Results-oriented',
            'Self-reliant',
            'Sense of Humor',
            'Sensible',
            'Sensitive',
            'Sensuous',
            'Sincere',
            'Skilled',
            'Social Consciousness',
            'Solid',
            'Sporty',
            'Thoughtful',
            'Trustworthy',
            'Understanding',
            'Warm',
            'Wise',
        ])

    def neg_attribute(self):
        """Return a negative attribute.

        Source: http://examples.yourdictionary.com/examples-of-attributes.html
        """
        return choice([
            'Aggressive',
            'Aloof',
            'Arrogant',
            'Belligerent',
            'Big-headed',
            'Bitchy',
            'Boastful',
            'Bone-idle',
            'Boring',
            'Bossy',
            'Callous',
            'Cantankerous',
            'Careless',
            'Changeable',
            'Clinging',
            'Compulsive',
            'Conservative',
            'Cowardly',
            'Cruel',
            'Cunning',
            'Cynical',
            'Deceitful',
            'Detached',
            'Dishonest',
            'Dogmatic',
            'Domineering',
            'Finicky',
            'Flirtatious',
            'Foolish',
            'Foolhardy',
            'Fussy',
            'Greedy',
            'Grumpy',
            'Gullible',
            'Garish',
            'Impatient',
            'Impolite',
            'Impulsive',
            'Inconsiderate',
            'Inconsistent',
            'Indecisive',
            'Indiscreet',
            'Inflexible',
            'Interfering',
            'Intolerant',
            'Irresponsible',
            'Jealous',
            'Lazy',
            'Machiavellian',
            'Materialistic',
            'Mean',
            'Miserly',
            'Moody',
            'Narrow-minded',
            'Nasty',
            'Naughty',
            'Nervous',
            'Obsessive',
            'Obstinate',
            'Overcritical',
            'Overemotional',
            'Parsimonious',
            'Patronizing',
            'Perverse',
            'Pessimistic',
            'Pompous',
            'Possessive',
            'Pusillanimous',
            'Quarrelsome',
            'Quick-tempered',
            'Resentful',
            'Rude',
            'Ruthless',
            'Sarcastic',
            'Secretive',
            'Selfish',
            'Self-centered',
            'Self-indulgent',
            'Silly',
            'Sneaky',
            'Stingy',
            'Stubborn',
            'Stupid',
            'Superficial',
            'Tactless',
            'Timid',
            'Touchy',
            'Thoughtless',
            'Truculent',
            'Unkind',
            'Unpredictable',
            'Unreliable',
            'Untidy',
            'Untrustworthy',
            'Vague',
            'Vain',
            'Vengeful',
            'Vulgar',
            'Weak-willed',
        ])

    def mood(self):
        """Return a random mood.

        Source: https://www.vocabulary.com/lists/535865
        """
        return choice([
            'abandoned',
            'accepted',
            'aggressive',
            'alienated',
            'amazed',
            'amused',
            'anxious',
            'apathetic',
            'ashamed',
            'astonished',
            'aversion',
            'avoidance',
            'awed',
            'awful',
            'bored',
            'confident',
            'confused',
            'courageous',
            'critical',
            'depressed',
            'despair',
            'detestable',
            'devastate',
            'disappointed',
            'disapproving',
            'disillusioned',
            'dismayed',
            'disrespectful',
            'distant',
            'eager',
            'ecstatic',
            'embarrassed',
            'empty',
            'energetic',
            'enraged',
            'excited',
            'frightened',
            'frustrated',
            'fulfilled',
            'furious',
            'guilty',
            'hateful',
            'hesitant',
            'hopeful',
            'hostile',
            'humiliated',
            'hurt',
            'ignored',
            'important',
            'inadequate',
            'indifferent',
            'inferior',
            'infuriated',
            'inquisitive',
            'insecure',
            'insignificant',
            'inspired',
            'interested',
            'intimate',
            'irritated',
            'isolated',
            'jealous',
            'joyful',
            'judgmental',
            'liberated',
            'loathing',
            'lonely',
            'loving',
            'mad',
            'open',
            'optimistic',
            'overwhelm',
            'peaceful',
            'perplexed',
            'playful',
            'powerful',
            'powerless',
            'proud',
            'provocative',
            'rejected',
            'remorseful',
            'repugnant',
            'resentful',
            'respected',
            'ridicule',
            'sarcastic',
            'scared',
            'sensitive',
            'shocked',
            'skeptical',
            'startled',
            'submissive',
            'suspicious',
            'terrified',
            'threatened',
            'victimized',
            'vulnerable',
            'withdrawn',
            'worried',
            'worthless',
        ])

    def gender(self):
        """Return a random gender. Taken from Facebook gender choices."""
        return choice([
            'Agender',
            'Androgyne',
            'Androgynous',
            'Bigender',
            'Cis',
            'Cisgender',
            'Cis Female',
            'Cis Male',
            'Cis Man',
            'Cis Woman',
            'Cisgender Female',
            'Cisgender Male',
            'Cisgender Man',
            'Cisgender Woman',
            'Female to Male',
            'FTM',
            'Gender Fluid',
            'Gender Nonconforming',
            'Gender Questioning',
            'Gender Variant',
            'Genderqueer',
            'Intersex',
            'Male to Female',
            'MTF',
            'Neither',
            'Neutrois',
            'Non-binary',
            'Other',
            'Pangender',
            'Trans',
            'Trans*',
            'Trans Female',
            'Trans* Female',
            'Trans Male',
            'Trans* Male',
            'Trans Man',
            'Trans* Man',
            'Trans Person',
            'Trans* Person',
            'Trans Woman',
            'Trans* Woman',
            'Transfeminine',
            'Transgender',
            'Transgender Female',
            'Transgender Male',
            'Transgender Man',
            'Transgender Person',
            'Transgender Woman',
            'Transmasculine',
            'Transsexual',
            'Transsexual Female',
            'Transsexual Male',
            'Transsexual Man',
            'Transsexual Person',
            'Transsexual Woman',
            'Two-Spirit',
        ])

    def religion(self):
        """Return a random (major) religion.

        Source: http://www.infoplease.com/ipa/A0904108.html

        >>> religion()
        >>> Pastafarian
        """
        return choice([
            'Atheism',
            'Christianity',
            'Islam',
            'Hinduism',
            'Buddhism',
            'Sikhism',
            'Judaism',
            'Bahaism',
            'Confucianism',
            'Jainism',
            'Shintoism',
            'Pastafarian',
        ])

    def race(self):
        """Return a random race.

        Source: http://people.virginia.edu/~sfr/enam358/races.html

        >>> race()
        >>> Alien/Unknown
        """
        return choice([
            'Alien/Unknown',
            'Aboriginal/Australian, South Pacific',
            'Aborigine',
            'African',
            'African/African-American/Black',
            'African-American',
            'African-American/Black',
            'American',
            'American Indian',
            'Arabian',
            'Arabic',
            'Arab/Middle Eastern',
            'Asian',
            'Asian/-American',
            'Asian/Indian',
            'Asian/Oriental',
            'Asian/Other than American',
            'Asian/Mongoloid',
            'Asian/Subcontinent',
            'Asian/Pacific',
            'Bi/multiracial',
            'Black',
            'Black/African',
            'Black/African descent',
            'Black/African-American',
            'Black/American',
            'Black/Central-Southern African',
            'Black/Other than American',
            'Brown/Hispanic',
            'Caucasion',
            'Caucasion/White',
            'Chinese',
            'Combination',
            'Eastern Indian',
            'Eskimo',
            'Eskimo/Aleutian',
            'European',
            'Filipino',
            'Hispanic',
            'Hispanic/American',
            'Hispanic/Latin',
            'Hispanic/Latino',
            'Hispanic/Other than American',
            'Human',
            'Indian',
            'Indian/Middle Asian',
            'Indian/Native American or otherwise',
            'Indian/Pakistani',
            'Islander',
            'Japanese',
            'Jewish',
            'Korean',
            'Latina',
            'Latino',
            'Latino/a',
            'Latino/Hispanic',
            'Mestiza/Mixed',
            'Mexican',
            'Middle Eastern',
            'Middle Eastern/American',
            'Middle Eastern/Arabic',
            'Middle Eastern/Other than American',
            'Mixed',
            'Mixes',
            'Mix of some',
            'Native American',
            'Native American/Aborigine',
            'Native American/Indian',
            'Native American/Indigenous People',
            'Oriental',
            'Pacific Islander',
            'Pacific Islander/East Asian',
            'Polynesian/Pacific Islander',
            'South American/Latin American descent',
            'Vietnamese',
            'White',
            'White/American',
            'White/Caucasian',
            'White/European',
            'White/Northern European',
            'White/Other than American',
            'Yellow/Asian/Pacific Islander/Native American',
        ])

    def eye_color(self):
        """Return a random eye-color."""
        return choice([
            'Amber',
            'Blue',
            'Brown',
            'Gray',
            'Green',
            'Hazel',
            'Red and violet',
            'Spectrum',
        ])

    def hair_color(self):
        """Return a random hair-color.

        Source: http://www.obsidianbookshelf.com/html/hair_colorlist.html
        """
        return choice([
            'Blond - Ash',
            'Blond - bronze',
            'Blond - flaxen',
            'Blond - ginger ',
            'Blond - golden',
            'Blond - honey',
            'Blond - platinum',
            'Blond - tawny',
            'Blond - wheaten',
            'Red - auburn',
            'Red - copper',
            'Red - flaming',
            'Red - strawberry blond',
            'Brown - ash',
            'Brown - ginger',
            'Brown - sandy',
            'Brown - chestnut',
            'Brown - russet',
            'Brown - russet',
            'Brown - sable',
            'Brown - sorrel',
            'Black - jet',
            'Black - raven',
            'Black - sooty black',
            'Gray - ash',
            'Gray - iron',
            'Gray - salt and pepper',
            'Gray - silver',
            'Gray - steel',
            'White - pearl',
            'White - snow',
        ])

    def shirt_size(self):
        """Return a random shirt/jacket (torso clothing) size."""
        return choice(['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'])

    def hair_style(self):
        """Return a random hairstyle.

        Source: https://en.wikipedia.org/wiki/List_of_hairstyles
        """
        return choice([
            'Afro',
            'Natural',
            'Asymmetric cut',
            'Beehive',
            'Bettie Page',
            'Big hair',
            'Blowout',
            'Blunt cut',
            'Bob cut',
            'Bouffant',
            'Bowl cut',
            'Braid',
            'Brush cut',
            'Bun',
            'Bunches',
            'Burr',
            'Business-man cut',
            'Butch cut',
            'Buzz cut',
            'Caesar cut',
            'Chignon',
            'Chonmage',
            'Comb over',
            'Conk',
            'Cornrows',
            'Crew cut',
            'Cropped hair',
            'Crown braid',
            'Croydon facelift',
            'Curtained hair',
            'Devilock',
            'Dice Bob',
            'Dido flip',
            'Dreadlocks',
            'Duck\'s ass or D.A.',
            'Eton crop',
            'Emo hair',
            'Fade',
            'Fallera hairdo',
            'Fauxhawk',
            'Feathered hair',
            'Finger wave',
            'Fishtail hair',
            'Flattop',
            'Flipped hair',
            'Fontange',
            'French braid',
            'French twist',
            'Fringe (bangs)',
            'Frosted tips',
            'Full crown',
            'G.I. haircut',
            'Hair extensions',
            'Half crown',
            'Half updo or Half Up, Half Down',
            'Harvard clip',
            'High and tight',
            'Highlights',
            'Hime cut',
            'Historical Christian hairstyles',
            'Hi-top fade',
            'Induction cut',
            'Ivy League',
            'Jewfro',
            'Jheri curl',
            'Layered hair',
            'Liberty spikes',
            'Line up',
            'Long hair',
            'Marcelling',
            'Mod cut',
            'Mohawk',
            'Mop-Top',
            'Mullet',
            'Odango',
            'Oseledets',
            'Pageboy',
            'Part',
            'Payot',
            'Perm',
            'Pigtails',
            'Pixie cut',
            'Pompadour',
            'Ponyhawk',
            'Ponytail',
            'Princeton',
            'Professional cut',
            'Psychobilly Wedge',
            'Queue',
            'Quiff',
            'The Rachel',
            'Rattail',
            'Razor cut',
            'Recon',
            'Regular haircut',
            'Regular taper cut',
            'Ringlets',
            'Shag',
            'Shape-Up',
            'Shingle bob',
            'Short back and sides',
            'Short brush cut',
            'Short hair',
            'Slicked-back',
            'Spiky hair',
            'Standard haircut',
            'Surfer hair',
            'Taper cut',
            'Tail On Back',
            'Tonsure',
            'Undercut',
            'Updo',
            'Waves',
            'Wings',
        ])
