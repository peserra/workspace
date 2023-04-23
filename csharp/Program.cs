var lista1 = new List<int>();
var lista2 = new List<int>();
var lista3 = new List<int>();

Random rand = new Random();

for (int i = 0; i < 10; i++)
{
    lista1.Add(rand.Next(100));
}
for (int i = 0; i < 20; i++)
{
    lista2.Add(rand.Next(100));
}
for (int i = 0; i < 20; i++)
{
    lista3.Add(rand.Next(100));
}

int tamanho1 = lista1.Count();
int tamanho2 = lista2.Count();
int tamanho3 = lista3.Count();

for(int i = 0; i< tamanho1 + tamanho2 + tamanho3; i++){
    System.Console.Write("-");
}
System.Console.WriteLine("|");
int prog1 = 0;
foreach(var element in lista1){
    prog1++;
    var progress = (double)(prog1 / tamanho1 *100);
    System.Console.Write("-");
}
//System.Console.WriteLine();
int prog2 = 0;
foreach(var element in lista2){
    prog2++;
    var progress = (double)(prog2 / tamanho1 *100);
    System.Console.Write("-");
}
//System.Console.WriteLine();
int prog3 = 0;
foreach(var element in lista3){
    prog3++;
    var progress = (double)(prog3 / tamanho1 *100);
    System.Console.Write("-");
}
System.Console.WriteLine();






