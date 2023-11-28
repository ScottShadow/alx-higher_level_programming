#include "lists.h"
/**
 * insert_node - inserts node element in order
 * @head: the head pointer of the list to insert to
 * @number: the value of the list element to insert
 * Return: address of the element inserted or NULL(fail)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prevPointer, *tempPointer = *head;
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	if (*head == NULL)
	{
		*head = newNode;
		newNode->next = NULL;
	}
	else
	{
		prevPointer = *head;
		while (tempPointer != NULL)
		{
			if (tempPointer->n > number && tempPointer == *head)
			{
				newNode->next = *head;
				*head = newNode;
				return (newNode);
			}
			if (tempPointer->n > number)
			{
				newNode->next = prevPointer->next;
				prevPointer->next = newNode;
				return (newNode);
			}

			prevPointer = tempPointer;
			tempPointer = tempPointer->next;
		}
		newNode->next = NULL;
		prevPointer->next = newNode;
	}
	return (newNode);
}
