#include<stdio.h>
#include "lists.h"
listint_t *reverselist(listint_t *head);
/**
 *reverselist - reverse the linkedlist
 *@head: pointer
 *Return: prev always success
 */
listint_t *reverselist(listint_t *head)
{
listint_t *prev, *curr, *next;
prev = NULL;
next = curr = head;
while (curr != NULL)
{
	next = next->next;
	curr->next = prev;
	prev = curr;
	curr = next;
}
return (prev);
}
/**
 *is_palindrome - check plaindrome
 *@head: pointer
 *Return: 1 always success
 */
int is_palindrome(listint_t **head)
{
listint_t *fast, *slow, *secondhalf, *firsthalf;
	fast = *head;
	slow = *head;
	firsthalf = *head;
	if (*head == NULL && (*head)->next == NULL)
		return (1);

	while (fast->next->next != NULL && fast->next != NULL)
{
	fast = fast->next->next;
	slow = slow->next;
}

	secondhalf = reverselist(slow->next);

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
