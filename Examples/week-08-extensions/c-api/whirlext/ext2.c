// C extension sample with argument handling.

#include "Python.h"

// string_peek function.

static PyObject *
string_peek(PyObject *self, PyObject *args)
{
   const char *pstr;
   int indx;
   
   if (!PyArg_ParseTuple(args, "si:string_peek", &pstr, &indx)) {
      return NULL;
   }

   int char_value = pstr[indx];
   
   return Py_BuildValue("i", char_value);
}

// string_peek_safe function.

static PyObject *
string_peek2(PyObject *self, PyObject *args)
{
   const char *pstr;
   int indx;
   
   if (!PyArg_ParseTuple(args, "si:string_peek", &pstr, &indx)) {
      return NULL;
   }

   if (indx < 0 || indx >= strlen(pstr)) {
      // Bad index value, raise an exception.
      PyErr_SetString(PyExc_IndexError, "peek index out of range");
      return NULL;
   }

   int char_value = pstr[indx];
   
   return Py_BuildValue("i", char_value);
}

// insert_powers

// def insert_powers(numbers, n):
//    powers = (n, n*n, n*n*n)
//    numbers[n] = powers
//    return powers

static PyObject *
insert_powers1(PyObject *self, PyObject *args)
{
   PyObject *numbers;
   int n;
   
   if (!PyArg_ParseTuple(args, "Oi", &numbers, &n)) {
      return NULL;
   }
   
   PyObject *powers = Py_BuildValue("(iii)", n, n*n, n*n*n);
   
   // Equivalent to Python: numbers[n] = powers
   if (PySequence_SetItem(numbers, n, powers) < 0) {
      return NULL;
   }

   return powers;
}

// def insert_powers(numbers, n):
//    powers = (n, n*n, n*n*n)
//    numbers[n] = powers
//    return powers

static PyObject *
insert_powers2(PyObject *self, PyObject *args)
{
   PyObject *numbers;
   int n;
   
   if (!PyArg_ParseTuple(args, "Oi", &numbers, &n)) {
      return NULL;
   }
   
   PyObject *powers = Py_BuildValue("(iii)", n, n*n, n*n*n);
   
   if (PySequence_SetItem(numbers, n, powers) < 0) {
      // Because we won't return powers, we have to discard it.
      Py_DECREF(powers);
      return NULL;
   }

   return powers;
}

// Module functions table.

static PyMethodDef
module_functions[] = {
   { "string_peek", string_peek, METH_VARARGS, "Pick a character from a string." },
   { "string_peek2", string_peek2, METH_VARARGS, "Safely pick a character from a string." },
   { "insert_powers1", insert_powers1, METH_VARARGS, "Insert a tuple of powers-of-n at index n" },
   { "insert_powers2", insert_powers2, METH_VARARGS, "Insert a tuple of powers-of-n at index n" },
   { NULL }
};

// This function is called to initialize the module.  It *must* be
// named initMOD, where MOD is the name of the module.
void
initext2(void)
{
   Py_InitModule3("ext2", module_functions, "A minimal module.");
}
