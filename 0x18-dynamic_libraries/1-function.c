#include<stdio.h>
#include"main.h"
#include <unistd.h>

/**
 * _putchar - writes the character c to stdout
 * @c: The character to print
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
int _putchar(char c)
{
	return (write(1, &c, 1));
}
/**
 *_islower - checks for lowercase character
 *@c: The character to print
 *
 * Return: On success 1.
 */
int _islower(int c)
{
int N = (int) (c);
if (N >= 97 && N <= 122)
	return (1);
else
	return (0);
}
/**
 *_isalpha - checks for all characters
 *@c: The character to print
 *
 * Return: On success 1.
 */
int _isalpha(int c)
{
int N = (int) (c);
if ((N >= 97 && N <= 122) || (N >= 65 && N <= 90))
	return (1);
else
	return (0);
}
/**
 *_abs - prints the signs of number
 *@n: The int to print
 *
 * Return: On success i.
 */
int _abs(int n)
{
int i = n;

	if (i > 0)
{
	i *= 1;
	return (i);
}
	else if (i == 0)
{
	i *= 1;
	return (i);
}
	else
{
	i *= -1;
	return (i);
}
}
/**
 *_isupper - checks for uppercase character
 *@c: The character to print
 *
 * Return: On success 1.
 */
int _isupper(int c)
{
int N = (int) (c);
if (N >= 65 && N <= 90)
	return (1);
else
	return (0);
}
