// ext1.c: A sample C extension: one simple function

#include "Python.h"

// hello_world function.

static PyObject *
hello_world(PyObject *self, PyObject *args)
{
    return Py_BuildValue("s", "hello, world!");
}

// Module functions table.

static PyMethodDef
module_functions[] = {
    { "hello_world", hello_world, METH_VARARGS, "Say hello." },
    { NULL }
};

// This function is called to initialize the module.

void
initext1(void)
{
    Py_InitModule3("ext1", module_functions, "A minimal module.");
}
