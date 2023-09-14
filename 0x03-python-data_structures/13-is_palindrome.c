#include "lists.h"

/**
 * checkPalindrome - recursive function to check if singly linked list
 * is a palindrome.
 * @left: pointer to left end of the list.
 * @right: pointer to right end of the list.
 *
 * Return: 1 if palindrome, 0 if not a palindrome.
 */
int checkPalindrome(listint_t **left, listint_t *right)
{
    if (right == NULL)
        return (1);

    int isPalin = checkPalindrome(left, right->next) && ((*left)->n == right->n);

    (*left) = (*left)->next;

    return isPalin;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to list.
 *
 * Return: 1 if palindrome, 0 if not a palindrome.
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return (1);

    return checkPalindrome(head, *head);
}

