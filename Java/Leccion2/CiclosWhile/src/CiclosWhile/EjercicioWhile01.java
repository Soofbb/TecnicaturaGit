
package CiclosWhile;

public class EjercicioWhile01 {
    public static void main(String[] args){
        var conteo = 0; // Inferencia de tipo
        while (conteo <= 7) {
            System.out.println("conteo = " + conteo); 
            conteo++; //Aumenta en 1 la variable
            
        }
        
        //Ciclo Do-While
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador <= 7);
        
        //Ciclo For 
        for (var contando = 0; contando < 7; contando++){
            System.out.println("contando = " + contando);
        }
        
    }

}
