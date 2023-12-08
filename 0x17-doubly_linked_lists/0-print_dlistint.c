#include "lists.h"
/**
 * print_dlistint - prints the whole list
 * @h:header node of the list to print
 * Return: size of elements printed
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t size = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		size++;
	}
	return (size);
}
