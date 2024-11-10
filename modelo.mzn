% Use this editor as a MiniZinc scratch book
int: cantRamos;
int: cantSalas;
int: cantBloques = 35;
array[1..cantRamos] of int: prioridad;
array[1..cantRamos] of int: bloques;
array[1..cantRamos] of int: interes;
array[1..cantSalas] of int: capacidad;
array[1..cantRamos, 1..cantBloques] of bool: disponibilidad;

array[1..cantRamos, 1..cantSalas, 0..cantBloques+1] of var bool: A;
array[1..cantRamos] of var bool: asignado;

constraint
  forall(i in 1..cantRamos)(
    forall(j in 1..cantSalas)(
      forall(k in 1..cantBloques)(
        A[i,j,k]*capacidad[j] >= interes[i]*A[i,j,k]
      )
    )
  );
  
constraint
  forall(i in 1..cantRamos)(
    forall(j in 1..cantSalas)(
      forall(k in 1..cantBloques)(
        A[i,j,k] <= disponibilidad[i,k]
      )
    )
  );
  
constraint
  forall(i in 1..cantRamos)(
    forall(j in 1..cantSalas)(
      forall(k in [7,14,21,28])(
        A[i,j,k]+A[i,j,k+1] <= 1
      )
    )
  );
  
constraint
  forall(i in 1..cantRamos, j in 1..cantSalas)(
    A[i,j,0] = 0 /\
    A[i,j,cantBloques+1] = 0
  );
  
constraint
  forall(i in 1..cantRamos)(
    forall(j in 1..cantSalas)(
      forall(k in 1..cantBloques)(
        A[i,j,k-1]+A[i,j,k]+A[i,j,k+1] >= bloques[i]*A[i,j,k]
      )
    )
  );

constraint
  forall(i in 1..cantRamos where prioridad[i]>=6)(
    asignado[i]>=1
  );
 
constraint
  forall(i in 1..cantRamos)(
    sum(j in 1..cantSalas, k in 1..cantBloques)(A[i,j,k]) = asignado[i] * bloques[i]
  );

constraint
  forall(j in 1..cantSalas, k in 1..cantBloques)(
    sum(i in 1..cantRamos) (A[i,j,k]) <=1
  );
  
solve maximize
  sum(i in 1..cantRamos) (
    prioridad[i]*asignado[i]*bloques[i]
  );
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  