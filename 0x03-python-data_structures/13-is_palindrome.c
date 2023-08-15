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
	listint_t *fast = *head, *slow = *head;
	listint_t *firsthalf = *head;
	listint_t *secondhalf = NULL;
	listint_t *prev_slow = NULL;
	listint_t *mid_node = NULL;
	int is_palindrome = 1;

	if (*head == NULL && (*head)->next == NULL)
		return (is_palindrome);
	while (fast != NULL && fast->next != NULL)
{
	fast = fast->next->next;
	prev_slow = slow;
	slow = slow->next;
}
	if (fast != NULL)
	{
	mid_node = slow;
	slow = slow->next;
	}
	secondhalf = reverselist(&slow);
	while (secondhalf != NULL)
	{
	if ((firsthalf)->n != secondhalf->n)
	{
		is_palindrome = 0;
		break;
	}
	firsthalf = firsthalf->next;
	secondhalf = secondhalf->next;
	}
	    reverselist(&slow);
	if (mid_node != NULL)
	{
	prev_slow->next = mid_node;
	mid_node->next = slow;
	}
	else
		prev_slow->next = slow;
	return (is_palindrome);
}
