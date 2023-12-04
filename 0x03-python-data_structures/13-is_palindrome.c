#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
/**
 * list_size - returns the amount of elements in a list
 * @head: the header node of the list
 * Return: size of the list
 */
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
/**
 * is_palindrome - checks whether a list is a palindrome or not
 * @head: header node of the list
 * Return: 1 (True) if the list is a palindrome else 0 (Fail)
 */
int is_palindrome(listint_t **head)

{
	int *tempArray = NULL;
	int *tempArrayPointer = NULL;
	int i, size;
	listint_t *tempPointer = *head;
	int isPalindrome = 1;

	if (head == NULL)
		return (1);
	else if (head)
	{
		size = list_size(head);
		if (size == 1)
			return (isPalindrome);
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
			{
				isPalindrome = 0;
				break;
			}
		}
		tempArrayPointer = NULL;
		free(tempArray);
		return (isPalindrome);
	}
	return (isPalindrome);
}
