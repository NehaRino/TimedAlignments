# TimedAlignments
Implementations of algorithms for aligning observation traces to time Petri net process models, over several metrics. 

testalign.py contains the testing section, that calls mixalign (from mixalign.py) that calculates mixed move alignments between traces and linear process models, and stampalign (from stampalign.py) that does the same but using stamp only distance. The trace is a list of timestamps, and linear process models are lists of interval constraints (as defined by the class LineModel). PWLCGraph.py and auxfunc.py both contain objects and functions useful for the stamp only distance alignment algorithm. 
