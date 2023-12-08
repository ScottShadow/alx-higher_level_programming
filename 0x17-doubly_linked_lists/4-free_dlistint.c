#include "lists.h"
/**
 * free_dlistint - frees doubly linked lists
 * @head: the head node of the list to free
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *tempPointer;
	dlistint_t *currentPointer = head;

	while (currentPointer != NULL)
	{
		tempPointer = currentPointer->next;
		free(currentPointer);
		currentPointer = tempPointer;
	}
}
