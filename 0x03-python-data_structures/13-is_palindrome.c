#include<stdio.h>
#include "lists.h"
/**
 *reverselist - reverse the linkedlist
 *@head: pointer
 *Return: *head always success
 */
listint_t *reverselist(listint_t **head)
{
listint_t *prev, *curr, *next;
prev = NULL;
curr = *head;
next = *head;

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
listint_t *fast, *slow, *secondhalf, *firsthalf ;

	fast = *head;
	slow = *head;
	if (*head == NULL && (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
{
	fast = fast->next->next;
	slow = slow->next;
}
	 if (fast != NULL)
    {
        secondhalf = slow->next;
    }
    else
    {
        secondhalf = slow;
    }

	secondhalf = reverselist(&(secondhalf));
	firsthalf = *head;

	while (firsthalf != NULL && secondhalf != NULL)
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
