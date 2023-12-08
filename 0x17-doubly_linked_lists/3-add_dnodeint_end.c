#include "lists.h"
/**
 * add_dnodeint_end - adds a node to the end of the list
 * @head: head node of our list
 * @n: the element to store in the node
 * Return: address of new node
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *tempPointer;
	dlistint_t *newNode;

	newNode = malloc(sizeof(dlistint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = n;

	if (*head == NULL)
	{
		newNode->prev = NULL;
		newNode->next = NULL;

		*head = newNode;
	}
	else
	{
		tempPointer = *head;
		while (tempPointer->next != NULL)
		{
			tempPointer = tempPointer->next;
		}
		newNode->prev = tempPointer;
		newNode->next = NULL;
		tempPointer->next = newNode;
	}
	return (newNode);
}
