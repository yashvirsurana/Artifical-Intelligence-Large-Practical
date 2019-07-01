#####################################################
# README FOR CAES-READER with BURDEN of PROOF 
# Copyright (C) 2015, Yashvir Surana, s1368177
# Author: Yashvir Surana <yashvirsurana@gmail.com>
# Reader/BOP Extension for: caes.py
#####################################################

1. Input Syntax.

The input syntax for the caes reader and BOP implementation is similar to JSON but with added comments functionality. 
For introduction to JSON, please visit: https://en.wikipedia.org/wiki/JSON#Example
Although JSON objects do not support comments, we have compensated for this by including a regex comment remover. 
This removes the comments and then loads the object as JSON (Java-script Object Notation). 
The first key "args" is not to be edited. This contains a list of all arguments as objects for a particular case.
All keys and set of values must be enclosed with quotes. 
Each argument in the list of arguments has five entities: 
1.a) PropLiterals:
	Input as a list of propLiterals enclosed with quotes. eg - "propLiterals":"murder,intent,kill"
1.b) arg: 
	Input in the form of- conclusion|premise1,premise2 (in this, conclusion and premises are separated by a '|' and premises by ',')
	Input in the form of- conclusion|premise&exception (in this, conclusion and premise and exception are separated by '|' followed by premise and exception being separated by '&'. In case of multiple premises and exceptions, same pattern follows: i.e conclusion|premise1,premise2&exception1,exception2 in the order. 
	NOTE: Arguments must be strictly inputted in this syntax, otherwise we will be unsuccesful.
1.c) audienceAssumptions: 
	Input in the form of a list of assumptions separated by a ',' and enclosed in quotes. For eg. "witness2,-unreliable2"
1.d) weight:
	Input in the form of a float enclosed in quotes. eg. "0.8"
1.e) proofStandard: 
	Input as a string enclosed in quotes.
	Leaving blank implies that lowest proofstandard is used. i.e. "scintilla"
Important Syntax Notes:
	Comments: Single line comments can be entered by typing // followed by comment. For eg. //Comment1234PythonIsGood
	Comments: Multiple line comments can be enclosed within /* and */ 
	File: file must be saved with extension .json in any text editor.

EXAMPLE OF A COMPLETE CASE INPUT with three arguments.
---------------------------------
{
"args":[
	{"propLiterals":"murder,intent,kill",
	"arg":"murder|intent,kill",
	"audienceAssumptions":"kill", //COMMENT
	"weight":"0.8", /* more comments added */
	"proofStandard":"beyond_reasonable_doubt"
	},
	{"propLiterals":"intent,witness1,unreliable1",
	"arg":"intent|witness1&unreliable1",
	"audienceAssumptions":"witness1",
	"weight":"0.3",
	"proofStandard":"scintilla"
	},
	{"propLiterals":"-intent,witness2,unreliable2",
	"arg":"-intent|witness2&unreliable2",
	"audienceAssumptions":"witness2,-unreliable2",
	"weight":"0.8",
	"proofStandard":"scintilla"
	}
	]
}
-----------------------------------

2. How to make it work?

To run the program, ensure the following files are in the same directory:
caes.py
reader.py
unitTests.py
murder_case.json
bankRob_case.json

To start, run CAES and BOP on cases individually...
Type python3.4 in the terminal after navigating to the directory
>>> from reader import Read
>>> c=Read()
>>> c.readFile('bankRob_case.json','bankRob') where bankRob_case.json is our input file, and bankRob is what we're trying to evaluate CAES and BOP for.











