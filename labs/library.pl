/*
MIT License

Copyright (c) 2020 Daniil Shchepetilnikov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

/* Student info. */

student(123000).
student(123001).
student(123002).
student(123003).

student_name('Osipov', 123000).
student_name('Enaleev', 123001).
student_name('Smirnov', 123002).
student_name('Shulman', 123003).

group('IDB-18-01', 123000).
group('IDB-18-01', 123001).
group('IDB-18-02', 123002).
group('IDB-18-03', 123003).

/* Book info. */

book(000100).
book(000200).
book(000300).
book(000400).
book(000500).

book_name('War and Peace', 000100).
book_name('Crime and Punishment', 000200).
book_name('Lolita', 000300).
book_name('The Lord of the Rings', 000400).
book_name('Anna Karenina', 000500).

author('Tolstoy', 000100).
author('Dostoyevskiy', 000200).
author('Nabokov', 000300).
author('Tolkien', 000400).
author('Tolstoy', 000500).

year(1869, 000100).
year(1866, 000200).
year(1955, 000300).
year(1954, 000400).
year(1878, 000500).

/* Info about books, taken by students. */

taken(000100, 123000, '15-10-2020').
taken(000300, 123000, '23-10-2020').
taken(000400, 123001, '30-11-2020').
taken(000100, 123002, '04-09-2020').
taken(000200, 123002, '05-12-2020').
taken(000400, 123003, '01-02-2021').

/* Variant #2. */

question_1(Group, Author) :- group(Group, Student),
  taken(Book, Student, _), author(Author, Book),
  student_name(Name, Student), write(Name), fail.

question_2(Student) :- taken(Book, Student, Date),
  book_name(Name, Book), author(Author, Book),
  write(Name), write(' '), write(Author), write(' '),
  write(Date), write('\n'), fail.

question_3(Year) :- year(BookYear, _), BookYear > Year.

question_4(BookName) :- book_name(BookName, Number), author(Author, Number),
  author(Author, Book), taken(Book, Student, _),
  student_name(StudentName, Student), group(Group, Student),
  write(StudentName), write(' '), write(Group), write('\n'), fail.

