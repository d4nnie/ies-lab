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

/* Clauses. */

man('Daniil').
man('Viktor').
man('Andrey').
man('Yuriy').

woman('Marina').
woman('Natalya').
woman('Tamara').
woman('Nina').
woman('Olga').

parent('Andrey', 'Daniil').
parent('Marina', 'Daniil').
parent('Marina', 'Olga').
parent('Yuriy', 'Andrey').
parent('Yuriy', 'Natalya').
parent('Tamara', 'Andrey').
parent('Tamara', 'Natalya').
parent('Nina', 'Sergey').
parent('Nina', 'Marina').

married('Andrey', 'Marina').
married('Yuriy', 'Tamara').
married('Viktor', 'Olga').

/* Some usefull procedures. */

sibling(X, Y) :- parent(Z, X), parent(Z, Y).
sister(X, Y) :-  woman(X), sibling(X, Y).
brother(X, Y) :- man(X), sibling(X, Y).
father(X, Y) :- man(X), parent(X, Y).

/* Variant #2. */

grandson(X, Y) :- man(Y), parent(Z, Y), parent(X, Z).
aunt(X, Y) :- sister(X, Z), parent(Z, Y).
father_in_law(X, Y) :- woman(Y), married(Z, Y), father(X, Z).
brother_in_law(X, Y) :-  man(Y), married(Y, Z), brother(X, Z).

