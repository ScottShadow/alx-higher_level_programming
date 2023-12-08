#include "lists.h"
/**
 * add_dnodeint - adds a node to the beginning of a list
 * @head: head node of our list
 * @n: the element to store in the node
 * Return: address of new node
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *newNode;

	newNode = malloc(sizeof(dlistint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->prev = NULL;
	newNode->n = n;
	newNode->next = *head;
	*head = newNode;

	return (newNode);
}
