#include<stdio.h>
#include"main.h"
/**
 *_strcat - write  a function that concatenates two strings.
 * @dest: Describe the string 1
 * @src: Describe the string 2
 * Return: Always dest (Success)
 */
char *_strcat(char *dest, char *src)
{
	int i, j;

	for (i = 0; dest[i] != '\0'; i++)
	{
	}
	for (j = 0; src[j] != '\0'; j++)
{
	dest[i + j] = src[j];
}
		return (dest);
}
/**
 *_strncat - write  a function that concatenates two strings.
 * @dest: Describe the string 1
 * @src: Describe the string 2
 * @n:  Describ the integer
 * Return: Always dest (Success)
 */
char *_strncat(char *dest, char *src, int n)
{
	int i, j;

	for (i = 0; dest[i] != '\0'; i++)
	{
	}
	for (j = 0; j < n;  j++)
	dest[i + j] = src[j];
		return (dest);

}
/**
 *_strncpy - write  a function that concatenates two strings.
 * @dest: Describe the string 1
 * @src: Describe the string 2
 * @n:  Describ the integer
 * Return: Always dest (Success)
 */
char *_strncpy(char *dest, char *src, int n)
{
	int i;

	if (n > 0)
{
	for (i = 0; i < n; i++)
{
	dest[i] = src[i];
}
		return (dest);
}
		else
		return (dest);
}
/**
 *_strcmp  - write  a function that concatenates two strings.
 * @s1: Describe the string 1
 * @s2: Describe the string 2
 * Return: Always 0 (Success)
 */
int _strcmp(char *s1, char *s2)
{
	int i, n;

	for (i = 0; s1[i] != '\0'; i++)
{
	if (s1[i] == s2[i])
	n = 0;

	else if (s1[i] > s2[i])
{
	n = (s1[i] - s2[i]);
	break;
}

	else
{
	n = (s1[i] - s2[i]);
	break;
}
}
	return (n);
}
/**
 *_memset -  fills memory with a constant byte.
 *@s: discripe the array
 *@b: discripe the array
 *@n: discripe the array
 *Return: 0 always success
 */
char *_memset(char *s, char b, unsigned int n)
{
}
