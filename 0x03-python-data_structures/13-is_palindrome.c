#include<stdio.h>
#include "lists.h"
listint_t *reverselist(listint_t **head);
/**
 *reverselist - reverse the linkedlist
 *@head: pointer
 *Return: prev always success
 */
listint_t *reverselist(listint_t **head)
{
listint_t *prev, *curr, *next;
prev = NULL;
curr = *head;
next = NULL;

while (curr != NULL)
{
	next = curr->next;
	curr->next = prev;
	prev = curr;
	curr = next;
}
*head = prev;
return (*head);
}
/**
 *is_palindrome - check plaindrome
 *@head: pointer
 *Return: 1 always success
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL && (*head)->next == NULL)
		return (1);
listint_t *fast, *slow, *secondhalf, *firsthalf;
	fast = *head;
	slow = *head;
	firsthalf = *head;

	while (fast->next != NULL && fast->next->next != NULL)
{
	fast = fast->next->next;
	slow = slow->next;
}

	secondhalf = reverselist(&(slow->next));

	while (secondhalf != NULL)
	{
	if ((firsthalf)->n != secondhalf->n)
	{
		return (0);
	}
	firsthalf = firsthalf->next;
	secondhalf = secondhalf->next;
	}
	return (1);
	}
