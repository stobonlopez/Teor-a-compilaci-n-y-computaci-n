
#
# 1.- La funcion cutc permite extraer campos de una lista de cadenas de
#     caracteres. Los campos estan delimitados por caracteres.
#
#     Ejemplo.
#     >>> x = ['uno:dos:tres',  'alpha:beta:omega']
#     >>> print(cutc(x, ':', 1, None))
#     ['dos', 'beta']
#     >>> print(cut(x, ':', 1, 2))
#     ['dos:tres', 'beta:omega']
#     >>> print(cut(x, ':', None, 1))
#     ['uno:dos',  'alpha:beta']
#
def cutc(x, delim, n=None, m=None):
    a = []
    b = []
    if n is not None and m is not None:
        if n > len(x):
            return ''
        else:
            for i in range(len(x)):
                aux = x[i].split(delim)[n:m+1]
                a.append(aux)
                b.append(delim.join(a[i]))
    elif n is None:
        for i in range(len(x)):
            aux = x[i].split(delim)[:m+1]
            a.append(aux)
            b.append(delim.join(a[i]))
    elif m is None:
        if n > len(x):
            return ''
        else:
            for i in range(len(x)):
                aux = x[i].split(delim)[n:n+1]
                a.append(aux)
                b.append(''.join(a[i]))

    else:
        return 'No meter ambos None'

    return(b)

# 
# 2.- La funcion pastec permite concatenar dos listas de cadenas de
#     caracteres elemento a elemento. Se debe especificar
#     el caracter delimitador
#
#     Ejemplo.
#     >>> x = ['linea 1', 'linea 2', 'linea 3']
#     >>> y = ['x', 'y', 'z']
#     >>> print(pastec(x, y, ';'))
#     ['linea 1;x', 'linea 2;y, 'linea 3;z']
#     >>> w = ['x', 'y', 'z', 'a', 'b']
#     >>> print(pastec(x, w, ';'))
#     ['linea 1;x', 'linea 2;y, 'linea 3;z', 'a', 'b']
#
def pastec(x, y, delim):
  a = []
  for i in range(max(len(x), len(y))):
    if i < len(x) and i < len(y):
      a.append(str(x[i]) + delim + str(y[i]))
    elif i < len(x) and i >= len(y):
      a.append(str(x[i]))
    elif i < len(y):
      a.append(y[i])
  return(a)

#
# 3.- La funcion wcc cuenta la ocurrencia de palabras en una lista de
#     cadenas de caracteres. La funcion wcc devuelve el resultado usando
#     un diccionario. Se debe especificar el caracter delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', ''hola mundo feliz', ''hola feliz']
#     >>> print(wcc(x, ' '))
#     {'hola':3, 'mundo':2, 'feliz':2}
#
def wcc(x, delim):
  dict = {}
  r = delim.join(x).split(delim)
  for i in r:
     dict[i] = r.count(i)

  return(dict)

#
# 4.- La funcion sortw ordena las palabras en una lista de cadenas de
#     caracteres ordenadas alfabeticamente. Se debe especificar el caracter
#     delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', ''hola mundo feliz', ''hola feliz']
#     >>> print(sortw(x, ' '))
#     ['feliz', 'feliz', 'hola', 'hola', 'hola','mundo', 'mundo']
#
def sortw(x, delim):
    return(sorted(delim.join(x).split(delim)))

#
# 5.- La funcion uniqc genera una lista compuesta por las palabras que
#     conforman una lista de cadenas de caracteres sin repeticion. Se
#     debe especificar el caracter delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', ''hola mundo feliz', ''hola feliz']
#     >>> print(uniqc(x, ' '))
#     ['hola', 'mundo', 'feliz']
#
def uniqc(x, delim):
    return(sorted(set(delim.join(x).split(delim))))


#
# 6.- La funcion selc genera una lista compuesta por las palabras que
#     conforman una lista de cadenas de caracteres y que ocurren un
#     determinado numero de veces. Se debe especificar el caracter
#     delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', ''hola mundo feliz', ''hola feliz']
#     >>> print(selc(x, 2, ' '))
#     [mundo', 'feliz']
#
def selc(x, n, delim):
  r = delim.join(x).split(delim)
  a = []
  for i in r:
    if r.count(i) == n:
      a.append(i)
  return(sorted(set(a)))
    #
