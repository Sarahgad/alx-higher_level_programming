#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include"lists.h"
/**
 *insert_node - insert node
 *@head: pointer
 *@number: int
 *Return: new always success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *previous;

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	current = *head;
	previous = NULL;

	while (current != NULL && current->n < new->n)
	{
	previous = current;
	current = current->next;
	}
	if (previous == NULL)
	{
	new->next = *head;
	*head = new;
	}
	else
	{
	previous->next = new;
	new->next = current;
	}

	return (new);
}
