<h1 align="center">IS 340 Final Project</h1>
<h3 align= "center">Business Application Programming</h3>

<h4 align="center">CALIFORNIA STATE UNIVERSITY, LONG BEACH</h4>
<h4 align="center">IS 340 – Business Application Programming</h4>
<h4 align="center">Fall 2014 Term – Session 1</h4>

<h1 align="center">Project Description</h1>
<p>
  IS340 final project<br>   
  Due on 12/07 Sunday 11:59pm<br>
  <br>
  Please name your file as Firstname_Lastname_finalproject.py and upload it to Beachboard dropbox. 
  Please write a Python program that performs CRUD (create, read, update and delete) of student grades. 
  When started, the program displays the following menu:
  Please select an operation by enter a number:
  1. Create    2. Read    3. Update      4. Delete    5. Quite<br>
  
  When a user enters a valid number (1 – 5), perform the corresponding action. Otherwise, display “wrong input, please enter a number between 1 and 5”. <br>
  <br>
  If enter “1”,  display “please enter a student name and score  between 0 and 100 separated by a space: ”
  If an input is a valid value, for example “Alice  95”, save the name and the score. Otherwise, display “invalid input, please enter a student name and score  between 0 and 100 separated by a space: ”.
  If a student name exists, display “please select 3 to update a student’s score”. <br>
  <br>
  If select “2”, display “please enter a student name to find score and grade”.  If an input is a valid vale, the program displays name, score and grade such as “Alice 95 A”.  The search should be case-insensitive, i.e., “alice” and ALiCE” should match “Alice”.   The student gets an A if his/her score is >= 90; B if  >= 80; C if >=70; D if >=60; F if <60.  If not found, display “not student found for ALICEE” where “ALICEE” is a no-existing input value. <br>
  <br>
  If select “3”, display “please enter a student name and score  between 0 and 100 separated by a space: ”. If it is an existing student name, update his/her score. Otherwise display an error message: “Unknown student name, please input a valid name.” If the input value is not valid, display “invalid input, please enter a student name and score  between 0 and 100 separated by a space: ”.<br>
  <br>
  
  If select “4”, display “please enter a student name to be deleted:”. Find a student record and delete it. If not found, display a message. <br>
  <br>
  If select “5”, exit the program. 
  <br>
  <br>
   
  You save your data into a CSV file named “student_score.txt”. You need read/write the file. 
  <br>
  
  Extra credit 50 points: if your program has a GUI.
</p>
