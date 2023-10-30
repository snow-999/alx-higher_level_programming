#include "lists.h"
#include "stdio.h"
#include "stdlib.h"
/**
 * check_cycle - check list is ceycled
 * @list: list will be cheacked
 * Return: 1 if equql, 0 or not
 *
 *
*/
int check_cycle(listint_t *list)
{
	listint_t* str = list;
	listint_t *ptr = list;

	while (ptr && ptr->next)
	{
		str = str->next;
		ptr = ptr->next->next;
		if (str == ptr)
		{
			return (1);
		}
	}
	return (0);
}
