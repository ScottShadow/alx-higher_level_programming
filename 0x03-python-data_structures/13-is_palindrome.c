#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

int list_size(listint_t **head)
{
	ssize_t size = 0;
	listint_t *temp = *head;

	while (temp != NULL)
	{
		size++;
		temp = temp->next;
	}
	return (size);
}
int is_palindrome(listint_t **head)
{
	int *tempArray = NULL;
	int *tempArrayPointer = NULL;
	int i, size;
	listint_t *tempPointer = *head;
	int isPalindrome = 1;

	if (head)
	{
		size = list_size(head);
		tempArray = malloc(sizeof(int) * size);
		if (tempArray == NULL)
			return (0);
		tempArrayPointer = tempArray;
		while (tempPointer != NULL)
		{
			*tempArrayPointer = tempPointer->n;
			tempArrayPointer++;
			tempPointer = tempPointer->next;
		}
		for (i = 0; i < size / 2; i++)
		{
			if (tempArray[i] != tempArray[size - i - 1])
				isPalindrome = 0;
			else
				isPalindrome = 1;
		}
		return (isPalindrome);
	}
	return (isPalindrome);
}
