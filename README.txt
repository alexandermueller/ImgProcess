README - ImgProcess 
Alexander Mueller
Jan 7, 2017

How to run:

simply cd into the ImgProcess directory and call: "$ ./ImgProcess.py"
this should tell you what commands and arguments you have 
available to you at each step of the assignment along with
the proper instruction format! 

Note: I've also included the source file inside 
the Assets/Images/Inputs folder as an example of where the 
input images are contained, otherwise place the desired image 
in there and then call the script using that image's name, 
as required.

When Testing:

1. Place the calibration file and source file for each test inside the ./ImgProcess/Tests/Images/Inputs folder,
   and the expected result file inside the ./ImgProcess/Tests/Images/Expected folder. 
2. Name each file like so: (calibration file) -> "calibration_<test #>.png", 
                                (source file) -> "<[match, mismatch]>_source_<test #>.png",
			      (expected file) -> "<test #>_<[match, mismatch]>.png"
   Eg: calibration_1.png, match_source_1.png, 1_match.png
   
   The match/mismatch prefix tells the test executable which of the tests are expected to match/mismatch. If the 
   expectation image does not match the output image, then the test passes if the files have 'mismatch' in their 
   names, otherwise it fails.

 