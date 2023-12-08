#include "lists.h"
/**
 * insert_dnodeint_at_index - inserts a new node at a given position.
 * @head: address of header node
 * @idx: index at which we want to enter our elemnt into
 * @n: the value of the element to insert
 * Return: address of the newnode
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **head,
									 unsigned int idx, int n)
{
	dlistint_t *p;
	dlistint_t *newnode;
	unsigned int i = 0;

	if (!head || (*head == NULL && idx != 0))
		return (NULL);
	newnode = malloc(sizeof(dlistint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = n;
	if (idx == 0)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	p = *head;

	for (i = 0; (p != NULL) && (i < (idx - 1)) && (idx > 0); i++)
		p = p->next;
	if (p == NULL)
	{
		free(newnode);
		return (NULL);
	}

	newnode->next = p->next;
	p->next = newnode;

	return (newnode);
}
