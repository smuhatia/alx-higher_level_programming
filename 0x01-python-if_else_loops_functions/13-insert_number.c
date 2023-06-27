#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that inserts a node in a sorted linked listint_t
 * @head: pointer to pointer of head node
 * @number: value to be inserted at the sorted position
 *
 * Return: pointer to the new node or NULL if allocation fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return new;
	}

	listint_t *current = *head;

	while (current->next && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return new;
}

