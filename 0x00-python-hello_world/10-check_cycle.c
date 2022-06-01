#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: listint_t list
 *
 * Return: 1 if there is a cycle in the list. Otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (fast == slow)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
