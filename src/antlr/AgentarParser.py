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
        4,1,65,438,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,3,4,91,8,4,1,4,3,4,94,8,4,1,4,3,4,
        97,8,4,1,4,5,4,100,8,4,10,4,12,4,103,9,4,1,4,5,4,106,8,4,10,4,12,
        4,109,9,4,1,5,1,5,1,5,5,5,114,8,5,10,5,12,5,117,9,5,1,5,1,5,1,6,
        1,6,1,6,5,6,124,8,6,10,6,12,6,127,9,6,1,6,1,6,1,7,1,7,1,7,5,7,134,
        8,7,10,7,12,7,137,9,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,145,8,8,10,8,12,
        8,148,9,8,1,8,1,8,1,9,1,9,1,9,5,9,155,8,9,10,9,12,9,158,9,9,1,9,
        1,9,1,9,1,9,5,9,164,8,9,10,9,12,9,167,9,9,1,9,1,9,1,10,1,10,1,10,
        1,10,3,10,175,8,10,1,10,1,10,1,10,1,10,1,10,5,10,182,8,10,10,10,
        12,10,185,9,10,1,10,1,10,1,11,1,11,1,11,5,11,192,8,11,10,11,12,11,
        195,9,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,5,13,204,8,13,10,13,
        12,13,207,9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,3,14,220,8,14,3,14,222,8,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,5,15,235,8,15,10,15,12,15,238,9,15,1,15,1,
        15,3,15,242,8,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,
        17,1,17,1,17,1,17,5,17,257,8,17,10,17,12,17,260,9,17,3,17,262,8,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,5,19,275,
        8,19,10,19,12,19,278,9,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,3,20,
        287,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,307,8,21,1,22,1,22,1,22,
        1,22,1,22,1,22,5,22,315,8,22,10,22,12,22,318,9,22,3,22,320,8,22,
        1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,4,24,333,
        8,24,11,24,12,24,334,1,24,1,24,1,24,4,24,340,8,24,11,24,12,24,341,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,355,
        8,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        5,24,395,8,24,10,24,12,24,398,9,24,1,25,1,25,1,25,1,25,5,25,404,
        8,25,10,25,12,25,407,9,25,3,25,409,8,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,5,26,421,8,26,10,26,12,26,424,9,26,3,26,
        426,8,26,1,26,1,26,1,27,1,27,1,27,1,27,3,27,434,8,27,1,28,1,28,1,
        28,0,1,48,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,0,4,1,0,16,23,1,0,51,52,1,0,49,50,
        1,0,28,32,475,0,63,1,0,0,0,2,75,1,0,0,0,4,77,1,0,0,0,6,83,1,0,0,
        0,8,90,1,0,0,0,10,110,1,0,0,0,12,120,1,0,0,0,14,130,1,0,0,0,16,140,
        1,0,0,0,18,151,1,0,0,0,20,170,1,0,0,0,22,188,1,0,0,0,24,196,1,0,
        0,0,26,199,1,0,0,0,28,210,1,0,0,0,30,226,1,0,0,0,32,246,1,0,0,0,
        34,251,1,0,0,0,36,265,1,0,0,0,38,269,1,0,0,0,40,282,1,0,0,0,42,306,
        1,0,0,0,44,308,1,0,0,0,46,324,1,0,0,0,48,354,1,0,0,0,50,399,1,0,
        0,0,52,412,1,0,0,0,54,433,1,0,0,0,56,435,1,0,0,0,58,62,3,4,2,0,59,
        62,3,6,3,0,60,62,3,26,13,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,
        0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,
        1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,76,3,38,19,0,69,76,3,40,20,
        0,70,76,3,42,21,0,71,76,3,28,14,0,72,76,3,30,15,0,73,76,3,32,16,
        0,74,76,3,44,22,0,75,68,1,0,0,0,75,69,1,0,0,0,75,70,1,0,0,0,75,71,
        1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,0,77,
        78,5,1,0,0,78,79,5,2,0,0,79,80,5,43,0,0,80,81,3,8,4,0,81,82,5,44,
        0,0,82,5,1,0,0,0,83,84,5,1,0,0,84,85,5,38,0,0,85,86,5,43,0,0,86,
        87,3,8,4,0,87,88,5,44,0,0,88,7,1,0,0,0,89,91,3,10,5,0,90,89,1,0,
        0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,94,3,12,6,0,93,92,1,0,0,0,93,
        94,1,0,0,0,94,96,1,0,0,0,95,97,3,14,7,0,96,95,1,0,0,0,96,97,1,0,
        0,0,97,101,1,0,0,0,98,100,3,16,8,0,99,98,1,0,0,0,100,103,1,0,0,0,
        101,99,1,0,0,0,101,102,1,0,0,0,102,107,1,0,0,0,103,101,1,0,0,0,104,
        106,3,20,10,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,
        108,1,0,0,0,108,9,1,0,0,0,109,107,1,0,0,0,110,111,5,3,0,0,111,115,
        5,43,0,0,112,114,3,40,20,0,113,112,1,0,0,0,114,117,1,0,0,0,115,113,
        1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,118,119,
        5,44,0,0,119,11,1,0,0,0,120,121,5,4,0,0,121,125,5,43,0,0,122,124,
        3,2,1,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,129,5,44,0,0,129,13,
        1,0,0,0,130,131,5,5,0,0,131,135,5,43,0,0,132,134,3,2,1,0,133,132,
        1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,138,
        1,0,0,0,137,135,1,0,0,0,138,139,5,44,0,0,139,15,1,0,0,0,140,141,
        5,6,0,0,141,142,5,38,0,0,142,146,5,43,0,0,143,145,3,18,9,0,144,143,
        1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,
        1,0,0,0,148,146,1,0,0,0,149,150,5,44,0,0,150,17,1,0,0,0,151,152,
        5,7,0,0,152,156,5,39,0,0,153,155,3,48,24,0,154,153,1,0,0,0,155,158,
        1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,156,
        1,0,0,0,159,160,5,40,0,0,160,161,5,8,0,0,161,165,5,43,0,0,162,164,
        3,2,1,0,163,162,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,168,1,0,0,0,167,165,1,0,0,0,168,169,5,44,0,0,169,19,
        1,0,0,0,170,171,5,9,0,0,171,172,5,38,0,0,172,174,5,39,0,0,173,175,
        3,22,11,0,174,173,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,
        5,40,0,0,177,178,5,46,0,0,178,179,3,46,23,0,179,183,5,43,0,0,180,
        182,3,2,1,0,181,180,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,
        184,1,0,0,0,184,186,1,0,0,0,185,183,1,0,0,0,186,187,5,44,0,0,187,
        21,1,0,0,0,188,193,3,24,12,0,189,190,5,45,0,0,190,192,3,24,12,0,
        191,189,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,
        194,23,1,0,0,0,195,193,1,0,0,0,196,197,3,46,23,0,197,198,5,38,0,
        0,198,25,1,0,0,0,199,200,5,25,0,0,200,201,5,38,0,0,201,205,5,43,
        0,0,202,204,3,40,20,0,203,202,1,0,0,0,204,207,1,0,0,0,205,203,1,
        0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,205,1,0,0,0,208,209,5,
        44,0,0,209,27,1,0,0,0,210,211,5,10,0,0,211,212,5,39,0,0,212,213,
        3,48,24,0,213,214,5,45,0,0,214,221,3,48,24,0,215,219,5,45,0,0,216,
        217,5,11,0,0,217,220,3,56,28,0,218,220,3,56,28,0,219,216,1,0,0,0,
        219,218,1,0,0,0,220,222,1,0,0,0,221,215,1,0,0,0,221,222,1,0,0,0,
        222,223,1,0,0,0,223,224,5,40,0,0,224,225,5,47,0,0,225,29,1,0,0,0,
        226,227,5,12,0,0,227,228,5,39,0,0,228,241,5,38,0,0,229,230,5,45,
        0,0,230,231,5,41,0,0,231,236,3,48,24,0,232,233,5,45,0,0,233,235,
        3,48,24,0,234,232,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,
        1,0,0,0,237,239,1,0,0,0,238,236,1,0,0,0,239,240,5,42,0,0,240,242,
        1,0,0,0,241,229,1,0,0,0,241,242,1,0,0,0,242,243,1,0,0,0,243,244,
        5,40,0,0,244,245,5,47,0,0,245,31,1,0,0,0,246,247,5,13,0,0,247,248,
        5,39,0,0,248,249,5,40,0,0,249,250,5,47,0,0,250,33,1,0,0,0,251,252,
        5,38,0,0,252,261,5,39,0,0,253,258,3,36,18,0,254,255,5,45,0,0,255,
        257,3,36,18,0,256,254,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,
        259,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,261,253,1,0,0,0,261,
        262,1,0,0,0,262,263,1,0,0,0,263,264,5,40,0,0,264,35,1,0,0,0,265,
        266,5,38,0,0,266,267,5,48,0,0,267,268,3,48,24,0,268,37,1,0,0,0,269,
        270,5,14,0,0,270,271,5,39,0,0,271,276,3,48,24,0,272,273,5,45,0,0,
        273,275,3,48,24,0,274,272,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,
        0,276,277,1,0,0,0,277,279,1,0,0,0,278,276,1,0,0,0,279,280,5,40,0,
        0,280,281,5,47,0,0,281,39,1,0,0,0,282,283,3,46,23,0,283,286,5,38,
        0,0,284,285,5,48,0,0,285,287,3,48,24,0,286,284,1,0,0,0,286,287,1,
        0,0,0,287,288,1,0,0,0,288,289,5,47,0,0,289,41,1,0,0,0,290,291,5,
        38,0,0,291,292,5,48,0,0,292,293,3,48,24,0,293,294,5,47,0,0,294,307,
        1,0,0,0,295,296,5,38,0,0,296,297,5,41,0,0,297,298,3,48,24,0,298,
        299,5,42,0,0,299,300,5,48,0,0,300,301,3,48,24,0,301,302,5,47,0,0,
        302,307,1,0,0,0,303,304,5,38,0,0,304,305,5,48,0,0,305,307,3,30,15,
        0,306,290,1,0,0,0,306,295,1,0,0,0,306,303,1,0,0,0,307,43,1,0,0,0,
        308,309,5,15,0,0,309,310,5,38,0,0,310,319,5,39,0,0,311,316,3,48,
        24,0,312,313,5,45,0,0,313,315,3,48,24,0,314,312,1,0,0,0,315,318,
        1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,320,1,0,0,0,318,316,
        1,0,0,0,319,311,1,0,0,0,319,320,1,0,0,0,320,321,1,0,0,0,321,322,
        5,40,0,0,322,323,5,47,0,0,323,45,1,0,0,0,324,325,7,0,0,0,325,47,
        1,0,0,0,326,327,6,24,-1,0,327,328,5,59,0,0,328,355,3,48,24,23,329,
        332,5,26,0,0,330,331,5,24,0,0,331,333,5,38,0,0,332,330,1,0,0,0,333,
        334,1,0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,355,1,0,0,0,336,
        339,5,27,0,0,337,338,5,24,0,0,338,340,5,38,0,0,339,337,1,0,0,0,340,
        341,1,0,0,0,341,339,1,0,0,0,341,342,1,0,0,0,342,355,1,0,0,0,343,
        355,3,50,25,0,344,355,3,52,26,0,345,355,3,54,27,0,346,355,5,38,0,
        0,347,348,5,39,0,0,348,349,3,48,24,0,349,350,5,40,0,0,350,355,1,
        0,0,0,351,355,5,35,0,0,352,355,3,34,17,0,353,355,3,56,28,0,354,326,
        1,0,0,0,354,329,1,0,0,0,354,336,1,0,0,0,354,343,1,0,0,0,354,344,
        1,0,0,0,354,345,1,0,0,0,354,346,1,0,0,0,354,347,1,0,0,0,354,351,
        1,0,0,0,354,352,1,0,0,0,354,353,1,0,0,0,355,396,1,0,0,0,356,357,
        10,22,0,0,357,358,5,60,0,0,358,395,3,48,24,23,359,360,10,21,0,0,
        360,361,5,61,0,0,361,395,3,48,24,22,362,363,10,20,0,0,363,364,5,
        62,0,0,364,395,3,48,24,21,365,366,10,19,0,0,366,367,7,1,0,0,367,
        395,3,48,24,20,368,369,10,18,0,0,369,370,7,2,0,0,370,395,3,48,24,
        19,371,372,10,17,0,0,372,373,5,53,0,0,373,395,3,48,24,18,374,375,
        10,16,0,0,375,376,5,54,0,0,376,395,3,48,24,17,377,378,10,15,0,0,
        378,379,5,55,0,0,379,395,3,48,24,16,380,381,10,14,0,0,381,382,5,
        56,0,0,382,395,3,48,24,15,383,384,10,13,0,0,384,385,5,57,0,0,385,
        395,3,48,24,14,386,387,10,12,0,0,387,388,5,58,0,0,388,395,3,48,24,
        13,389,390,10,4,0,0,390,391,5,41,0,0,391,392,3,48,24,0,392,393,5,
        42,0,0,393,395,1,0,0,0,394,356,1,0,0,0,394,359,1,0,0,0,394,362,1,
        0,0,0,394,365,1,0,0,0,394,368,1,0,0,0,394,371,1,0,0,0,394,374,1,
        0,0,0,394,377,1,0,0,0,394,380,1,0,0,0,394,383,1,0,0,0,394,386,1,
        0,0,0,394,389,1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,396,397,1,
        0,0,0,397,49,1,0,0,0,398,396,1,0,0,0,399,408,5,41,0,0,400,405,3,
        48,24,0,401,402,5,45,0,0,402,404,3,48,24,0,403,401,1,0,0,0,404,407,
        1,0,0,0,405,403,1,0,0,0,405,406,1,0,0,0,406,409,1,0,0,0,407,405,
        1,0,0,0,408,400,1,0,0,0,408,409,1,0,0,0,409,410,1,0,0,0,410,411,
        5,42,0,0,411,51,1,0,0,0,412,425,5,43,0,0,413,414,5,38,0,0,414,415,
        5,46,0,0,415,422,3,48,24,0,416,417,5,45,0,0,417,418,5,38,0,0,418,
        419,5,46,0,0,419,421,3,48,24,0,420,416,1,0,0,0,421,424,1,0,0,0,422,
        420,1,0,0,0,422,423,1,0,0,0,423,426,1,0,0,0,424,422,1,0,0,0,425,
        413,1,0,0,0,425,426,1,0,0,0,426,427,1,0,0,0,427,428,5,44,0,0,428,
        53,1,0,0,0,429,434,5,33,0,0,430,434,5,34,0,0,431,434,5,37,0,0,432,
        434,5,36,0,0,433,429,1,0,0,0,433,430,1,0,0,0,433,431,1,0,0,0,433,
        432,1,0,0,0,434,55,1,0,0,0,435,436,7,3,0,0,436,57,1,0,0,0,39,61,
        63,75,90,93,96,101,107,115,125,135,146,156,165,174,183,193,205,219,
        221,236,241,258,261,276,286,306,316,319,334,341,354,394,396,405,
        408,422,425,433
    ]

class AgentarParser ( Parser ):

    grammarFileName = "Agentar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'agent'", "'mother'", "'fields'", "'initialize'", 
                     "'destroy'", "'receive'", "'when'", "'then'", "'action'", 
                     "'send'", "'msg_type='", "'spawn'", "'kill'", "'print'", 
                     "'do'", "'int'", "'float'", "'string'", "'bool'", "'void'", 
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
                      "<INVALID>", "MESSAGE", "MSG", "SELF", "MSGTYPE_INFORM", 
                      "MSGTYPE_ASK", "MSGTYPE_REQUEST", "MSGTYPE_CONFIRM", 
                      "MSGTYPE_DENY", "INT", "FLOAT", "AGENTID", "BOOL", 
                      "STRING", "ID", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                      "LBRACE", "RBRACE", "COMMA", "COLON", "SEMI", "ASSIGN", 
                      "PLUS", "MINUS", "STAR", "SLASH", "EQ", "NEQ", "LT", 
                      "GT", "LEQ", "GEQ", "NOT", "AND", "OR", "XOR", "BLOCK_COMMENT", 
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
    RULE_killStmt = 16
    RULE_messageInit = 17
    RULE_messageFieldAssign = 18
    RULE_printStmt = 19
    RULE_variableDecl = 20
    RULE_assignment = 21
    RULE_doStmt = 22
    RULE_type = 23
    RULE_expression = 24
    RULE_listLiteral = 25
    RULE_mapLiteral = 26
    RULE_literal = 27
    RULE_msgTypeValue = 28

    ruleNames =  [ "program", "statement", "motherDecl", "agentDecl", "agentBody", 
                   "fieldSection", "initialSection", "destroySection", "receiveSection", 
                   "whenBlock", "actionSection", "parameterList", "parameter", 
                   "messageDecl", "sendStmt", "spawnStmt", "killStmt", "messageInit", 
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
    T__23=24
    MESSAGE=25
    MSG=26
    SELF=27
    MSGTYPE_INFORM=28
    MSGTYPE_ASK=29
    MSGTYPE_REQUEST=30
    MSGTYPE_CONFIRM=31
    MSGTYPE_DENY=32
    INT=33
    FLOAT=34
    AGENTID=35
    BOOL=36
    STRING=37
    ID=38
    LPAREN=39
    RPAREN=40
    LBRACK=41
    RBRACK=42
    LBRACE=43
    RBRACE=44
    COMMA=45
    COLON=46
    SEMI=47
    ASSIGN=48
    PLUS=49
    MINUS=50
    STAR=51
    SLASH=52
    EQ=53
    NEQ=54
    LT=55
    GT=56
    LEQ=57
    GEQ=58
    NOT=59
    AND=60
    OR=61
    XOR=62
    BLOCK_COMMENT=63
    LINE_COMMENT=64
    WS=65

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
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==25:
                self.state = 61
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.motherDecl()
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.agentDecl()
                    pass

                elif la_ == 3:
                    self.state = 60
                    self.messageDecl()
                    pass


                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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


        def killStmt(self):
            return self.getTypedRuleContext(AgentarParser.KillStmtContext,0)


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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.printStmt()
                pass
            elif token in [16, 17, 18, 19, 20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.variableDecl()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.assignment()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.sendStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.spawnStmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.killStmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
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
            self.state = 77
            self.match(AgentarParser.T__0)
            self.state = 78
            self.match(AgentarParser.T__1)
            self.state = 79
            self.match(AgentarParser.LBRACE)
            self.state = 80
            self.agentBody()
            self.state = 81
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
            self.state = 83
            self.match(AgentarParser.T__0)
            self.state = 84
            self.match(AgentarParser.ID)
            self.state = 85
            self.match(AgentarParser.LBRACE)
            self.state = 86
            self.agentBody()
            self.state = 87
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
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 89
                self.fieldSection()


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 92
                self.initialSection()


            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 95
                self.destroySection()


            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 98
                self.receiveSection()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 104
                self.actionSection()
                self.state = 109
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
            self.state = 110
            self.match(AgentarParser.T__2)
            self.state = 111
            self.match(AgentarParser.LBRACE)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16711680) != 0):
                self.state = 112
                self.variableDecl()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
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
            self.state = 120
            self.match(AgentarParser.T__3)
            self.state = 121
            self.match(AgentarParser.LBRACE)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274894681088) != 0):
                self.state = 122
                self.statement()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
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
            self.state = 130
            self.match(AgentarParser.T__4)
            self.state = 131
            self.match(AgentarParser.LBRACE)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274894681088) != 0):
                self.state = 132
                self.statement()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
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
            self.state = 140
            self.match(AgentarParser.T__5)
            self.state = 141
            self.match(AgentarParser.ID)
            self.state = 142
            self.match(AgentarParser.LBRACE)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 143
                self.whenBlock()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
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
            self.state = 151
            self.match(AgentarParser.T__6)
            self.state = 152
            self.match(AgentarParser.LPAREN)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576472846864220160) != 0):
                self.state = 153
                self.expression(0)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self.match(AgentarParser.RPAREN)
            self.state = 160
            self.match(AgentarParser.T__7)
            self.state = 161
            self.match(AgentarParser.LBRACE)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274894681088) != 0):
                self.state = 162
                self.statement()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
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
            self.state = 170
            self.match(AgentarParser.T__8)
            self.state = 171
            self.match(AgentarParser.ID)
            self.state = 172
            self.match(AgentarParser.LPAREN)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16711680) != 0):
                self.state = 173
                self.parameterList()


            self.state = 176
            self.match(AgentarParser.RPAREN)
            self.state = 177
            self.match(AgentarParser.COLON)
            self.state = 178
            self.type_()
            self.state = 179
            self.match(AgentarParser.LBRACE)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274894681088) != 0):
                self.state = 180
                self.statement()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
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
            self.state = 188
            self.parameter()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 189
                self.match(AgentarParser.COMMA)
                self.state = 190
                self.parameter()
                self.state = 195
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
            self.state = 196
            self.type_()
            self.state = 197
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
            self.state = 199
            self.match(AgentarParser.MESSAGE)
            self.state = 200
            self.match(AgentarParser.ID)
            self.state = 201
            self.match(AgentarParser.LBRACE)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16711680) != 0):
                self.state = 202
                self.variableDecl()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
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
            self.state = 210
            self.match(AgentarParser.T__9)
            self.state = 211
            self.match(AgentarParser.LPAREN)
            self.state = 212
            self.expression(0)
            self.state = 213
            self.match(AgentarParser.COMMA)
            self.state = 214
            self.expression(0)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 215
                self.match(AgentarParser.COMMA)
                self.state = 219
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 216
                    self.match(AgentarParser.T__10)
                    self.state = 217
                    self.msgTypeValue()
                    pass
                elif token in [28, 29, 30, 31, 32]:
                    self.state = 218
                    self.msgTypeValue()
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 223
            self.match(AgentarParser.RPAREN)
            self.state = 224
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
            self.state = 226
            self.match(AgentarParser.T__11)
            self.state = 227
            self.match(AgentarParser.LPAREN)
            self.state = 228
            self.match(AgentarParser.ID)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 229
                self.match(AgentarParser.COMMA)
                self.state = 230
                self.match(AgentarParser.LBRACK)
                self.state = 231
                self.expression(0)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 232
                    self.match(AgentarParser.COMMA)
                    self.state = 233
                    self.expression(0)
                    self.state = 238
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 239
                self.match(AgentarParser.RBRACK)


            self.state = 243
            self.match(AgentarParser.RPAREN)
            self.state = 244
            self.match(AgentarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KillStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(AgentarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AgentarParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(AgentarParser.SEMI, 0)

        def getRuleIndex(self):
            return AgentarParser.RULE_killStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKillStmt" ):
                listener.enterKillStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKillStmt" ):
                listener.exitKillStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKillStmt" ):
                return visitor.visitKillStmt(self)
            else:
                return visitor.visitChildren(self)




    def killStmt(self):

        localctx = AgentarParser.KillStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_killStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(AgentarParser.T__12)
            self.state = 247
            self.match(AgentarParser.LPAREN)
            self.state = 248
            self.match(AgentarParser.RPAREN)
            self.state = 249
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
        self.enterRule(localctx, 34, self.RULE_messageInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(AgentarParser.ID)
            self.state = 252
            self.match(AgentarParser.LPAREN)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 253
                self.messageFieldAssign()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 254
                    self.match(AgentarParser.COMMA)
                    self.state = 255
                    self.messageFieldAssign()
                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 263
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
        self.enterRule(localctx, 36, self.RULE_messageFieldAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(AgentarParser.ID)
            self.state = 266
            self.match(AgentarParser.ASSIGN)
            self.state = 267
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
        self.enterRule(localctx, 38, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(AgentarParser.T__13)
            self.state = 270
            self.match(AgentarParser.LPAREN)
            self.state = 271
            self.expression(0)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 272
                self.match(AgentarParser.COMMA)
                self.state = 273
                self.expression(0)
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 279
            self.match(AgentarParser.RPAREN)
            self.state = 280
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
        self.enterRule(localctx, 40, self.RULE_variableDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.type_()
            self.state = 283
            self.match(AgentarParser.ID)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 284
                self.match(AgentarParser.ASSIGN)
                self.state = 285
                self.expression(0)


            self.state = 288
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
        self.enterRule(localctx, 42, self.RULE_assignment)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = AgentarParser.SimpleAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(AgentarParser.ID)
                self.state = 291
                self.match(AgentarParser.ASSIGN)
                self.state = 292
                self.expression(0)
                self.state = 293
                self.match(AgentarParser.SEMI)
                pass

            elif la_ == 2:
                localctx = AgentarParser.IndexAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(AgentarParser.ID)
                self.state = 296
                self.match(AgentarParser.LBRACK)
                self.state = 297
                self.expression(0)
                self.state = 298
                self.match(AgentarParser.RBRACK)
                self.state = 299
                self.match(AgentarParser.ASSIGN)
                self.state = 300
                self.expression(0)
                self.state = 301
                self.match(AgentarParser.SEMI)
                pass

            elif la_ == 3:
                localctx = AgentarParser.SpawnAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(AgentarParser.ID)
                self.state = 304
                self.match(AgentarParser.ASSIGN)
                self.state = 305
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
        self.enterRule(localctx, 44, self.RULE_doStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(AgentarParser.T__14)
            self.state = 309
            self.match(AgentarParser.ID)
            self.state = 310
            self.match(AgentarParser.LPAREN)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 576472846864220160) != 0):
                self.state = 311
                self.expression(0)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 312
                    self.match(AgentarParser.COMMA)
                    self.state = 313
                    self.expression(0)
                    self.state = 318
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 321
            self.match(AgentarParser.RPAREN)
            self.state = 322
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
        self.enterRule(localctx, 46, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16711680) != 0)):
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = AgentarParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 327
                self.match(AgentarParser.NOT)
                self.state = 328
                self.expression(23)
                pass

            elif la_ == 2:
                localctx = AgentarParser.MessageAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 329
                self.match(AgentarParser.MSG)
                self.state = 332 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 330
                        self.match(AgentarParser.T__23)
                        self.state = 331
                        self.match(AgentarParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 334 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 3:
                localctx = AgentarParser.SelfAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 336
                self.match(AgentarParser.SELF)
                self.state = 339 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 337
                        self.match(AgentarParser.T__23)
                        self.state = 338
                        self.match(AgentarParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 341 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass

            elif la_ == 4:
                localctx = AgentarParser.ListExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 343
                self.listLiteral()
                pass

            elif la_ == 5:
                localctx = AgentarParser.MapExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 344
                self.mapLiteral()
                pass

            elif la_ == 6:
                localctx = AgentarParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 345
                self.literal()
                pass

            elif la_ == 7:
                localctx = AgentarParser.VarReferenceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 346
                self.match(AgentarParser.ID)
                pass

            elif la_ == 8:
                localctx = AgentarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 347
                self.match(AgentarParser.LPAREN)
                self.state = 348
                self.expression(0)
                self.state = 349
                self.match(AgentarParser.RPAREN)
                pass

            elif la_ == 9:
                localctx = AgentarParser.AgentIdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 351
                self.match(AgentarParser.AGENTID)
                pass

            elif la_ == 10:
                localctx = AgentarParser.MessageInitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 352
                self.messageInit()
                pass

            elif la_ == 11:
                localctx = AgentarParser.MsgTypeValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 353
                self.msgTypeValue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 394
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = AgentarParser.AndExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 356
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 357
                        self.match(AgentarParser.AND)
                        self.state = 358
                        self.expression(23)
                        pass

                    elif la_ == 2:
                        localctx = AgentarParser.OrExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 359
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 360
                        self.match(AgentarParser.OR)
                        self.state = 361
                        self.expression(22)
                        pass

                    elif la_ == 3:
                        localctx = AgentarParser.XorExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 362
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 363
                        self.match(AgentarParser.XOR)
                        self.state = 364
                        self.expression(21)
                        pass

                    elif la_ == 4:
                        localctx = AgentarParser.MulDivExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 365
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 366
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==51 or _la==52):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 367
                        self.expression(20)
                        pass

                    elif la_ == 5:
                        localctx = AgentarParser.AddSubExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 368
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 369
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==49 or _la==50):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 370
                        self.expression(19)
                        pass

                    elif la_ == 6:
                        localctx = AgentarParser.EqExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 371
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 372
                        self.match(AgentarParser.EQ)
                        self.state = 373
                        self.expression(18)
                        pass

                    elif la_ == 7:
                        localctx = AgentarParser.NeqExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 374
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 375
                        self.match(AgentarParser.NEQ)
                        self.state = 376
                        self.expression(17)
                        pass

                    elif la_ == 8:
                        localctx = AgentarParser.LtExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 377
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 378
                        self.match(AgentarParser.LT)
                        self.state = 379
                        self.expression(16)
                        pass

                    elif la_ == 9:
                        localctx = AgentarParser.GtExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 380
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 381
                        self.match(AgentarParser.GT)
                        self.state = 382
                        self.expression(15)
                        pass

                    elif la_ == 10:
                        localctx = AgentarParser.LeqExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 383
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 384
                        self.match(AgentarParser.LEQ)
                        self.state = 385
                        self.expression(14)
                        pass

                    elif la_ == 11:
                        localctx = AgentarParser.GeqExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 386
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 387
                        self.match(AgentarParser.GEQ)
                        self.state = 388
                        self.expression(13)
                        pass

                    elif la_ == 12:
                        localctx = AgentarParser.IndexExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 389
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 390
                        self.match(AgentarParser.LBRACK)
                        self.state = 391
                        self.expression(0)
                        self.state = 392
                        self.match(AgentarParser.RBRACK)
                        pass

             
                self.state = 398
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
        self.enterRule(localctx, 50, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(AgentarParser.LBRACK)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 576472846864220160) != 0):
                self.state = 400
                self.expression(0)
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 401
                    self.match(AgentarParser.COMMA)
                    self.state = 402
                    self.expression(0)
                    self.state = 407
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 410
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
        self.enterRule(localctx, 52, self.RULE_mapLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(AgentarParser.LBRACE)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 413
                self.match(AgentarParser.ID)
                self.state = 414
                self.match(AgentarParser.COLON)
                self.state = 415
                self.expression(0)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 416
                    self.match(AgentarParser.COMMA)
                    self.state = 417
                    self.match(AgentarParser.ID)
                    self.state = 418
                    self.match(AgentarParser.COLON)
                    self.state = 419
                    self.expression(0)
                    self.state = 424
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 427
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
        self.enterRule(localctx, 54, self.RULE_literal)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                localctx = AgentarParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(AgentarParser.INT)
                pass
            elif token in [34]:
                localctx = AgentarParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(AgentarParser.FLOAT)
                pass
            elif token in [37]:
                localctx = AgentarParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.match(AgentarParser.STRING)
                pass
            elif token in [36]:
                localctx = AgentarParser.BoolLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 432
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
        self.enterRule(localctx, 56, self.RULE_msgTypeValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8321499136) != 0)):
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
        self._predicates[24] = self.expression_sempred
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
         




