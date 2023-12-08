#include "lists.h"
/**
 * dlistint_len - calculates the size of a list
 * @h: header node of our list
 * Return: size of the list
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t size = 0;

	for (; h; h = h->next)
		size++;

	return (size);
}
