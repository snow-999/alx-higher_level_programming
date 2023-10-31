#include "lists.h"
#include <strdlib.h>
/**
 * insert_node - insetr a node
 * @head: firat node
 * @number: number will be given to insetr
 * Return: node , NULL
 *
 *
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *Onode = *head, Nnode = malloc(sizeof(listint_t));

	if (!Nnode)
	{
		return (NULL);
	}
	Nnew->n = number;
	Nnew->next = NULL;
	if (!Onode || new->n < Onode->n)
	{
		Nnew->next = Onode;
		return (*head = Nnew);
	}
	while (Onode)
	{
		if (!Omode->next || Nnew->n < Onode->next->n)
		{
			Nnew->next = Onode->next;
			Onode->next = Nnew;
			return (Onode);
		}
		Onode = Onode->next;
	}
	return (NULL);
}
