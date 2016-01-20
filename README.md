Simply utility script to get rid of crap like "smart quotes" and the like.  Tested on Python 2.7.10 and (except for i/o, which should be fine) on 3.4.0.

Targets the situation where you've copied-and-pasted in text from, say, Microsoft Word or a webpage into a text editor that saves by default in UTF-8 (like Sublime Text, Atom, etc. seem to do) for programmatic processing, displaying in HTML, etc., and then realize: "oh crap, I've got those horrible smart quotes or something in there, and now I have to figure out a bunch of arcane nonsense about encoding in order to keep them from showing up on my webpage or whev as question marks in black diamonds, or else manually search and replace them."

Manually search and replace no longer, my friend.  

Usage: on command line.  `python cleanpunct.py YOURFILE.txt`

Produces a file cleaned-YOURFILE.txt which replaces "smart quotes," (single and double) "m-dashes," "n-dashes," and curly apostrophes with their ASCII equivalents.  

If you want fancier, add it to the "drek" dictionary yourself (all sane pull requests happily accepted).  Or just use [the demoroniser](https://www.fourmilab.ch/webtools/demoroniser/).  [ASCII damnit](https://github.com/tnajdek/ASCII--Dammit) might also work for you, but it gives me weird replacements on the test text.


Currently, this targets the following unicode monstrosities, as represented internally by python 2: 

    bad double quotes:   \xe2\x80\x9c 
                        \xe2\x80\x9d
    
    bad single quotes:  \xe2\x80\x99
                        \xe2\x80\x98
    
    bad dashes:         \xe2\x80\x94
                        \xe2\x88\x92
                        
As I said, you wanna get rid of any other garbage, submit a pull request.
