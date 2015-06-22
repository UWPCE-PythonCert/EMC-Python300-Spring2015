#include <Python.h>

static PyObject* 
memleak(PyObject *self, PyObject *args) 
{
    // deliberately create a memory leak
    PyInt_FromLong( 10 );
    Py_RETURN_NONE;
}

static PyMethodDef memleak_methods[] = {
    {"memleak",  memleak, METH_NOARGS, "Leak some memory"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initmemleak(void) {
    Py_InitModule("memleak", memleak_methods);
}
