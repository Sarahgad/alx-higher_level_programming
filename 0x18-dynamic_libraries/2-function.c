#include<stdio.h>
#include"main.h"
/**
 *_isdigit  - checks for digit
 *@c: The character to print
 *
 * Return: On success 1.
 */
int _isdigit(int c)
{
int N = (int) (c);
if (N >= 48 && N <= 57)
	return (1);
else
	return (0);
}
/**
 * _strlen - writes the character c to stdout
 * @s : Decribe the char arry
 * Return: On success i.
 */
int _strlen(char *s)
{
	int i;

	for (i = 0; s[i] != '\0'; i++)
	{
	}
		return (i);
}
/**
 * _puts - writes the character c to stdout
 * @str : Decribe the char arry
 */
void _puts(char *str)
{
	int i;

	for (i = 0; str[i] != '\0'; i++)
	{
		putchar(str[i]);
	}
		putchar('\n');
}
/**
 *_strcpy - write  a function that concatenates two strings.
 *@dest: Describe the string 1
 *@src: Describe the string 2
 *Return: Always dest (Success)
 */
char *_strcpy(char *dest, char *src)
{
}
#include<stdio.h>
#include"main.h"
/**
 *_atoi - Write a function that searches a string for any of a set of bytes.
 *@s: discripe the array
 *Return: 0 always success
 */
int _atoi(char *s)
{
}
