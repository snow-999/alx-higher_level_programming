#include "lists.h"
/**
 * is_palindrome - cheak if palindorme
 * @head: the start node
 * Return: 1 
 *
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	return (auxPalind(head, *head));
}
/**
 * auxPalind - cheack how is palindorme
 * @head: start node
 * @e: the end node
 * Return: 1 or thr last node
*/
int auxPalind(listint_t **head, listint_t *e)
{
	if (e == NULL)
	{
		return (1);
	}
	if (auxPalind(head, e->next) && (*head)->n == e->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
