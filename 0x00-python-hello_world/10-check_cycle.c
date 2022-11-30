#include "lists.h"

/**
 * check_cycle - function to check if singly linked list has a cycle
 * @list: head pointer to singly linked list
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *mylist;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	mylist = list;
	while (mylist->next != NULL && mylist->next->next != NULL)
	{
		list = list->next;
		mylist = mylist->next->next;
		if (list == mylist)
			return (1);
	}
	return (0);
}
