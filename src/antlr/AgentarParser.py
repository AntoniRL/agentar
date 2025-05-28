# Generated from /home/toni/mgr/agentar/grammar/Agentar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,64,430,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,4,3,4,88,8,4,1,4,3,4,91,8,4,1,4,3,4,94,8,4,1,4,5,4,
        97,8,4,10,4,12,4,100,9,4,1,4,5,4,103,8,4,10,4,12,4,106,9,4,1,5,1,
        5,1,5,5,5,111,8,5,10,5,12,5,114,9,5,1,5,1,5,1,6,1,6,1,6,5,6,121,
        8,6,10,6,12,6,124,9,6,1,6,1,6,1,7,1,7,1,7,5,7,131,8,7,10,7,12,7,
        134,9,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,142,8,8,10,8,12,8,145,9,8,1,
        8,1,8,1,9,1,9,1,9,5,9,152,8,9,10,9,12,9,155,9,9,1,9,1,9,1,9,1,9,
        5,9,161,8,9,10,9,12,9,164,9,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,172,
        8,10,1,10,1,10,1,10,1,10,1,10,5,10,179,8,10,10,10,12,10,182,9,10,
        1,10,1,10,1,11,1,11,1,11,5,11,189,8,11,10,11,12,11,192,9,11,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,5,13,201,8,13,10,13,12,13,204,9,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,217,
        8,14,3,14,219,8,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,5,15,232,8,15,10,15,12,15,235,9,15,1,15,1,15,3,15,239,
        8,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,5,16,249,8,16,10,16,
        12,16,252,9,16,3,16,254,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,18,5,18,267,8,18,10,18,12,18,270,9,18,1,18,1,18,
        1,18,1,19,1,19,1,19,1,19,3,19,279,8,19,1,19,1,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        3,20,299,8,20,1,21,1,21,1,21,1,21,3,21,305,8,21,1,21,1,21,5,21,309,
        8,21,10,21,12,21,312,9,21,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,1,23,4,23,325,8,23,11,23,12,23,326,1,23,1,23,1,23,4,23,
        332,8,23,11,23,12,23,333,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,3,23,347,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,5,23,387,8,23,10,23,12,23,390,9,23,1,24,
        1,24,1,24,1,24,5,24,396,8,24,10,24,12,24,399,9,24,3,24,401,8,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,413,8,25,
        10,25,12,25,416,9,25,3,25,418,8,25,1,25,1,25,1,26,1,26,1,26,1,26,
        3,26,426,8,26,1,27,1,27,1,27,0,1,46,28,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,0,4,1,0,15,
        22,1,0,50,51,1,0,48,49,1,0,27,31,467,0,61,1,0,0,0,2,72,1,0,0,0,4,
        74,1,0,0,0,6,80,1,0,0,0,8,87,1,0,0,0,10,107,1,0,0,0,12,117,1,0,0,
        0,14,127,1,0,0,0,16,137,1,0,0,0,18,148,1,0,0,0,20,167,1,0,0,0,22,
        185,1,0,0,0,24,193,1,0,0,0,26,196,1,0,0,0,28,207,1,0,0,0,30,223,
        1,0,0,0,32,243,1,0,0,0,34,257,1,0,0,0,36,261,1,0,0,0,38,274,1,0,
        0,0,40,298,1,0,0,0,42,300,1,0,0,0,44,316,1,0,0,0,46,346,1,0,0,0,
        48,391,1,0,0,0,50,404,1,0,0,0,52,425,1,0,0,0,54,427,1,0,0,0,56,60,
        3,4,2,0,57,60,3,6,3,0,58,60,3,26,13,0,59,56,1,0,0,0,59,57,1,0,0,
        0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,
        1,0,0,0,63,61,1,0,0,0,64,65,5,0,0,1,65,1,1,0,0,0,66,73,3,36,18,0,
        67,73,3,38,19,0,68,73,3,40,20,0,69,73,3,28,14,0,70,73,3,30,15,0,
        71,73,3,42,21,0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,72,69,
        1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,3,1,0,0,0,74,75,5,1,0,0,75,
        76,5,2,0,0,76,77,5,42,0,0,77,78,3,8,4,0,78,79,5,43,0,0,79,5,1,0,
        0,0,80,81,5,1,0,0,81,82,5,37,0,0,82,83,5,42,0,0,83,84,3,8,4,0,84,
        85,5,43,0,0,85,7,1,0,0,0,86,88,3,10,5,0,87,86,1,0,0,0,87,88,1,0,
        0,0,88,90,1,0,0,0,89,91,3,12,6,0,90,89,1,0,0,0,90,91,1,0,0,0,91,
        93,1,0,0,0,92,94,3,14,7,0,93,92,1,0,0,0,93,94,1,0,0,0,94,98,1,0,
        0,0,95,97,3,16,8,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,
        99,1,0,0,0,99,104,1,0,0,0,100,98,1,0,0,0,101,103,3,20,10,0,102,101,
        1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,9,1,
        0,0,0,106,104,1,0,0,0,107,108,5,3,0,0,108,112,5,42,0,0,109,111,3,
        38,19,0,110,109,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,
        1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,116,5,43,0,0,116,11,
        1,0,0,0,117,118,5,4,0,0,118,122,5,42,0,0,119,121,3,2,1,0,120,119,
        1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,
        1,0,0,0,124,122,1,0,0,0,125,126,5,43,0,0,126,13,1,0,0,0,127,128,
        5,5,0,0,128,132,5,42,0,0,129,131,3,2,1,0,130,129,1,0,0,0,131,134,
        1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,132,
        1,0,0,0,135,136,5,43,0,0,136,15,1,0,0,0,137,138,5,6,0,0,138,139,
        5,37,0,0,139,143,5,42,0,0,140,142,3,18,9,0,141,140,1,0,0,0,142,145,
        1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,143,
        1,0,0,0,146,147,5,43,0,0,147,17,1,0,0,0,148,149,5,7,0,0,149,153,
        5,38,0,0,150,152,3,46,23,0,151,150,1,0,0,0,152,155,1,0,0,0,153,151,
        1,0,0,0,153,154,1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,157,
        5,39,0,0,157,158,5,8,0,0,158,162,5,42,0,0,159,161,3,2,1,0,160,159,
        1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,165,
        1,0,0,0,164,162,1,0,0,0,165,166,5,43,0,0,166,19,1,0,0,0,167,168,
        5,9,0,0,168,169,5,37,0,0,169,171,5,38,0,0,170,172,3,22,11,0,171,
        170,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,39,0,0,174,
        175,5,45,0,0,175,176,3,44,22,0,176,180,5,42,0,0,177,179,3,2,1,0,
        178,177,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,
        181,183,1,0,0,0,182,180,1,0,0,0,183,184,5,43,0,0,184,21,1,0,0,0,
        185,190,3,24,12,0,186,187,5,44,0,0,187,189,3,24,12,0,188,186,1,0,
        0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,23,1,0,0,
        0,192,190,1,0,0,0,193,194,3,44,22,0,194,195,5,37,0,0,195,25,1,0,
        0,0,196,197,5,24,0,0,197,198,5,37,0,0,198,202,5,42,0,0,199,201,3,
        38,19,0,200,199,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,
        1,0,0,0,203,205,1,0,0,0,204,202,1,0,0,0,205,206,5,43,0,0,206,27,
        1,0,0,0,207,208,5,10,0,0,208,209,5,38,0,0,209,210,3,46,23,0,210,
        211,5,44,0,0,211,218,3,46,23,0,212,216,5,44,0,0,213,214,5,11,0,0,
        214,217,3,54,27,0,215,217,3,54,27,0,216,213,1,0,0,0,216,215,1,0,
        0,0,217,219,1,0,0,0,218,212,1,0,0,0,218,219,1,0,0,0,219,220,1,0,
        0,0,220,221,5,39,0,0,221,222,5,46,0,0,222,29,1,0,0,0,223,224,5,12,
        0,0,224,225,5,38,0,0,225,238,5,37,0,0,226,227,5,44,0,0,227,228,5,
        40,0,0,228,233,3,46,23,0,229,230,5,44,0,0,230,232,3,46,23,0,231,
        229,1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,
        236,1,0,0,0,235,233,1,0,0,0,236,237,5,41,0,0,237,239,1,0,0,0,238,
        226,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,5,39,0,0,241,
        242,5,46,0,0,242,31,1,0,0,0,243,244,5,37,0,0,244,253,5,38,0,0,245,
        250,3,34,17,0,246,247,5,44,0,0,247,249,3,34,17,0,248,246,1,0,0,0,
        249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,254,1,0,0,0,
        252,250,1,0,0,0,253,245,1,0,0,0,253,254,1,0,0,0,254,255,1,0,0,0,
        255,256,5,39,0,0,256,33,1,0,0,0,257,258,5,37,0,0,258,259,5,47,0,
        0,259,260,3,46,23,0,260,35,1,0,0,0,261,262,5,13,0,0,262,263,5,38,
        0,0,263,268,3,46,23,0,264,265,5,44,0,0,265,267,3,46,23,0,266,264,
        1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,271,
        1,0,0,0,270,268,1,0,0,0,271,272,5,39,0,0,272,273,5,46,0,0,273,37,
        1,0,0,0,274,275,3,44,22,0,275,278,5,37,0,0,276,277,5,47,0,0,277,
        279,3,46,23,0,278,276,1,0,0,0,278,279,1,0,0,0,279,280,1,0,0,0,280,
        281,5,46,0,0,281,39,1,0,0,0,282,283,5,37,0,0,283,284,5,47,0,0,284,
        285,3,46,23,0,285,286,5,46,0,0,286,299,1,0,0,0,287,288,5,37,0,0,
        288,289,5,40,0,0,289,290,3,46,23,0,290,291,5,41,0,0,291,292,5,47,
        0,0,292,293,3,46,23,0,293,294,5,46,0,0,294,299,1,0,0,0,295,296,5,
        37,0,0,296,297,5,47,0,0,297,299,3,30,15,0,298,282,1,0,0,0,298,287,
        1,0,0,0,298,295,1,0,0,0,299,41,1,0,0,0,300,301,5,14,0,0,301,302,
        5,37,0,0,302,304,5,38,0,0,303,305,3,46,23,0,304,303,1,0,0,0,304,
        305,1,0,0,0,305,310,1,0,0,0,306,307,5,44,0,0,307,309,3,46,23,0,308,
        306,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,
        313,1,0,0,0,312,310,1,0,0,0,313,314,5,39,0,0,314,315,5,46,0,0,315,
        43,1,0,0,0,316,317,7,0,0,0,317,45,1,0,0,0,318,319,6,23,-1,0,319,
        320,5,58,0,0,320,347,3,46,23,23,321,324,5,25,0,0,322,323,5,23,0,
        0,323,325,5,37,0,0,324,322,1,0,0,0,325,326,1,0,0,0,326,324,1,0,0,
        0,326,327,1,0,0,0,327,347,1,0,0,0,328,331,5,26,0,0,329,330,5,23,
        0,0,330,332,5,37,0,0,331,329,1,0,0,0,332,333,1,0,0,0,333,331,1,0,
        0,0,333,334,1,0,0,0,334,347,1,0,0,0,335,347,3,48,24,0,336,347,3,
        50,25,0,337,347,3,52,26,0,338,347,5,37,0,0,339,340,5,38,0,0,340,
        341,3,46,23,0,341,342,5,39,0,0,342,347,1,0,0,0,343,347,5,34,0,0,
        344,347,3,32,16,0,345,347,3,54,27,0,346,318,1,0,0,0,346,321,1,0,
        0,0,346,328,1,0,0,0,346,335,1,0,0,0,346,336,1,0,0,0,346,337,1,0,
        0,0,346,338,1,0,0,0,346,339,1,0,0,0,346,343,1,0,0,0,346,344,1,0,
        0,0,346,345,1,0,0,0,347,388,1,0,0,0,348,349,10,22,0,0,349,350,5,
        59,0,0,350,387,3,46,23,23,351,352,10,21,0,0,352,353,5,60,0,0,353,
        387,3,46,23,22,354,355,10,20,0,0,355,356,5,61,0,0,356,387,3,46,23,
        21,357,358,10,19,0,0,358,359,7,1,0,0,359,387,3,46,23,20,360,361,
        10,18,0,0,361,362,7,2,0,0,362,387,3,46,23,19,363,364,10,17,0,0,364,
        365,5,52,0,0,365,387,3,46,23,18,366,367,10,16,0,0,367,368,5,53,0,
        0,368,387,3,46,23,17,369,370,10,15,0,0,370,371,5,54,0,0,371,387,
        3,46,23,16,372,373,10,14,0,0,373,374,5,55,0,0,374,387,3,46,23,15,
        375,376,10,13,0,0,376,377,5,56,0,0,377,387,3,46,23,14,378,379,10,
        12,0,0,379,380,5,57,0,0,380,387,3,46,23,13,381,382,10,4,0,0,382,
        383,5,40,0,0,383,384,3,46,23,0,384,385,5,41,0,0,385,387,1,0,0,0,
        386,348,1,0,0,0,386,351,1,0,0,0,386,354,1,0,0,0,386,357,1,0,0,0,
        386,360,1,0,0,0,386,363,1,0,0,0,386,366,1,0,0,0,386,369,1,0,0,0,
        386,372,1,0,0,0,386,375,1,0,0,0,386,378,1,0,0,0,386,381,1,0,0,0,
        387,390,1,0,0,0,388,386,1,0,0,0,388,389,1,0,0,0,389,47,1,0,0,0,390,
        388,1,0,0,0,391,400,5,40,0,0,392,397,3,46,23,0,393,394,5,44,0,0,
        394,396,3,46,23,0,395,393,1,0,0,0,396,399,1,0,0,0,397,395,1,0,0,
        0,397,398,1,0,0,0,398,401,1,0,0,0,399,397,1,0,0,0,400,392,1,0,0,
        0,400,401,1,0,0,0,401,402,1,0,0,0,402,403,5,41,0,0,403,49,1,0,0,
        0,404,417,5,42,0,0,405,406,5,37,0,0,406,407,5,45,0,0,407,414,3,46,
        23,0,408,409,5,44,0,0,409,410,5,37,0,0,410,411,5,45,0,0,411,413,
        3,46,23,0,412,408,1,0,0,0,413,416,1,0,0,0,414,412,1,0,0,0,414,415,
        1,0,0,0,415,418,1,0,0,0,416,414,1,0,0,0,417,405,1,0,0,0,417,418,
        1,0,0,0,418,419,1,0,0,0,419,420,5,43,0,0,420,51,1,0,0,0,421,426,
        5,32,0,0,422,426,5,33,0,0,423,426,5,36,0,0,424,426,5,35,0,0,425,
        421,1,0,0,0,425,422,1,0,0,0,425,423,1,0,0,0,425,424,1,0,0,0,426,
        53,1,0,0,0,427,428,7,3,0,0,428,55,1,0,0,0,39,59,61,72,87,90,93,98,
        104,112,122,132,143,153,162,171,180,190,202,216,218,233,238,250,
        253,268,278,298,304,310,326,333,346,386,388,397,400,414,417,425
    ]

class AgentarParser ( Parser ):

    grammarFileName = "Agentar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'agent'", "'mother'", "'fields'", "'initialize'", 
                     "'destroy'", "'receive'", "'when'", "'then'", "'action'", 
                     "'send'", "'msg_type='", "'spawn'", "'print'", "'do'", 
                     "'int'", "'float'", "'string'", "'bool'", "'void'", 
                     "'list'", "'map'", "'agentid'", "'.'", "'message'", 
                     "'msg'", "'self'", "'inform'", "'ask'", "'request'", 
                     "'confirm'", "'deny'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "':'", "';'", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'NOT'", "'AND'", "'OR'", "'XOR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MESSAGE", "MSG", "SELF", "MSGTYPE_INFORM", "MSGTYPE_ASK", 
                      "MSGTYPE_REQUEST", "MSGTYPE_CONFIRM", "MSGTYPE_DENY", 
                      "INT", "FLOAT", "AGENTID", "BOOL", "STRING", "ID", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", 
                      "RBRACE", "COMMA", "COLON", "SEMI", "ASSIGN", "PLUS", 
                      "MINUS", "STAR", "SLASH", "EQ", "NEQ", "LT", "GT", 
                      "LEQ", "GEQ", "NOT", "AND", "OR", "XOR", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_motherDecl = 2
    RULE_agentDecl = 3
    RULE_agentBody = 4
    RULE_fieldSection = 5
    RULE_initialSection = 6
    RULE_destroySection = 7
    RULE_receiveSection = 8
    RULE_whenBlock = 9
    RULE_actionSection = 10
    RULE_parameterList = 11
    RULE_parameter = 12
    RULE_messageDecl = 13
    RULE_sendStmt = 14
    RULE_spawnStmt = 15
    RULE_messageInit = 16
    RULE_messageFieldAssign = 17
    RULE_printStmt = 18
    RULE_variableDecl = 19
    RULE_assignment = 20
    RULE_doStmt = 21
    RULE_type = 22
    RULE_expression = 23
    RULE_listLiteral = 24
    RULE_mapLiteral = 25
    RULE_literal = 26
    RULE_msgTypeValue = 27

    ruleNames =  [ "program", "statement", "motherDecl", "agentDecl", "agentBody", 
                   "fieldSection", "initialSection", "destroySection", "receiveSection", 
                   "whenBlock", "actionSection", "parameterList", "parameter", 
                   "messageDecl", "sendStmt", "spawnStmt", "messageInit", 
                   "messageFieldAssign", "printStmt", "variableDecl", "assignment", 
                   "doStmt", "type", "expression", "listLiteral", "mapLiteral", 
                   "literal", "msgTypeValue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    MESSAGE=24
    MSG=25
    SELF=26
    MSGTYPE_INFORM=27
    MSGTYPE_ASK=28
    MSGTYPE_REQUEST=29
    MSGTYPE_CONFIRM=30
    MSGTYPE_DENY=31
    INT=32
    FLOAT=33
    AGENTID=34
    BOOL=35
    STRING=36
    ID=37
    LPAREN=38
    RPAREN=39
    LBRACK=40
    RBRACK=41
    LBRACE=42
    RBRACE=43
    COMMA=44
    COLON=45
    SEMI=46
    ASSIGN=47
    PLUS=48
    MINUS=49
    STAR=50
    SLASH=51
    EQ=52
    NEQ=53
    LT=54
    GT=55
    LEQ=56
    GEQ=57
    NOT=58
    AND=59
    OR=60
    XOR=61
    BLOCK_COMMENT=62
    LINE_COMMENT=63
    WS=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AgentarParser.EOF, 0)

        def motherDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.MotherDeclContext)
            else:
                return self.getTypedRuleContext(AgentarParser.MotherDeclContext,i)


        def agentDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.AgentDeclContext)
            else:
                return self.getTypedRuleContext(AgentarParser.AgentDeclContext,i)


        def messageDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.MessageDeclContext)
            else:
                return self.getTypedRuleContext(AgentarParser.MessageDeclContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AgentarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==24:
                self.state = 59
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.motherDecl()
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.agentDecl()
                    pass

                elif la_ == 3:
                    self.state = 58
                    self.messageDecl()
                    pass


                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(AgentarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printStmt(self):
            return self.getTypedRuleContext(AgentarParser.PrintStmtContext,0)


        def variableDecl(self):
            return self.getTypedRuleContext(AgentarParser.VariableDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(AgentarParser.AssignmentContext,0)


        def sendStmt(self):
            return self.getTypedRuleContext(AgentarParser.SendStmtContext,0)


        def spawnStmt(self):
            return self.getTypedRuleContext(AgentarParser.SpawnStmtContext,0)


        def doStmt(self):
            return self.getTypedRuleContext(AgentarParser.DoStmtContext,0)


        def getRuleIndex(self):
            return AgentarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AgentarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.printStmt()
                pass
            elif token in [15, 16, 17, 18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.variableDecl()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.assignment()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.sendStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.spawnStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.doStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MotherDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def agentBody(self):
            return self.getTypedRuleContext(AgentarParser.AgentBodyContext,0)


        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def getRuleIndex(self):
            return AgentarParser.RULE_motherDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMotherDecl" ):
                listener.enterMotherDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMotherDecl" ):
                listener.exitMotherDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMotherDecl" ):
                return visitor.visitMotherDecl(self)
            else:
                return visitor.visitChildren(self)




    def motherDecl(self):

        localctx = AgentarParser.MotherDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_motherDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(AgentarParser.T__0)
            self.state = 75
            self.match(AgentarParser.T__1)
            self.state = 76
            self.match(AgentarParser.LBRACE)
            self.state = 77
            self.agentBody()
            self.state = 78
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def agentBody(self):
            return self.getTypedRuleContext(AgentarParser.AgentBodyContext,0)


        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def getRuleIndex(self):
            return AgentarParser.RULE_agentDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentDecl" ):
                listener.enterAgentDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentDecl" ):
                listener.exitAgentDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentDecl" ):
                return visitor.visitAgentDecl(self)
            else:
                return visitor.visitChildren(self)




    def agentDecl(self):

        localctx = AgentarParser.AgentDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_agentDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(AgentarParser.T__0)
            self.state = 81
            self.match(AgentarParser.ID)
            self.state = 82
            self.match(AgentarParser.LBRACE)
            self.state = 83
            self.agentBody()
            self.state = 84
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldSection(self):
            return self.getTypedRuleContext(AgentarParser.FieldSectionContext,0)


        def initialSection(self):
            return self.getTypedRuleContext(AgentarParser.InitialSectionContext,0)


        def destroySection(self):
            return self.getTypedRuleContext(AgentarParser.DestroySectionContext,0)


        def receiveSection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ReceiveSectionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ReceiveSectionContext,i)


        def actionSection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ActionSectionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ActionSectionContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_agentBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentBody" ):
                listener.enterAgentBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentBody" ):
                listener.exitAgentBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentBody" ):
                return visitor.visitAgentBody(self)
            else:
                return visitor.visitChildren(self)




    def agentBody(self):

        localctx = AgentarParser.AgentBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_agentBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 86
                self.fieldSection()


            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 89
                self.initialSection()


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 92
                self.destroySection()


            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 95
                self.receiveSection()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 101
                self.actionSection()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def variableDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.VariableDeclContext)
            else:
                return self.getTypedRuleContext(AgentarParser.VariableDeclContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_fieldSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldSection" ):
                listener.enterFieldSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldSection" ):
                listener.exitFieldSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldSection" ):
                return visitor.visitFieldSection(self)
            else:
                return visitor.visitChildren(self)




    def fieldSection(self):

        localctx = AgentarParser.FieldSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fieldSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(AgentarParser.T__2)
            self.state = 108
            self.match(AgentarParser.LBRACE)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8355840) != 0):
                self.state = 109
                self.variableDecl()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AgentarParser.StatementContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_initialSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialSection" ):
                listener.enterInitialSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialSection" ):
                listener.exitInitialSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialSection" ):
                return visitor.visitInitialSection(self)
            else:
                return visitor.visitChildren(self)




    def initialSection(self):

        localctx = AgentarParser.InitialSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initialSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(AgentarParser.T__3)
            self.state = 118
            self.match(AgentarParser.LBRACE)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137447339008) != 0):
                self.state = 119
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestroySectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AgentarParser.StatementContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_destroySection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestroySection" ):
                listener.enterDestroySection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestroySection" ):
                listener.exitDestroySection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestroySection" ):
                return visitor.visitDestroySection(self)
            else:
                return visitor.visitChildren(self)




    def destroySection(self):

        localctx = AgentarParser.DestroySectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_destroySection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(AgentarParser.T__4)
            self.state = 128
            self.match(AgentarParser.LBRACE)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137447339008) != 0):
                self.state = 129
                self.statement()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiveSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def whenBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.WhenBlockContext)
            else:
                return self.getTypedRuleContext(AgentarParser.WhenBlockContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_receiveSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiveSection" ):
                listener.enterReceiveSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiveSection" ):
                listener.exitReceiveSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiveSection" ):
                return visitor.visitReceiveSection(self)
            else:
                return visitor.visitChildren(self)




    def receiveSection(self):

        localctx = AgentarParser.ReceiveSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_receiveSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(AgentarParser.T__5)
            self.state = 138
            self.match(AgentarParser.ID)
            self.state = 139
            self.match(AgentarParser.LBRACE)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 140
                self.whenBlock()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhenBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AgentarParser.StatementContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_whenBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenBlock" ):
                listener.enterWhenBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenBlock" ):
                listener.exitWhenBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhenBlock" ):
                return visitor.visitWhenBlock(self)
            else:
                return visitor.visitChildren(self)




    def whenBlock(self):

        localctx = AgentarParser.WhenBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whenBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(AgentarParser.T__6)
            self.state = 149
            self.match(AgentarParser.LPAREN)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 288236423432110080) != 0):
                self.state = 150
                self.expression(0)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(AgentarParser.RPAREN)
            self.state = 157
            self.match(AgentarParser.T__7)
            self.state = 158
            self.match(AgentarParser.LBRACE)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137447339008) != 0):
                self.state = 159
                self.statement()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(AgentarParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(AgentarParser.TypeContext,0)


        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def parameterList(self):
            return self.getTypedRuleContext(AgentarParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AgentarParser.StatementContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_actionSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionSection" ):
                listener.enterActionSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionSection" ):
                listener.exitActionSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionSection" ):
                return visitor.visitActionSection(self)
            else:
                return visitor.visitChildren(self)




    def actionSection(self):

        localctx = AgentarParser.ActionSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_actionSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(AgentarParser.T__8)
            self.state = 168
            self.match(AgentarParser.ID)
            self.state = 169
            self.match(AgentarParser.LPAREN)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8355840) != 0):
                self.state = 170
                self.parameterList()


            self.state = 173
            self.match(AgentarParser.RPAREN)
            self.state = 174
            self.match(AgentarParser.COLON)
            self.state = 175
            self.type_()
            self.state = 176
            self.match(AgentarParser.LBRACE)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137447339008) != 0):
                self.state = 177
                self.statement()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ParameterContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COMMA)
            else:
                return self.getToken(AgentarParser.COMMA, i)

        def getRuleIndex(self):
            return AgentarParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = AgentarParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.parameter()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 186
                self.match(AgentarParser.COMMA)
                self.state = 187
                self.parameter()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(AgentarParser.TypeContext,0)


        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def getRuleIndex(self):
            return AgentarParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = AgentarParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.type_()
            self.state = 194
            self.match(AgentarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessageDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MESSAGE(self):
            return self.getToken(AgentarParser.MESSAGE, 0)

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def variableDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.VariableDeclContext)
            else:
                return self.getTypedRuleContext(AgentarParser.VariableDeclContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_messageDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessageDecl" ):
                listener.enterMessageDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessageDecl" ):
                listener.exitMessageDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMessageDecl" ):
                return visitor.visitMessageDecl(self)
            else:
                return visitor.visitChildren(self)




    def messageDecl(self):

        localctx = AgentarParser.MessageDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_messageDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(AgentarParser.MESSAGE)
            self.state = 197
            self.match(AgentarParser.ID)
            self.state = 198
            self.match(AgentarParser.LBRACE)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8355840) != 0):
                self.state = 199
                self.variableDecl()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SendStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COMMA)
            else:
                return self.getToken(AgentarParser.COMMA, i)

        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(AgentarParser.SEMI, 0)

        def msgTypeValue(self):
            return self.getTypedRuleContext(AgentarParser.MsgTypeValueContext,0)


        def getRuleIndex(self):
            return AgentarParser.RULE_sendStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSendStmt" ):
                listener.enterSendStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSendStmt" ):
                listener.exitSendStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSendStmt" ):
                return visitor.visitSendStmt(self)
            else:
                return visitor.visitChildren(self)




    def sendStmt(self):

        localctx = AgentarParser.SendStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sendStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(AgentarParser.T__9)
            self.state = 208
            self.match(AgentarParser.LPAREN)
            self.state = 209
            self.expression(0)
            self.state = 210
            self.match(AgentarParser.COMMA)
            self.state = 211
            self.expression(0)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 212
                self.match(AgentarParser.COMMA)
                self.state = 216
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 213
                    self.match(AgentarParser.T__10)
                    self.state = 214
                    self.msgTypeValue()
                    pass
                elif token in [27, 28, 29, 30, 31]:
                    self.state = 215
                    self.msgTypeValue()
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 220
            self.match(AgentarParser.RPAREN)
            self.state = 221
            self.match(AgentarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpawnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(AgentarParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COMMA)
            else:
                return self.getToken(AgentarParser.COMMA, i)

        def LBRACK(self):
            return self.getToken(AgentarParser.LBRACK, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def RBRACK(self):
            return self.getToken(AgentarParser.RBRACK, 0)

        def getRuleIndex(self):
            return AgentarParser.RULE_spawnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpawnStmt" ):
                listener.enterSpawnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpawnStmt" ):
                listener.exitSpawnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpawnStmt" ):
                return visitor.visitSpawnStmt(self)
            else:
                return visitor.visitChildren(self)




    def spawnStmt(self):

        localctx = AgentarParser.SpawnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_spawnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(AgentarParser.T__11)
            self.state = 224
            self.match(AgentarParser.LPAREN)
            self.state = 225
            self.match(AgentarParser.ID)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 226
                self.match(AgentarParser.COMMA)
                self.state = 227
                self.match(AgentarParser.LBRACK)
                self.state = 228
                self.expression(0)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 229
                    self.match(AgentarParser.COMMA)
                    self.state = 230
                    self.expression(0)
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 236
                self.match(AgentarParser.RBRACK)


            self.state = 240
            self.match(AgentarParser.RPAREN)
            self.state = 241
            self.match(AgentarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessageInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def messageFieldAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.MessageFieldAssignContext)
            else:
                return self.getTypedRuleContext(AgentarParser.MessageFieldAssignContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COMMA)
            else:
                return self.getToken(AgentarParser.COMMA, i)

        def getRuleIndex(self):
            return AgentarParser.RULE_messageInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessageInit" ):
                listener.enterMessageInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessageInit" ):
                listener.exitMessageInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMessageInit" ):
                return visitor.visitMessageInit(self)
            else:
                return visitor.visitChildren(self)




    def messageInit(self):

        localctx = AgentarParser.MessageInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_messageInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(AgentarParser.ID)
            self.state = 244
            self.match(AgentarParser.LPAREN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 245
                self.messageFieldAssign()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 246
                    self.match(AgentarParser.COMMA)
                    self.state = 247
                    self.messageFieldAssign()
                    self.state = 252
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 255
            self.match(AgentarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessageFieldAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(AgentarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AgentarParser.RULE_messageFieldAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessageFieldAssign" ):
                listener.enterMessageFieldAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessageFieldAssign" ):
                listener.exitMessageFieldAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMessageFieldAssign" ):
                return visitor.visitMessageFieldAssign(self)
            else:
                return visitor.visitChildren(self)




    def messageFieldAssign(self):

        localctx = AgentarParser.MessageFieldAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_messageFieldAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(AgentarParser.ID)
            self.state = 258
            self.match(AgentarParser.ASSIGN)
            self.state = 259
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(AgentarParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COMMA)
            else:
                return self.getToken(AgentarParser.COMMA, i)

        def getRuleIndex(self):
            return AgentarParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = AgentarParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(AgentarParser.T__12)
            self.state = 262
            self.match(AgentarParser.LPAREN)
            self.state = 263
            self.expression(0)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 264
                self.match(AgentarParser.COMMA)
                self.state = 265
                self.expression(0)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self.match(AgentarParser.RPAREN)
            self.state = 272
            self.match(AgentarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(AgentarParser.TypeContext,0)


        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def SEMI(self):
            return self.getToken(AgentarParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(AgentarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AgentarParser.RULE_variableDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDecl" ):
                listener.enterVariableDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDecl" ):
                listener.exitVariableDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDecl" ):
                return visitor.visitVariableDecl(self)
            else:
                return visitor.visitChildren(self)




    def variableDecl(self):

        localctx = AgentarParser.VariableDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_variableDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.type_()
            self.state = 275
            self.match(AgentarParser.ID)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 276
                self.match(AgentarParser.ASSIGN)
                self.state = 277
                self.expression(0)


            self.state = 280
            self.match(AgentarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AgentarParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(AgentarParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(AgentarParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleAssign" ):
                listener.enterSimpleAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleAssign" ):
                listener.exitSimpleAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleAssign" ):
                return visitor.visitSimpleAssign(self)
            else:
                return visitor.visitChildren(self)


    class IndexAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)
        def LBRACK(self):
            return self.getToken(AgentarParser.LBRACK, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def RBRACK(self):
            return self.getToken(AgentarParser.RBRACK, 0)
        def ASSIGN(self):
            return self.getToken(AgentarParser.ASSIGN, 0)
        def SEMI(self):
            return self.getToken(AgentarParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexAssign" ):
                listener.enterIndexAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexAssign" ):
                listener.exitIndexAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexAssign" ):
                return visitor.visitIndexAssign(self)
            else:
                return visitor.visitChildren(self)


    class SpawnAssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(AgentarParser.ASSIGN, 0)
        def spawnStmt(self):
            return self.getTypedRuleContext(AgentarParser.SpawnStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpawnAssign" ):
                listener.enterSpawnAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpawnAssign" ):
                listener.exitSpawnAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpawnAssign" ):
                return visitor.visitSpawnAssign(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = AgentarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = AgentarParser.SimpleAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(AgentarParser.ID)
                self.state = 283
                self.match(AgentarParser.ASSIGN)
                self.state = 284
                self.expression(0)
                self.state = 285
                self.match(AgentarParser.SEMI)
                pass

            elif la_ == 2:
                localctx = AgentarParser.IndexAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(AgentarParser.ID)
                self.state = 288
                self.match(AgentarParser.LBRACK)
                self.state = 289
                self.expression(0)
                self.state = 290
                self.match(AgentarParser.RBRACK)
                self.state = 291
                self.match(AgentarParser.ASSIGN)
                self.state = 292
                self.expression(0)
                self.state = 293
                self.match(AgentarParser.SEMI)
                pass

            elif la_ == 3:
                localctx = AgentarParser.SpawnAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.match(AgentarParser.ID)
                self.state = 296
                self.match(AgentarParser.ASSIGN)
                self.state = 297
                self.spawnStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(AgentarParser.SEMI, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COMMA)
            else:
                return self.getToken(AgentarParser.COMMA, i)

        def getRuleIndex(self):
            return AgentarParser.RULE_doStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoStmt" ):
                listener.enterDoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoStmt" ):
                listener.exitDoStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoStmt" ):
                return visitor.visitDoStmt(self)
            else:
                return visitor.visitChildren(self)




    def doStmt(self):

        localctx = AgentarParser.DoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_doStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(AgentarParser.T__13)
            self.state = 301
            self.match(AgentarParser.ID)
            self.state = 302
            self.match(AgentarParser.LPAREN)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 288236423432110080) != 0):
                self.state = 303
                self.expression(0)


            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 306
                self.match(AgentarParser.COMMA)
                self.state = 307
                self.expression(0)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 313
            self.match(AgentarParser.RPAREN)
            self.state = 314
            self.match(AgentarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AgentarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = AgentarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8355840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AgentarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MapExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mapLiteral(self):
            return self.getTypedRuleContext(AgentarParser.MapLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapExpr" ):
                listener.enterMapExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapExpr" ):
                listener.exitMapExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapExpr" ):
                return visitor.visitMapExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(AgentarParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class SelfAccessExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SELF(self):
            return self.getToken(AgentarParser.SELF, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.ID)
            else:
                return self.getToken(AgentarParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelfAccessExpr" ):
                listener.enterSelfAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelfAccessExpr" ):
                listener.exitSelfAccessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelfAccessExpr" ):
                return visitor.visitSelfAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class LeqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def LEQ(self):
            return self.getToken(AgentarParser.LEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeqExpr" ):
                listener.enterLeqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeqExpr" ):
                listener.exitLeqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeqExpr" ):
                return visitor.visitLeqExpr(self)
            else:
                return visitor.visitChildren(self)


    class XorExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def XOR(self):
            return self.getToken(AgentarParser.XOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXorExpr" ):
                listener.enterXorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXorExpr" ):
                listener.exitXorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXorExpr" ):
                return visitor.visitXorExpr(self)
            else:
                return visitor.visitChildren(self)


    class GeqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def GEQ(self):
            return self.getToken(AgentarParser.GEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeqExpr" ):
                listener.enterGeqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeqExpr" ):
                listener.exitGeqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeqExpr" ):
                return visitor.visitGeqExpr(self)
            else:
                return visitor.visitChildren(self)


    class MessageAccessExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MSG(self):
            return self.getToken(AgentarParser.MSG, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.ID)
            else:
                return self.getToken(AgentarParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessageAccessExpr" ):
                listener.enterMessageAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessageAccessExpr" ):
                listener.exitMessageAccessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMessageAccessExpr" ):
                return visitor.visitMessageAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class LtExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(AgentarParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLtExpr" ):
                listener.enterLtExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLtExpr" ):
                listener.exitLtExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLtExpr" ):
                return visitor.visitLtExpr(self)
            else:
                return visitor.visitChildren(self)


    class GtExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def GT(self):
            return self.getToken(AgentarParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGtExpr" ):
                listener.enterGtExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGtExpr" ):
                listener.exitGtExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGtExpr" ):
                return visitor.visitGtExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(AgentarParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class IndexExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def LBRACK(self):
            return self.getToken(AgentarParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(AgentarParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexExpr" ):
                listener.enterIndexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexExpr" ):
                listener.exitIndexExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpr" ):
                return visitor.visitIndexExpr(self)
            else:
                return visitor.visitChildren(self)


    class AgentIdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AGENTID(self):
            return self.getToken(AgentarParser.AGENTID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentIdExpr" ):
                listener.enterAgentIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentIdExpr" ):
                listener.exitAgentIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentIdExpr" ):
                return visitor.visitAgentIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarReferenceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarReference" ):
                listener.enterVarReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarReference" ):
                listener.exitVarReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarReference" ):
                return visitor.visitVarReference(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def STAR(self):
            return self.getToken(AgentarParser.STAR, 0)
        def SLASH(self):
            return self.getToken(AgentarParser.SLASH, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(AgentarParser.EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpr" ):
                listener.enterEqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpr" ):
                listener.exitEqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class NeqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def NEQ(self):
            return self.getToken(AgentarParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeqExpr" ):
                listener.enterNeqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeqExpr" ):
                listener.exitNeqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeqExpr" ):
                return visitor.visitNeqExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(AgentarParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class MsgTypeValueExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def msgTypeValue(self):
            return self.getTypedRuleContext(AgentarParser.MsgTypeValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsgTypeValueExpr" ):
                listener.enterMsgTypeValueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsgTypeValueExpr" ):
                listener.exitMsgTypeValueExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMsgTypeValueExpr" ):
                return visitor.visitMsgTypeValueExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(AgentarParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def listLiteral(self):
            return self.getTypedRuleContext(AgentarParser.ListLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpr" ):
                listener.enterListExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpr" ):
                listener.exitListExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpr" ):
                return visitor.visitListExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class MessageInitExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def messageInit(self):
            return self.getTypedRuleContext(AgentarParser.MessageInitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessageInitExpr" ):
                listener.enterMessageInitExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessageInitExpr" ):
                listener.exitMessageInitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMessageInitExpr" ):
                return visitor.visitMessageInitExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(AgentarParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(AgentarParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AgentarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = AgentarParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 319
                self.match(AgentarParser.NOT)
                self.state = 320
                self.expression(23)
                pass

            elif la_ == 2:
                localctx = AgentarParser.MessageAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 321
                self.match(AgentarParser.MSG)
                self.state = 324 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 322
                        self.match(AgentarParser.T__22)
                        self.state = 323
                        self.match(AgentarParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 326 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 3:
                localctx = AgentarParser.SelfAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 328
                self.match(AgentarParser.SELF)
                self.state = 331 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 329
                        self.match(AgentarParser.T__22)
                        self.state = 330
                        self.match(AgentarParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 333 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass

            elif la_ == 4:
                localctx = AgentarParser.ListExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 335
                self.listLiteral()
                pass

            elif la_ == 5:
                localctx = AgentarParser.MapExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 336
                self.mapLiteral()
                pass

            elif la_ == 6:
                localctx = AgentarParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 337
                self.literal()
                pass

            elif la_ == 7:
                localctx = AgentarParser.VarReferenceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 338
                self.match(AgentarParser.ID)
                pass

            elif la_ == 8:
                localctx = AgentarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 339
                self.match(AgentarParser.LPAREN)
                self.state = 340
                self.expression(0)
                self.state = 341
                self.match(AgentarParser.RPAREN)
                pass

            elif la_ == 9:
                localctx = AgentarParser.AgentIdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 343
                self.match(AgentarParser.AGENTID)
                pass

            elif la_ == 10:
                localctx = AgentarParser.MessageInitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 344
                self.messageInit()
                pass

            elif la_ == 11:
                localctx = AgentarParser.MsgTypeValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 345
                self.msgTypeValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 386
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = AgentarParser.AndExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 348
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 349
                        self.match(AgentarParser.AND)
                        self.state = 350
                        self.expression(23)
                        pass

                    elif la_ == 2:
                        localctx = AgentarParser.OrExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 351
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 352
                        self.match(AgentarParser.OR)
                        self.state = 353
                        self.expression(22)
                        pass

                    elif la_ == 3:
                        localctx = AgentarParser.XorExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 354
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 355
                        self.match(AgentarParser.XOR)
                        self.state = 356
                        self.expression(21)
                        pass

                    elif la_ == 4:
                        localctx = AgentarParser.MulDivExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 357
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 358
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==50 or _la==51):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 359
                        self.expression(20)
                        pass

                    elif la_ == 5:
                        localctx = AgentarParser.AddSubExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 360
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 361
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==48 or _la==49):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 362
                        self.expression(19)
                        pass

                    elif la_ == 6:
                        localctx = AgentarParser.EqExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 363
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 364
                        self.match(AgentarParser.EQ)
                        self.state = 365
                        self.expression(18)
                        pass

                    elif la_ == 7:
                        localctx = AgentarParser.NeqExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 366
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 367
                        self.match(AgentarParser.NEQ)
                        self.state = 368
                        self.expression(17)
                        pass

                    elif la_ == 8:
                        localctx = AgentarParser.LtExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 369
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 370
                        self.match(AgentarParser.LT)
                        self.state = 371
                        self.expression(16)
                        pass

                    elif la_ == 9:
                        localctx = AgentarParser.GtExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 372
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 373
                        self.match(AgentarParser.GT)
                        self.state = 374
                        self.expression(15)
                        pass

                    elif la_ == 10:
                        localctx = AgentarParser.LeqExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 375
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 376
                        self.match(AgentarParser.LEQ)
                        self.state = 377
                        self.expression(14)
                        pass

                    elif la_ == 11:
                        localctx = AgentarParser.GeqExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 378
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 379
                        self.match(AgentarParser.GEQ)
                        self.state = 380
                        self.expression(13)
                        pass

                    elif la_ == 12:
                        localctx = AgentarParser.IndexExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 381
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 382
                        self.match(AgentarParser.LBRACK)
                        self.state = 383
                        self.expression(0)
                        self.state = 384
                        self.match(AgentarParser.RBRACK)
                        pass

             
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(AgentarParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(AgentarParser.RBRACK, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COMMA)
            else:
                return self.getToken(AgentarParser.COMMA, i)

        def getRuleIndex(self):
            return AgentarParser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLiteral" ):
                return visitor.visitListLiteral(self)
            else:
                return visitor.visitChildren(self)




    def listLiteral(self):

        localctx = AgentarParser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(AgentarParser.LBRACK)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 288236423432110080) != 0):
                self.state = 392
                self.expression(0)
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 393
                    self.match(AgentarParser.COMMA)
                    self.state = 394
                    self.expression(0)
                    self.state = 399
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 402
            self.match(AgentarParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(AgentarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentarParser.RBRACE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.ID)
            else:
                return self.getToken(AgentarParser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COLON)
            else:
                return self.getToken(AgentarParser.COLON, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AgentarParser.COMMA)
            else:
                return self.getToken(AgentarParser.COMMA, i)

        def getRuleIndex(self):
            return AgentarParser.RULE_mapLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapLiteral" ):
                listener.enterMapLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapLiteral" ):
                listener.exitMapLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapLiteral" ):
                return visitor.visitMapLiteral(self)
            else:
                return visitor.visitChildren(self)




    def mapLiteral(self):

        localctx = AgentarParser.MapLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_mapLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(AgentarParser.LBRACE)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 405
                self.match(AgentarParser.ID)
                self.state = 406
                self.match(AgentarParser.COLON)
                self.state = 407
                self.expression(0)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 408
                    self.match(AgentarParser.COMMA)
                    self.state = 409
                    self.match(AgentarParser.ID)
                    self.state = 410
                    self.match(AgentarParser.COLON)
                    self.state = 411
                    self.expression(0)
                    self.state = 416
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 419
            self.match(AgentarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AgentarParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(AgentarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class BoolLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(AgentarParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLiteral" ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(AgentarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AgentarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = AgentarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literal)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                localctx = AgentarParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(AgentarParser.INT)
                pass
            elif token in [33]:
                localctx = AgentarParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(AgentarParser.FLOAT)
                pass
            elif token in [36]:
                localctx = AgentarParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 423
                self.match(AgentarParser.STRING)
                pass
            elif token in [35]:
                localctx = AgentarParser.BoolLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 424
                self.match(AgentarParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MsgTypeValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MSGTYPE_INFORM(self):
            return self.getToken(AgentarParser.MSGTYPE_INFORM, 0)

        def MSGTYPE_ASK(self):
            return self.getToken(AgentarParser.MSGTYPE_ASK, 0)

        def MSGTYPE_REQUEST(self):
            return self.getToken(AgentarParser.MSGTYPE_REQUEST, 0)

        def MSGTYPE_CONFIRM(self):
            return self.getToken(AgentarParser.MSGTYPE_CONFIRM, 0)

        def MSGTYPE_DENY(self):
            return self.getToken(AgentarParser.MSGTYPE_DENY, 0)

        def getRuleIndex(self):
            return AgentarParser.RULE_msgTypeValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsgTypeValue" ):
                listener.enterMsgTypeValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsgTypeValue" ):
                listener.exitMsgTypeValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMsgTypeValue" ):
                return visitor.visitMsgTypeValue(self)
            else:
                return visitor.visitChildren(self)




    def msgTypeValue(self):

        localctx = AgentarParser.MsgTypeValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_msgTypeValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4160749568) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 4)
         




