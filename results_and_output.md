# Model and settings

multlingual-ngram-10-500-150-0-100

Embedding model: Universal-Sentence-Encoder-Multilingual-Large

ngram_vocab_args = {
    "threshold": 10,
    "min_count": 500
},
umap_args = {
    "n_neighbors": 150,
    "min_dist": 0,
    "n_components": 5,
    "metric": "cosine",
    "random_state": 19991222
},
hbdscan_args = {
    "min_cluster_size": 100,
    "metric": "euclidean",
    "cluster_evaluation_method": "eom"
}

# Evaluation

## Before reduction

**Number of topics: 38**

**Topic sizes**
(array([11514,  9197,  7679,  2232,  1736,  1395,  1323,  1008,   965,
          781,   780,   733,   699,   691,   663,   629,   559,   547,
          533,   493,   490,   457,   448,   427,   398,   353,   318,
          295,   285,   271,   256,   245,   230,   209,   149,   132,
          129,   125], dtype=int64),
 array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
        34, 35, 36, 37], dtype=int64))

**Topic words**

Topic 0
['dark souls' 'soulsborne' 'darksouls' 'bloodborne' 'soulsbourne' 'skyrim'
 'souls' 'oblivion' 'zelda' 'soulslike']

Topic 1
['fps' 'gameplay' 'unplayable' 'vsync' 'laggy' 'framerate' 'playable'
 'ever played' 'lags' 'git gud']

Topic 2
['ever played' 'gameplay' 'git gud' 'game' 'juego' 'jogo' 'playthrough'
 'rpg' 'playable' 'ingame']

Topic 3
['botw' 'meh' 'foe' 'shit' 'ck' 'blah' 'bruh' 'fucking' 'sh' 'heck']

Topic 4
['good' 'gud' 'excellent' 'decent' 'well' 'nice' 'fine' 'great' 'alright'
 'superb']

Topic 5
['multiplayer' 'coop' 'singleplayer' 'matchmaking' 'mmo' 'unplayable'
 'git gud' 'gameplay' 'ingame' 'ever played']

Topic 6
['dying' 'dies' 'dead' 'death' 'died' 'die' 'killed' 'deaths' 'lived'
 'kills']

Topic 7
['elden ring' 'eldenring' 'ring' 'rings' 'elden' 'zelda' 'oblivion'
 'elite' 'leyndell' 'lore']

Topic 8
['ultrawide support' 'ultrawide' 'vsync' 'fps' 'widescreen' 'fullscreen'
 'unplayable' 'framerate' 'ultra' 'unoptimized']

Topic 9
['game' 'juego' 'jogo' 'games' 'gameplay' 'gaming' 'ingame' 'gamers'
 'gamer' 'videogame']

Topic 10
['refunded' 'refunding' 'refund' 'returned' 'returning' 'return'
 'replayable' 'replay' 'replaying' 'respawn']

Topic 11
['good' 'game' 'gud' 'juego' 'excellent' 'jogo' 'gameplay' 'git gud'
 'well' 'decent']

Topic 12
['invisible' 'unplayable' 'glitches' 'enemies' 'glitch' 'enemys' 'enemy'
 'bug' 'bugged' 'anticheat']

Topic 13
['fun' 'enjoyable' 'enjoying' 'enjoyment' 'entertaining' 'enjoys'
 'enjoyed' 'enjoy' 'boring' 'unenjoyable']

Topic 14
['game' 'gameplay' 'juego' 'jogo' 'great' 'amazing' 'superb' 'ever played'
 'magnificent' 'awesome']

Topic 15
['review' 'reviews' 'criticism' 'comments' 'reviewers' 'comment'
 'overrated' 'opinion' 'rating' 'gameplay']

Topic 16
['finger' 'hole' 'fingers' 'try' 'screw' 'tried' 'thumbs' 'trying'
 'attempt' 'attempting']

Topic 17
['difficult' 'hardest' 'easy' 'easily' 'hard' 'easiest' 'tough' 'easier'
 'harder' 'difficulty']

Topic 18
['maidens' 'maiden' 'maidenless' 'nor' 'not' 'не' 'maliketh' 'non' 'no'
 'aren']

Topic 19
['yes' 'yea' 'yeah' 'yep' 'ya' 'sure' 'no' 'non' 'nope' 'nah']

Topic 20
['malenia fuck' 'fuck malenia' 'melina' 'malenia blade' 'malenia'
 'am malenia' 'marika' 'ranni' 'miquella am' 'rennala']

Topic 21
['masterpiece' 'magnificent' 'superb' 'fantastic' 'outstanding' 'crafted'
 'epic' 'brilliant' 'wonderful' 'master']

Topic 22
['greatsword' 'sword' 'katana' 'swords' 'katanas' 'blade' 'knife'
 'samurai' 'malenia blade' 'weapon']

Topic 23
['pvp' 'pve' 'git gud' 'nerfed' 'mmo' 'afk' 'fps' 'darksouls'
 'matchmaking' 'bloodborne']

Topic 24
['elden ring' 'eldenring' 'ring' 'rings' 'elden' 'leyndell' 'circle'
 'zelda' 'ornstein' 'radahn']

Topic 25
['eh' 'se' 'ah' 'oh' 'th' 'af' 'ai' 'tho' 'he' 'er']

Topic 26
['buy' 'purchase' 'buying' 'bought' 'purchasing' 'purchased' 'sell' 'get'
 'selling' 'sold']

Topic 27
['dog' 'dogs' 'bloodhound' 'cat' 'sheep' 'dogshit' 'wolf' 'rats' 'goat'
 'wolves']

Topic 28
['year' 'game' 'juego' 'jogo' 'games' 'years' 'ever played' 'gaming'
 'gameplay' 'ingame']

Topic 29
['hug' 'arms' 'woman' 'lady' 'women' 'touched' 'girl' 'hand' 'hands'
 'beloved']

Topic 30
['goty' 'gael' 'gank' 'wary' 'godskin' 'godrick' 'wonky' 'grrm' 'botw'
 'dull']

Topic 31
['miyazaki' 'waifu' 'samurai' 'japanese' 'anime' 'zelda' 'nioh' 'melina'
 'miquella am' 'janky']

Topic 32
['hole' 'finger' 'fingers' 'thumbs' 'screw' 'stick' 'jaw' 'handle' 'dick'
 'hands']

Topic 33
['dog' 'dogs' 'cat' 'bloodhound' 'human' 'rats' 'creature' 'tier'
 'creatures' 'sheep']

Topic 34
['mid' 'middle' 'medium' 'half' 'halfway' 'average' 'media' 'semi'
 'mediocre' 'mean']

Topic 35
['night' 'fort' 'dark' 'strong' 'stronger' 'moon' 'nightmare' 'strongest'
 'strength' 'forces']

Topic 36
['right' 'correctly' 'left' 'wrong' 'fair' 'properly' 'correct' 'proper'
 'unfair' 'downright']

Topic 37
['clinton' 'bill' 'pope' 'dollars' 'dollar' 'orthodox' 'grace' 'rabbi'
 'vote' 'praise']

---

## After reduction

**Number of topics after reduction: 20**

**Topic words**
Topic 0
['dark souls' 'soulsborne' 'darksouls' 'bloodborne' 'soulsbourne' 'skyrim'
 'souls' 'oblivion' 'zelda' 'git gud']

Topic 1
['fps' 'gameplay' 'unplayable' 'vsync' 'laggy' 'framerate' 'lags'
 'playable' 'lagging' 'performance issues']

Topic 2
['ever played' 'gameplay' 'git gud' 'game' 'juego' 'jogo' 'playthrough'
 'rpg' 'playable' 'ingame']

Topic 3
['meh' 'blah' 'botw' 'eh' 'heck' 'damn' 'bruh' 'fucking' 'foe' 'shit']

Topic 4
['malenia fuck' 'fuck malenia' 'malenia blade' 'meh' 'greatsword' 'lmao'
 'bruh' 'goddamn' 'btw' 'fuck']

Topic 5
['good' 'gud' 'excellent' 'decent' 'nice' 'well' 'fine' 'great' 'superb'
 'awesome']

Topic 6
['multiplayer' 'mmo' 'git gud' 'matchmaking' 'singleplayer' 'unplayable'
 'coop' 'gameplay' 'pve' 'ever played']

Topic 7
['elden ring' 'eldenring' 'ring' 'rings' 'elden' 'zelda' 'oblivion'
 'leyndell' 'lore' 'elite']

Topic 8
['dying' 'dies' 'dead' 'died' 'death' 'killed' 'crashed' 'die' 'rip'
 'kills']

Topic 9
['refunded' 'refund' 'refunding' 'replayable' 'unplayable' 'returned'
 'replaying' 'replay' 'returning' 'respawn']

Topic 10
['gameplay' 'game' 'ever played' 'juego' 'jogo' 'superb' 'great'
 'excellent' 'amazing' 'magnificent']

Topic 11
['unplayable' 'glitches' 'invisible' 'glitch' 'bugged' 'enemies' 'git gud'
 'bug' 'enemys' 'anti cheat']

Topic 12
['game' 'juego' 'jogo' 'games' 'gameplay' 'gaming' 'ingame' 'ever played'
 'playable' 'played']

Topic 13
['ultrawide support' 'vsync' 'ultrawide' 'fps' 'widescreen' 'fullscreen'
 'framerate' 'unplayable' 'ultra' 'unoptimized']

Topic 14
['review' 'reviews' 'criticism' 'gameplay' 'overrated' 'overhyped'
 'reviewers' 'comments' 'git gud' 'comment']

Topic 15
['maidenless' 'nor' 'maiden' 'not' 'maidens' 'не' 'arent' 'non' 'havent'
 'unable']

Topic 16
['git gud' 'gud' 'game' 'good' 'juego' 'gameplay' 'jogo' 'excellent'
 'decent' 'playable']

Topic 17
['fun' 'enjoyable' 'enjoying' 'boring' 'enjoyment' 'entertaining' 'enjoys'
 'enjoyed' 'enjoy' 'unenjoyable']

Topic 18
['finger' 'hole' 'fingers' 'try' 'screw' 'thumbs' 'tried' 'trying' 'stick'
 'attempt']

Topic 19
['difficult' 'hardest' 'hard' 'tough' 'harder' 'difficulty' 'easy'
 'easily' 'easiest' 'easier']

---

## Comparing over classes

### Representative words

Comparing original topic vector vs re-calculated negative and positive reviews. For most topics, there are few to no differences in the top 5 representative words or the order of their occurence. For other topics such as topics 5 and 11, there are massive differences in the most representative words. In still other topics, such as topic 8, only one of the re-calculated topics have changed.

Topic: 0
Original: ['dark souls' 'soulsborne' 'darksouls' 'bloodborne' 'soulsbourne']
Negative: ['dark souls' 'soulsborne' 'darksouls' 'bloodborne' 'soulsbourne']
Positive: ['dark souls' 'soulsborne' 'darksouls' 'bloodborne' 'soulsbourne']

Topic: 1
Original: ['fps' 'gameplay' 'unplayable' 'vsync' 'laggy']
Negative: ['fps' 'gameplay' 'unplayable' 'vsync' 'laggy']
Positive: ['fps' 'gameplay' 'framerate' 'performance issues' 'vsync']

Topic: 2
Original: ['ever played' 'gameplay' 'git gud' 'game' 'juego']
Negative: ['gameplay' 'git gud' 'ever played' 'game' 'juego']
Positive: ['ever played' 'gameplay' 'game' 'juego' 'jogo']

Topic: 3
Original: ['meh' 'blah' 'botw' 'eh' 'heck']
Negative: ['meh' 'shit' 'blah' 'fucking' 'botw']
Positive: ['meh' 'blah' 'eh' 'heck' 'botw']

Topic: 4
Original: ['malenia fuck' 'fuck malenia' 'malenia blade' 'meh' 'greatsword']
Negative: ['bruh' 'lmao' 'malenia fuck' 'goddamn' 'fuck']
Positive: ['malenia fuck' 'meh' 'fuck malenia' 'greatsword' 'lmao']

Topic: 5
Original: ['good' 'gud' 'excellent' 'decent' 'nice']
Negative: ['bad' 'terrible' 'badly' 'awful' 'shitty']
Positive: ['good' 'excellent' 'gud' 'nice' 'decent']

Topic: 6
Original: ['multiplayer' 'mmo' 'git gud' 'matchmaking' 'singleplayer']
Negative: ['multiplayer' 'mmo' 'git gud' 'matchmaking' 'unplayable']
Positive: ['multiplayer' 'mmo' 'git gud' 'singleplayer' 'gameplay']

Topic: 7
Original: ['elden ring' 'eldenring' 'ring' 'rings' 'elden']
Negative: ['elden ring' 'eldenring' 'ring' 'elden' 'rings']
Positive: ['elden ring' 'eldenring' 'ring' 'rings' 'elden']

Topic: 8
Original: ['dying' 'dies' 'dead' 'died' 'death']
Negative: ['crashed' 'crashes' 'crashing' 'crash' 'ruined']
Positive: ['dying' 'dies' 'dead' 'died' 'death']

Topic: 9
Original: ['refunded' 'refund' 'refunding' 'replayable' 'unplayable']
Negative: ['refunded' 'refunding' 'refund' 'unplayable' 'replayable']
Positive: ['refunded' 'ever played' 'refunding' 'refund' 'dlc']

Topic: 10
Original: ['gameplay' 'game' 'ever played' 'juego' 'jogo']
Negative: ['gameplay' 'ever played' 'git gud' 'game' 'playable']
Positive: ['ever played' 'gameplay' 'game' 'best' 'greatest']

Topic: 11
Original: ['unplayable' 'glitches' 'invisible' 'glitch' 'bugged']
Negative: ['unplayable' 'glitches' 'glitch' 'bugged' 'git gud']
Positive: ['git gud' 'boss fights' 'melee' 'bossfight' 'kills']

Topic: 12
Original: ['game' 'juego' 'jogo' 'games' 'gameplay']
Negative: ['game' 'juego' 'jogo' 'gameplay' 'games']
Positive: ['game' 'juego' 'jogo' 'games' 'gameplay']

Topic: 13
Original: ['ultrawide support' 'vsync' 'ultrawide' 'fps' 'widescreen']
Negative: ['ultrawide support' 'vsync' 'ultrawide' 'fps' 'widescreen']
Positive: ['ultrawide support' 'vsync' 'fps' 'ultrawide' 'framerate']

Topic: 14
Original: ['review' 'reviews' 'criticism' 'gameplay' 'overrated']
Negative: ['reviews' 'review' 'gameplay' 'criticism' 'git gud']
Positive: ['review' 'reviews' 'criticism' 'gameplay' 'reviewers']

Topic: 15
Original: ['maidenless' 'nor' 'maiden' 'not' 'maidens']
Negative: ['not' 'nor' 'не' 'non' 'no']
Positive: ['maidenless' 'nor' 'maiden' 'maidens' 'aimlessly']

Topic: 16
Original: ['git gud' 'gud' 'game' 'good' 'juego']
Negative: ['git gud' 'bad' 'game' 'gameplay' 'badly']
Positive: ['git gud' 'gud' 'good' 'game' 'juego']

Topic: 17
Original: ['fun' 'enjoyable' 'enjoying' 'boring' 'enjoyment']
Negative: ['boring' 'bored' 'unenjoyable' 'fun' 'enjoyable']
Positive: ['fun' 'enjoyable' 'enjoying' 'enjoyment' 'enjoys']

Topic: 18
Original: ['finger' 'hole' 'fingers' 'try' 'screw']
Negative: ['finger' 'fingers' 'hole' 'thumbs' 'screw']
Positive: ['finger' 'hole' 'fingers' 'try' 'screw']

Topic: 19
Original: ['difficult' 'hardest' 'hard' 'tough' 'harder']
Negative: ['difficult' 'hardest' 'hard' 'tough' 'difficulty']
Positive: ['difficult' 'hardest' 'hard' 'tough' 'harder']



---


### Representative words: Differences

When it comes to taking the differences between topic vectors, subtracting the positive or negative vectors seems to have a profound effect on the sentiment of the most representative words. Topics 2 and 6 are very clear examples of this. It would appear that subtracting the negative from the positive or vice versa makes for more drastic changes in sentiment (compared to subtracting from the original topic vector).

Topic: 0
Original:          ['dark souls' 'soulsborne' 'darksouls' 'bloodborne' 'soulsbourne']
Original-Positive: ['negatives' 'sucks' 'complaints' 'worst' 'shitty']
Original-Negative: ['soulsborne' 'dark souls' 'soulsbourne' 'souls' 'darksouls']
Negative-Positive: ['negatives' 'complaints' 'worst' 'sucks' 'negative']
Positive-Negative: ['soulsborne' 'dark souls' 'soulsbourne' 'souls' 'darksouls']

Topic: 1
Original:          ['fps' 'gameplay' 'unplayable' 'vsync' 'laggy']
Original-Positive: ['unplayable' 'couldnt' 'gamepad' 'cant' 'cannot']
Original-Negative: ['respawn' 'screwed' 'recover' 'reset' 'replay']
Negative-Positive: ['pc port' 'gamepad' 'couldnt' 'unplayable' 'cant']
Positive-Negative: ['performance' 'phenomenal' 'outstanding' 'spectacular'
 'performance issues']

Topic: 2
Original:          ['ever played' 'gameplay' 'git gud' 'game' 'juego']
Original-Positive: ['worst' 'shitty' 'bad' 'worse' 'sucks']
Original-Negative: ['greatest' 'best' 'magnificent' 'superb' 'amazing']
Negative-Positive: ['shitty' 'ruin' 'sucks' 'ruins' 'ruining']
Positive-Negative: ['greatest' 'magnificent' 'amazing' 'amazingly' 'incredible']

Topic: 3
Original:          ['meh' 'blah' 'botw' 'eh' 'heck']
Original-Positive: ['rubbish' 'garbage' 'shitty' 'trash' 'awful']
Original-Negative: ['sure' 'yeah' 'yes' 'yea' 'yep']
Negative-Positive: ['garbage' 'rubbish' 'trash' 'shitty' 'mess']
Positive-Negative: ['sure' 'yeah' 'yes' 'yea' 'yep']

Topic: 4
Original:          ['malenia fuck' 'fuck malenia' 'malenia blade' 'meh' 'greatsword']
Original-Positive: ['malenia fuck' 'malenia blade' 'fuck malenia' 'melina' 'unplayable']
Original-Negative: ['melina' 'miyazaki' 'miquella am' 'malenia blade' 'hug']
Negative-Positive: ['garbage' 'unplayable' 'shitty' 'rubbish' 'lacks']
Positive-Negative: ['hug' 'miquella am' 'precious' 'receive' 'grace']

Topic: 5
Original:          ['good' 'gud' 'excellent' 'decent' 'nice']
Original-Positive: ['bad' 'worse' 'worst' 'badly' 'terrible']
Original-Negative: ['nice' 'sure' 'great' 'excellent' 'awesome']
Negative-Positive: ['worst' 'worse' 'ruin' 'ruining' 'ruins']
Positive-Negative: ['nice' 'awesome' 'sure' 'enjoyed' 'great']

Topic: 6
Original:          ['multiplayer' 'mmo' 'git gud' 'matchmaking' 'singleplayer']
Original-Positive: ['disconnects' 'disconnections' 'disconnecting' 'lag' 'lags']
Original-Negative: ['pvp' 'pve' 'beast' 'superb' 'exceptional']
Negative-Positive: ['disconnections' 'disconnects' 'disconnecting' 'lags' 'lag']
Positive-Negative: ['magnificent' 'amazingly' 'amazing' 'breathtaking' 'incredible']

Topic: 7
Original:          ['elden ring' 'eldenring' 'ring' 'rings' 'elden']
Original-Positive: ['clinton' 'stuttering' 'retarded' 'mess' 'buggy']
Original-Negative: ['rings' 'ring' 'elden ring' 'eldenring' 'award']
Negative-Positive: ['unplayable' 'laggy' 'frustrating' 'horribly' 'frustrated']
Positive-Negative: ['elden ring' 'rings' 'ring' 'eldenring' 'award']

Topic: 8
Original:          ['dying' 'dies' 'dead' 'died' 'death']
Original-Positive: ['crashes' 'inconsistent' 'unplayable' 'crash' 'laggy']
Original-Negative: ['death' 'dies' 'die' 'living' 'dying']
Negative-Positive: ['laggy' 'crashes' 'performance issues' 'buggy' 'lagging']
Positive-Negative: ['death' 'living' 'die' 'dies' 'lived']

Topic: 9
Original:          ['refunded' 'refund' 'refunding' 'replayable' 'unplayable']
Original-Positive: ['refund' 'refunding' 'refunded' 'feedback' 'returning']
Original-Negative: ['refund' 'refunding' 'refunded' 'returned' 'return']
Negative-Positive: ['performance issues' 'refund' 'unresponsive' 'unplayable' 'refunding']
Positive-Negative: ['buy' 'bought' 'become' 'purchase' 'buying']

Topic: 10
Original:          ['gameplay' 'game' 'ever played' 'juego' 'jogo']
Original-Positive: ['interesting' 'phenomenal' 'awesome' 'stunning' 'fascinating']
Original-Negative: ['wonderful' 'awesome' 'amazing' 'magnificent' 'fantastic']
Negative-Positive: ['frustrated' 'frustrating' 'worse' 'terrible' 'underwhelming']
Positive-Negative: ['favorite' 'best' 'favourite' 'greatest' 'forever']

Topic: 11
Original:          ['unplayable' 'glitches' 'invisible' 'glitch' 'bugged']
Original-Positive: ['invisible' 'visible' 'unplayable' 'unoptimized' 'performance issues']
Original-Negative: ['invisible' 'visible' 'vision' 'sight' 'hidden']
Negative-Positive: ['unplayable' 'performance issues' 'unoptimized' 'laggy' 'optimised']
Positive-Negative: ['stab' 'killing' 'kill' 'aggro' 'hunt']

Topic: 12
Original:          ['game' 'juego' 'jogo' 'games' 'gameplay']
Original-Positive: ['shitty' 'garbage' 'crap' 'suck' 'sucks']
Original-Negative: ['year' 'years' 'decade' 'decades' 'term']
Negative-Positive: ['shitty' 'sucks' 'garbage' 'suck' 'crap']
Positive-Negative: ['year' 'years' 'decade' 'decades' 'present']

Topic: 13
Original:          ['ultrawide support' 'vsync' 'ultrawide' 'fps' 'widescreen']
Original-Positive: ['nope' 'unacceptable' 'no' 'non' 'ultrawide support']
Original-Negative: ['ultrawide support' 'ultrawide' 'widescreen' 'wide' 'expansive']
Negative-Positive: ['nope' 'unacceptable' 'no' 'disabled' 'non']
Positive-Negative: ['geforce' 'gpu' 'shader' 'nvidia' 'graphics']

Topic: 14
Original:          ['review' 'reviews' 'criticism' 'gameplay' 'overrated']
Original-Positive: ['dislike' 'sucks' 'shitty' 'negatives' 'negative']
Original-Negative: ['review' 'rated' 'praise' 'consider' 'deserves']
Negative-Positive: ['unplayable' 'laggy' 'fps' 'disabled' 'vsync']
Positive-Negative: ['eldenring' 'consider' 'considering' 'praise' 'elden ring']

Topic: 15
Original:          ['maidenless' 'nor' 'maiden' 'not' 'maidens']
Original-Positive: ['no' 'nope' 'nah' 'non' 'не']
Original-Negative: ['maidens' 'maiden' 'maliketh' 'maidenless' 'mimic']
Negative-Positive: ['not' 'не' 'no' 'non' 'doesnt']
Positive-Negative: ['maidens' 'maiden' 'maliketh' 'maidenless' 'mimic']

Topic: 16
Original:          ['git gud' 'gud' 'game' 'good' 'juego']
Original-Positive: ['worst' 'worse' 'ruins' 'disaster' 'failure']
Original-Negative: ['enjoyed' 'enjoys' 'enjoy' 'enjoying' 'enjoyment']
Negative-Positive: ['worst' 'ruins' 'ruin' 'disaster' 'worse']
Positive-Negative: ['enjoyed' 'enjoys' 'enjoy' 'enjoying' 'enjoyment']

Topic: 17
Original:          ['fun' 'enjoyable' 'enjoying' 'boring' 'enjoyment']
Original-Positive: ['boring' 'uninteresting' 'unnecessarily' 'unnecessary' 'lack']
Original-Negative: ['enjoys' 'joy' 'enjoying' 'enjoyment' 'pleasure']
Negative-Positive: ['lack' 'lacks' 'unnecessary' 'unbalanced' 'unnecessarily']
Positive-Negative: ['joy' 'enjoys' 'enjoying' 'enjoyment' 'happy']

Topic: 18
Original:          ['finger' 'hole' 'fingers' 'try' 'screw']
Original-Positive: ['aimlessly' 'arent' 'needlessly' 'barely' 'hardly']
Original-Negative: ['seek' 'find' 'finding' 'search' 'discover']
Negative-Positive: ['cannot' 'couldnt' 'cant' 'couldn' 'hardly']
Positive-Negative: ['seek' 'find' 'finding' 'search' 'exploring']

Topic: 19
Original:          ['difficult' 'hardest' 'hard' 'tough' 'harder']
Original-Positive: ['lacking' 'lack' 'lacks' 'unnecessarily' 'missing']
Original-Negative: ['solely' 'simply' 'merely' 'simple' 'just']
Negative-Positive: ['lacks' 'lack' 'lacking' 'unnecessary' 'missing']
Positive-Negative: ['strongest' 'best' 'rewarding' 'enjoyable' 'accomplishment']






