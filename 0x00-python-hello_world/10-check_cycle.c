#include "lists.h"
/**
 * check_cycle - checks if the list if in an infinite cycle and return 1
 * @list: the head of the list
 * Return: 0(Fail) or 1(Success)
 */
int check_cycle(listint_t *list)
{
	listint_t *testList = list;
	listint_t *tempList = list;

	while (testList != NULL && tempList != NULL && tempList->next != NULL)
	{
		testList = testList->next;
		tempList = tempList->next->next;
		if (testList == tempList)
			return (1);
	}
	return (0);
}
