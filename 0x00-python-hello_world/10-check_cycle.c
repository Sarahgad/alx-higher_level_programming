#include"lists.h"
/**
 *check_cycle - detect the cycle of the linked list
 *@list: the pointer
 *Return: 0 always success
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
