#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;

	printf("-----------------\n");

	insert_node(&head, 27);
	insert_node(&head, 10);
	insert_node(&head, 1);
	insert_node(&head, 50);

	print_listint(head);

	printf("-----------------\n");
	free_listint(head);

	return (0);
}
