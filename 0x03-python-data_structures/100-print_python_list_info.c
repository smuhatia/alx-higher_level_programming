#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info on python lists
 * @p: a pyobject list
 */

void print_python_list_info(pyObject *p)
{
	int list_len, list_alloc, idx;
	pyObject *element;

	list_len = py_SIZE(P);
	list_alloc = ((pyListObject *)p)->allocated;

	printf("[*] size of the python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", list_alloc);

	for (idx = 0; idx < list_len; idx++)
	{
		printf("Element %d: ", idx);

		element = Pylist_GetItem(p , idx);
		printf("%s\n", Py_TYPE(element)->tp_name);
	}
}
