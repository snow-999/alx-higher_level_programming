#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insetr a node
 * @head: first node
 * @number: number will be given to insetr
 * Return: node , NULL
 *
 *
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *Onode = *head, *Nnode = malloc(sizeof(listint_t));

	if (!Nnode)
	{
		return (NULL);
	}
	Nnode->n = number;
	Nnode->next = NULL;
	if (!Onode || Nnode->n < Onode->n)
	{
		Nnode->next = Onode;
		return (*head = Nnode);
	}
	while (Onode)
	{
		if (!Onode->next || Nnode->n < Onode->next->n)
		{
			Nnode->next = Onode->next;
			Onode->next = Nnode;
			return (Onode);
		}
		Onode = Onode->next;
	}
	return (NULL);
}
