SQL + JOIN RECALL NOTES
========================

Purpose
-------
Ye notes quick revision ke liye hain. Jab JOIN, GROUP BY, HAVING, COUNT,
AVG, MAX, MIN, SUM, WHERE ya ORDER BY bhool jao, is file ko recall sheet
ki tarah use karo.


1. SQL QUERY KA BASIC FLOW
--------------------------

Learning ke liye is order ko yaad rakho:

SELECT
  ↓
FROM
  ↓
JOIN + ON
  ↓
WHERE
  ↓
GROUP BY
  ↓
HAVING
  ↓
ORDER BY
  ↓
LIMIT

Important:
- WHERE individual rows ko filter karta hai.
- GROUP BY rows ko groups mein divide karta hai.
- HAVING groups ko filter karta hai.
- ORDER BY result ko sort karta hai.
- LIMIT result ki rows ki maximum number set karta hai.

Note:
Ye learning/mental model hai. SQL engine internally query ko isi exact
order mein execute nahi karta.


2. FROM A JOIN B — LEFT AUR RIGHT KAISE PEHCHANE
-----------------------------------------------

Sabse important rule:

FROM ke baad wali table = LEFT table
JOIN ke baad wali table = RIGHT table

Example:

FROM course
LEFT JOIN student

Position:

course              student
  LEFT                RIGHT

Example:

FROM student
LEFT JOIN course

Position:

student              course
  LEFT                RIGHT

IMPORTANT:
"LEFT JOIN student" ka matlab ye nahi ki student LEFT hai.
student LEFT JOIN ke baad likha hai, isliye student RIGHT side par hai.

Hamesha table ki POSITION dekho.


3. INNER JOIN
-------------

Basic form:

SELECT ...
FROM A
INNER JOIN B
ON A.column = B.column;

JOIN alone bhi normally INNER JOIN hota hai:

FROM A
JOIN B
ON A.column = B.column;

Rule:

INNER JOIN = sirf matching rows

Example:

student.course_id = course.course_id

Agar student aur course ka course_id match karta hai,
to row result mein aayegi.

Agar match nahi karta, row nahi aayegi.

Shortcut:

INNER = MATCH ONLY


4. LEFT JOIN
------------

Basic form:

FROM A
LEFT JOIN B
ON A.column = B.column;

Rule:

LEFT JOIN = LEFT table ki saari rows + matching RIGHT data

Example:

FROM course
LEFT JOIN student
ON student.course_id = course.course_id;

Position:

course       student
LEFT         RIGHT

Isliye course ki SAARI rows preserve hongi.

Agar course ka koi student nahi hai:

MBA | NULL

Shortcut:

LEFT JOIN = LEFT SAFE


5. RIGHT JOIN
-------------

Basic form:

FROM A
RIGHT JOIN B
ON A.column = B.column;

Rule:

RIGHT JOIN = RIGHT table ki saari rows + matching LEFT data

Example:

FROM student
RIGHT JOIN course
ON student.course_id = course.course_id;

Position:

student      course
LEFT         RIGHT

Isliye course ki SAARI rows preserve hongi.

MBA ka student nahi hone par bhi:

MBA | NULL

Shortcut:

RIGHT JOIN = RIGHT SAFE


6. JOIN KA GOLDEN MEMORY RULE
----------------------------

FROM A JOIN B

        A           B
        ↓           ↓
      LEFT        RIGHT

Then:

INNER JOIN -> matching only
LEFT JOIN  -> LEFT table all rows
RIGHT JOIN -> RIGHT table all rows

Bas position dekho. JOIN ke naam mein table ka naam mat dhoondo.


7. ON CLAUSE
------------

JOIN ke baad matching condition ON mein likhte hain.

Example:

ON student.course_id = course.course_id

Meaning:

student table ka course_id
        =
course table ka course_id

Jab values match hoti hain, tables ke related rows connect hoti hain.


8. SELECT MEIN TABLE.COLUMN
---------------------------

Agar dono tables mein same naam ka column ho, table name ke saath
column likhna safe aur clear hota hai.

Example:

SELECT student.name, course.course_name

Meaning:

student table se name
course table se course_name


9. WHERE
--------

WHERE individual rows ko filter karta hai.

Example:

SELECT student.name, course.course_name, student.marks
FROM student
JOIN course
ON student.course_id = course.course_id
WHERE student.marks >= 70;

Meaning:

Pehle matching student-course data,
phir marks >= 70 wali rows.

WHERE = ROW FILTER


10. GROUP BY
------------

GROUP BY same value wali rows ko groups mein divide karta hai.

Example:

SELECT course, COUNT(*)
FROM student
GROUP BY course;

Meaning:

Har course ka alag group banao,
phir har group par COUNT lagao.

GROUP BY = GROUP BANANA


11. AGGREGATE FUNCTIONS
-----------------------

COUNT(*)       -> rows count karta hai
COUNT(column)  -> column ki non-NULL values count karta hai
AVG(column)    -> average
MAX(column)    -> maximum
MIN(column)    -> minimum
SUM(column)    -> total/sum

Examples:

COUNT(*)
AVG(student.marks)
MAX(student.marks)
MIN(student.marks)
SUM(student.marks)


12. COUNT(*) VS COUNT(column)
-----------------------------

Very important.

COUNT(*) = rows count karta hai.

COUNT(student.id) = student.id ki non-NULL values count karta hai.

LEFT JOIN mein unmatched row ke right-side columns NULL hote hain.

Example:

SELECT course.course_name,
       COUNT(student.id)
FROM course
LEFT JOIN student
ON student.course_id = course.course_id
GROUP BY course.course_name;

MBA ka koi student nahi hai.

MBA | 0

Why?

MBA ke unmatched row mein:

student.id = NULL

COUNT(student.id) NULL ko count nahi karta.

Important:
Agar yahan COUNT(*) use karoge, unmatched LEFT JOIN row bhi count ho
sakti hai, aur MBA ke liye 1 aa sakta hai. Student count ke liye
COUNT(student.id) ya kisi guaranteed non-NULL student column ko count
karna better hai.


13. HAVING
----------

HAVING GROUP ko filter karta hai.

Example:

SELECT course.course_name,
       COUNT(student.id) AS student_count
FROM course
LEFT JOIN student
ON student.course_id = course.course_id
GROUP BY course.course_name
HAVING COUNT(student.id) > 1;

Result:

MCA | 2

Meaning:

- GROUP BY ne course-wise groups banaye.
- COUNT ne har group mein students count kiye.
- HAVING ne sirf count > 1 wale groups rakhe.

HAVING = GROUP FILTER


14. WHERE VS HAVING
-------------------

WHERE:

WHERE marks >= 70

Individual rows filter karta hai.

HAVING:

HAVING COUNT(student.id) > 1

Groups filter karta hai.

Easy memory:

WHERE  -> ROWS
HAVING -> GROUPS


15. ALIAS
---------

Alias kisi column ko temporary readable naam deta hai.

Example:

COUNT(student.id) AS student_count

AVG(student.marks) AS avg_marks

Then ORDER BY mein alias use kar sakte hain:

ORDER BY student_count DESC

PostgreSQL mein HAVING ke andar SELECT alias ko directly use karna
generally valid nahi hota in this situation.

Wrong:

HAVING student_count > 1

Correct:

HAVING COUNT(student.id) > 1


16. ORDER BY
------------

ORDER BY result ko sort karta hai.

ASC = ascending = chhote se bade
DESC = descending = bade se chhote

Example:

ORDER BY student_count ASC

0, 1, 1, 2

Example:

ORDER BY student_count DESC

2, 1, 1, 0

Important:
ORDER BY ko FROM se pehle nahi likhte.

Wrong:

SELECT ...
ORDER BY student_count ASC
FROM course ...

Correct:

SELECT ...
FROM course ...
GROUP BY ...
ORDER BY student_count ASC;


17. NULL
--------

NULL ka matlab missing/unknown value hai.

NULL normal value nahi hai.

Wrong:

WHERE marks = NULL

Correct:

WHERE marks IS NULL

Non-NULL:

WHERE marks IS NOT NULL

Important:

NULL = NULL
is not TRUE.

SQL NULL comparisons special behavior follow karte hain.

Aggregate reminder:

COUNT(column) NULL values ko count nahi karta.

AVG, MAX, MIN, SUM bhi NULL values ko generally ignore karte hain,
lekin agar group mein koi non-NULL value hi nahi hai to result NULL ho
sakta hai.

Example:
MBA ka koi student nahi hai:

MAX(student.marks) -> NULL


18. CURRENT PRACTICE TABLES
---------------------------

student:

id   name    age   course    marks   course_id
102  Rahul   22    B.TECH    100     1
103  Priya   21    BBA       62      2
104  Ramesh  25    MCA       70      3
105  Raju    26    MCA       69      3

course:

course_id   course_name
1           B.TECH
2           BBA
3           MCA
4           MBA


19. MOST IMPORTANT JOIN EXAMPLES
--------------------------------

A. INNER JOIN

SELECT student.name, course.course_name
FROM student
JOIN course
ON student.course_id = course.course_id;

Result:

Rahul   | B.TECH
Priya   | BBA
Ramesh  | MCA
Raju    | MCA

MBA nahi aayega because matching student nahi hai.


B. COURSE KI SAARI ROWS CHAHIYE

SELECT student.name, course.course_name
FROM course
LEFT JOIN student
ON student.course_id = course.course_id;

Result:

Rahul   | B.TECH
Priya   | BBA
Ramesh  | MCA
Raju    | MCA
        | MBA

Course LEFT side hai, isliye course ki saari rows preserve hoti hain.


C. RIGHT JOIN SE COURSE KI SAARI ROWS

SELECT student.name, course.course_name
FROM student
RIGHT JOIN course
ON student.course_id = course.course_id;

Right side course hai, isliye course ki saari rows preserve hoti hain.


D. JOIN + WHERE

SELECT student.name,
       course.course_name,
       student.marks
FROM student
JOIN course
ON student.course_id = course.course_id
WHERE student.marks >= 70;

Result:

Rahul   | B.TECH | 100
Ramesh  | MCA    | 70


E. COURSE-WISE STUDENT COUNT

SELECT course.course_name,
       COUNT(student.id) AS student_count
FROM course
LEFT JOIN student
ON student.course_id = course.course_id
GROUP BY course.course_name;

Result conceptually:

B.TECH | 1
BBA    | 1
MCA    | 2
MBA    | 0


F. ONLY COURSES WITH MORE THAN 1 STUDENT

SELECT course.course_name,
       COUNT(student.id) AS student_count
FROM course
LEFT JOIN student
ON student.course_id = course.course_id
GROUP BY course.course_name
HAVING COUNT(student.id) > 1;

Result:

MCA | 2


G. COURSE-WISE AVERAGE, ONLY AVG > 65

SELECT course.course_name,
       AVG(student.marks) AS avg_marks
FROM student
JOIN course
ON student.course_id = course.course_id
GROUP BY course.course_name
HAVING AVG(student.marks) > 65;

Result:

MCA    | 69.5
B.TECH | 100


H. COURSE-WISE MAX MARKS INCLUDING MBA

SELECT course.course_name,
       MAX(student.marks) AS max_marks
FROM course
LEFT JOIN student
ON student.course_id = course.course_id
GROUP BY course.course_name;

Result:

B.TECH | 100
BBA    | 62
MCA    | 70
MBA    | NULL


20. QUICK RECALL — 30 SECOND VERSION
------------------------------------

JOIN:
    Tables ko common column ke basis par connect karo.

FROM A JOIN B:
    A = LEFT
    B = RIGHT

INNER:
    Matching only.

LEFT:
    LEFT table ki all rows.

RIGHT:
    RIGHT table ki all rows.

ON:
    Matching condition.

WHERE:
    Rows filter.

GROUP BY:
    Groups banao.

COUNT:
    Count.

AVG:
    Average.

MAX:
    Maximum.

MIN:
    Minimum.

SUM:
    Total.

HAVING:
    Groups filter.

ORDER BY:
    Sort.

ASC:
    Small -> Large.

DESC:
    Large -> Small.

NULL:
    Missing/unknown.

IS NULL:
    NULL find.

IS NOT NULL:
    Non-NULL find.

COUNT(column):
    NULL ko count nahi karta.


21. ONE-LINE MEMORY TRICK
-------------------------

"FROM se LEFT/RIGHT dekho,
ON se matching karo,
WHERE se rows filter karo,
GROUP BY se groups banao,
HAVING se groups filter karo,
ORDER BY se sort karo."

End of recall sheet.
