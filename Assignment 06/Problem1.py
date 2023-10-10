Programming Assignment 3
Problem 1
A) 
line 9:		Θ(1)
line 10:	Θ(n)
line 11:	Θ(1)
line 12 - 13:	n*Θ(1)
line 19:	Θ(1)
line 20 - 23:	n*Θ(1)
line 25 - 28:	Θ(1)
sum:		Θ(1)+Θ(n)+Θ(1)+n*Θ(1)+Θ(1)+n*Θ(1)+Θ(1) = Θ(3*n) + 4*Θ(1) = Θ(n)

B)
line 8 - 9:	Θ(1)
line 10 - 18:	n*Θ(1)
line 21 - 24:	Θ(1)
sum:		Θ(n)

Problem 2
A)
line 11:	n*Θ(1)
line 12:	n*Θ(1)
line 14:	Θ(1)
line 17 - 18:	Θ(1)
line 19 - 20:	Θ(1)
line 21 - 24:	n*Θ(1)
line 25 - 28:	Θ(1)
sum:		Θ(n)

B)
line 8:		n*Θ(1)
line 9:		n*Θ(1)
line 12 - 15:	n*Θ(1)
sum:		Θ(n)

C)
line 8:		n*Θ(1)
line 9:		n*Θ(1)
line 11:	Θ(1)
line 13 - 14:	Θ(1)
line 23 - 27:	n*(n*Θ(1))
line 28:	Θ(1)
line 29 - 32:	n*Θ(1)
line 33 - 36:	Θ(1)
sum:		Θ(n^2)

Problem 3
A)
line 8:		n*O(1)
line 9 - 11:	O(1)
line 12 - 20:	n*[(n-i)*((j+1-i)*O(1))] = O(n^3) {worst case when i = 0 and j = n-1}
line 24 - 27:	n*O(1) {worst case printing all sequence}
sum:		O(n^3)

B)
line 10:	n*O(1)
line 11 - 13:	O(1)
line 14 - 20:	n*[(n-i)*(O(n))] = O(n^3)
line 24 - 27:	n*O(1)
sum:		O(n^3)

C)
line 8:		n*Θ(1)
line 9 - 11:	Θ(1)
line 12 - 20:	n*[(n-i)*(Θ(1))] = Θ(n^2)
line 24 - 27:	n*Θ(1) 
sum:		Θ(n^2)

D)
line 8:		n*Θ(1)
line 9 - 13:	Θ(1)
line 14 - 26:	n*Θ(1) = Θ(n)
line 30 - 33:	n*Θ(1) 
sum:		Θ(n)

Programming Assignment 4
Problem 1
Worst case: Θ(n). The word is a palindrome and we run through the length of the word n/2.
Best case: Θ(1). The first and last letter do not match. The loop will break from the first iteration.
Problem 2
B)
Worst case: Θ(n). The code will run through the list from start=0 to end=n.
Best case: Θ(1). The code will run for 1 element of the list start=end.
C)
Worst case: Θ(n^2). The code will run n(n+1)/2 times.
Best case: Θ(n^2). The code will still run n(n+1)/2 times.
Problem 3
A)
Worst case: O(n^3). All characters are the same, i.e. 'aaaaaaaa'.
Best case: O(n^2). The word has no similar characters, i.e. 'abcdef'.
B)
Worst case: O(n^3). All characters are the same, i.e. 'aaaaaaaa'.
Best case: O(n^2). The word has no similar characters, i.e. 'abcdef'.
C)
Worst case: Θ(n^2). All characters are the same, i.e. 'aaaaaaaa'.
Best case: Θ(n). The word has no similar characters, i.e. 'abcdef'.